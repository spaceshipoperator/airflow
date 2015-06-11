'''
Imports the hooks dynamically while keeping the package API clean,
abstracting the underlying modules
'''
from airflow.utils import import_module_attrs as _import_module_attrs
from airflow.plugins_manager import plugins
from airflow.hooks.base_hook import BaseHook as _BaseHook

_hooks = {
    'hive_hooks': [
        'HiveCliHook',
        'HiveMetastoreHook',
        'HiveServer2Hook',
    ],
    'hdfs_hook': ['HDFSHook'],
    'mysql_hook': ['MySqlHook'],
    'postgres_hook': ['PostgresHook'],
    'presto_hook': ['PrestoHook'],
    'samba_hook': ['SambaHook'],
    'sqlite_hook': ['SqliteHook'],
    'S3_hook': ['S3Hook'],
}

_import_module_attrs(globals(), _hooks)

# Loading plugins
for _plugin in plugins:
    if issubclass(_plugin, _BaseHook):
        globals()[_plugin.__name__] = _plugin
