import numpy as np
import matplotlib.pyplot as plt
imgtest= np.random.randint(0,3, (160,144))
res = np.copy(imgtest)
a = np.copy(imgtest)
plt.imshow(imgtest) # Check initial image
for row in range(a.shape[0]):
    input = ''.join(a[row,:].astype(str).tolist())
res[row,:] = primero()
for col in range(a.shape[1]):
    input = ''.join(a[:,col].astype(str).tolist())
#res[value, :]
# After treatment by automata acceptance test
plt.imshow(imgtest)
21012
def primero():
    transitions = {
        'q0': {'0': 'q0', '1': 'q0', '2': '2'},
        '2': {'0': 'q0', '1': '21', '2': '2'},
        '21': {'0': '210', '1': 'q0', '2': '2'},
        '210': {'0': 'q0', '1': '2101', '2': '2'},
        '2101': {'0': 'q0', '1': 'q0', '2': '21012'},
        '21012': {'0': '21012', '1': '21012', '2': '21012'}
    }
    
