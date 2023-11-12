from coda.docs.tt21.mixins.indexer import IndexerMixin
from coda.lib import Coda


class ProjectThemes(IndexerMixin):
    def __init__(self, semester, coda_token):
        self.coda = Coda('tt-22', semester, coda_token)
        self.table = self.coda.table('Темы проектов')
        self.data = self.table.rows_dict()
        self.indexes = {}
        self.add_index('key')
        self.add_index('Студент')

    def by_key(self, key):
        return self.find('key', key)

    def by_student(self, student):
        return self.find('Студент', student)

    def update(self, row_id, changes):  # todo: move to common base class
        self.table.update(row_id, changes)
