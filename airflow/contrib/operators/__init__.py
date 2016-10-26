# Imports the operators dynamically while keeping the package API clean,
# abstracting the underlying modules
from airflow.utils.helpers import import_module_attrs as _import_module_attrs

_operators = {
    'ssh_execute_operator': ['SSHExecuteOperator'],
    'vertica_operator': ['VerticaOperator'],
    'vertica_to_hive': ['VerticaToHiveTransfer'],
    'qubole_operator': ['QuboleOperator'],
    'astronomer_s3_key_sensor': ['AstronomerS3KeySensor']
}

_import_module_attrs(globals(), _operators)
