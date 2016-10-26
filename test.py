print('Fuck You World!')

import numpy as np

def circumference(r):
    circ = 2. * np.pi * r
    print('The circumference is', circ)
    
def area(r):
    """This is apparently a docstring. We are confused"""
    surface = np.pi * r**2
    print('The surface is', surface)
    