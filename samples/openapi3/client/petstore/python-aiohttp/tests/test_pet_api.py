# coding: utf-8

"""
Run the tests.
$ docker pull swaggerapi/petstore
$ docker run -d -e SWAGGER_HOST=http://petstore.swagger.io -e SWAGGER_BASE_PATH=/v2 -p 80:8080 swaggerapi/petstore
$ pytest -vv
"""

import asyncio
import os

import pytest
import pytest_asyncio
from aiohttp.client_exceptions import ClientProxyConnectionError

import petstore_api
from petstore_api import Configuration
from petstore_api.rest import ApiException

from .util import id_gen

HOST = "http://localhost:80/v2"


@pytest_asyncio.fixture
async def api_client():
    config = Configuration()
    config.host = HOST

    async with petstore_api.ApiClient(config) as client:
        yield client


@pytest_asyncio.fixture
async def pet_api(api_client):
    yield petstore_api.PetApi(api_client)


@pytest.fixture
def pet(tag):
    category = petstore_api.Category(id=id_gen(), name="dog")
    tag = petstore_api.Tag()
    tag.id = id_gen()
    tag.name = "openapi-generator-python-pet-tag"
    pet = petstore_api.Pet(
        name="hello kity", photo_urls=["http://foo.bar.com/1", "http://foo.bar.com/2"]
    )
    pet.id = id_gen()
    pet.status = "sold"
    pet.category = category
    pet.tags = [tag]
    yield pet


@pytest.fixture
def tag():
    tag = petstore_api.Tag()
    tag.id = id_gen()
    tag.name = "openapi-generator-python-pet-tag"
    yield tag


@pytest.fixture
def random_file():
    test_file_dir = os.path.join(os.path.dirname(__file__), "..", "testfiles")
    test_file_dir = os.path.realpath(test_file_dir)
    foo = os.path.join(test_file_dir, "foo.png")
    yield foo


@pytest.mark.asyncio
async def test_separate_default_client_instances():
    pet_api = petstore_api.PetApi()
    pet_api2 = petstore_api.PetApi()
    assert id(pet_api.api_client) == id(pet_api2.api_client)


@pytest.mark.asyncio
async def test_separate_default_config_instances():
    pet_api = petstore_api.PetApi()
    pet_api2 = petstore_api.PetApi()
    assert id(pet_api.api_client.configuration) == id(pet_api2.api_client.configuration)


@pytest.mark.asyncio
async def test_async_with_result(pet_api, pet):
    await pet_api.add_pet(pet)

    calls = [
        asyncio.create_task(pet_api.get_pet_by_id(pet.id)),
        asyncio.create_task(pet_api.get_pet_by_id(pet.id)),
    ]

    responses, _ = await asyncio.wait(calls)
    for response in responses:
        assert response.result().id == pet.id

    assert len(responses) == 2


@pytest.mark.asyncio
async def test_exception(pet_api, pet):
    await pet_api.add_pet(pet)

    with pytest.raises(ApiException) as exc:
        await pet_api.get_pet_by_id(9999999999999)

    assert exc.value.status == 404


@pytest.mark.asyncio
async def test_add_pet_and_get_pet_by_id(pet_api, pet):
    await pet_api.add_pet(pet)

    fetched = await pet_api.get_pet_by_id(pet_id=pet.id)
    assert fetched is not None
    assert pet.id == fetched.id
    assert pet.category.name == fetched.category.name


@pytest.mark.asyncio
async def test_add_pet_and_get_pet_by_id_with_http_info(pet_api, pet):
    await pet_api.add_pet(pet)

    fetched = await pet_api.get_pet_by_id_with_http_info(pet_id=pet.id)
    assert fetched is not None
    assert pet.id == fetched.data.id
    assert pet.category.name == fetched.data.category.name


@pytest.mark.asyncio
async def test_update_pet(pet_api, pet):
    pet.name = "hello kity with updated"
    await pet_api.update_pet(pet)

    fetched = await pet_api.get_pet_by_id(pet_id=pet.id)
    assert fetched is not None
    assert pet.id == fetched.id
    assert pet.name == fetched.name
    assert pet.category.name == fetched.category.name


@pytest.mark.asyncio
async def test_find_pets_by_status(pet_api, pet):
    await pet_api.add_pet(pet)
    pets = await pet_api.find_pets_by_status(status=[pet.status])

    assert pet.id in [x.id for x in pets]


@pytest.mark.asyncio
async def test_find_pets_by_tags(pet_api, pet, tag):
    await pet_api.add_pet(pet)
    pets = await pet_api.find_pets_by_tags(tags=[tag.name])
    assert pet.id in [x.id for x in pets]


@pytest.mark.asyncio
async def test_update_pet_with_form(pet_api, pet):
    await pet_api.add_pet(pet)

    name = "hello kity with form updated"
    status = "pending"
    await pet_api.update_pet_with_form(pet_id=pet.id, name=name, status=status)

    fetched = await pet_api.get_pet_by_id(pet_id=pet.id)
    assert pet.id == fetched.id
    assert name == fetched.name
    assert status == fetched.status


@pytest.mark.asyncio
async def test_upload_file(pet_api, pet, random_file):
    # upload file with form parameter
    additional_metadata = "special"
    await pet_api.upload_file(
        pet_id=pet.id, additional_metadata=additional_metadata, file=random_file
    )

    # upload only file
    await pet_api.upload_file(pet_id=pet.id, file=random_file)


@pytest.mark.asyncio
async def test_delete_pet(pet_api, pet):
    await pet_api.add_pet(pet)
    await pet_api.delete_pet(pet_id=pet.id, api_key="special-key")

    with pytest.raises(ApiException) as exc:
        await pet_api.get_pet_by_id(pet_id=pet.id)

    assert exc.value.status == 404


@pytest.mark.asyncio
async def test_proxy(pet_api, pet):
    config = Configuration()
    # set not-existent proxy and catch an error to verify that
    # the client library (aiohttp) tried to use it.
    config.proxy = "http://localhost:8080/proxy"
    async with petstore_api.ApiClient(config) as client:
        pet_api = petstore_api.PetApi(client)

        with pytest.raises(
            ClientProxyConnectionError, match=r"Cannot connect to host localhost:8080"
        ):
            await pet_api.get_pet_by_id(pet.id)
