import numpy as np

a = 2
b = 8

tolerance = 0.1


def Q(t):
    return 8 + 5 * np.cos(0.4 * t)**2


def c(t):
    return 5 * np.exp(-0.5 * t) + 3 * np.exp(0.15 * t)

def f(t):
    return Q(t) * c(t)


I = np.zeros((5, 5))



n = 1
h = (b - a) / n

I[0, 0] = h / 2 * (f(a) + f(b))


for i in range(1, 5):

    n = 2**i
    h = (b - a) / n

    summation = 0

    for j in range(1, n):

        t = a + j * h

        summation = summation + f(t)

    I[i, 0] = h / 2 * (
        f(a) + f(b) + 2 * summation
    )


for k in range(1, 5):

    for i in range(0, 5-k):

        I[i, k] = (
            4**k * I[i+1, k-1]
            - I[i, k-1]
              ) / (4**k - 1)


print("\nTRAPEZOIDAL VALUES")
print("--------------------------------")

for i in range(5):

    print(
        "I({},1) = {:.6f}".format(
            i + 1,
            I[i, 0]
        )
    )


print("\nROMBERG VALUES")
print("--------------------------------")

for k in range(1, 5):

    print(
        "I(1,{}) = {:.6f}".format(
            k + 1,
            I[0, k]
        )
    )

    if k < 4:

        print(
            "I(2,{}) = {:.6f}".format(
                k + 1,
                I[1, k]
            )
        )


print("\n==============================================")
print("              ROMBERG TABLE")
print("==============================================")

for i in range(5):

    for j in range(5 - i):

        print(
            "{:.6f}".format(I[i, j]),
            end="        "
        )

    print()


print("\n==============================================")
print("               ERROR CHECK")
print("==============================================")


error_2 = abs(
    (I[0, 1] - I[1, 0]) / I[0, 1]
) * 100

print(
    "Ea for I(1,2) = {:.6f}%".format(
        error_2
    )
)


error_3 = abs(
    (I[0, 2] - I[1, 1]) / I[0, 2]
) * 100

print(
    "Ea for I(1,3) = {:.6f}%".format(
        error_3
    )
)



error_4 = abs(
    (I[0, 3] - I[1, 2]) / I[0, 3]
) * 100

print(
    "Ea for I(1,4) = {:.6f}%".format(
        error_4
    )
)


error_5 = abs(
    (I[0, 4] - I[1, 3]) / I[0, 4]
) * 100

print(
    "Ea for I(1,5) = {:.6e}%".format(
        error_5
    )
)


print("\n==============================================")
print("              FINAL RESULT")
print("==============================================")

print("Tolerance =", tolerance, "%")

print(
    "Final value = I(1,5) = {:.6f} mg".format(
        I[0, 4]
    )
)

print(
    "Final error = {:.6e}%".format(
        error_5
    )
)

print(
    "\nMass transported = {:.6f} mg".format(
        I[0, 4]
    )
)
