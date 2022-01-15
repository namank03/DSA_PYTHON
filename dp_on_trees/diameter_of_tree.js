const solve = (root, res) => {
  // base cond
  if (!root) return 0;
  l = solve(root.left, res);
  r = solve(root.right, res);
  //  agar ans nahi banna to vo tmp ans hai and hum tmp-ans hi return krte hai
  tmp_ans = 1 + Math.max(l, r);
  // ans is max of either (1+l+r) or tmp_ans
  ans = Math.max(tmp_ans, 1 + l + r);
  // update final res if required
  res = max(res, ans);
  return tmp_ans;
};

const diameterOfTree = (root) => {
  let res = -100;
  solve(root, res);
  return res;
};
