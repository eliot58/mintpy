import asyncio
from tonsdk.utils import to_nano
from client import get_client
from wallet import wallet
from body import create_collection, create_nft_mint, create_batch_nft_mint
from tonsdk.contract import Address

async def deploy_items():

    collection = create_collection()

    client = await get_client()

    contents = []


    for _ in range(200):
        contents.append(
            ("1.json", Address("0QBsqOeWeZbiaLgLy3-qZ5jY9_ZyIY2VC_w_a9eR0gTg7N18"))
        )
    
    split_contents = [contents[i:i+4] for i in range(0, len(contents), 4)]

    recipes = []

    index = 1000

    for content in split_contents:
        body = create_batch_nft_mint(index, content)

        recipes.append({
            'address': collection.address.to_string(),
            'payload': body,
            'amount': to_nano('0.05', 'ton'),
            'send_mode': 3
        })
        index += 4
            

    query = wallet.create_transfer_message(recipients_list=recipes, query_id=0)


    await client.raw_send_message(query['message'].to_boc(False))

    print("items deployed")
    print(collection.address.to_string())




if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(deploy_items())