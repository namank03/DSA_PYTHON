graph = {
  a: ["b", "c"],
  b: ["d"],
  c: ["e", "f"],
  d: ["f"],
  e: [],
  f: [],
  k: ["p"],
};

const has_path = (graph, src, dst, set = new Set()) => {
  if (src === dst) return true;
  if (src in set) return false;
  set.add(src);
  for (let next of graph[src]) {
    if (has_path(graph, next, dst, set)) return true;
  }
  return false;
};

src = "a";
dst = "p";
res = has_path(graph, src, dst);
console.log(`res`, res);

const edge_list = [
  ["a", "b"],
  ["a", "c"],
  ["c", "d"],
  ["d", "e"],
  ["e", "f"],
  ["m", "n"],
  ["y", "z"],
];

const edge_to_graph = (edge_list) => {
  graph = {};
  for (let pair of edge_list) {
    const [a, b] = pair;
    graph[a] = graph[a] ?? [];
    graph[a].push(b);
  }
  return graph;
};

res = edge_to_graph(edge_list);
console.log(`res`, res);

const connected_comp = (graph) => {
  let count = 0;
  const visited = new Set();
  const explore = (node, visited) => {
    if (visited.has(node)) return false;
    visited.add(node);
    for (let next of graph[node] ? graph[node] : []) {
      explore(next, visited);
    }
    return true;
  };
  for (let node in graph) {
    count += explore(node, visited);
  }
  return count;
};

res = connected_comp(res);
console.log(`res`, res);

const largest_comp = (graph) => {
  let count = 0;
  const visited = new Set();
  const explore = (node, visited) => {
    if (visited.has(node)) return 0;
    visited.add(node);
    size = 1;
    for (let next of graph[node] ? graph[node] : []) {
      size += explore(next, visited);
    }
    return size;
  };
  for (let node in graph) {
    count = Math.max(explore(node, visited), count);
  }
  return count;
};

res = largest_comp(graph);
console.log(`res`, res);
