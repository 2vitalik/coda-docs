from coda.docs.adv19.mixins.indexer import IndexerMixin
from coda.lib import Coda


class Lessons(IndexerMixin):
    def __init__(self, semester, coda_token):
        self.coda = Coda('adv18', semester, coda_token)
        self.table = self.coda.table('Все занятия')
        self.data = self.table.rows_dict()

    def get(self, discipline, type, num):
        for row_id, row_data in self.data.items():
            if row_data['Предмет'] == discipline \
                    and row_data['Вид занятия'] == type \
                    and row_data['#'] == num:
                return row_id
        return None
