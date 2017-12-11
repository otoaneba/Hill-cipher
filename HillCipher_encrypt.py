import numpy as np

words = 'hill'

secret = [[9, 8, 5, 6],
          [6, 10, 5, 9],
          [9, 4, 8, 5],
          [6, 10, 11, 4]]

cipher = ''
length = len(secret)
matrix = np.array(secret)
arr = [ord(i) - ord('a') for i in words]
count = 0
for ch in words:
    if str.isalpha(str(ch)):
        cipher += chr(sum(matrix[count % length] * arr) % 26 + ord('a'))
        count += 1
print(cipher)
