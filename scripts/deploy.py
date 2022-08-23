from brownie import accounts, config, SimpleStorage,network

def deploy_simple_storage():
    account = get_account()
    # print('value', config["wallets"]["from_key"] )
    # account = accounts.add(config["wallets"]["from_key"])
    simple_storage = SimpleStorage.deploy({"from":account})
    stored_value = simple_storage.retrieve()
    print(stored_value)
    transaction = simple_storage.store(17, {"from": account})
    transaction.wait(1)
    updated_stored_value = simple_storage.retrieve()
    print(updated_stored_value)

def get_account():
    print('show active ',network.show_active())
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_simple_storage()