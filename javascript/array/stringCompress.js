const solve = (s) => {
  let count = 1;
  let res = "";
  for (let i = 0; i < s.length - 1; i++) {
    if (s[i] === s[i + 1]) {
      count += 1;
    } else {
      res += s[i] + count;
      count = 1;
    }
  }
  res += s[s.length - 1] + count;
  return res;
};

const res = solve("aaaaan");
console.log(`res`, res);
