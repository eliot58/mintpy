from tonsdk.contract.token.nft import NFTCollection, NFTItem
from getgems import NFTSale
from tonsdk.contract import Address
from tonsdk.utils import to_nano

def create_collection():
    royalty_base = 1000
    royalty_factor = 50
    code = "B5EE9C724102140100021F000114FF00F4A413F4BCF2C80B0102016202030202CD04050201200E0F04E7D10638048ADF000E8698180B8D848ADF07D201800E98FE99FF6A2687D20699FEA6A6A184108349E9CA829405D47141BAF8280E8410854658056B84008646582A802E78B127D010A65B509E58FE59F80E78B64C0207D80701B28B9E382F970C892E000F18112E001718112E001F181181981E0024060708090201200A0B00603502D33F5313BBF2E1925313BA01FA00D43028103459F0068E1201A44343C85005CF1613CB3FCCCCCCC9ED54925F05E200A6357003D4308E378040F4966FA5208E2906A4208100FABE93F2C18FDE81019321A05325BBF2F402FA00D43022544B30F00623BA9302A402DE04926C21E2B3E6303250444313C85005CF1613CB3FCCCCCCC9ED54002C323401FA40304144C85005CF1613CB3FCCCCCCC9ED54003C8E15D4D43010344130C85005CF1613CB3FCCCCCCC9ED54E05F04840FF2F00201200C0D003D45AF0047021F005778018C8CB0558CF165004FA0213CB6B12CCCCC971FB008002D007232CFFE0A33C5B25C083232C044FD003D0032C03260001B3E401D3232C084B281F2FFF2742002012010110025BC82DF6A2687D20699FEA6A6A182DE86A182C40043B8B5D31ED44D0FA40D33FD4D4D43010245F04D0D431D430D071C8CB0701CF16CCC980201201213002FB5DAFDA89A1F481A67FA9A9A860D883A1A61FA61FF480610002DB4F47DA89A1F481A67FA9A9A86028BE09E008E003E00B01A500C6E"

    collection = NFTCollection(
        code=code,
        royalty_base=royalty_base,
        royalty=royalty_factor,
        royalty_address=Address('EQBcJ0nCBGbNPJ-7kB8jAAoKNagW2kI-jQ1uypBPsche34KE'),
        owner_address=Address('EQBcJ0nCBGbNPJ-7kB8jAAoKNagW2kI-jQ1uypBPsche34KE'),
        collection_content_uri='https://s.getgems.io/nft/b/c/62fba50217c3fe3cbaad9e7f/meta.json',
        nft_item_content_base_uri='https://ipfs.io/ipfs/QmP5ctrH4ZndkofykJkkHyVPRHPf27nLheNrGu2QN8r5vg/',
        nft_item_code_hex=NFTItem.code)

    return collection


def create_nft_mint(owner, content, nft_item_index):
    collection = create_collection()

    body = collection.create_mint_body(item_index=nft_item_index,
                                       new_owner_address=Address(owner),
                                       item_content_uri=content,
                                       amount=to_nano(0.02, 'ton'))

    return body


def create_batch_nft_mint(from_item_index, contents_and_owners):

    collection = create_collection()

    body = collection.create_batch_mint_body(from_item_index=from_item_index,
                                      contents_and_owners=contents_and_owners,
                                      amount_per_one=to_nano(0.01, 'ton'))
    return body


def create_sale(nft_address):


    sale = NFTSale(
        is_complete=False,
        marketplace_address=Address("EQBYTuYbLf8INxFtD8tQeNk5ZLy-nAX9ahQbG_yl1qQ-GEMS"),
        nft_address=Address(nft_address),
        full_price=to_nano(10, "ton"),
        marketplace_fee_address=Address("EQCjk1hh952vWaE9bRguFkAhDAL5jj3xj9p0uPWrFBq_GEMS"),
        marketplace_fee=to_nano(1, "ton"),
        royalty_address=Address("EQBcJ0nCBGbNPJ-7kB8jAAoKNagW2kI-jQ1uypBPsche34KE"),
        royalty_amount=to_nano(0.5, "ton"),
    )




    return sale