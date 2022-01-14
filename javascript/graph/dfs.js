const graph = { a: ["b", "c"], b: ["d"], c: ["e"], d: ["f"], e: [], f: [] };
let res = [];
const dfs = (node) => {
  res = [...res, node];
  for (const key of graph[node]) {
    dfs(key);
  }
};

dfs("a");
console.log(`res`, res);

let res2 = [];
const bfs = (node) => {
  queue = [node];
  while (queue.length > 0) {
    node = queue.shift();
    res2 = [...res2, node];
    for (const key of graph[node]) {
      queue.push(key);
    }
  }
};

bfs("a");

console.log(`res2`, res2);

let res3 = [];
const leftView = (root, size) => {
  if (res3.length === size) {
    res3 = [...res3, root];
  }
  for (const key of graph[root]) {
    leftView(key, size + 1);
  }
};

leftView("a", 0);

console.log(`res3`, res3);

let res4 = [];
const rightView = (root, size) => {
  if (res4.length === size) {
    res4 = [...res4, root];
  }
  for (const key of graph[root].reverse()) {
    rightView(key, size + 1);
  }
};

rightView("a", 0);

console.log(`res4`, res4);

// var climbStairs = function (n) {
//   if (n === 0 || n == 1) return n;
//   return climbStairs(n - 1) + climbStairs(n - 2);
// };

const nums = [1, 2, 3, 4, 1, 2];

console.log(nums.slice(0, -2));

var rob = function (nums, memo = {}) {
  if (nums.length < 1) return 0;
  memo[nums.length] = Math.max(
    nums[nums.length - 1] + rob(nums.slice(0, -2), memo),
    rob(nums.slice(0, -1), memo)
  );
  return memo[nums.length];
};

// const r = nums.reduce((a, b) => console.log(a, b));
// console.log(`res`, r);
