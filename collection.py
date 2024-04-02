import asyncio
from tonsdk.utils import to_nano
from client import get_client
from body import create_collection
from wallet import wallet
from tonsdk.contract import Address


async def deploy_collection():

    collection = create_collection()
    state_init = collection.create_state_init()['state_init']

    client = await get_client()

    recipes = [
        {
            'address': collection.address.to_string(),
            'amount': to_nano(0.05, 'ton'),
            'state_init': state_init,
            'send_mode': 3
        }
    ]

    query = wallet.create_transfer_message(recipients_list=recipes, query_id=0)


    await client.raw_send_message(query['message'].to_boc(False))

    print("collection deployed")
    print(collection.address.to_string())


async def change_owner(new_owner_address):
    collection = create_collection()

    client = await get_client()

    recipes = [
        {
            'address': collection.address.to_string(),
            'amount': to_nano(0.05, 'ton'),
            'payload': collection.create_change_owner_body(new_owner_address),
            'send_mode': 3
        }
    ]

    query = wallet.create_transfer_message(recipients_list=recipes, query_id=0)


    await client.raw_send_message(query['message'].to_boc(False))

    print("owner change")
    print(collection.address.to_string())



async def edit_collection():
    collection = create_collection()

    client = await get_client()


    params = {
        "collection_content_uri": "https://s.getgems.io/nft/b/c/62fba50217c3fe3cbaad9e7f/meta.json",
        "nft_item_content_base_uri": "https://brown-real-meerkat-526.mypinata.cloud/ipfs/QmNoEEi69nb1mYzLkqr8aJfAm6rQJYkpXyBHdvNdSsU4UD/",
        "royalty_factor": 50,
        "royalty_base": 1000,
        "royalty_address": Address("kQA89rIdEQH7kP1_cs-QUO4q6V7MRbWFzutmrx1YVPRoKv_y"),
        "royalty": 1
    }

    recipes = [
        {
            'address': collection.address.to_string(),
            'amount': to_nano(0.05, 'ton'),
            'payload': collection.create_edit_content_body(params),
            'send_mode': 3
        }
    ]

    query = wallet.create_transfer_message(recipients_list=recipes, query_id=0)


    await client.raw_send_message(query['message'].to_boc(False))

    print("collection edit")
    print(collection.address.to_string())



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(edit_collection())