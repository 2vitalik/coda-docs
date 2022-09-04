from coda.docs.adv20.mixins.indexer import IndexerMixin
from coda.lib import Coda


class Lessons(IndexerMixin):
    def __init__(self, semester, coda_token):  # move all to class attributes
        self.coda = Coda('tt-21', semester, coda_token)
        self.table = self.coda.table('Все занятия')
        self.data = self.table.rows_dict()

    def get(self, type, num):
        for row_id, row_data in self.data.items():
            if row_data['Вид занятия'] == type and row_data['#'] == num:
                return row_id
        return None
