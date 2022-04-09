from braket.circuits import Circuit

QASMType = str

def circuit_to_qasm(circuit: Circuit) -> QASMType:
    """Converts a `braket.circuits.Circuit` to an OpenQASM string.

    Args:
        circuit: Amazon Braket quantum circuit

    Returns:
        The OpenQASM string equivalent to the circuit

    Example:
        >>> from braket.circuits import Circuit
        >>> circuit = Circuit().h(0).cnot(0,1).cnot(1,2)
        >>> print(circuit)
        T  : |0|1|2|

        q0 : -H-C---
                |
        q1 : ---X-C-
                  |
        q2 : -----X-

        T  : |0|1|2|
        >>> print(circuit_to_qasm(circuit))
        OPENQASM 2.0;
        include "qelib1.inc";

        qreg q[3];

        h q[0];
        cx q[0],q[1];
        cx q[1],q[2];

    """
    result = ''

    # add version to the result string
    # add includes to the string

    # add number of registers to the string 

    for instruction in list(circuit.instructions):
        result += str(instruction.operator) + ' '
        
        for operator in instruction.target:
              result += str(operator) + ' '
        
        result += '\n'

    return result
