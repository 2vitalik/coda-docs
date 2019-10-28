from coda.util import read_yaml, root_dir


class Coda:
    def __init__(self, doc_name, token):
        self.doc_name = doc_name
        self.token = token
        self._data = read_yaml(f'{root_dir}/docs/{self.doc_name}.yaml')
        self.doc_id = self._data['doc_id']
        self.telegram_chat = self._data['telegram_chat']
        self._tables = self._data['tables']
