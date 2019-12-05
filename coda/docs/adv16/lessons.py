from coda.docs.adv18.mixins.indexer import IndexerMixin
from coda.lib import Coda


class Lessons(IndexerMixin):
    def __init__(self, coda_token):
        self.coda = Coda('adv16', coda_token)
        self.table = self.coda.lessons
        self.data = self.table.rows_dict()

    def get(self, num):
        for row_id, row_data in self.data.items():
            if row_data['num'] == num:
                return row_id
        return None