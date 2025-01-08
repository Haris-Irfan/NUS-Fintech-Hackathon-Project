class BlockChain:
    def __init__(self, chain_type):
        if chain_type not in ["KYC", "SmartContract"]:
            raise ValueError("Invalid blockchain type. Must be 'KYC' or 'SmartContract'.")
        self.chain_type = chain_type
        self.chain = []

    def add_block(self, block_data):
        # Add block to the chain
        block = {
            "index": len(self.chain) + 1,
            "data": block_data,
        }
        self.chain.append(block)
        return block

    def get_latest_block(self):
        # Return the most recent block
        return self.chain[-1] if self.chain else None

    def get_all_blocks(self):
        # Return the entire blockchain
        return self.chain
