django-goshstorefield
=====================
django-gohstore field is a reusable Django field that allows you to get or set values from hstore fields.


How to use
----------
Assuming you have a django model defined:

.. code-block:: python

    from django.db import models
    from goshstore import GosHStoreField

    class MyModel(models.Model):
        hstores = GosHStoreField(default={})

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
