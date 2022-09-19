from matplotlib import pyplot as plt

fig = plt.figure(figsize=(5.5, 4))


def dots_plot(x, y, x_err=0, y_err=0, label=''):
    plt.errorbar(x, y, fmt=".r", xerr=x_err, yerr=y_err, label=label)


def plot(x, y, label=''):
    plt.errorbar(x, y, label=label, color='blue')


def show(title='', xlabel='', ylable='', ylog=False, xlog=False):
    plt.grid(linestyle='--', which='major')
    plt.grid(linestyle=':', which='minor')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylable)

    if ylog:
        plt.yscale("log")
    if xlog:
        plt.xscale("log")

    plt.savefig('out/' + title)
    plt.show()
