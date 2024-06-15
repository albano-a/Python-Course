import numpy as np

numeros = np.linspace(0, 10, 60)  # 10 é inclusivo
# print(numeros)

num = np.arange(0, 10, 2)  # 10 é exclusivo
print(num)

arr = np.array(
    [
        [1, 2, 3],
        [3, 4, 5],
        [7, 8, 9],
    ]
)
arr2 = np.array(
    [
        [1, 2, 3],
        [3, 4, 5],
        [7, 8, 9],
    ]
)

print(np.dot(arr, arr2))
