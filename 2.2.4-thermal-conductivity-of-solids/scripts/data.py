import pandas as pd

# ======================================================================================================================
# Time of establishment of thermal equilibrium
# ======================================================================================================================
equilibrium_time = pd.read_csv("time_of_establishment.csv")

# ======================================================================================================================
# Voltage on radius dependence
# ======================================================================================================================
heat_loss = pd.read_csv("voltage_on_radius.csv")
heat_loss['voltage'] = heat_loss['voltage'] / heat_loss['sensitivity']
