# coding: utf-8

# flake8: noqa

"""
Run the tests.
$ pip install -U pytest
$ cd petstore_api-python
$ pytest
"""

import os
import sys
import unittest

import pytest

import petstore_api
from petstore_api.rest import ApiException

from .util import id_gen


class ApiExceptionTests(unittest.TestCase):

    def setUp(self):
        self.api_client = petstore_api.ApiClient()
        self.pet_api = petstore_api.PetApi(self.api_client)
        self.setUpModels()

    def setUpModels(self) -> None:
        self.category = petstore_api.Category(name="dog")
        self.category.id = id_gen()
        self.category.name = "dog"
        self.tag = petstore_api.Tag()
        self.tag.id = id_gen()
        self.tag.name = "blank"
        self.pet = petstore_api.Pet(name="hello kity", photoUrls=["http://foo.bar.com/1", "http://foo.bar.com/2"])
        self.pet.id = id_gen()
        self.pet.status = "sold"
        self.pet.category = self.category
        self.pet.tags = [self.tag]

    def test_404_error(self):
        self.pet_api.add_pet(self.pet)
        assert self.pet.id is not None
        self.pet_api.delete_pet(pet_id=self.pet.id)

        with pytest.raises(ApiException, match="Pet not found") as exc:
            self.pet_api.get_pet_by_id(pet_id=self.pet.id)

        assert exc.value.status == 404
        assert exc.value.reason == "Not Found"
        assert exc.value.body is not None
        assert "Pet not found" in exc.value.body

    def test_500_error(self):
        self.pet_api.add_pet(self.pet)
        assert self.pet.id is not None

        with pytest.raises(ApiException, match="Internal Server Error") as exc:
            self.pet_api.upload_file(
                pet_id=self.pet.id,
                additional_metadata="special",
                file=None
            )

        assert exc.value.status == 500
        assert exc.value.reason == "Internal Server Error"
        assert exc.value.body is not None
        assert "Error 500 Internal Server Error" in exc.value.body
