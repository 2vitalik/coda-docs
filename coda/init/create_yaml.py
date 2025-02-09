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
    docs = [
        # {
        #     'semester': '2020-1',
        #     'doc_name': 'adv18',
        #     'doc_id': 'PlGYEhaEib',
        #     'telegram_chat': -399927652,
        # },
        # {
        #     'semester': '2020-1',
        #     'doc_name': 'adv17',
        #     'doc_id': 'zqT1QhwbTC',
        #     'telegram_chat': -291308716,
        # },
        # {
        #     'semester': '2020-1',
        #     'doc_name': 'adv16',
        #     'doc_id': 'aazaYSoRBc',
        #     'telegram_chat': -357420276,
        # },
        # {
        #     'semester': '2020-1',
        #     'doc_name': 'oop',
        #     'doc_id': 'TdQAh6nS1P',
        #     'telegram_chat': -436357091,
        # },
        # {
        #     'semester': '2020-1',
        #     'doc_name': 'adv18_data',
        #     'doc_id': 'xEcFwErxgY',
        #     'telegram_chat': -436357091,
        # },
        # {
        #     'semester': 'default',
        #     'doc_name': 'diary_old',
        #     'doc_id': 'zjzcA2QDFg',
        #     'telegram_chat': None,
        # },
        # {
        #     'semester': '2020-2',
        #     'doc_name': 'adv19',
        #     'doc_id': 'JIdLdwGrze',
        #     'telegram_chat': -412658504,
        # },
        # {
        #     'semester': '2020-2',
        #     'doc_name': 'adv18',
        #     'doc_id': '8m3KXK65wo',
        #     'telegram_chat': -399927652,
        # },
        # {
        #     'semester': '2020-2',
        #     'doc_name': 'adv17',
        #     'doc_id': 'Ln1BHsM9yF',
        #     'telegram_chat': -291308716,
        # },
        # {
        #     'semester': '2020-2',
        #     'doc_name': 'adv19_bonuses',
        #     'doc_id': 'l9wptfDsEo',
        #     'telegram_chat': -460682053,
        # },
        # {
        #     'semester': '2020-2',
        #     'doc_name': 'adv18_bonuses',
        #     'doc_id': 'ggx-Rzn_7v',
        #     'telegram_chat': -358956865,
        # },
        # {
        #     'semester': '2020-2',
        #     'doc_name': 'cist_nure',
        #     'doc_id': 'Oe7JK0Jhnv',
        #     'telegram_chat': -1001443393626,
        # },
        # --------------------------------------------------------------------
        # {
        #     'semester': 'default',
        #     'doc_name': 'diary',
        #     'doc_id': 'BPqqG0xD2g',
        #     'telegram_chat': None,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'nure_20',
        #     'doc_id': 'jeeUEoCmQG',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'nure_19',
        #     'doc_id': 'UQnRtL3gs3',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'nure_18',
        #     'doc_id': 'V3_PfzHd4q',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'nure_17',
        #     'doc_id': 'ki2WRSxuak',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'adv17',
        #     'doc_id': '6AWlFObC3R',
        #     'telegram_chat': -291308716,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'adv18',
        #     'doc_id': '40fixv94zQ',
        #     'telegram_chat': -399927652,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'adv19',
        #     'doc_id': '6av8owel2d',
        #     'telegram_chat': -412658504,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'adv19_bonuses',
        #     'doc_id': 'mcSsb7_-AE',
        #     'telegram_chat': -460682053,
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'adv18_bonuses',
        #     'doc_id': 'o7eTMCYpOE',
        #     'telegram_chat': -358956865,
        # },
        # {
        #     'semester': 'default',
        #     'doc_name': 'anvileight',
        #     'doc_id': 't_RcQ4HRNr',
        #     'telegram_chat': '',
        # },
        # {
        #     'semester': '2021-1',
        #     'doc_name': 'oop',  # todo: update completely later
        #     'doc_id': 'wt3_f1JTX-',
        #     'telegram_chat': '',
        # },
        # --------------------------------------------------------------------
        # {
        #     'semester': '2021-2',
        #     'doc_name': 'timetable',
        #     'doc_id': 'DQFWMzQIyq',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2021-2',
        #     'doc_name': 'adv20',
        #     'doc_id': 'DEsp3ZOQ-6',
        #     'telegram_chat': -603913534,
        # },
        # ====================================================================
        # {
        #     'semester': '2022-1',
        #     'doc_name': 'timetable',
        #     'doc_id': '569kzNvqNU',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2022-1',
        #     'doc_name': 'adv20',
        #     'doc_id': 'sJDDVJj2U5',
        #     'telegram_chat': -603913534,
        # },
        # {
        #     'semester': '2022-1',
        #     'doc_name': 'oop-old',
        #     'doc_id': '7DufWMIETl',
        #     'telegram_chat': -436357091,
        # },
        # {
        #     'semester': '2022-1',
        #     'doc_name': 'oop',
        #     'doc_id': 'kGPDB3udhv',
        #     'telegram_chat': -436357091,
        # },
        # ====================================================================
        # {
        #     'semester': '2022-2',
        #     'doc_name': 'timetable',
        #     'doc_id': 'Lkl_3M3nDb',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2022-2',
        #     'doc_name': 'tt-21',
        #     'doc_id': 'UWSxxPgVM_',
        #     'telegram_chat': -603913534,
        # },
        # ====================================================================
        # {
        #     'semester': '2023-1',
        #     'doc_name': 'tt-21',
        #     'doc_id': 'RS6X6cg3mC',
        #     'telegram_chat': -603913534,
        # },
        # {
        #     'semester': '2023-1',
        #     'doc_name': 'timetable',
        #     'doc_id': 'yXxNDhyt7r',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2023-1',
        #     'doc_name': 'oop',
        #     'doc_id': '1GDyxjRqoL',
        #     'telegram_chat': -436357091,
        # },
        # ====================================================================
        # {
        #     'semester': '2023-2',
        #     'doc_name': 'timetable',
        #     'doc_id': 'sYR0tZEp3F',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2023-2',
        #     'doc_name': 'tt-22',
        #     'doc_id': 'EkMPD-98lz',
        #     'telegram_chat': -603913534,
        # },
        # # ====================================================================
        # {
        #     'semester': '2024-1',
        #     'doc_name': 'timetable',
        #     'doc_id': 'F7M3c032cb',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2024-1',
        #     'doc_name': 'tt-22',
        #     'doc_id': 'lDE7OWv5aP',
        #     'telegram_chat': -603913534,
        # },
        # ====================================================================
        # {
        #     'semester': '2024-2',
        #     'doc_name': 'timetable',
        #     'doc_id': 'hTosFjkfFg',
        #     'telegram_chat': -1001443393626,
        # },
        # {
        #     'semester': '2024-2',
        #     'doc_name': 'tt-23',
        #     'doc_id': '21u5mAJaa_',
        #     'telegram_chat': -603913534,
        # },
        # ====================================================================
        {
            'semester': '2025-1',
            'doc_name': 'timetable',
            'doc_id': 'huz_lGXO4n',
            'telegram_chat': -1001443393626,
        },
        {
            'semester': '2025-1',
            'doc_name': 'tt-23',
            'doc_id': '_f6glF7PMi',
            'telegram_chat': -603913534,
        },
    ]

    for doc in docs:
        semester, doc_name, doc_id, telegram_chat = doc.values()
        # create_tables(semester, doc_name, doc_id, telegram_chat)
        update_tables(semester, doc_name)


# todo: make it able to use this script outside this project (via bot?), but it seems that's impossible for now
