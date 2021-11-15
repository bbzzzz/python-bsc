from web3 import Web3

def show_balance(contract, wallet, role):
    balance = contract.functions.balanceOf(wallet).call()
    symbol = contract.functions.symbol().call()
    print('{} has {} {}'.format(role, 
                                web3.fromWei(balance_sender, 'ether'), 
                                symbol))