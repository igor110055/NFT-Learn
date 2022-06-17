from lib2to3.pgen2 import token
from brownie import AdvancedCollectible, accounts, config
from scripts.helpful_scripts import get_punk
import time

STATIC_SEED = 123


def main():
    dev = accounts.add(config["wallets"]["from_key"])
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) - 1]
    transaction = advanced_collectible.createCollectible(
        "None", STATIC_SEED, {"from": dev}
    )
    transaction.wait(1)
    time.sleep(35)
    requestId = transaction.events["requestedCollectible"]["requestId"]
    token_id = advanced_collectible.requestIdToToken(requestId)
    punk = get_punk(advanced_collectible.tokenIdToPunk(token_id))
    print(f'Punk of tokenId {token_id} is {punk}')
