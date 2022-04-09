# qbraid-sdk-demo

Please make sure you have installed the qbraid-sdk environment. You will just
need to follow the same procedure as
[Installing Amazon Braket in qBraid](../../qbraid_braket_setup/Install_Braket.ipynb)
but install the qbraid-SDK environment.

To access Amazon Braket devices using the qBraid SDK environment, make sure to
run `qbraid enable account qbraid_sdk`. You can refer to the
[Enable account tutorial](../../qbraid_braket_setup/Enable_account.ipynb).

## Translate your circuits from Qiskit to Amazon Braket etc.

The qbraid sdk allows users to transpile circuits from various quantum computing
frameworks including Amazon Braket, cirq, qiskit, pyquil, and PennyLane. Please
see the `qbraid_sdk_transpiler.ipynb` notebook for more information.

## Submit jobs on various simulators and backends all in one go.

With the sdk you can also submit jobs to various backends. Currently we only
support full service access to Amazon Braket ie
`qbraid enable account qbraid_sdk` will allow you to submit jobs using qBraid
credits. If you are interested in submitting jobs to say IBMQ, you will need to
include your own access key provided by IBM. Please see the `qbraid_sdk.ipynb`
notebook for more information.
