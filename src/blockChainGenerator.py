import random
import csv
from blockChain import blockChain
from Block import block


def create_blockchains(dataset, numOfBlockChains : int, failedHashRate : float = 0, seed: int = 2):
    random.seed(seed)
    
    completeDataBlockChain = []

    for i in range(numOfBlockChains):
        completeDataBlockChain.append(blockChain())

    for i in range(len(dataset)):
        j = random.randint(0, numOfBlockChains - 1)
        k = random.random() >= failedHashRate
        
        curr = dataset[i]
        completeDataBlockChain[j].add_block(block(curr["amount"], curr["transaction_type"], curr["login_frequency"],
                                                    curr["session_duration"], curr["purchase_pattern"], curr["age_group"], curr["anomaly"],
                                                    completeDataBlockChain[j].get_last_block_hash() if k else completeDataBlockChain[j].get_last_block_hash()[::-1]))
    
    return completeDataBlockChain


def create_dtl_dataset_from_blockchain(a):
    completeDataDict = []
    
    chains_that_were_tampered = []

    for i in range(len(a)):
        if not a[i].is_chain_valid():
            chains_that_were_tampered.append(a[i].chain)
            continue

        for j in range(len(a[i].chain)):
            completeDataDict.append(a[i].chain[j].toDict(i))

    with open("src/dataset.csv", "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=completeDataDict[0].keys())
        writer.writeheader()
        writer.writerows(completeDataDict)
