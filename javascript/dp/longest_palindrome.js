const solve = (s) => {
  let maxStr = "";
  const maxPalindrome = (i, j) => {
    while (i >= 0 && j < s.length && s[j] === s[i]) {
      i--;
      j++;
    }
    const str = s.slice(i + 1, j);
    maxStr = maxStr.length > str.length ? maxStr : str;
  };
  for (let i = 0; i < s.length; i++) {
    maxPalindrome(i, i);
    maxPalindrome(i, i + 1);
  }
  return maxStr;
};

const res = solve("namanam");
console.log(`res`, res);
