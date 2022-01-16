class TrieNode {
  constructor() {
    this.children = {};
    this.isWord = false;
  }

  insert(word) {
    let cur = this;
    for (const ch of word) {
      if (!(ch in cur.children)) {
        cur.children[ch] = new TrieNode();
      }
      cur = cur.children[ch];
    }
    cur.isWord = word;
  }
}

trie = new TrieNode();
trie.insert("Naman");
trie.insert("Name");
trie.insert("rand");

const graph = [
  ["N", "a", "m", "e"],
  ["a", "b", "a", "d"],
  ["c", "d", "n", "p"],
  ["c", "d", "n", "p"],
];

const dfs = (i, j, trie) => {
  if (trie.isWord) {
    console.log(`trie.isWord`, trie.isWord);
    trie.isWord = false;
  }
  if (i < 0 || i >= graph.length || j < 0 || j >= graph[0].length) {
    return;
  }

  tmp = graph[i][j];
  trie = trie.children[tmp];
  if (!trie) return;
  graph[i][j] = "#";
  for (let [dx, dy] of [
    [1, 0],
    [0, 1],
    [-1, 0],
    [0, -1],
  ]) {
    dfs(i + dx, j + dy, trie);
  }
  graph[i][j] = tmp;
};

const solve = (graph, trie) => {
  for (let i = 0; i < graph.length; i++) {
    for (let j = 0; j < graph[0].length; j++) {
      if (graph[i][j] in trie.children) {
        dfs(i, j, trie);
      }
    }
  }
};

solve(graph, trie);
