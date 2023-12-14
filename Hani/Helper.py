import pandas

duplicated = lambda data, i : data.shape[0] != data[i].nunique()
