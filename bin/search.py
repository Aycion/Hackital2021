import sys
sys.path.insert(0, '../')


class Searcher:

    def __init__(self, pageText, searchTerm, synTerms=[]):
        self.toSearch = pageText.lower()
        self.searchTerm = searchTerm
        self.synTerms = synTerms
        self.termMatches = []
        self.synMatches = []
        match_term()

    def match_term(self):
        found = self.toSearch.find(self.searchTerm)

        while prev != -1:
            termMatches.append(found)
            found = self.toSearch.find(self.searchTerm)
