from brownie import accounts, SimpleStorage

def test_retrieve():
    #initiliaze
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({'from': account})
    expected = 0
    #Assert
    assert simple_storage.retrieve() == expected

    expected_2 = 1213
    simple_storage.store(expected_2, {'from': account})
    assert simple_storage.retrieve() == expected_2
    
    