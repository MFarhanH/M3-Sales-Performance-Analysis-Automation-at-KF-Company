# Judul Project
Sales Performance Analysis Automation at KF Company

## Repository Outline

M3-Sales-Performance-Analysis-Automation-at-KF-Company/
├── dags
|   └── P2M3_MuhammadFarhan_Hendriyanto_DAG.py
├── data
|   ├── P2M3_MuhammadFarhan_Hendriyanto_KimiaFarma_Dataset_sampling.csv
|   └── P2M3_MuhammadFarhan_Hendriyanto_KimiaFarma_Dataset_sampling_clean.csv
├── images
|   ├── Introduction & Objective.png
|   ├── kesimpulan.png
|   ├── plot & insight 01.png
|   ├── plot & insight 02.png
|   ├── plot & insight 03.png
|   ├── plot & insight 04.png
|   ├── plot & insight 05.png
|   └── plot & insight 06.png
├── postgres_data
├── .env
├── .gitignore
├── airflow_ES.yaml
├── P2M3_MuhammadFarhan_Hendriyanto_Contextual.txt
├── P2M3_MuhammadFarhan_Hendriyanto_DAG_Graph.jpg
├── P2M3_MuhammadFarhan_Hendriyanto_ddl.txt
├── P2M3_MuhammadFarhan_Hendriyanto_GX.ipynb
└── README.md

## Problem Background
Menurut Prosple Indonesia (https://id.prosple.com/career-planning/10-perusahaan-terbaik-untuk-lulusan-farmasi), Kimia Farma merupakan salah satu perusahaan farmasi terbesar di Indonesia. Kesuksesan perusahaan ini tidak lepas dari kinerja penjualan harian yang dilakukan oleh setiap cabang. Oleh karena itu, performa masing-masing cabang memiliki peran penting dalam mendukung pertumbuhan dan keberlangsungan bisnis Kimia Farma secara keseluruhan.

## Project Output
Output dari project ini adalah untuk membantu mempermudah proses eksekusi dari pembambilan data dari datase, 
melakukan cleaning/transformasi, dan melakukan loading data ke platform kibana untuk melakukan pembuatan visualisasi
yang nantinya diharapkan dapat membantu pengambilan keputusan yang lebih baik.

## Data
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 50000 entries, 0 to 49999
Data columns (total 20 columns):
 #   Column                 Non-Null Count  Dtype  
---  ------                 --------------  -----  
 0   Product Id             50000 non-null  object 
 1   Product Name           50000 non-null  object 
 2   Product Category       50000 non-null  object 
 3   Price                  50000 non-null  int64  
 4   Transaction Id         50000 non-null  object 
 5   Date                   50000 non-null  object 
 6   Branch Id              50000 non-null  int64  
 7   Customer Name          50000 non-null  object 
 8   Discount Percentage    50000 non-null  float64
 9   Rating Transaksi       50000 non-null  float64
 10  Branch Category        50000 non-null  object 
 11  Branch Name            50000 non-null  object 
 12  Kota                   50000 non-null  object 
 13  Provinsi               50000 non-null  object 
 14  Rating Cabang          50000 non-null  float64
 15  Inventory Id           50000 non-null  object 
 16  Opname Stock           50000 non-null  int64  
 17  Persentase Gross Laba  50000 non-null  float64
 18  Nett Sales             50000 non-null  float64
 19  Nett Profit            50000 non-null  float64
dtypes: float64(6), int64(3), object(11)
memory usage: 7.6+ MB

Detail Kolom:

- transaction_id: Transaction ID code
- date: Transaction date
- branch_id: Kimia Farma branch ID code
- branch_name: Kimia Farma branch name
- kota: City of the Kimia Farma branch
- provinsi: Province of the Kimia Farma branch
- rating_cabang: Customer rating of the Kimia Farma branch
- customer_name: Name of the customer who made the transaction
- product_id: Product ID code
- product_name: Name of the medicine
- price: Price of the medicine
- discount_percentage: Discount percentage applied to the medicine
- persentase_gross_laba: persentase_gross_laba: Gross profit percentage based on the following conditions:
    - Price ≤ Rp 50,000 → 10% profit
    - Price > Rp 50,000 - 100,000 → 15% profit
    - Price > Rp 100,000 - 300,000 → 20% profit
    - Price > Rp 300,000 - 500,000 → 25% profit
    - Price > Rp 500,000 → 30% profit
- nett_sales: Price after discount
- nett_profit: Profit earned by Kimia Farma
- rating_transaksi: Customer rating of the transaction
- product category: kategori produk
- branch category: kategori cabang
- inventory id
- opname stock

```
## Method
Project ini diselesaikan menggunakan docker yang akan membantu menjalankan aiflow, kibana, elasticsearch, dan postgresql.

## Stacks
- python
- pandas
- great expectation
- airflow
- sqlalchemy
- elasticsearch

## Reference
- https://www.kaggle.com/datasets/anggundwilestari/kimia-farma-performance-analysis-2020-2023?select=Analysis+Kimia+Farma_Query.txt

**Referensi tambahan:**
- https://id.prosple.com/career-planning/10-perusahaan-terbaik-untuk-lulusan-farmasi
