from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os

# Add /opt/airflow/src to the Python path
sys.path.append('/opt/airflow/src')

from check_vars import check_variable_in_range  # Import from src

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
}

with DAG(
    dag_id='test_main_py_dag',
    default_args=default_args,
    description='A DAG to run main.py from the src folder',
    schedule_interval=None,
    start_date=datetime(2023, 1, 1),
    catchup=False,
    tags=['test'],
) as dag:

    run_test = PythonOperator(
        task_id='check_variable_in_range',
        op_kwargs={
            'dataset_path': '/opt/airflow/data/precipitation.nc',  # Adjust path to match container structure
            'variable_name': 'precipitation',
            'min_value': 0,
            'max_value': 500,
        },
        python_callable=check_variable_in_range,
    )

    run_test