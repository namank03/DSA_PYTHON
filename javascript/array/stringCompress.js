const solve = (s) => {
  let count = 1;
  let res = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] === s[i + 1]) {
      count += 1;
    } else {
      res += s[i] + count;
      count = 1;
    }
  }
  return res;
};

const res = solve("aaaaa");
console.log(`res`, res);
