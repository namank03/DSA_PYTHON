const arrr = [[1, 2, 3], 4, [5, [6, 7]], [8, 9, [10]]];
const res2 = [];
const solve2 = (arr) => {
  if (!(typeof arr === "object")) {
    return arr;
  }
  for (const el of arr) {
    const tmp = solve2(el);
    if (tmp) res2.push(tmp);
  }
};

solve2(arrr);

console.log(`res2`, res2);
