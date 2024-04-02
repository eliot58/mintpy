import asyncio
from tonsdk.utils import to_nano, b64str_to_bytes
from client import get_client, get_seqno
from wallet import wallet
from body import create_sale, create_collection
from ton.utils import read_address
from tonsdk.boc import Cell
from tonsdk.contract.token.nft import NFTItem
from tonsdk.contract import Address

async def get_nft_address(client, index: int):
    collection = create_collection()
    stack = (await client.raw_run_method(address=collection.address.to_string(),
                                         method='get_nft_address_by_index', stack_data=[["number", index]]))['stack']
    nft_address = read_address(Cell.one_from_boc(b64str_to_bytes(stack[0][1]['bytes']))).to_string(True, True, True)
    return nft_address

async def deploy_sale():


    client = await get_client()

    seqno = 4

    for i in range(1000):
        nft_addr = await get_nft_address(client, i)

        sale = create_sale(nft_addr)

        state_init = sale.create_state_init()['state_init']


        query = wallet.create_transfer_message(to_addr=sale.address.to_string(),
                                       amount=to_nano(0.05, 'ton'),
                                       state_init=state_init,
                                       seqno=seqno)
        
        seqno +=1
        
        await client.raw_send_message(query['message'].to_boc(False))

        await asyncio.sleep(10)

        body = NFTItem().create_transfer_body(new_owner_address=Address(sale.address.to_string()))

        query = wallet.create_transfer_message(to_addr=nft_addr,
                                       amount=to_nano(0.05, 'ton'),
                                       seqno=seqno,
                                       payload=body)
        
        seqno += 1
        
        await client.raw_send_message(query['message'].to_boc(False))

        print(f"{i} put up for sale")

        





if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(deploy_sale())