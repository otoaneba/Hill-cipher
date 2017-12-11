import numpy as np

words = 'hill'

encrypt = [[9, 8, 5, 6],
          [6, 10, 5, 9],
          [9, 4, 8, 5],
          [6, 10, 11, 4]]

cipher = ''
length = len(encrypt)
matrix = np.array(encrypt)
arr = [ord(i) - ord('a') for i in words]
row = 0
for ch in words:
    if str.isalpha(str(ch)):
        cipher += chr(sum(matrix[row % length] * arr) % 26 + ord('a'))
        row += 1
print(cipher)
