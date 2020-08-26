from shared_utils.api.coda.coda_utils import get_rows_dict_by_yaml, \
    get_rows_data_by_yaml, update_row_by_yaml, append_row_by_yaml, \
    is_request_completed

from coda.util import read_yaml, root_dir


class Coda:
    def __init__(self, doc_name, semester='default', token=None):
        self.doc_name = doc_name
        self.token = token
        path = f'{root_dir}/yaml/{semester}/{self.doc_name}.yaml'
        self._data = read_yaml(path)
        self.doc_id = self._data['doc_id']
        self.telegram_chat = self._data['telegram_chat']
        self._tables = self._data['tables']
        self.tables_dict = {name: Table(self, name, info)
                            for name, info in self._tables.items()}

    def __getattr__(self, item):
        if item in self.tables_dict:
            return self.tables_dict[item]
        raise AttributeError()

    def table(self, name):
        return self.tables_dict[name]

    def tables(self):
        return self.tables_dict.values()

    def is_completed(self, request_id):
        return is_request_completed(self.token, request_id)


class Table:
    def __init__(self, coda, name, info):
        self.coda = coda
        self.name = name
        self.info = info

    def rows_list(self, query=None):
        return get_rows_data_by_yaml(self.coda.token, self.coda.doc_id,
                                     self.info, query)

    def rows_dict(self, query=None):
        return get_rows_dict_by_yaml(self.coda.token, self.coda.doc_id,
                                     self.info, query)

    def update(self, row_id, changes):
        return update_row_by_yaml(self.coda.token, self.coda.doc_id,
                                  self.info, row_id, changes)

    def append(self, row_data):
        return append_row_by_yaml(self.coda.token, self.coda.doc_id,
                                  self.info, row_data)


if __name__ == '__main__':
    coda = Coda('adv18', '2019-2')
    print(coda.doc_name)
    print(coda.students)
    print(coda.unknown)
