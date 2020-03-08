from shared_utils.api.coda.coda_utils import get_tables, get_columns
from shared_utils.io.io import write, append

from coda.conf.coda_token import coda_token
from coda.util import root_dir, read_yaml, write_yaml


def create_tables(semester, doc_name, doc_id, telegram_chat):
    yaml_path = f'{root_dir}/yaml/{semester}/{doc_name}.yaml'
    write(yaml_path, f'')
    append(yaml_path, f'telegram_chat: {telegram_chat}')
    append(yaml_path, f'doc_id: {doc_id}')
    append(yaml_path, 'tables:')

    tables = get_tables(coda_token, doc_id)
    for table in tables['items']:
        append(yaml_path, f"  '{table['name']}':")
        append(yaml_path, f"    table_id: {table['id']}")


def update_tables(semester, doc_name):
    yaml_path = f'{root_dir}/yaml/{semester}/{doc_name}.yaml'
    data = read_yaml(yaml_path)
    doc_id = data['doc_id']
    tables = data['tables']
    for table_name, table in tables.items():
        table_id = table['table_id']
        columns_data = get_columns(coda_token, doc_id, table_id)
        table['columns'] = {}
        for column in columns_data['items']:
            print(f"{column['name']}: {column['id']}")
            table['columns'][column['name']] = column['id']
    write_yaml(yaml_path, data)


if __name__ == '__main__':
    semester = '2020-1'

    docs = [
        {
            'doc_name': 'adv18',
            'doc_id': 'PlGYEhaEib',
            'telegram_chat': -399927652,
        },
        {
            'doc_name': 'adv17',
            'doc_id': 'zqT1QhwbTC',
            'telegram_chat': -291308716,
        },
    ]

    for doc in docs:
        doc_name, doc_id, telegram_chat = doc.values()
        # create_tables(semester, doc_name, doc_id, telegram_chat)
        update_tables(semester, doc_name)
