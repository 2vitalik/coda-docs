from coda.lib import Coda


class ResultsChanges:
    def __init__(self, semester, coda_token):
        self.coda = Coda('adv18', semester, coda_token)
        self.table = self.coda.results_changes
        self.data = self.table.rows_dict()

    def append(self, row_data):
        self.table.append(row_data)
