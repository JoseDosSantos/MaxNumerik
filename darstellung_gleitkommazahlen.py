import matplotlib.pyplot as plt

def get_mantisse(e, t=4):
    mant_list = [1 + 1/8 * i for i in range(2**(t-1))]
    return [2**e * m for m in mant_list]

values = {}
for e in range(-6, 8):
    values[e] = get_mantisse(e)

fig, ax = plt.subplots(nrows=2, ncols=1, figsize=[8, 10], dpi=300)
fig.suptitle("Nice plots")

subplot1 = ax[0]
for e in values:
    if e < 0:
        subplot1.scatter(values[e], values[e], label=e, s=10)
    subplot1.legend(prop={'size': 10})

subplot2 = ax[1]
for e in values:
    subplot2.scatter(values[e], values[e], label=e, s=10)
    subplot2.set_xscale('log')
    subplot2.legend(prop={'size': 10})

plt.show()