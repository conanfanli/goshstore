from unittest.mock import patch
from decimal import Decimal

from django.test import TestCase
from django.db import models

from goshstore.fields import GosHStoreField


class DummyModel(models.Model):
    hstores = GosHStoreField(default={})
    second_gos = GosHStoreField(default={})

    def calculate(self):
        return 10 * 10

    @hstores.getter(key='batman', converter=Decimal)
    def gos_batman(self, save=True, reset=False):
        return self.calculate()


class GosHstoreFieldTestCase(TestCase):

    @patch.object(DummyModel, 'calculate')
    def test_goshstorefield_save_false(self, mock):
        '''If hstore field (in this case named "hstores") is empty, calling
        gos_batman should call calculate().
        '''
        mock.return_value = 1
        instance = DummyModel()
        self.assertFalse(instance.hstores)
        self.assertEqual(instance.gos_batman(save=False), 1)
        # gos_batman() should call calculate()
        mock.assert_called_once_with()
        mock.reset_mock()
        mock.assert_not_called()
        self.assertEqual(instance.hstores, {'batman': '1'})
        # Calling gos_batman() again should NOT call calculate()
        instance.gos_batman()
        mock.assert_not_called()
