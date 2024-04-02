import asyncio
from tonsdk.contract.wallet import WalletVersionEnum, Wallets
from tonsdk.crypto import mnemonic_new
from client import get_client


async def create_wallet():
    mnemonics = mnemonic_new()
    _mnemonics, _pub_k, _priv_k, wallet = Wallets.from_mnemonics(mnemonics, WalletVersionEnum('hv2'), 0)
    
    print(" ".join(mnemonics))
    
    print(wallet.address.to_string(True, True, True))

    input("Скиньте тоны на адрес выше и нажмите на enter")

    await asyncio.sleep(30)

    print("start deployed")

    query = wallet.create_init_external_message()
    client = await get_client()
    await client.raw_send_message(query['message'].to_boc(False))

    print("deployed")



if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(create_wallet())