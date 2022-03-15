import numpy as np
import matplotlib.pyplot as plt


def automata(input):
    transitions = {
        'q0': {'0': 'q8', '1': 'DEAD', '2': 'q2'},
        'q2': {'0': 'DEAD', '1': 'q3', '2': 'DEAD'},
        'q3': {'0': 'q4', '1': 'DEAD', '2': 'DEAD'},
        'q4': {'0': 'DEAD', '1': 'q5', '2': 'DEAD'},
        'q5': {'0': 'DEAD', '1': 'DEAD', '2': 'q6'},
        'q6': {'0': 'q6', '1': 'q6', '2': 'q6'},  # Final state case A
        'q8': {'0': 'q1', '1': 'DEAD', '2': 'DEAD'},
        'q1': {'0': 'q10', '1': 'q1', '2': 'q1'},
        'q10': {'0': 'q11', '1': 'q1', '2': 'q1'},
        'q11': {'0': 'q11', '1': 'q1', '2': 'q1'},  # Final state case B
        'DEAD': {'0': 'DEAD', '1': 'DEAD', '2': 'DEAD'}
    }
    actual_state = 'q0'
    for element in input:
        actual_state = transitions[actual_state][element]
    if actual_state == 'q6':
        return 2
    elif actual_state == 'q11':
        return 0
    else:
        return -1


imgtest = np.random.randint(0, 3, (160, 144))
res = np.copy(imgtest)
plt.imshow(imgtest)  # Check initial image
plt.show()
for row in range(res.shape[0]):
    input = ''.join(res[row, :].astype(str).tolist())
    valor_automata = automata(input)
    if valor_automata != -1:
        res[row, :] = str(valor_automata)
for col in range(res.shape[1]):
    input = ''.join(res[:, col].astype(str).tolist())
    valor_automata = automata(input)
    if valor_automata != -1:
        res[:, col] = str(valor_automata)

# After treatment by automata acceptance test
plt.imshow(res)
plt.show()
