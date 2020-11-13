from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from datetime import datetime, timedelta

dag_name = 'mon-premier-dag'

#------------------------------------------------------------------------------
# Args du DAG
default_args = {
    'owner': 'corentin',
    'start_date': datetime(2020, 11, 7),
    'retries': 1,
    'retry_delay': timedelta(minutes=15)
}

dag = DAG(
    dag_id=dag_name,
    default_args=default_args,
    schedule_interval='@once',
    max_active_runs=1,
    template_searchpath=(
        "/home/ec2-user/airflow/dags/" + dag_name +"/"    
    )
)


#------------------------------------------------------------------------------
# Task
task_1=DummyOperator(
    task_id='task-1',
    dag=dag
)

task_2=DummyOperator(
    task_id='task-2',
    dag=dag
)

task_3=DummyOperator(
    task_id='task-3',
    dag=dag
)

task_1 >> task_2 >> task_3
