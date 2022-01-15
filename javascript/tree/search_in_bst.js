class Node {
  constructor(val) {
    this.val = val;
    this.left = null;
    this.right = null;
  }
}

node1 = new Node(2);
node2 = new Node(1);
node3 = new Node(3);
node4 = new Node(-4);
node5 = new Node(-3);

node1.left = node2;
node1.right = node3;
node2.left = node4;
node3.right = node5;

const search_val = 6;

const search_in_bst = (root, target) => {
  if (!root) return false;
  if (root.val === target) return true;
  if (root.val > target) return search_in_bst(root.left, target);
  else return search_in_bst(root.right, target);
};

const resul = search_in_bst(node1, 6);
console.log(`resul`, resul);

const insert_in_st = (root, target) => {
  if (!root) return new Node(target);
  else {
    if (root.val > target) {
      root.left = insert_in_st(root.left, target);
    } else {
      root.right = insert_in_st(root.right, target);
    }
  }
  return root;
};

insert_in_st(node1, -10);

const result = [];

const solve = (root) => {
  if (!root) return;
  result.push(root.val);
  solve(root.left);
  solve(root.right);
};

solve(node1);

console.log(`result`, result);

const same_tree = (root1, root2) => {
  if (root1 && !root2) return false;
  if (root2 && !root1) return false;
  if (!root1 && !root2) return true;
  return (
    root1.val === root2.val &&
    same_tree(root1.left, root2.left) &&
    same_tree(root1.right, root2.right)
  );
};

const size_of_tree = (root) => {
  if (!root) return 0;
  return 1 + size_of_tree(root.left) + size_of_tree(root.right);
};

res = size_of_tree(node1);
console.log(`res`, res);

const height_of_tree = (root) => {
  if (!root) return 0;
  return 1 + Math.max(height_of_tree(root.left), height_of_tree(root.right));
};

res = height_of_tree(node1);
console.log(`res`, res);

const root_to_leef_sum = (root, target) => {
  //   if (!root.left && !root.right && root.value === target) return true;
  if (!root) {
    if (target === 0) return true;
    else return false;
  }
  if (
    root_to_leef_sum(root.left, target - root.val) ||
    root_to_leef_sum(root.right, target - root.val)
  )
    return true;
  else return false;
};

// res = root_to_leef_sum(node1, 10);
// console.log(`res`, res);

res = root_to_leef_sum(node1, -11);
console.log(`res`, res);

//! the below code is wrong
// const check_if_bst = (root) => {
//   if (!root) return true;
//   else {
//     if (root?.left.val > root.val || root?.right.val < root.val) false;
//     else return true;
//   }
//   return check_if_bst(root.left) && check_if_bst(root.right);
// };

// res = check_if_bst(node1);
// console.log(`res`, res);
