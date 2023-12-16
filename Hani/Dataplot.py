import matplotlib.pyplot as plt
import seaborn; seaborn.set_style('whitegrid')

def sinplot(data, label, title):
  timp = data[label].value_counts()
  timp_plot = timp.plot.bar(title=title, rot=0)
  timp_plot.bar_label(timp_plot.containers[0]);
