

class IndexerMixin:
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

    def find(self, field, value):
        if field in self.indexes:
            return self.indexes[field].get(value)
        for row_id, row_data in self.data.items():
            if row_data[field] == value:
                return row_id
        return None
