# 208. 实现 Trie（前缀树）
# https://leetcode.cn/problems/implement-trie-prefix-tree/
# 难度：中等
#
# 实现一个 Trie 类，包含以下方法：
#   - insert(word)：向前缀树中插入字符串 word。
#   - search(word)：返回字符串 word 是否已经插入过。
#   - startsWith(prefix)：返回是否存在以 prefix 为前缀的字符串。
#
# 示例：
# trie.insert("apple")
# trie.search("apple")    -> true
# trie.search("app")      -> false
# trie.startsWith("app")  -> true

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False  # 标记是否是某个单词的结尾


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))     # True
    print(trie.search("app"))       # False
    print(trie.startsWith("app"))   # True
    trie.insert("app")
    print(trie.search("app"))       # True
