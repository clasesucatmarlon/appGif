'use strict'

let array1 = [
  [11, 20, 3],
  [4, 135, 6],
  [7, 1, 19]
]

let array2 = [
   [9, 20, 3],
   [4, 135, 66],
   [7, 10, 20]
 ]

 let suma = 0;
 let arraySuma = [];

 for (let i = 0; i < 3; i++) {
   for (let j = 0; j < 3; j++) {
      arraySuma.push(array1[i][j] + array2[i][j]); 
   }
 }

 console.log('La matriz suma es: ' + arraySuma);