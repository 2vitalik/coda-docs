from coda.docs.adv19.mixins.indexer import IndexerMixin
from coda.lib import Coda


class Students(IndexerMixin):  # todo: some common base class?
    def __init__(self, semester, coda_token, skip_load_data=False):  # todo: default: True?
        self.coda = Coda('adv17', semester, coda_token)
        self.table = self.coda.table('Все студенты')
        self.data = self.load_data() if not skip_load_data else None
        self.indexes = {}  # todo: move to indexer mixin
        self.add_index('telegram')

    def load_data(self):
        return self.table.rows_dict()

    def reload_data(self):
        self.data = self.load_data()

    def value(self, field, row_id):
        return self.data.get(row_id, {}).get(field)

    def by_telegram_id(self, telegram_id):
        return self.find('telegram', telegram_id)

    def update(self, row_id, changes):  # todo: move to common base class
        self.table.update(row_id, changes)
