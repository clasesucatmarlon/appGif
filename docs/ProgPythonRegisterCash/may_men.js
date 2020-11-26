'use strict'

let matriz3x3 = [
  [11, 20, 3],
  [4, 135, 6],
  [7, 1, 19]
]

let may = 0;
let men = matriz3x3[0][0];

for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (matriz3x3[i][j] > may) {
      may = matriz3x3[i][j]
    } else if (matriz3x3[i][j] < men) {
      men = matriz3x3[i][j]
    }
  }
}
console.log('El mayor elemento dentro de la matriz es: ' + may)
console.log('El menor elemento dentro de la matriz es: ' + men)