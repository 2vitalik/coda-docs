from coda.lib import Coda


class Contests:
    def __init__(self, semester, coda_token):
        self.coda = Coda('tt-22', semester, coda_token)
        self.table = self.coda.contests
        self.data = self.table.rows_dict()
