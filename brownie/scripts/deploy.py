"""
Course - solidity - tutorial - youtube video - last left at 4:20

Notes:
4: ---> Just starting to get serious 


questions:
1. what is infura.io
2. yearn.finance
3. 
"""

from brownie import accounts, config, SimpleStorage

def deploy_simple_storage():
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    print(account)
    print(simple_storage)
    value = simple_storage.retrieve()
    print(value)
    simple_storage.store(1213, {"from": account})
    print(simple_storage.retrieve())



def main():
    deploy_simple_storage()