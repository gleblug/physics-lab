from plot import Plot
import pandas as pd
import numpy as np

exps = ['22', '34', '44', '55']
graph = Plot(f"Dependence ln(U) on time")

for i in exps:
    data = pd.read_csv(f"{i}.csv")

    x = np.array(data["time"])
    y = np.array(data["voltage"])
    
    graph.dots(x, np.log(y))
    graph.plot(x, np.log(y), label=f"{i} torr")

graph.show(xlabel="time", ylable="log(voltage)")
graph.save()
