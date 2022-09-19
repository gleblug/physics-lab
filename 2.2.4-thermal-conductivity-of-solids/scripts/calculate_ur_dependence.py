import data
import plot
from approximate import approximate

x_dots = data.heat_loss['radius']
y_dots = data.heat_loss['voltage']

x_err = 2
y_err = 0.001

plot.dots_plot(x_dots, y_dots,
               x_err=x_err,
               y_err=y_err
               )

plot.show("Dependence of voltage on thermocouples on radius",
          "Radius from center, mm",
          "Voltage / sensitivity")
