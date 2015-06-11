import imp
import inspect
import logging
import os

from airflow.configuration import conf
from airflow.models import BaseOperator
from airflow.hooks.base_hook import BaseHook

pluggable_classes = (BaseOperator, BaseHook,)
plugins_folder = conf.get('core', 'plugins_folder')


if not plugins_folder:
    plugins_folder = conf.get('core', 'airflow_home') + '/plugins'

plugins = []
for root, dirs, files in os.walk(plugins_folder):
    for f in files:
        try:
            filepath = os.path.join(root, f)
            if not os.path.isfile(filepath):
                continue
            mod_name, file_ext = os.path.splitext(
                os.path.split(filepath)[-1])
            if file_ext != '.py':
                continue
            m = imp.load_source(mod_name, filepath)
            for obj in m.__dict__.values():
                if any([
                        inspect.isclass(obj) and
                        issubclass(obj, c) and
                        c is not obj
                        for c in pluggable_classes]
                ):
                    plugins.append(obj)
        except Exception() as e:
            logging.exception(e)
            logging.error('Failed to import plugin ' + filepath)
