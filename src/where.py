import re

###
# Parser for WHERE part of SQL query
###
class WHERE:

    def __init__(self):
        self.attributes = []
        self.corrupted = False

    ###
    # parses the query with WHERE data
    ###
    def parse(self, queryData):
        # TODO
        # Detect multiple select statement and handle

        # no nested statments, so multiple conditions
        self.queryData = queryData
        queryData = re.split('and | or | AND | OR', queryData)

        for conditions in queryData:
            if len(conditions) <= 2: continue
            rvalue, lvalue = re.split('<|>|=| = | > | <', conditions)
            self.attributes.extend([rvalue])
            if self.checkAnamoly(rvalue, lvalue):
                self.corrupted = True

    # most of the application based attacks occurs via
    # application data is the modification of queries inattributes.
    # These can be fixed by santizing the attribute values.
    # In our attacks can be mitigated by having good parser and checking attribute rvalues.
    def checkAnamoly(self, rvalue, lvalue):
        if len(rvalue) == 0:
            return True
        if not (ord(rvalue[0]) >= ord('a') and ord(rvalue[0]) <= ord('z')) \
            or (ord(rvalue[0]) >= ord('A') and ord(rvalue[0]) <= ord('Z')):
               return True
        return False

    # Overriding == comparator
    def __eq__(self, other):
        return set(self.attributes) == set(other.attributes)
