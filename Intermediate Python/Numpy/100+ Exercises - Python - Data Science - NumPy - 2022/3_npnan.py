#np.isnan
'''
numpy.isnan(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj]) = <ufunc 'isnan'>
Test element-wise for NaN and return result as a boolean array.
'''
import numpy as np
A = np.array([[3, 2, 1, np.nan],
              [5, np.nan, 1, 6]])
print(np.isnan(A))