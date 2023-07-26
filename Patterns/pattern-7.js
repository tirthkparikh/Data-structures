// Input Format: N = 3
// Result:
//   *
//  ***
// *****
// Input Format: N = 6
// Result:
//      *
//     ***
//    *****
//   *******
//  *********
// ***********

const patern = (n) => {
  var str = "";
  for (let i = 0; i < n; i++) {
    for (let j = 0; j < n - i - 1; j++) {
      str += ` `;
    }
    for (let j = 0; j < 2 * i + 1; j++) {
      str += `*`;
    }

    console.log(str);
    str = "";
  }
};
patern(5);
