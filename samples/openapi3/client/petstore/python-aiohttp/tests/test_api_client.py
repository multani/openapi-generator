# coding: utf-8

import pytest

import petstore_api


@pytest.mark.asyncio
async def test_context_manager_closes_client():
    async with petstore_api.ApiClient() as client:
        # pool_manager
        assert not client.rest_client.pool_manager.closed
        rest_pool_ref = client.rest_client.pool_manager

    assert rest_pool_ref.closed
