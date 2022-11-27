from sqlalchemy import Boolean, Column, Integer, String, DateTime, Text, ForeignKey, Table
from sqlalchemy.orm import relationship
import database

db_instance = database.Database()
Base = db_instance.db_base


class BaseModel:
    if db_instance.db_engine_type == 'memsql':
        id = Column(Integer, primary_key=True)
        name = Column(String(255), nullable=False)
    else:
        id = Column(Integer, primary_key=True, index=True)
        name = Column(String(255), unique=True, nullable=False)
    description = Column(Text)
    notes = Column(Text)
    sync_tags = Column(Text)


class Tenants(Base, BaseModel):
    __tablename__ = "tenants"

    tenant_type = Column(String(16), nullable=False)
    status = Column(String(16), nullable=False)
    host = Column(String(255), nullable=False)
    port = Column(Integer, nullable=False)
    ha_fail_over_tenant = Column(Integer)
    tenant_manager = Column(Integer)
    db_engine_type = Column(String(16), nullable=False)
    db_name = Column(String(255), nullable=False)
    db_host = Column(String(255), nullable=False)
    db_port = Column(Integer, nullable=False)
    backup = Column(Boolean, nullable=False)
    backup_host = Column(String(255))
    backup_port = Column(Integer)
    # Sample Password Policy
    # Length, Uppercase, Numbers, Symbols
    # Uppercase, Numbers, and Symbols are boolean
    # (16, 1, 1, 0)
    password_policy = Column(String(16), nullable=False)
    # Relationship fields
    # Relationships


class Users(Base, BaseModel):
    __tablename__ = "users"

    if db_instance.db_engine_type == 'memsql':
        email = Column(String(255), nullable=False)
        password = Column(Text, nullable=False)
        username = Column(String(255), nullable=False)
    else:
        email = Column(String(255), unique=True, nullable=False)
        password = Column(Text, unique=True, nullable=False)
        username = Column(String(255), unique=True, nullable=False)
    address = Column(Text)
    phone = Column(String(32))
    status = Column(String(16), nullable=False)
    last_login = Column(DateTime)
    active = Column(Boolean, nullable=False)
    verified = Column(Boolean, nullable=False)
    # Relationship fields
    # Relationships


class AccessGroups(Base, BaseModel):
    __tablename__ = "access_groups"

    read_write = Column(Integer, nullable=False)
    # Relationship fields
    # Relationships


class Dashboards(Base, BaseModel):
    __tablename__ = "dashboards"

    dashboard_type = Column(String(32), nullable=False)
    base_dashboard = Column(Integer)
    design = Column(Text, nullable=False)
    # Relationship fields
    # Relationships


class Customers(Base, BaseModel):
    __tablename__ = "customers"

    if db_instance.db_engine_type == 'memsql':
        shortname = Column(String(255), nullable=False)
    else:
        shortname = Column(String(255), unique=True, nullable=False)
    subsidiary = Column(Text)
    website = Column(Text)

    # Relationship fields
    # Relationships


class Customer_Employees(Base, BaseModel):
    __tablename__ = "customer_employees"

    address = Column(Text)
    phone = Column(String(32))
    email = Column(String(255), nullable=False)
    # Relationship fields
    # Relationships


class Runbooks(Base, BaseModel):
    __tablename__ = "runbooks"

    initial_input = Column(Text)
    initial_output = Column(Text)
    # Relationship fields
    # Relationships


class Actions(Base, BaseModel):
    __tablename__ = "actions"
    # Relationship fields
    # Relationships


class Incidents(Base):
    __tablename__ = "incidents"

    if db_instance.db_engine_type == 'memsql':
        id = Column(Integer, primary_key=True)
    else:
        id = Column(Integer, primary_key=True, index=True)
    account_group = Column(String(255))
    account_name = Column(String(255))
    actioned_time = Column(DateTime)
    alert_category = Column(String(255))
    alert_info = Column(Text)
    alert_name = Column(Text)
    alert_source = Column(Text)
    arrival_time = Column(DateTime)
    attachment_file_type = Column(String(255))
    attachment_md5 = Column(String(32))
    attachment_name = Column(Text)
    attachment_sha256 = Column(String(64))
    attachment_size = Column(Integer)
    category = Column(String(255))
    cve = Column(String(16))
    cvss = Column(Text)
    detection_time = Column(DateTime)
    dst_domain = Column(Text)
    dst_hostname = Column(Text)
    dst_ipv4 = Column(String(16))
    dst_ipv6 = Column(String(64))
    dst_mac = Column(String(32))
    dst_parameters = Column(Text)
    dst_path = Column(Text)
    dst_port = Column(Integer)
    dst_protocol = Column(String(8))
    email_address = Column(Text)
    email_bcc = Column(Text)
    email_body_html = Column(Text)
    email_body_text = Column(Text)
    email_cc = Column(Text)
    email_headers = Column(Text)
    email_in_reply_to = Column(Text)
    email_message_id = Column(Text)
    email_original_ip = Column(Text)
    email_received = Column(Text)
    email_reply_to = Column(Text)
    email_reporter = Column(Text)
    email_reporter_address = Column(Text)
    email_return_path = Column(Text)
    email_size = Column(Integer)
    email_subject = Column(Text)
    email_to = Column(Text)
    email_url = Column(Text)
    event_group = Column(Text)
    event_number = Column(Integer)
    event_status = Column(Text)
    event_time = Column(DateTime)
    event_type = Column(Text)
    file_md5 = Column(String(32))
    file_name = Column(Text)
    file_path = Column(Text)
    file_sha256 = Column(String(64))
    file_size = Column(Integer)
    file_type = Column(String(255))
    initial_investigation_time = Column(DateTime)
    mitre_attack_subtechnique = Column(String(255))
    mitre_attack_tactic = Column(String(255))
    mitre_attack_technique = Column(String(255))
    notes = Column(Text)
    parent_process_command_line = Column(Text)
    parent_process_name = Column(Text)
    parent_process_uid = Column(Text)
    pcap_file_location = Column(Text)
    pcap_file_name = Column(Text)
    pcap_file_size = Column(Integer)
    process_command_line = Column(Text)
    process_name = Column(Text)
    process_uid = Column(Text)
    raw_event = Column(Text)
    react_action = Column(String(255))
    react_stage = Column(String(255))
    reported_time = Column(DateTime)
    src_domain = Column(Text)
    src_hostname = Column(Text)
    src_ipv4 = Column(Text)
    src_ipv6 = Column(Text)
    src_mac = Column(Text)
    src_parameters = Column(Text)
    src_path = Column(Text)
    src_port = Column(Integer)
    src_protocol = Column(Text)
    subcategory = Column(String(255))
    username = Column(String(255))
    # Relationship fields
    # Relationships


class IncidentTypes(Base, BaseModel):
    __tablename__ = "incident_types"

    # Relationship fields
    # Relationships


class Fields(Base, BaseModel):
    __tablename__ = "fields"

    field_type = Column(String(255), nullable=False)
    # Relationship fields
    # Relationships


class Verdicts(Base, BaseModel):
    __tablename__ = "verdicts"

    minimum_value = Column(Integer, nullable=False)
    maximum_value = Column(Integer, nullable=False)
    # Relationship fields
    # Relationships


class Scripts(Base, BaseModel):
    __tablename__ = "scripts"

    script_full_path = Column(Text, nullable=False)
    inputs = Column(Text)
    outputs = Column(Text)
    functions = Column(Text)
    run_interval = Column(Integer, nullable=False)
    # Relationship fields
    # Relationships


class Reports(Base, BaseModel):
    __tablename__ = "reports"

    run_interval = Column(Integer, nullable=False)
    save_after_run = Column(Boolean, nullable=False)
    save_type = Column(String(255))
    save_full_path = Column(Text)
    # Relationship fields
    # Relationships


class IndicatorTypes(Base, BaseModel):
    __tablename__ = "indicator_types"

    regex = Column(Text)
    # Relationship fields
    # Relationships


class Indicators(Base, BaseModel):
    __tablename__ = "indicators"

    value = Column(Text, nullable=False)
    status = Column(String(16), nullable=False)
    confidence = Column(Integer, nullable=False)
    reputation = Column(Integer, nullable=False)
    created = Column(DateTime, nullable=False)
    seen_first = Column(DateTime)
    seen_last = Column(DateTime)
    indicator_update = Column(DateTime, nullable=False)
    expiration = Column(DateTime, nullable=False)
    source_name = Column(String(255))
    source_location = Column(Text)
    # Relationship fields
    # Relationships


class Extractors(Base, BaseModel):
    __tablename__ = "extractors"

    key_value = Column(String(255), nullable=False)
    # Relationship fields
    # Relationships


class Classifiers(Base, BaseModel):
    __tablename__ = "classifiers"

    script_function = Column(Text)
    classifier_type = Column(String(255), nullable=False)
    input_key = Column(String(255), nullable=False)
    input_value = Column(Text, nullable=False)
    output_type = Column(String(255), nullable=False)
    output_value = Column(Integer, nullable=False)
    # Relationship fields
    # Relationships
