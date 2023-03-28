from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.bash import BashOperator

import os

default_args = {
    "owner": "team_name",
    "depends_on_past": False,
    "start_date": datetime(2023, 3, 28),
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

# go ahead and set this locally on your machine, I have mine 
# set to run the `example_python.py` file in this folder, but it can 
# be run from anywhere if you set the environment variable on your
# computer and then you can set it on the server
python_file_path = os.environ.get("PYTHON_FILE_PATH", "/opt/airflow/plugins/example_python.py")

x_dag = DAG(
    "my_dag",
    default_args=default_args,
    schedule_interval="0 6 * * *",  # every day at 6am
    max_active_runs=1,
)

example_task = BashOperator(
    dag=x_dag,
    task_id="echo_task_example",
    bash_command=f"echo 'Running my file from `{python_file_path}`'",
)

transform_extract_load = BashOperator(
    dag=x_dag,
    task_id="executing_python_task_example",
    bash_command=f"python3 {python_file_path}",
)

example_task >> transform_extract_load