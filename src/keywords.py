from selectsql import SELECT
from insert import INSERT
from delete import DELETE
from update import UPDATE

###
# Keyword class takes care of objects of all keywords in SQLquery
###
class Keyword:

    def __init__(self):
        pass

    # initialize_keywords creates hashmap of all SQL keywords
    # Class variable keyword is populated with all the data.
    def initialize_keywords(self):
        # TODO configaration file to allow and disallow SQL keywords.

        # self.keyword = dict()
        #
        # self.keyword['SELECT'] = SELECT()
        # self.keyword['INSERT'] = INSERT()
        # self.keyword['CREATE'] = False
        # self.keyword['DROP'] = False
        # self.keyword['UPDATE'] = False
        # self.keyword['DELETE'] = DELETE()
        # self.keyword['TRUNCATE'] = False
        pass

    def getKeyword(self, keyword):
        if keyword == 'SELECT':
            return SELECT()
        elif keyword == 'INSERT':
            return INSERT()
        elif keyword == 'UPDATE':
            return UPDATE()
        elif keyword == 'DELETE':
            return DELETE()
        else:
            return None

    def validKeyword(self, keyword):
        return self.key in keyword

    def setKey(self, key):
        self.key = key
