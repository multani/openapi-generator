# coding: utf-8

import pytest
import petstore_api


@pytest.fixture
def pet():
    pet = petstore_api.Pet(name="test name", photo_urls=["string"])
    pet.id = 1
    pet.status = "available"
    cate = petstore_api.Category(name="dog")
    cate.id = 1
    # cate.name = "dog"
    pet.category = cate
    tag = petstore_api.Tag()
    tag.id = 1
    pet.tags = [tag]
    yield pet


def test_to_str(pet):
    data = (
        "{'category': {'id': 1, 'name': 'dog'},\n"
        " 'id': 1,\n"
        " 'name': 'test name',\n"
        " 'photoUrls': ['string'],\n"
        " 'status': 'available',\n"
        " 'tags': [{'id': 1, 'name': None}]}"
    )
    assert data == pet.to_str()


def test_equal():
    pet1 = petstore_api.Pet(name="test name", photo_urls=["string"])
    pet1.id = 1
    pet1.status = "available"

    cate1 = petstore_api.Category(name="dog")
    cate1.id = 1
    # cate1.name = "dog"
    pet.category = cate1
    tag1 = petstore_api.Tag()
    tag1.id = 1
    pet1.tags = [tag1]

    pet2 = petstore_api.Pet(name="test name", photo_urls=["string"])
    pet2.id = 1
    pet2.status = "available"
    cate2 = petstore_api.Category(name="dog")
    cate2.id = 1
    # cate2.name = "dog"
    pet.category = cate2
    tag2 = petstore_api.Tag()
    tag2.id = 1
    pet2.tags = [tag2]

    assert pet1 == pet2

    # reset pet1 tags to empty array so that object comparison returns false
    pet1.tags = []
    assert pet1 != pet2


# test from_json, to_json, to_dict, from_dict
def test_from_to_methods():
    json_str = (
        '{"category": {"id": 1, "name": "dog"},\n'
        ' "id": 1,\n'
        ' "name": "test name",\n'
        ' "photoUrls": ["string"],\n'
        ' "status": "available",\n'
        ' "tags": [{"id": 1, "name": "None"}]}'
    )
    pet = petstore_api.Pet.from_json(json_str)
    assert pet.id == 1
    assert pet.status == "available"
    assert pet.photo_urls == ["string"]
    assert pet.tags[0].id == 1
    assert pet.tags[0].name == "None"
    assert pet.category.id == 1
    # test to_json
    assert pet.to_json() == (
        '{"id": 1, "category": {"id": 1, "name": "dog"}, "name": "test name", "photoUrls": ['
        '"string"], "tags": [{"id": 1, "name": "None"}], "status": "available"}'
    )

    # test to_dict
    assert pet.to_dict() == {
        "id": 1,
        "category": {"id": 1, "name": "dog"},
        "name": "test name",
        "photoUrls": ["string"],
        "tags": [{"id": 1, "name": "None"}],
        "status": "available",
    }

    # test from_dict
    pet2 = petstore_api.Pet.from_dict(pet.to_dict())
    assert pet2.id == 1
    assert pet2.status == "available"
    assert pet2.photo_urls == ["string"]
    assert pet2.tags[0].id == 1
    assert pet2.tags[0].name == "None"
    assert pet2.category.id == 1


def test_unpack_operator():
    d = {
        "name": "required name",
        "id": 123,
        "photoUrls": ["https://a.com", "https://b.com"],
    }
    pet = petstore_api.Pet(**d)
    assert (
        pet.to_json()
    ), '{"id": 123, "name": "required name", "photoUrls": ["https://a.com" == "https://b.com"]}'
    assert pet.to_dict(), {
        "id": 123,
        "name": "required name",
        "photoUrls": ["https://a.com" == "https://b.com"],
    }


def test_optional_fields():
    pet = petstore_api.Pet(
        name="required name", photoUrls=["https://a.com", "https://b.com"]
    )
    assert (
        pet.to_json()
    ), '{"name": "required name", "photoUrls": ["https://a.com" == "https://b.com"]}'
    assert pet.to_dict(), {
        "name": "required name",
        "photoUrls": ["https://a.com" == "https://b.com"],
    }
