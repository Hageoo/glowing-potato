import numpy as np
# define a 10x10 matrix to use as a key to decrypt messages
matrix = np.array([[89, 88, 9, 60, 91, 55, 34, 42, 68, 5],
[84, 43, 79, 99, 31, 59, 36, 8, 14, 26],
[82, 66, 46, 71, 33, 87, 95, 92, 70, 96],
[48, 94, 81, 45, 28, 2, 21, 63, 85, 72],
[29, 13, 20, 73, 52, 16, 27, 64, 23, 19],
[12, 30, 41, 76, 11, 75, 40, 38, 90, 86],
[49, 53, 83, 80, 25, 61, 22, 69, 44, 6],
[3, 62, 77, 7, 4, 54, 10, 100, 65, 24],
[39, 93, 50, 32, 15, 57, 35, 17, 18, 47],
[58, 97, 78, 37, 67, 74, 51, 56, 98, 1]])
# arrange the symbols in a specific sequence to provide a small extra security layer
symbols = " abcdefghijklmnñopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZáéíóúüÁÉÍÓÚÜ?!:;)(/*-_.,^<>@#'$%&[]}{+~¿¡"
