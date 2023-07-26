// Input Format: N = 3
// Result:
// * * *
// * *
// *

// Input Format: N = 6
// Result:
// * * * * * *
// * * * * *
// * * * *
// * * *
// * *
// *

const patern = (n) => {
  var str = "";
  for (let i = 1; i <= n; i++) {
    for (let j = n; j >= i; j--) {
      str += "* ";
    }
    console.log(str);
    str = "";
  }
};
patern(5);
