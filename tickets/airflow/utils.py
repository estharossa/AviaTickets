class SearchParams:
    def __init__(self, query):
        self.origin = query[0:3]
        self.destination = query[4:7]
        self.date = query[7:15]
        self.adults = query[15:16]
        self.childs = query[16:17]
        self.infants = query[17:18]
        self.youths = query[18:19]
