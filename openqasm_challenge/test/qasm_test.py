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

from typing import Tuple
import pytest
import numpy as np
from braket.circuits import Circuit
from braket.circuits.unitary_calculation import calculate_unitary
from solution import circuit_to_qasm
from .qasm_lib import (
    qasm_to_unitary_cirq,
    qasm_to_unitary_qiskit,
    assert_allclose_up_to_global_phase,
)


def braket_ghz() -> Tuple[Circuit, np.ndarray]:
    """Returns gzh circuit and its unitary"""

    circ = Circuit()

    circ.h(0)
    circ.cnot(0, 1)
    circ.cnot(1, 2)

    unitary = calculate_unitary(circ.qubit_count, circ.instructions)

    return circ, unitary


def braket_fourteen() -> Tuple[Circuit, np.ndarray]:
    """Returns circuit with 14 unique gates and its unitary"""

    circ = Circuit()

    circ.h([0, 1, 2, 3])
    circ.x([0, 1])
    circ.y(2)
    circ.z(3)
    circ.s(0)
    circ.si(1)
    circ.t(2)
    circ.ti(3)
    circ.rx(0, np.pi / 4)
    circ.ry(1, np.pi / 2)
    circ.rz(2, 3 * np.pi / 4)
    circ.v(0)
    circ.vi(1)
    circ.cnot(0, 1)

    unitary = calculate_unitary(circ.qubit_count, circ.instructions)

    return circ, unitary


test_data = [braket_ghz(), braket_fourteen()]


@pytest.mark.parametrize("circuit,unitary_expected", test_data)
def test_consistency_qasm_to_cirq_unitary(circuit, unitary_expected):
    """Test consistensy with cirq qasm parser"""
    qasm_str = circuit_to_qasm(circuit)
    unitary_test = qasm_to_unitary_cirq(qasm_str)
    assert_allclose_up_to_global_phase(unitary_test, unitary_expected, atol=1e-7)


@pytest.mark.parametrize("circuit,unitary_expected", test_data)
def test_consistency_qasm_to_qiskit_unitary(circuit, unitary_expected):
    """Test consistensy with qiskit qasm parser"""
    qasm_str = circuit_to_qasm(circuit)
    unitary_test = qasm_to_unitary_qiskit(qasm_str)
    assert_allclose_up_to_global_phase(unitary_test, unitary_expected, atol=1e-7)
