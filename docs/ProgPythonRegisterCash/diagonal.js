'use strict'

let suma = 0;
let matriz3x3 = [
  [11, 2, 3],
  [4, 15, 6],
  [7, 8, 19]
]

// La diagonal principal es 11 15 y 19.  Su suma es 45

for (let i = 0; i < 3; i++) {
  for (let j = 0; j < 3; j++) {
    if (i === j) {
      // suma = suma + matriz3x3[i][j];
      suma +=  matriz3x3[i][j]; // esta es otra manera. es lo mismo de arriba

    }
  }
}
console.log(suma)
