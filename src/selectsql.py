from From import FROM

###
# SELECT class parses and stores the graph of all SELECT related data.
###
class SELECT:

    def __init__(self):
        self.FROM = []

    # this method parses the SQL query to extract SELECT related data
    def parse(self, query):
        # SELECT column1, column2, ...
        # FROM table_name
        # WHERE condition;
        query = query.split()

        # Parsing columns
        index = 1
        self.FROM.append(FROM())
        fromIndex = 0 if len(self.FROM) == 0 else len(self.FROM)-1
        column = []
        while index < len(query) and query[index].upper() != 'FROM':
            column.append(query[index])
            index += 1
        self.FROM[fromIndex].setColumn(column)

        # parsing FROM data
        # TODO handle nested statements in FROM
        index += 1
        fromData = ""
        while index < len(query) and query[index].upper() != 'WHERE':
            fromData += query[index] + " "
            index += 1
        self.FROM[fromIndex].parse(fromData.strip())

        # parsing WHERE data
        # TODO handle nested statements for WHERE
        index += 1
        whereData = ""
        while index < len(query):
            whereData += query[index] + " "
            index += 1
        self.FROM[fromIndex].poplateWhere(whereData)


    # Overriding = comparator
    def __eq__(self, other):
        # check for matching FROM nodes
        for curr in self.FROM:
            if curr in other.FROM:
                return True
        return False
