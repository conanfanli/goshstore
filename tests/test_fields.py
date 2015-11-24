from django.test import TestCase
from django.db import models

from goshstore.fields import GosHStoreField


class DummyModel(models.Model):
    hstores = GosHStoreField(default={})
    second_gos = GosHStoreField(default={})


class GosHstoreFieldTestCase(TestCase):

    def test_goshstorefield_get(self):
        pass
