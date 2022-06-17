from brownie import AdvancedCollectible, accounts, network, interface, config


def fund_advanced_collectible(nft_contract):
    # because you're funding AdvancedCollectible - Idk sha!
    dev = accounts.add(config["wallets"]["from_key"])
    link_token = interface.LinkTokenInterface(
        config["networks"][network.show_active()]["link_token"]
    )
    link_token.transfer(nft_contract, 1000000000000000000, {"from": dev})


def get_punk(punk_number):
    switch = {
        0: "S_CAP",
        1: "GREEN",
        2: "KING",
        3: "RAINBOW",
        4: "SMOKE",
        5: "HEADPHONES",
    }
    return switch[punk_number]
