import random
import datetime
import json
import requests
import names
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import scoped_session, sessionmaker

metadata = MetaData()
db_user = 'root'
db_password = '42B-=-edA?ucH3bA'
db_host = '192.168.1.105'
db_port = '3306'
db_database = 'thanatosdb'
db_engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}')
db_session = scoped_session(sessionmaker(autocommit=True,
                                         autoflush=True,
                                         bind=db_engine))
# db_session.connection().connection.set_isolation_level(0)
thanatos_engine = create_engine(f'mysql+pymysql://{db_user}:{db_password}@{db_host}/{db_database}')
thanatos_session = scoped_session(sessionmaker(autocommit=True,
                                               autoflush=True,
                                               bind=thanatos_engine))
response = requests.get('https://www.mit.edu/~ecprice/wordlist.10000')
unfiltered_words = response.text.splitlines()
words = []
for each_word in unfiltered_words:
    if len(each_word) > 3:
        words.append(each_word)

max_customers = 30
max_employees = 10
max_incidents = 100000
max_dashboards = 10
max_extractors = 30
max_indicator_types = 10
max_indicators = 10
max_reports = 5
max_runbooks = 10
max_scripts = 50
max_users = 10


def create_fields_data():
    sample = {'name': random.choice(words),
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'field_type': random.choice(words)
              }
    db_command = f"INSERT INTO fields ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_incident_types_data():
    sample = {'name': random.choice(words),
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512)))
              }
    db_command = f"INSERT INTO incident_types ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_incident_data(tenant_id=None):
    alert_category = ['malicious', 'non-malicious', 'false positive', 'true positive']
    hash_chars = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    file_extension = ['pdf', 'docx', 'zip', 'json', 'csv', 'jpeg', 'gif', 'eml', 'xml', 'tar']
    tld = ['.com', '.org', '.net']
    react_stage = ['preparation', 'identification', 'containment', 'eradication', 'recovery', 'lessons learned']
    mitre_tactic = ['reconnaissance',
                    'resource development',
                    'initial access',
                    'execution',
                    'persistence',
                    'privilege escalation',
                    'defense evasion',
                    'credential access',
                    'discovery',
                    'lateral movement',
                    'collection',
                    'command and control',
                    'exfiltration',
                    'impact']
    sample = {'account_group': ''.join(random.choice(words) for x in range(3)),
              'account_name': names.get_full_name(),
              'actioned_time': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'alert_category': random.choice(alert_category),
              'alert_info': '',
              'alert_name': ' '.join(random.choice(words) for x in range(5)),
              'alert_source': ' '.join(random.choice(words) for x in range(8)),
              'arrival_time': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'attachment_file_type': random.choice(file_extension),
              'attachment_md5': ''.join(random.choice(hash_chars) for x in range(32)),
              'attachment_name': f"{'_'.join(random.choice(words) for x in range(4))}"
                                 f".{random.choice(file_extension)}",
              'attachment_sha256': ''.join(random.choice(hash_chars) for x in range(64)),
              'attachment_size': random.randint(1024, 2048000),
              'category': random.choice(alert_category),
              'cve': f"CVE-{random.randint(2015, 2021)}-{random.randint(1000, 20000)}",
              'cvss': f"{random.randint(1, 9)}.{random.randint(1, 9)}",
              'detection_time': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'dst_domain': f"{'_'.join(random.choice(words) for x in range(2))}{random.choice(tld)}",
              'dst_hostname': f"{'_'.join(random.choice(words) for x in range(2))}{random.choice(tld)}",
              'dst_ipv4': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}."
                          f"{random.randint(1, 255)}",
              'dst_ipv6': f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}",
              'dst_mac': f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}",
              'dst_parameters': '?'.join(random.choice(words) for x in range(4)),
              'dst_path': '/'.join(random.choice(words) for x in range(4)),
              'dst_port': random.randint(1, 65535),
              'dst_protocol': random.choice(['icmp', 'tcp', 'udp']),
              'email_address': f"{names.get_full_name().lower().replace(' ', '')}@"
                               f"{''.join(random.choice(words) for x in range(3))}{random.choice(tld)}",
              'email_bcc': f"{names.get_full_name().lower().replace(' ', '')}@"
                           f"{''.join(random.choice(words) for x in range(3))}{random.choice(tld)}",
              'email_body_html': ' '.join(random.choice(words) for x in range(random.randint(512, 1024))),
              'email_body_text': ' '.join(random.choice(words) for x in range(random.randint(512, 1024))),
              'email_cc': f"{names.get_full_name().lower().replace(' ', '')}@"
                          f"{''.join(random.choice(words) for x in range(3))}{random.choice(tld)}",
              'email_headers': '',
              'email_in_reply_to': '',
              'email_message_id': f"{random.choice(hash_chars)}@"
                                  f"{''.join(random.choice(words) for x in range(3))}{random.choice(tld)}",
              'email_original_ip': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}."
                                   f"{random.randint(1, 255)}",
              'email_received': '',
              'email_reply_to': '',
              'email_reporter': names.get_full_name(),
              'email_reporter_address': f"{names.get_full_name().lower().replace(' ', '')}@"
                                        f"{''.join(random.choice(words) for x in range(3))}{random.choice(tld)}",
              'email_return_path': '',
              'email_size': random.randint(1024, 2048000),
              'email_subject': ' '.join(random.choice(words) for x in range(8)),
              'email_to': f"{names.get_full_name().lower().replace(' ', '')}@"
                          f"{''.join(random.choice(words) for x in range(3))}{random.choice(tld)}",
              'email_url': f"https[://]www.{'_'.join(random.choice(words) for x in range(2))}{random.choice(tld)}",
              'event_group': '',
              'event_number': random.randint(1000000, 9999999),
              'event_status': random.choice(['open', 'closed', 'review', 'error', 'analysis', 'arrived']),
              'event_time': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'event_type': '',
              'file_md5': ''.join(random.choice(hash_chars) for x in range(32)),
              'file_name': f"{'_'.join(random.choice(words) for x in range(4))}"
                           f".{random.choice(file_extension)}",
              'file_path': '/'.join(random.choice(words) for x in range(4)),
              'file_sha256': ''.join(random.choice(hash_chars) for x in range(64)),
              'file_size': random.randint(1024, 2048000),
              'file_type': random.choice(file_extension),
              'initial_investigation_time': datetime.datetime.strftime(datetime.datetime.now(),
                                                                       '%Y-%m-%d %H:%M:%S'),
              'mitre_attack_subtechnique': '',
              'mitre_attack_tactic': random.choice(mitre_tactic),
              'mitre_attack_technique': '',
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'parent_process_command_line': f"c:\>{' '.join(random.choice(words) for x in range(4))}",
              'parent_process_name': '_'.join(random.choice(words) for x in range(4)),
              'parent_process_uid': ''.join(random.choice(hash_chars) for x in range(64)),
              'pcap_file_location': '/'.join(random.choice(words) for x in range(4)),
              'pcap_file_name': f"{'_'.join(random.choice(words) for x in range(4))}.pcap",
              'pcap_file_size': random.randint(1024, 2048000),
              'process_command_line': f"c:\>{' '.join(random.choice(words) for x in range(4))}",
              'process_name': '_'.join(random.choice(words) for x in range(4)),
              'process_uid': ''.join(random.choice(hash_chars) for x in range(64)),
              'raw_event': ' '.join(random.choice(words) for x in range(random.randint(1024, 2048))),
              'react_action': '',
              'react_stage': random.choice(react_stage),
              'reported_time': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'src_domain': f"{'_'.join(random.choice(words) for x in range(2))}{random.choice(tld)}",
              'src_hostname': f"{'_'.join(random.choice(words) for x in range(2))}{random.choice(tld)}",
              'src_ipv4': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}."
                          f"{random.randint(1, 255)}",
              'src_ipv6': f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}:"
                          f"{''.join(random.choice(hash_chars) for x in range(4))}",
              'src_mac': f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}-"
                         f"{''.join(random.choice(hash_chars) for x in range(2))}",
              'src_parameters': '?'.join(random.choice(words) for x in range(4)),
              'src_path': '/'.join(random.choice(words) for x in range(4)),
              'src_port': random.randint(1, 65535),
              'src_protocol': random.choice(['icmp', 'tcp', 'udp']),
              'subcategory': random.choice(alert_category),
              'username': names.get_full_name().lower().replace(' ', ''),
              }
    db_command = f"INSERT INTO incidents ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_customer_data():
    customer_name = ' '.join(random.choice(words).title() for x in range(5))
    tld = ['.com', '.org', '.net']
    sample = {'name': customer_name,
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'shortname': ''.join(customer_name.lower().split(' ')[:3]),
              'subsidiary': 'No subsidiary.',
              'website': f"{'_'.join(random.choice(words) for x in range(2))}{random.choice(tld)}/"
                         f"{'/'.join(random.choice(words) for x in range(4))}"}
    db_command = f"INSERT INTO customers ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)
    db_command = f"SELECT * FROM customers"
    customer_list = thanatos_session.execute(db_command).all()
    customer_id = ''
    for each_customer in customer_list:
        if each_customer[1] == customer_name:
            customer_id = each_customer[0]
            break
    for i in range(random.randint(1, max_employees)):
        employee_name = names.get_full_name()
        sample = {'name': employee_name,
                  'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
                  'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
                  'address': f"{random.randint(100, 900)} {random.choice(words)} "
                             f"{random.choice(['Ave', 'Blvd', 'St'])}",
                  'phone': f"1-{random.randint(100, 900)}-{random.randint(100, 900)}-{random.randint(1000, 9000)}",
                  'email': f"{employee_name.lower().replace(' ', '')}@"
                           f"{''.join(random.choice(words) for x in range(3))}{random.choice(tld)}"}
        db_command = f"INSERT INTO customer_employees ({', '.join(sample.keys())}) " \
                     f"VALUES {tuple(sample.values())} "
        thanatos_session.execute(db_command)
    sample = {'name': ''.join(customer_name.lower().split(' ')[:3]),
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'tenant_type': random.choice(['manager', 'developer', 'customer']),
              'status': random.choice(['active', 'deactive', 'trial', 'pending']),
              'host': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}."
                      f"{random.randint(1, 255)}",
              'port': random.randint(1, 65535),
              'ha_fail_over_tenant': 0,
              'tenant_manager': 0,
              'db_engine_type': 'memsql',
              'db_name': 'MemSQL',
              'db_host': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}."
                         f"{random.randint(1, 255)}",
              'db_port': random.randint(1, 65535),
              'backup': False,
              'backup_host': f"{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}."
                             f"{random.randint(1, 255)}",
              'backup_port': random.randint(1, 65535),
              'sync_tags': '',
              'password_policy': '(16, 1, 1, 0)'
              }
    db_command = f"INSERT INTO tenants ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)
    for i in range(random.randint(int(max_incidents / 2), max_incidents)):
        create_incident_data()


def create_database(database_name):
    db_command = f'CREATE DATABASE {database_name}'
    db_session.execute(db_command)


def create_dashboard_data():
    sample = {'name': f'{random.choice(words)}_dashboard',
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'dashboard_type': random.choice(['tenant', 'incident', 'indicator', 'management']),
              'base_dashboard': 0,
              'design': json.dumps({'height': 0,
                                    'width': 0,
                                    'rows': 3,
                                    'columns': 3})
              }
    db_command = f"INSERT INTO dashboards ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_extractors_data():
    sample = {'name': f'{random.choice(words)}_dashboard',
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'key_value': '_'.join(random.choice(words) for x in range(2))
              }
    db_command = f"INSERT INTO extractors ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_verdicts_data():
    sample = {'name': f'{random.choice(words)}',
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'minimum_value': 0,
              'maximum_value': 100
              }
    db_command = f"INSERT INTO verdicts ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_indicator_types_data():
    sample = {'name': f'{random.choice(words)}',
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'regex': '^.+'
              }
    db_command = f"INSERT INTO indicator_types ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_indicators_data():
    sample = {'name': f'{random.choice(words)}',
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'value': ' '.join(random.choice(words) for x in range(random.randint(8, 16))),
              'status': random.choice(['active', 'deactive', 'review']),
              'confidence': random.randint(1, 100),
              'reputation': random.randint(1, 100),
              'created': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'seen_first': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'seen_last': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'indicator_update': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'expiration': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'source_name': ' '.join(random.choice(words) for x in range(4)),
              'source_location': ' '.join(random.choice(words) for x in range(random.randint(8, 16)))
              }
    db_command = f"INSERT INTO indicators ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_reports_data():
    sample = {'name': f'{random.choice(words)}',
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'run_interval': 3600,
              'save_after_run': False,
              'save_type': random.choice(['pdf', 'csv', 'json', 'txt']),
              'save_full_path': '/'.join(random.choice(words) for x in range(4))
              }
    db_command = f"INSERT INTO reports ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_runbooks_data():
    sample = {'name': f'{random.choice(words)}',
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'initial_input': json.dumps({'field_1': 'value_1',
                                           'field_2': 'value_2'}),
              'initial_output': json.dumps({'field_1': 'value_1',
                                           'field_2': 'value_2'}),
              }
    db_command = f"INSERT INTO runbooks ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_scripts_data():
    sample = {'name': f'{random.choice(words)}',
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'script_full_path': '/'.join(random.choice(words) for x in range(4)),
              'inputs': json.dumps({'field_1': 'value_1',
                                           'field_2': 'value_2'}),
              'outputs': json.dumps({'field_1': 'value_1',
                                           'field_2': 'value_2'}),
              'functions': json.dumps({'function1': 'input1',
                                       'function2': 'input2'}),
              'run_interval': 3600
              }
    db_command = f"INSERT INTO scripts ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def create_users_data():
    username = names.get_full_name()
    tld = ['.com', '.org', '.net']
    sample = {'name': username,
              'description': ' '.join(random.choice(words) for x in range(random.randint(128, 256))),
              'notes': ' '.join(random.choice(words) for x in range(random.randint(256, 512))),
              'password': '',
              'username': '',
              'address': f"{random.randint(100, 900)} {random.choice(words)} "
                         f"{random.choice(['Ave', 'Blvd', 'St'])}",
              'phone': f"1-{random.randint(100, 900)}-{random.randint(100, 900)}-{random.randint(1000, 9000)}",
              'email': f"{username.lower().replace(' ', '')}@"
                       f"{''.join(random.choice(words) for x in range(3))}{random.choice(tld)}",
              'status': random.choice(['active', 'inactive']),
              'last_login': datetime.datetime.strftime(datetime.datetime.now(), '%Y-%m-%d %H:%M:%S'),
              'active': False,
              'verified': True
              }
    db_command = f"INSERT INTO users ({', '.join(sample.keys())}) " \
                 f"VALUES {tuple(sample.values())} "
    thanatos_session.execute(db_command)


def clean_wipe():
    db_command = 'SHOW DATABASES'
    database_list = db_session.execute(db_command).fetchall()
    for each_db in database_list:
        if each_db[1] not in ['memsql', 'cluster', 'information_schema', 'postgres', 'template0', 'template1']:
            db_command = f'DROP DATABASE {each_db[1]};'
            db_session.execute(db_command)


def main():
    create_fields_data()
    create_incident_types_data()
    for i in range(random.randint(1, max_customers)):
        create_customer_data()
    for i in range(random.randint(1, max_dashboards)):
        create_dashboard_data()
    for i in range(random.randint(1, max_extractors)):
        create_extractors_data()
    create_verdicts_data()
    for i in range(random.randint(1, max_indicator_types)):
        create_indicator_types_data()
    for i in range(random.randint(1, max_indicators)):
        create_indicators_data()
    for i in range(random.randint(1, max_reports)):
        create_reports_data()
    for i in range(random.randint(1, max_runbooks)):
        create_runbooks_data()
    for i in range(random.randint(1, max_scripts)):
        create_scripts_data()
    for i in range(random.randint(1, max_users)):
        create_users_data()


if __name__ == '__main__':
    # clean_wipe()
    # create_database(db_database)
    main()
