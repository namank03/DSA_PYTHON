const largestPalindrome = (s) => {
  const solve = (l, r) => {
    if (l < 0 || r >= s.length) return 0;
    if (s[l] === s[r]) return 2 + solve(l - 1, r + 1);
    else return 0;
  };
  let maxSize = 0;
  for (let i = 0; i < s.length; i++) {
    maxSize = Math.max(maxSize, solve(i, i) - 1, solve(i, i + 1));
  }
  return maxSize;
};

const res = largestPalindrome("nabanbammab");
console.log(`res`, res);
