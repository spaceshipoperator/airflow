Quick Start
'''''''''''
The installation is quick and straightforward.

.. code-block:: bash

    # Airflow needs a configuration file, which may be specified by
    # the environment variable AIRFLOW_CONFIG
    # (optional, if unset defaults to ~/airflow/airflow.cfg)
    export AIRFLOW_CONFIG=~/airflow/airflow.cfg

    # install from pypi using pip
    pip install airflow

    # initialize the database
    airflow initdb

    # start the web server, default port is 8080
    airflow webserver -p 8080

The location of AIRFLOW_CONFIG is referred to as the Airflow home (or
AIRFLOW_HOME).  When the airflow command is run if the specified
configuration file does not exist it will be created with default settings,
afterwards you can inspect these settings through the UI from the
``Admin->Configuration`` menu.

Out of the box, airflow uses a sqlite database, which you should outgrow
fairly quickly since no parallelization is possible using this database
backend. It works in conjunction with the ``SequentialExecutor`` which will
only run task instances sequentially. While this is very limiting, it allows
you to get up and running quickly and take a tour of the UI and the
command line utilities.

Here are a few commands that will trigger a few task instances. You should
be able to see the status of the jobs change in the ``example1`` DAG as you
run the commands below.

.. code-block:: bash

    # run your first task instance
    airflow run example_bash_operator runme_0 2015-01-01
    # run a backfill over 2 days
    airflow backfill example_bash_operator -s 2015-01-01 -e 2015-01-02

From this point, you can move on to the :doc:`tutorial` section, and come back
if/when you are ready to make your Airflow sandbox more of a serious
environment.
