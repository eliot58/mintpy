from tonsdk.contract.wallet import Wallets, WalletVersionEnum

mnemonics = "fan rotate modify hour increase latin panel turtle oppose left cover romance plate learn stereo walk excess table pull joke cotton rescue peace denial".split()

# mnemonics = "dose flat system gentle student moral axis radar project mango choice sausage faint crazy economy glue play sweet flight nation panther raccoon turtle strike".split()

mnemonics, pub_k, priv_k, wallet = Wallets.from_mnemonics(mnemonics=mnemonics, version=WalletVersionEnum("hv2"),
                                                          workchain=0)


# dose flat system gentle student moral axis radar project mango choice sausage faint crazy economy glue play sweet flight nation panther raccoon turtle strike