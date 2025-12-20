import numpy as np

def zero(coe):
    coe = np.array([float(c) for c in coe])
    roots = np.roots(coe)
    real_roots = []
    for r in roots:
        if abs(r.imag) < 1e-7:
            real_roots.append(round(float(r.real), 6))
    if len(real_roots) == 0:
        return 0
    real_roots = list(set(real_roots))
    return real_roots