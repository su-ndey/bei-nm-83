import numpy as np

A = np.array([
    [0, 2, 1],
    [1, -2, -3],
    [2, 3, 1]
], dtype=float)

B = np.array([8, -11, -3], dtype=float)

size = len(B)
order = np.arange(size)

for k in range(size - 1):
    temp = np.abs(A[k:, k:])
    r, c = np.unravel_index(temp.argmax(), temp.shape)
    r += k
    c += k

    A[[k, r], :] = A[[r, k], :]
    B[[k, r]] = B[[r, k]]

    A[:, [k, c]] = A[:, [c, k]]
    order[[k, c]] = order[[c, k]]

    for i in range(k + 1, size):
        multiplier = A[i, k] / A[k, k]
        A[i, k:] = A[i, k:] - multiplier * A[k, k:]
        B[i] = B[i] - multiplier * B[k]

solution = np.zeros(size)

for i in range(size - 1, -1, -1):
    value = np.dot(A[i, i + 1:], solution[i + 1:])
    solution[i] = (B[i] - value) / A[i, i]

answer = np.zeros(size)

for i in range(size):
    answer[order[i]] = solution[i]

if np.allclose(answer, np.round(answer)):
    answer = np.round(answer).astype(int)

print("Solution:")
print(answer)