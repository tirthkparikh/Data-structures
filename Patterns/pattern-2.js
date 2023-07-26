// Input: 5

// Output:
// *
// * *
// * * *
// * * * *
// * * * * *

const patern = (n) => {
  str = "* ";
  for (let i = 0; i < n; i++) {
    console.log(str);
    str += "* ";
  }
};
patern(5);
