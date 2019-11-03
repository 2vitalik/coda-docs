from coda.lib import Coda


class Students:  # todo: some common base class?
    def __init__(self, coda_token, skip_load_data=False):
        self.coda = Coda('adv18', coda_token)
        self.table = self.coda.students
        self.data = self.load_data() if not skip_load_data else None
        self.indexes = {}
        self.add_index('yandex_account')

    def load_data(self):
        return self.table.rows_dict()

    def reload_data(self):
        self.data = self.load_data()

    def add_index(self, field):
        index = {}
        for row_id, row_data in self.data.items():
            value = row_data[field]
            if value in index:
                # todo: raise exception
                return False
            index[value] = row_id
        self.indexes[field] = index
        return True

    def value(self, field, row_id):
        return self.data.get(row_id, {}).get(field)

    def find(self, field, value):
        if field in self.indexes:
            return self.indexes[field].get(value)
        for row_id, row_data in self.data.items():
            if row_data[field] == value:
                return row_id
        return None

    def by_yandex(self, yandex_account):
        return self.find('yandex_account', yandex_account)

    def update(self, row_id, changes):
        self.table.update(row_id, changes)

    def filtered_data(self, fields):  # useless?
        return {
            row_id: {
                field: row_data[field]
                for field in fields
            }
            for row_id, row_data in self.data.items()
        }
