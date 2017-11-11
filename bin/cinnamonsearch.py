import sys
sys.path.insert(0, '../')
from ThesaurusAPI.thesaurus import Word

class Query:

    def __init__(self, query, pos = -1):
        print (query)
        if len(query.split()) != 1:
            raise ValueError("Query should only one word.")
        self.query = query
        singleWord = self.query
        self.search = Word(singleWord)
        print (singleWord)
        if pos == -1:

            self.syns = self.search.synonyms()
        else:
            self.syns = self.search.synonyms('all', partOfSpeech=pos)
