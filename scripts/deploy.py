"""
stopped video at: 5:29


problems:
    brownie isnt working as expected


"""


from tkinter import W
from brownie import FundMe,MockV3Aggregator, network, config
from scripts.helpful_scripts import get_account, deploy_mocks, HELPFUL_LOCAL_BLOCKCHAIN_ENVIRONEMENTS

def deploy_FundMe():
    accont = get_account()
    #if on persistent network like rinkeby - use associated address
    #otherwise use mocks
    price_feed_address = 0
    if network.show_active() != HELPFUL_LOCAL_BLOCKCHAIN_ENVIRONEMENTS:
        print(f"The active network is {network.show_active()}")
        price_feed_address = config['networks'][network.show_active()]['eth_to_usd_price_feed']
    else:
        deploy_mocks()
        price_feed_address = MockV3Aggregator[-1].address


    
    fund_me = FundMe.deploy(price_feed_address,{'from':accont}, 
    publish_source = config['networks'][network.show_active()].get('verify'),)
    print(f'contract deployed at {fund_me.address}')


def main():
    pass