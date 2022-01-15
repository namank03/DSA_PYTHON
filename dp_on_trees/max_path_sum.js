const solve2 = (root, res) => {
  // base cond
  if (!root) return 0;
  l = solve(root.left, res);
  r = solve(root.right, res);
  //! there are 2 conditions in cal the tmp ans here. if max(l,r) is < 0 then it makes no sense to add the result into root.val as it'll only gonna dec it's value
  tmp_ans = Math.max(root.val + Math.max(l, r), root.val);
  ans = Math.max(tmp_ans, root.val + l + r);
  // update final res if required
  res = max(res, ans);
  return tmp_ans;
};

const maxPathSum = (root) => {
  let res = -100;
  solve(root, res);
  return res;
};
