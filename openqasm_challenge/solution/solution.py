import json 
QASMType = str

def get_corresponding_gate(gate: str) -> str:
    """
    Transpile Braket gates to OpenQASM using the qiskit_to_qasm.json file.
    
    :param gate - the lower-cased name of the gate in Braket
    :return     - the OpenQASM gate name
    """
    try:
        json_file_path = 'qiskit_to_qasm.json'
        with open(json_file_path, 'r') as j:
             outstr = json.loads(j.read())['gates_transpilation'][gate]
    except:
        outstr = gate
    
    return outstr

def ctl(circuit: Circuit) -> np.ndarray:
    """
    Brakes the circuit into an array of steps with each steps
    including the gate and the qubits acted on.
    
    :param  circuit - the Braket circuit object.
    :return         - numpy array of instructions array.
    
    Example output:
    [
        [H('qubit_count': 1), Qubit(0)],
        [Si('qubit_count': 1), Qubit(1)],
        [Rx('angle': 0.7853981633974483, 'qubit_count': 1), Qubit(0)],
        [CNot('qubit_count': 2), Qubit(0), Qubit(1)]
    ] 
    """
    ops = []
    for i in list(circuit.instructions):
        subops = []
        subops.append(i.operator)
        for j in i.target:
            subops.append(j)
        ops.append(subops)
    return(ops)

def outstring(a:np.ndarray) -> (string,int):
    """
    Generates OpenQASM instructions part.
    
    :param  a           - the Braket object
    :return (str, int)  - tuple of the whole OpenQASM 
            program containing only the instructions 
            without the headers and the number of quantum
            registers needed.
    Example output:
        \n\nh q[0];\nCX q[0],q[1];\nCX q[2],q[3];\nx q[3];\nh q[1];\ny q[4];\nsxdg q[5];\nswap q[4],q[5];\nz q[5];\nswap q[7],q[13];\n
    """
    idx = 0
    maxi = 0
    while str(a[0])[idx] != '(':
        idx += 1

    gate = str(a[0])[:idx].lower()
    outstr = get_corresponding_gate(gate)

    try:
        outstr += '('+str(a[0].angle)+') '
    except:
        outstr += ' '

    for z in range(1, len(a)):
        outstr += 'q['+str(int(a[z]))+']'
        if int(a[z]) > maxi:
            maxi = int(a[z])
        if z != len(a)-1:
            outstr += ','

    outstr += ';'
    return(outstr, maxi)

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
    output = ''
    maxx = 0
    for a in ctl(circuit):
        output += (outstring(a)[0] + '\n')
        if outstring(a)[1] > maxx:
            maxx = outstring(a)[1]
    output = 'OPENQASM 2.0;\ninclude "qelib1.inc";\n\nqreg q['+str(maxx+1)+'];\n\n' + output

    return output
