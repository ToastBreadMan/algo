import matplotlib.pyplot as plt

fig, ax = plt.subplots()

def calc(num, recursion):
    x.append(num)
    y.append(recursion)
    if num == 1:
        return recursion
    if num % 2 == 0:
        return calc(num / 2, recursion+1)
    else:
        return calc(num * 3 + 1, recursion+1)


for i in range(20, 40):
    x = []
    y = []
    print(i, calc(i, 0))
    plt.plot(y, x)
plt.show()