import datetime


class SearchParams:
    def __init__(self, query):
        self.query = query
        self.origin = query[0:3]
        self.destination = query[4:7]
        self.date = query[7:15]
        self.count = query[15:16]

    def get_date(self):
        return datetime.datetime.strptime(self.date, '%Y%m%d').date()

    def validate(self):
        if len(self.query) != 16:
            return False
        return True
