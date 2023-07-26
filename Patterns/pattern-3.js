// Input Format: N = 3
// Result:
// 1
// 1 2
// 1 2 3

// Input Format: N = 6
// Result:
// 1
// 1 2
// 1 2 3
// 1 2 3 4
// 1 2 3 4 5
// 1 2 3 4 5 6

const patern = (n) => {
  str = "";
  for (let i = 1; i <= n; i++) {
    str += `${i} `;
    console.log(str);
  }
};
patern(5);
