import inspect
from functools import wraps

from django.contrib.postgres.fields import HStoreField


def reset_all_goshstore(self):
    '''Refresh all hstore values.'''
    for field_name in self._hstore_getters:
        for getter_name in self._hstore_getters[field_name]:
            method = getattr(self, getter_name)
            method(save=False, reset=True)

    self.save(update_fields=list(self._hstore_getters.keys()))


class GosHStoreField(HStoreField):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Simply set _registered_getters
        self._registered_getters = []

    def contribute_to_class(self, cls, name, virtual_only=False):
        '''Override contribute_to_class to set _registered_getters on the
        model class.
        '''
        super().contribute_to_class(cls, name, virtual_only=virtual_only)
        hstore_getters = getattr(cls, '_hstore_getters', {})
        hstore_getters[name] = self._registered_getters
        setattr(cls, '_hstore_getters', hstore_getters)
        cls.reset_all_goshstore = reset_all_goshstore

    def getter(self, key, converter=None):
        '''A decorator used to declare a model method as a hstore property.

        Example:
            @hstores.getter(key='foo', converter=Decimal)
            def get_foo(self, reset=False, save=True):
                return max(range(100))

        Calling instance.get_foo() will return instance.hstores['foo'] if 'foo'
        is in instance.hstores. Otherwise, 100 will be stored into
        instance.hstores['foo'] and instance.save(update_fields=['hstores'])
        will be called. To prevent calling instance.save(), call
        instance.get_foo(save=False).

        When calling instance.get_foo(reset=True), max(range(100)) will be
        evaluated and returned regardless whether 'foo' is already in
        instance.hstores.
        '''

        def wrapper1(method):
            if converter and not callable(converter):
                raise AssertionError('{} is not callable'.format(converter))

            method_args = inspect.getargspec(method).args
            expected_args = ['self', 'save', 'reset']
            if method_args != expected_args:
                raise AssertionError('A hstore getter method must have the '
                                     'exact arguments: {}'.format(
                                         expected_args))

            self._registered_getters.append(method.__name__)

            @wraps(method)
            def wrapper2(model_instance, save=True, reset=False):
                # It's actually very important to make a COPY of the dict
                # object instead of directly modifying it.
                hstores_dict = dict(self.value_from_object(model_instance))
                if key in hstores_dict and not reset:
                    ret = hstores_dict[key]
                else:
                    ret = method(model_instance, save, reset)
                    hstores_dict[key] = str(ret)
                    # Then remember set the field vaule
                    setattr(model_instance, self.attname, hstores_dict)
                    if save:
                        model_instance.save(update_fields=[self.attname])

                if converter:
                    ret = converter(ret)

                return ret

            return wrapper2

        return wrapper1
