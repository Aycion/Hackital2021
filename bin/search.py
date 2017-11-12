import sys
sys.path.insert(0, '../')


class Searcher:

    def __init__(self, pageText, searchTerm, synTerms=[]):
        self.toSearch = pageText.lower()
        self.searchTerm = searchTerm
        self.synTerms = synTerms
        self.termMatches = []
        self.synMatches = []
        self.match_term()
        if synTerms: match_synonyms()

    def match_term(self):
        found = self.toSearch.find(self.searchTerm)
        while found != -1:
            self.termMatches.append(found)
            found = self.toSearch.find(self.searchTerm, found+1)

    #def match_synonyms(self):

        #for syn in synTerms:
