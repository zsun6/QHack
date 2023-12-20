from qiskit import Aer, QuantumCircuit, transpile, assemble
from qiskit.visualization import plot_histogram
from qiskit.quantum_info import Statevector
from qiskit.providers.aer import AerSimulator
from qiskit.algorithms import Grover, AmplificationProblem
from qiskit.circuit.library import PhaseOracle

# Define the oracle for the problem
compromised_code = '101'  # This is the code we're looking for
oracle = PhaseOracle(f'~x0 & x1 & ~x2')  # Represents the code 101

# Create Grover's algorithm object
grover = Grover(quantum_instance=Aer.get_backend('aer_simulator'))

# Create an Amplification problem
problem = AmplificationProblem(oracle, is_good_state=oracle.evaluate_bitstring)

# Use Grover's algorithm to find the solution
result = grover.amplify(problem)

# Print the result
print("Result:", result)

# Visualization
sv_sim = AerSimulator(method='statevector')
qc = QuantumCircuit(3)
qc.compose(oracle, inplace=True)
qc = transpile(qc, sv_sim)
qobj = assemble(qc)
statevector = sv_sim.run(qobj).result().get_statevector()
plot_histogram(statevector.probabilities_dict())
