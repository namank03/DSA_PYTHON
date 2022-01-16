const s = "namnakloputran";
const solve = (s) => {
  let [i, j] = [0, 0];
  let maxSize = 0;
  let map = {};
  while (j < s.length) {
    map[s[j]] = map[s[j]] ? map[s[j]] + 1 : 1;
    if (Object.keys(map).length === j - i + 1) {
      maxSize = Math.max(maxSize, j - i + 1);
      console.log(`s.slice(i,j+1)`, s.slice(i, j + 1));
    } else if (Object.keys(map).length < j - i + 1) {
      while (Object.keys(map).length < j - i + 1) {
        map[s[i]] = map[s[i]] === 0 ? delete map[s[i]] : map[s[i]] - 1;
        i += 1;
      }
    }
    j += 1;
  }
  return maxSize;
};

const res = solve(s);
console.log(`res`, res);
