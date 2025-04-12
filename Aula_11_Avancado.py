pip install qiskit

import numpy as np
from qiskit import QuantumCircuit, Aer, transpile, assemble, execute

# Tamanhos das chaves
n = 10  # Para simulação rápida, usar valores pequenos; na prática, muito maiores

# Alice gera bits aleatórios
alice_bits = np.random.randint(2, size=n)

# Alice escolhe bases aleatórias (0 = base computacional, 1 = base Hadamard)
alice_bases = np.random.randint(2, size=n)

# Bob escolhe bases aleatórias para medição
bob_bases = np.random.randint(2, size=n)

# Criar o circuito quântico para enviar os qubits
qubits = []
for i in range(n):
    qc = QuantumCircuit(1, 1)  # Um qubit e um bit clássico
    if alice_bits[i] == 1:
        qc.x(0)  # Aplica porta X (NOT) se o bit for 1
    if alice_bases[i] == 1:
        qc.h(0)  # Aplica porta Hadamard se a base escolhida for Hadamard
    qubits.append(qc)

# Simulação da transmissão dos qubits (potencial espionagem de Eve)
eve_intercept = np.random.choice([True, False], size=n, p=[0.2, 0.8])  # 20% das mensagens interceptadas

# Bob mede os qubits na base escolhida
backend = Aer.get_backend('qasm_simulator')
bob_results = []
for i in range(n):
    qc = qubits[i]
    if eve_intercept[i]:  # Se Eve interceptou, há risco de alteração do estado
        qc.measure(0, 0)
        job = execute(qc, backend, shots=1)
        result = job.result()
        measured_value = int(list(result.get_counts())[0])  # Obtém resultado da medição
        if np.random.rand() < 0.5:  # 50% de chance de erro devido à medição de Eve
            measured_value = 1 - measured_value
        bob_results.append(measured_value)
    else:
        if bob_bases[i] == 1:
            qc.h(0)  # Aplicar Hadamard novamente se Bob usar base Hadamard
        qc.measure(0, 0)
        job = execute(qc, backend, shots=1)
        result = job.result()
        measured_value = int(list(result.get_counts())[0])  # Obtém resultado da medição
        bob_results.append(measured_value)

# Criar chave compartilhada comparando apenas onde as bases de Alice e Bob coincidem
shared_key_alice = []
shared_key_bob = []
for i in range(n):
    if alice_bases[i] == bob_bases[i]:  # Apenas bits onde as bases coincidem são válidos
        shared_key_alice.append(alice_bits[i])
        shared_key_bob.append(bob_results[i])

# Comparação da chave final
print("Chave gerada por Alice:", shared_key_alice)
print("Chave gerada por Bob:  ", shared_key_bob)

# Detectar possíveis interferências (ataque de Eve)
error_rate = sum(a != b for a, b in zip(shared_key_alice, shared_key_bob)) / len(shared_key_alice)
if error_rate > 0.1:
    print("ALERTA: Possível interceptação detectada! Erro na chave acima do esperado.")
else:
    print("Chave segura estabelecida com sucesso.")


