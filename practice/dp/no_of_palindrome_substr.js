const noOfPalindrome = (s) => {
  const solve = (l, r) => {
    if (l < 0 || r >= s.length) return 0;
    if (s[l] === s[r]) return 1 + solve(l - 1, r + 1);
    else return 0;
  };
  let count = 0;
  for (let i = 0; i < s.length; i++) {
    count += solve(i, i) + solve(i, i + 1);
  }
  return count;
};

const res = noOfPalindrome("naban");
console.log(`res`, res);
