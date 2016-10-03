from trie import Trie


class Autocomplete(object):
    """Create autocomplete class"""
    def __init__(self, words_list, max_completions=5):
        """creates words and sets up max of 5 completions."""
        self.trie = Trie(iterable=words_list)
        self.max_completions = max_completions

    def __call__(self, item=None):
        result = []
        count = 0
        if item and isinstance(item, type('alpha')):
            for w in self.trie.traversal(item[0]):
                if count < self.max_completions:
                    if w.startswith(item):
                        result.append(w)
                        count += 1
        return result
