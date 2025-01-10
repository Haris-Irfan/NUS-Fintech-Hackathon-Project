import random
from blockChain import blockChain
from Block import block
from predictor import make_prediction
from blockChainGenerator import *
import csv

def get_new_demo_blockchains(chain_length : int, seed : int):
    chain = blockChain()
    random.seed(seed)

    txn = ["sale", "purchase", "transfer", "scam", "phishing"]
    ptn = ["high_value", "random", "focused"]
    age = ["veteran", "new", "established"]
    
    for i in range(chain_length):
        chain.add_block(
            block(random.randint(0, 2000),
                  txn[random.randint(0, 4)],
                  random.randint(1, 8),
                  random.randint(20, 159),
                  ptn[random.randint(0, 2)],
                  age[random.randint(0, 2)],
                  "NA",
                  chain.get_last_block_hash())
        )
    
    return chain

def diy_blockchain(arr):
    chain = blockChain()
    for i in range(3):
        chain.add_block(
            block(arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4], arr[i][5], "NA", chain.get_last_block_hash)
        )
    return chain


def main():
    with open("src/metaverse_transactions_dataset.csv", 'r', newline='') as file:
        reader = csv.DictReader(file)
        data = [row for row in reader]

    create_dtl_dataset_from_blockchain(create_blockchains(data, 20, 0.00005, 10))


    create_own = 0
    while create_own != "y" and create_own != "n":
        create_own = input("Would you like to create your own blockchain of length 3? y for Yes or n for No. ")

    if create_own =='n':
        num_of_blocks = int(input("How many transactions to analyse in the blockchain? "))
        seed = int(input("What randomised seed would you like to use? "))
        chain = get_new_demo_blockchains(num_of_blocks, seed)
    else:
        txn_choice = ["sale", "purchase", "transfer", "scam", "phishing"]
        ptn_choice = ["high_value", "random", "focused"]
        age_choice = ["veteran", "new", "established"]
        a = []
        for i in range(3):
            amt, txn, freq, dur, ptn, age = -1, -1, -1, -1, -1, -1

            while amt < 0 or amt > 2000:
                amt = int(input(f"Enter block {i}'s transaction amount (integer from 0 to 2000): "))
            while txn not in txn_choice:
                txn = input(f"Choose block {i}'s transaction type from these: sale, purchase, transfer, scam, phishing. ")
            while freq < 0 or freq > 20:
                freq = int(input(f"Enter block {i}'s user login frequency (integer from 0 to 20): "))
            while dur < 0 or dur > 300:
                dur = int(input(f"Enter block {i}'s user last session duration (integer from 0 to 300): "))
            while ptn not in ptn_choice:
                ptn = input(f"Choose block {i}'s user purchase pattern from these: high_value, random, focused. ")
            while age not in age_choice:
                age = input(f"Choose block {i}'s user age from these: veteran, new, established. ")

            a.append([amt, txn, freq, dur, ptn, age])
        
        chain = diy_blockchain(a)

    # high, low, moderate
    classified_risk = [0, 0, 0]

    for i in range(len(chain.chain)):
        block = chain.chain[i]
        print("Block's transaction information: ", block.amount, block.txn_type, block.login_freq, block.sess_dur, block.pattern, block.age)
        prediction = make_prediction(int(block.amount), block.txn_type, block.login_freq, block.sess_dur, block.pattern, block.age)
        print(['High Risk', 'Low Risk', 'Moderate Risk'][prediction])
        classified_risk[prediction] += 1

    print(f"There were {classified_risk[0]} high risk transactions, {classified_risk[2]} moderate risk transactions and {classified_risk[1]} low risk transactions")

main()