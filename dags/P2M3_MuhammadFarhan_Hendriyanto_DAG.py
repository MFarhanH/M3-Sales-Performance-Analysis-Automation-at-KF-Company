'''
=================================================
Milestone 3

Nama  : Muhammad Farhan Hendriyanto
Batch : FTDS-027-HCK

Program ini dibuat untuk melakukan automatisasi transform dan load data dari PostgreSQL ke ElasticSearch.
Dataset yang diguanakan adalah dataset dari penjualan berdasarkan cabang dan daerah dari Kimia Farma.

Tujuan utama dashboard ini adalah untuk membantu mempermudah proses eksekusi dari pengambilan data dari database, 
melakukan cleaning/transformasi, dan melakukan loading data ke platform kibana untuk melakukan pembuatan visualisasi
yang nantinya diharapkan dapat membantu pengambilan keputusan yang lebih baik. 
=================================================
'''


import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine
from airflow import DAG
from airflow.decorators import task
from airflow.operators.empty import EmptyOperator
from elasticsearch import Elasticsearch

default_args = {
    'owner': 'Farhan',
    'start_date': datetime(2024, 11, 1)
}

def readCSV():
    '''
    Function used to read CSV file
    '''
    df = pd.read_csv(
        '/opt/airflow/data/P2M3_MuhammadFarhan_Hendriyanto_KimiaFarma_Dataset_sampling.csv')

with DAG(
    dag_id='P2M3_muhammadfarhan_hendriyanto_DAG',
    description='from csv to postgres',
    schedule_interval='*/10 9 * * 6',
    default_args=default_args,
    catchup=False
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    @task()
    def extract():
        '''
        Function used to transform data
        '''
        
        database = 'airflow'
        username = 'airflow'
        password = 'airflow'
        host = 'postgres'

        postgres_url = f'postgresql+psycopg2://{username}:{password}@{host}/{database}'

        engine = create_engine(postgres_url)
        conn = engine.connect()

        df = pd.read_sql('select * from table_m3', conn)
        df.to_csv(
            '/opt/airflow/data/P2M3_MuhammadFarhan_Hendriyanto_KimiaFarma_Dataset_sampling.csv', index=False)
        # df = pd.read_csv('/opt/airflow/data/P2M3_MuhammadFarhan_Hendriyanto_KimiaFarma_Dataset_sampling.csv')
        print('Success extract to airflow')

    @task()
    def transform():
        '''
        Function used to transform data
        '''
        df = pd.read_csv(
            '/opt/airflow/data/P2M3_MuhammadFarhan_Hendriyanto_KimiaFarma_Dataset_sampling.csv')

        # Remove Duplicates (tidak ada)
        df.drop_duplicates(inplace=True)

        # Handle missing values

        for col in df.columns:
            # untuk kolom numerik
            if df[col].dtype in ['float64', 'int64']:
                median = df[col].median()
                df[col].fillna(median, inplace=True)
            # untuk kolom kategorik
            else:
                mode = df[col].mode()[0]
                df[col].fillna(mode, inplace=True)

        # Mengubah spasi menjadi underscore
        df.columns = df.columns.str.replace(' ', '_')

        # Membuat nama kolom menjadi lowercase
        df.columns = df.columns.str.lower()

        print('Preprocessed data is success')
        print(df.head())
        df.to_csv(
            '/opt/airflow/data/P2M3_MuhammadFarhan_Hendriyanto_KimiaFarma_Dataset_sampling_clean.csv', index=False)

    @task
    def loading():
        '''
        Function to load data to ElasticSearch
        '''
        es = Elasticsearch('http://elasticsearch:9200')

        # Read data file
        df = pd.read_csv(
            '/opt/airflow/data/P2M3_MuhammadFarhan_Hendriyanto_KimiaFarma_Dataset_sampling_clean.csv')

        # Send data to ElasticSearch
        for i, row in df.iterrows():
            res = es.index(index='data_milestone', id=i+1, body=row.to_json())
            print(f'ini data ke - {i+1}')

    # definisikan flownya
    start >> extract() >> transform() >> loading() >> end
