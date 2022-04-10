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
    def ctl(circuit: Circuit) -> np.ndarray:
        ops = []
        for i in list(circuit.instructions):
            subops = []
            subops.append(i.operator)
            for j in i.target:
                subops.append(j)
            ops.append(subops)
        return(ops)

    def outstring(a:np.ndarray) -> (string,int):
        idx = 0
        maxi = 0
        while str(a[0])[idx] != '(':
            idx += 1

        gate = str(a[0])[:idx].lower()
        if gate == 'cnot':
            outstr = 'CX'
        elif gate == 'vi':
            outstr = 'sxdg'
        elif gate == 'v':
            outstr = 'sx'
        elif str(a[0])[idx-1].lower() == 'i':
            outstr = str(a[0])[:idx-1].lower() + 'dg'
        else:
            outstr = gate

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

    output = ''
    maxx = 0
    for a in ctl(circuit):
        output += (outstring(a)[0] + '\n')
        if outstring(a)[1] > maxx:
            maxx = outstring(a)[1]
    output = 'OPENQASM 2.0;\ninclude "qelib1.inc";\n\nqreg q['+str(maxx+1)+'];\n\n' + output

    return output
