const arr = [2, 1, 0, 3, 4];

const solve = (arr) => {
  let [stack, res] = [[], []];
  const top = (stack) => stack[stack.length - 1];
  for (let i = arr.length - 1; i > -1; i--) {
    if (!stack[i]) res.push(-1);
    else if (top(stack) < arr[i]) {
      res.push(top(stack));
    } else if (!stack || top(stack) >= arr[i]) {
      while (!stack || top(stack) >= arr[i]) {
        stack.pop();
      }
      !stack ? res.push(-1) : res.push(top(stack));
    }
    stack.push(arr[i]);
  }
  return res.reverse();
};

const res = solve(arr);
console.log(`res`, res);
