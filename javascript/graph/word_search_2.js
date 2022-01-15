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
