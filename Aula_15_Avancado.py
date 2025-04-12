pip install hashlib json


import hashlib
import json
import time

class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')  # Bloco Gênesis

    def create_block(self, proof, previous_hash, data="Transação Inicial"):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': str(time.time()),
            'data': data,
            'proof': proof,
            'previous_hash': previous_hash
        }
        block['hash'] = self.hash(block)
        self.chain.append(block)
        return block

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def get_previous_block(self):
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4] == '0000':  # Critério de dificuldade
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            if self.chain[i]['previous_hash'] != self.hash(self.chain[i - 1]):
                return False
        return True

# Criando Blockchain
blockchain = Blockchain()

# Adicionando novos blocos
previous_block = blockchain.get_previous_block()
proof = blockchain.proof_of_work(previous_block['proof'])
new_block = blockchain.create_block(proof, previous_block['hash'], data="Nova Transação")

# Exibindo Blockchain
for block in blockchain.chain:
    print(json.dumps(block, indent=4))
