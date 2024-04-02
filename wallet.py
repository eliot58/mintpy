from tonsdk.contract.wallet import Wallets, WalletVersionEnum

# mnemonics = "inner blue athlete face library clock time brand chaos holiday anchor spread pink vapor win about culture balance face civil depth pig aerobic remove".split()

mnemonics = "dose flat system gentle student moral axis radar project mango choice sausage faint crazy economy glue play sweet flight nation panther raccoon turtle strike".split()

mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum.v4r2,
                                                          workchain=0)


# dose flat system gentle student moral axis radar project mango choice sausage faint crazy economy glue play sweet flight nation panther raccoon turtle strike