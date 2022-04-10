import json 
QASMType = str

def get_corresponding_gate(gate: str) -> str:
    try:
        json_file_path = 'qiskit_to_qasm.json'
        with open(json_file_path, 'r') as j:
             outstr = json.loads(j.read())['gates_transpilation'][gate]
    except:
        outstr = gate
    
    return outstr

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
    output = ''
    maxx = 0
    for a in ctl(circuit):
        output += (outstring(a)[0] + '\n')
        if outstring(a)[1] > maxx:
            maxx = outstring(a)[1]
    output = 'OPENQASM 2.0;\ninclude "qelib1.inc";\n\nqreg q['+str(maxx+1)+'];\n\n' + output

    return output
