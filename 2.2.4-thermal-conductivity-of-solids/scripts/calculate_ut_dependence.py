# Calculation script
import data
import plot
from approximate import approximate
import numpy as np

u_room = 1.1405

x_dots = np.array(data.equilibrium_time['time'], dtype=np.float64)[:-1]
y_dots = np.array(u_room) - np.array(data.equilibrium_time['voltage'], dtype=np.float64)[:-1]
y_dots_log = np.log(y_dots)

x_err = 1
y_err = 0.005

x, y = approximate(x_dots, y_dots_log)

plot.dots_plot(x_dots,
               y_dots,
               x_err=x_err,
               y_err=y_err)
plot.plot(x, np.exp(y))
plot.show("The dependence of voltage on thermocouples on time (not log)",
          "Time, seconds",
          "Voltage, $mV$",
          ylog=False)
