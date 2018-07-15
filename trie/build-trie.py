#Build trie with only dict

#Init, progress, end
def buildTrie (words) :
    trie = {}
    for w in words:
        t = trie
        for c in w:
            if c not in t:
                t[c] = {} #init
            t = t[c] #progress
        t['#'] = '#' #end
    print(trie)
    print(trie.keys())

words = ['sea', 'she']

buildTrie(words)
