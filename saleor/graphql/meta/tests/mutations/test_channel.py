import graphene

from . import PRIVATE_KEY, PRIVATE_VALUE, PUBLIC_KEY, PUBLIC_VALUE
from .test_delete_metadata import (
    execute_clear_public_metadata_for_item,
    item_without_public_metadata,
)
from .test_delete_private_metadata import (
    execute_clear_private_metadata_for_item,
    item_without_private_metadata,
)
from .test_update_metadata import (
    execute_update_public_metadata_for_item,
    item_contains_proper_public_metadata,
)
from .test_update_private_metadata import (
    execute_update_private_metadata_for_item,
    item_contains_proper_private_metadata,
)


def test_delete_private_metadata_for_channel(
    staff_api_client, permission_manage_channels, channel_USD
):
    # given
    channel_USD.store_value_in_private_metadata({PRIVATE_KEY: PRIVATE_VALUE})
    channel_USD.save(update_fields=["private_metadata"])
    channel_id = graphene.Node.to_global_id("Channel", channel_USD.pk)

    # when
    response = execute_clear_private_metadata_for_item(
        staff_api_client, permission_manage_channels, channel_id, "Channel"
    )

    # then
    assert item_without_private_metadata(
        response["data"]["deletePrivateMetadata"]["item"], channel_USD, channel_id
    )


def test_delete_public_metadata_for_gift_card(
    staff_api_client, permission_manage_channels, channel_USD
):
    # given
    channel_USD.store_value_in_metadata({PUBLIC_KEY: PUBLIC_VALUE})
    channel_USD.save(update_fields=["metadata"])
    channel_id = graphene.Node.to_global_id("Channel", channel_USD.pk)

    # when
    response = execute_clear_public_metadata_for_item(
        staff_api_client, permission_manage_channels, channel_id, "Channel"
    )

    # then
    assert item_without_public_metadata(
        response["data"]["deleteMetadata"]["item"], channel_USD, channel_id
    )


def test_add_public_metadata_for_channel_USD(
    staff_api_client, permission_manage_channels, channel_USD
):
    # given
    channel_id = graphene.Node.to_global_id("Channel", channel_USD.pk)

    # when
    response = execute_update_public_metadata_for_item(
        staff_api_client, permission_manage_channels, channel_id, "Channel"
    )

    # then
    assert item_contains_proper_public_metadata(
        response["data"]["updateMetadata"]["item"], channel_USD, channel_id
    )


def test_add_private_metadata_for_channel_USD(
    staff_api_client, permission_manage_channels, channel_USD
):
    # given
    channel_id = graphene.Node.to_global_id("Channel", channel_USD.pk)

    # when
    response = execute_update_private_metadata_for_item(
        staff_api_client, permission_manage_channels, channel_id, "Channel"
    )

    # then
    assert item_contains_proper_private_metadata(
        response["data"]["updatePrivateMetadata"]["item"], channel_USD, channel_id
    )
