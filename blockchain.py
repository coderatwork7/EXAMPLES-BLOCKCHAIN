blockchain = []

def get_last_blockchain_value():
    return blockchain[-1]

def add_value(transaction_amount ,last_transaction=[1]):
	blockchain.append([last_transaction,transaction_amount])
   
def get_user_input():
    return float(input('your transaction amount please: '))   

txamount = get_user_input() 
add_value(txamount)
txamount= get_user_input()
add_value(last_transaction = get_last_blockchain_value(),transaction_amount=txamount)
txamount= get_user_input()
add_value(txamount,get_last_blockchain_value())

print(blockchain)