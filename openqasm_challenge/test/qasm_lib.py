# Copyright 2022 qBraid Development Team
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator
from cirq import Circuit, LineQubit
from cirq.contrib.qasm_import import circuit_from_qasm
from cirq.testing import assert_allclose_up_to_global_phase


def qasm_to_unitary_cirq(qasm: str) -> np.ndarray:
    """Create Cirq circuit from qasm string and return its matrix rep"""
    circuit = circuit_from_qasm(qasm)
    qubits = list(circuit.all_qubits())
    qubits.sort()
    qubits = list(reversed(qubits))
    qubit_map = {str(q.name): i for i, q in enumerate(qubits)}
    mirror_circuit = Circuit()
    for opr in circuit.all_operations():
        qubit_indicies = [qubit_map[str(q.name)] for q in opr.qubits]
        mirror_qubits = [LineQubit(i) for i in qubit_indicies]
        mirror_circuit.append(opr.gate.on(*mirror_qubits))
    return mirror_circuit.unitary()


def qasm_to_unitary_qiskit(qasm: str) -> np.ndarray:
    """Create Qiskit circuit from qasm string and return its matrix rep"""
    circuit = QuantumCircuit.from_qasm_str(qasm)
    return Operator(circuit).data
