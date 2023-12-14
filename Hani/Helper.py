import pandas

duplicated = lambda data, i : data.shape[0] != data[i].nunique()

def nullities(table):
    null_i = table.isnull().sum()
    if null_i.sum() == 0:
        return 0
    null_i = null_i[null_i != 0]
    null_i = null_i.to_frame()
    null_i.columns = ["Missing"]
    return null_i