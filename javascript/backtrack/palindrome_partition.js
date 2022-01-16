const solve = (s) => {
  const isPalindrome = (s) => {
    return s === s.split("").reverse().join("");
  };
  const bt = (res, tmp, s) => {
    if (!s) res.push(tmp.slice());
    for (let i = 1; i <= s.length; i++) {
      const el = s.slice(0, i);
      if (isPalindrome(el)) {
        bt(res, [...tmp, el], s.slice(i));
      }
    }
  };
  let res = [];
  bt(res, [], s);
  return res;
};

const res = solve("aab");
console.log(`res`, res);
