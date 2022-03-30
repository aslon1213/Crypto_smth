"""
Course - solidity - tutorial - youtube video - last left at 4:20

Notes:
4: ---> Just starting to get serious 


questions:
1. what is infura.io
2. 
"""

from dis import Bytecode
from solcx import compile_standard, install_solc
install_solc("0.6.0")
import json
from dotenv_config import Config
config = Config()
from web3 import Web3
import os

 
#for connecting to Ganache/rinkeby 
w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
chain_id = 1337
my_address = "0x90F8bf6A479f320ead074411a4B0e7944Ea8c9C1"
print(config("PRIVATE_KEY"))
PRIVATE_KEY = config("PRIVATE_KEY")



with open("SimpleStoroge.sol","r") as file:
    simple_storage_file = file.read()


#compiled sol
compiled_sol = compile_standard(
    {
        "language":"Solidity",
        "sources":{"SimpleStorage.sol":{"content":simple_storage_file}},
        "settings":{
            "outputSelection":{
                "*":{"*":["abi","metadata","evm.bytecode","evm.sourceMap"]}
            }
        },
    },
    solc_version= "0.6.0",
)


with open("compiled_code.json","w") as file:
    json.dump(compiled_sol,file)


# get bytecode
bytecode = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["evm"]["bytecode"]["object"]
#get abi
abi = compiled_sol["contracts"]["SimpleStorage.sol"]["SimpleStorage"]["abi"]
#creating contract in python
SimpleStorage = w3.eth.contract(abi=abi, bytecode = bytecode)
# get nonce
nonce = w3.eth.getTransactionCount(my_address)

"""
Steps for making transaction
1. Bulding transaction
2. sign transaction
3. send transaction
"""
#building transaction
transaction = SimpleStorage.constructor().buildTransaction(
    {
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce,
    }
)
#signing transaction
print("deploying contract")
signed_transaction = w3.eth.account.sign_transaction(transaction,PRIVATE_KEY)
#sending transaction
tx_hash = w3.eth.send_raw_transaction(signed_transaction.rawTransaction)
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

#contract - build transaction
simple_storage = w3.eth.contract(address=tx_receipt.contractAddress, abi=abi)

#initial value of davorite number
print(simple_storage.functions.retrieve().call())
print("Updating")
store_transaction = simple_storage.functions.store(33).buildTransaction
({
        "chainId": chain_id,
        "from": my_address,
        "nonce": nonce+1,
    })
#sign 
signed_store_tx = w3.eth.account.sign_transaction(store_transaction,private_key = PRIVATE_KEY)
#send
send_store_tx = w3.eth.send_raw_transaction(signed_store_tx.rawTransaction)
tx_receipt_2 = w3.eth.wait_for_transaction_receipt(send_store_tx)
print("Updated")
print(simple_storage.functions.retrieve().call())
