from django.test import TestCase
from django.db import models

from goshstore.fields import GosHstoreField


class DummyModel(models.Model):
    hstores = GosHstoreField(default={})
    second_gos = GosHstoreField(default={})


class GosHstoreFieldTestCase(TestCase):

    def test_goshstorefield_get(self):
        pass
