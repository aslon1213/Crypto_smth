from brownie import FundMe
from helpful_scripts import *




def fund():
    fund_me = FundMe[-1]
    account = get_account()
    entrance_fee = fund_me.getEntranceFee({'from':account})
    print(f"entrance fee is {entrance_fee}")
    fund_me.fund({'from':account, 'value':entrance_fee})
    print("Funding")


def withdraw():
    fund_me = FundMe[-1]
    account = get_account()
    fund_me.wintdraw({'from':account})

def main():
    fund()
    withdraw()