
from datetime import datetime
from airflow.sdk import dag, task 
from airflow.providers.common.sql.operators.sql import SQLExecuteQueryOperator

@dag(
    dag_id="etl_exemplo_persistencia_postgres",
    schedule="@daily",
    start_date=datetime(2026, 1, 1),
    catchup=False,
    tags=["exemplo2", "etl2"],
)
def etl_exemplo_persistencia_postgres():
    MYCONNAME = 'data-stg'

    create_pet_table = SQLExecuteQueryOperator(
        task_id="create_pet_table",
        conn_id=MYCONNAME,
        sql="sql/pet_schema.sql",
    )

    

    create_pet_table



etl_exemplo_persistencia_postgres()