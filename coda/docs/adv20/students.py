from coda.docs.adv20.mixins.indexer import IndexerMixin
from coda.lib import Coda


class Students(IndexerMixin):  # todo: some common base class?
    def __init__(self, semester, coda_token, skip_load_data=False):  # todo: default: True?
        self.coda = Coda('adv20', semester, coda_token)
        self.table = self.coda.table('Все студенты')
        self.data = self.load_data() if not skip_load_data else None
        self.indexes = {}  # todo: move to indexer mixin
        self.add_index('Яндекс-аккаунт')
        self.add_index('Codeforces-аккаунт')
        self.add_index('telegram')

    def load_data(self):
        return self.table.rows_dict()

    def reload_data(self):
        self.data = self.load_data()

    def value(self, field, row_id):
        return self.data.get(row_id, {}).get(field)

    # todo: decorator -- if no data -- reload_data()
    def by_yandex(self, yandex_account):  # todo: universalize methods by __getattr__
        return self.find('Яндекс-аккаунт', yandex_account)

    def by_codeforces(self, codeforces_account):
        return self.find('Codeforces-аккаунт', codeforces_account)

    def by_telegram_id(self, telegram_id):
        return self.find('telegram', telegram_id)

    def update(self, row_id, changes):  # todo: move to common base class
        self.table.update(row_id, changes)

    def filtered_data(self, fields):  # useless?
        return {
            row_id: {
                field: row_data[field]
                for field in fields
            }
            for row_id, row_data in self.data.items()
        }
