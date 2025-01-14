import os
from brownie import accounts, AdvancedCollectible, config, interface, network


def get_breed(breed_number):
    switch = {
        0: "PUG",
        1: "SHIBA_INU",
        2: "BRENARD"
    }
    return switch[breed_number]


def fund_advanced_collectible(nft_contract):
    dev = accounts.add(os.getenv(config['wallets']['from_key']))
    # Get the most recent PriceFeed Object
    interface.LinkTokenInterface(config['networks'][network.show_active()]['link_token']).transfer(
        nft_contract, config['networks'][network.show_active()]['fee'], {'from': dev})
