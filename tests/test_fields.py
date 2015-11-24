from decimal import Decimal

from django.test import TestCase
from django.db import models

from goshstore.fields import GosHStoreField


class DummyModel(models.Model):
    hstores = GosHStoreField(default={})
    second_gos = GosHStoreField(default={})

    @hstores.getter(key='batman', converter=Decimal)
    def gos_batman(self, save=True, reset=False):
        return 100 * 100


class GosHstoreFieldTestCase(TestCase):

    def test_goshstorefield_no_args(self):
        instance = DummyModel()
        print(instance.gos_batman())
