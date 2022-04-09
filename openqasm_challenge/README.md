# qBraid OpenQASM Parser Challenge

<a href="https://qbraid.com/">
    <img src="_static/logo.png"
         alt="qbraid logo"
         width="210px"
         align="right">
</a>

Welcome to the [QCHack](https://www.quantumcoalition.io/) qBraid <> Braket OpenQASM challenge!


## Background


The Open Quantum Assembly Language (OpenQASM) is an imperative programming language designed for near-term quantum computing algorithms and applications. Its main goal is to serve as an intermediate representation for higher-level compilers to communicate with quantum hardware.

Recently, Amazon Braket added OpenQASM support for gate-based quantum devices and simulators, see [Running your circuits with OpenQASM 3.0](https://docs.aws.amazon.com/braket/latest/developerguide/braket-openqasm.html). This new integration allows creating and submitting quantum tasks directly from OpenQASM programs.

## Challenge

In this challenge, you will attempt to 'reverse engineer' this quantum protocol. Namely, you will build a program that disects pythonic quantum circuit objects into parameterized sets of physical logic gates.

```python
from braket.circuits import Circuit

def circuit_to_qasm(circuit: Circuit) -> str:
    """Converts a `braket.circuits.Circuit` to an OpenQASM string.

    Args:
        circuit: Amazon Braket quantum circuit

    Returns:
        The OpenQASM string equivalent to the circuit

    """

    return NotImplemented
```

## Toy example

```python
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
```

## Scope

Given the time constrains of the hackathon, don't worry about processing [result types](https://github.com/aws/amazon-braket-sdk-python/blob/0d28a8fa89263daf5d88bc706e79200d8dc091a8/src/braket/circuits/result_types.py) or [noise](https://github.com/aws/amazon-braket-sdk-python/blob/0d28a8fa89263daf5d88bc706e79200d8dc091a8/src/braket/circuits/noise.py). Instead, you can focus on gate-based operators and instructions.

Additionally, we encourage participants to implement solutions using OpenQASM 2.0 for ease of testing and compatibility with other frontend quantum modules. OpenQASM 3 is backwards compatible with OpenQASM 2.0, so your
parser may still have a long and full life. However, if the additional challenge sounds enticing, these [qiskit docs](https://qiskit.github.io/openqasm/index.html) are a good place to start. In the `test` directory, we've included a couple unit-tests that interface with the `cirq` and `qiskit` qasm converters to help get you started.

## Judging

A seperate auto-grader, similar but not equivalent to the test directory, will be used to grade your submission. Well-implemented programs should be able to interface with other qasm parsers to a certain degree, although full-coverage is not expected. However, competitive submissions will demonstrate unitary equivalance up to a global phase for input-output programs over most common / standard gate sets, and implement backstops / error handling to ensure program completion when exceptions do arise.

Exactly one member of your team should submit the URL/link to your team’s forked repository via the [QCHack 2022 Challenge Submission Form](https://forms.gle/rBW6tDC8hjW35Lc76). Feel free to reach out on the `#qbraid` Discord channel with any questions or clarifications. Good luck!
