from distutils.command.config import config
from brownie import accounts, network, config, MockV3Aggregator
from web3 import Web3

HELPFUL_LOCAL_BLOCKCHAIN_ENVIRONEMENTS = ["ganache-local",'development']
PRICE = 200000000
DECIMALS = 8


def get_account():
    if network.show_active() == HELPFUL_LOCAL_BLOCKCHAIN_ENVIRONEMENTS:
        return accounts[0]
    else:
        return accounts.add(config['wallets']['from_key'])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying Mocks....")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS,PRICE, {'from':get_account()})
    