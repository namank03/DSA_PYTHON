const arr = [4, 5, 11, -2];
const target = 3;
const res = [];
const solve = (arr, target, op = []) => {
  if (target < 0) return;
  if (target === 0) {
    res.push(op);
    return true;
  }
  for (let i = 0; i < arr.length; i++) {
    const tmp = arr[i];
    arr[i] = Number.POSITIVE_INFINITY;
    if (solve(arr, target - tmp, [...op, i])) return true;
    arr[i] = tmp;
  }
};

solve(arr, target);

console.log(`res`, res);
