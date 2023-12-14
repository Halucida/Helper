import pandas

def duplicated(table, i):
    if table.shape[0] == table[i].nunique():
        return "All Good !"
    result = table[table.duplicated(subset=i)]
    return result

def nullities(table):
    null_i = table.isnull().sum()
    if null_i.sum() == 0:
        return 0
    null_i = null_i[null_i != 0]
    null_i = null_i.to_frame()
    null_i.columns = ["Missing"]
    return null_i