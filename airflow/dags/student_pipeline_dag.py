from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

# ----------------------------------------
# Default DAG arguments
# ----------------------------------------
default_args = {
    'owner': 'talentum',
    'depends_on_past': False,
    'start_date': datetime(2026, 2, 10),
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

# ----------------------------------------
# Create DAG
# ----------------------------------------
with DAG(
    dag_id='student_activity_etl_pipeline',
    default_args=default_args,
    schedule_interval='@hourly',   # can change later
    catchup=False
) as dag:

    # ----------------------------------------
    # Task 1: Silver Map → Structured
    # ----------------------------------------
    silver_to_structured = BashOperator(
        task_id='silver_map_to_structured',
        bash_command="""
        spark-submit \
        /home/talentum/student_streaming_project/spark/silver_map_to_structured.py
        """
    )

    # ----------------------------------------
    # Task 2: Gold Aggregation
    # ----------------------------------------
    gold_aggregation = BashOperator(
        task_id='gold_aggregation',
        bash_command="""
        spark-submit \
        /home/talentum/student_streaming_project/spark/gold_aggregation.py
        """
    )

    # ----------------------------------------
    # Task Dependency
    # ----------------------------------------
    silver_to_structured >> gold_aggregation

