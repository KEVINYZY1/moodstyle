#coding=utf-8


__ALL__ = ["ngram2List","ngram"]
def ngram2List(content, splitor = lambda x : x.split(" ") , n = 2):
    """ngram用于文本中的处理
        test:
            >>> ngram2List("a b c d")
            [['a', 'b'], ['b', 'c'], ['c', 'd']]
            >>> ngram2List("a b c d",n=1)
            [['a'], ['b'], ['c'], ['d']]
            >>> ngram2List("a b c d",splitor = lambda x: x.split("\|"))
            ['a b c d']
    """
    if content is None:
        return []
    words = splitor(content)
    if len(words) <= 1:
        return [content]
    return [[ words[i+j] for j in range(n)] for i in range(0,len(words) - n + 1)]
    
def ngram(content, splitor = " "  , n = 2 ):
    """ngram用于文本中的处理
        test:
            >>> ngram("a b c d")
            ['a b', 'b c', 'c d']
            >>> ngram("a b c d",n=1)
            ['a', 'b', 'c', 'd']
            >>> ngram("a b c d",splitor = "  ")
            ['a b c d']
    """
    if content is None:
        return [] 
    words = content.split(splitor)
    if len(words) <= 1:
        return [content]
    result = []
    for i in range(0,len(words)-n + 1):
        result.append( splitor.join([words[i+j] for j in range(n)]))
    return result
