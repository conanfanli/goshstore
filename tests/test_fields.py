from unittest.mock import patch
from decimal import Decimal

from django.test import TestCase
from django.db import models

from goshstore.fields import GosHStoreField

sequence = iter(range(10000))
database = {}


class DummyModel(models.Model):
    hstores = GosHStoreField(default={})
    second_gos = GosHStoreField(default={})

    def batman(self):
        return 10 * 10

    def superman(self):
        return 100 * 100

    @hstores.getter(key='batman', converter=Decimal)
    def gos_batman(self, save=True, reset=False):
        return self.batman()

    @second_gos.getter('superman', converter=float)
    def gos_superman(self, save, reset):
        return self.superman()

    def save(self, *args, **kwargs):
        '''Save to the dictionary instead of database.'''
        pass


class GosHstoreFieldTestCase(TestCase):

    @patch.object(DummyModel, 'batman')
    def test_call_batman_only_once(self, mock):
        '''If hstore field (in this case named "hstores") is empty, calling
        gos_batman should call batman().
        '''
        mock.return_value = 1
        instance = DummyModel()
        self.assertFalse(instance.hstores)
        self.assertEqual(instance.gos_batman(), 1)
        # gos_batman() should call batman()
        mock.assert_called_once_with()
        mock.reset_mock()
        mock.assert_not_called()
        self.assertEqual(instance.hstores, {'batman': '1'})
        # Calling gos_batman() again should NOT call batman()
        instance.gos_batman()
        mock.assert_not_called()

    @patch.object(DummyModel, 'superman')
    def test_call_super_only_once(self, mock):
        '''If hstore field (in this case named "second_gos") is empty, calling
        gos_superman should call superman().
        '''
        mock.return_value = 2
        instance = DummyModel()
        self.assertFalse(instance.second_gos)
        self.assertEqual(instance.gos_superman(), 2)
        mock.assert_called_once_with()
        mock.reset_mock()
        mock.assert_not_called()
        self.assertEqual(instance.second_gos, {'superman': '2'})
        instance.gos_superman()
        mock.assert_not_called()

    def test_reset_all_goshstore(self):
        '''DummyModel.reset_all_goshstore should collect all hstore getters
        and execute them regardless whether they are empty.
        '''
        instance = DummyModel()
        self.assertFalse(instance.hstores)
        self.assertFalse(instance.second_gos)
        instance.reset_all_goshstore()
        self.assertEqual(instance.hstores, {'batman': '100'})
        self.assertEqual(instance.second_gos, {'superman': '10000'})
