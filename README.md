🚀 STRATUS
### Student Time-Based Real-Time Activity Tracking & Unified Streaming Platform

STRATUS is an end-to-end **real-time big data streaming and analytics platform** designed to track, process, and analyze **student engagement behavior in online learning environments**.  
The system simulates real-time student activity events, processes them using a **Kafka–Spark streaming architecture**, orchestrates workflows with **Apache Airflow**, and produces analytical insights through a **Gold-layer aggregation model**.

---

## 📊 Dataset Overview

This project is inspired by and modeled on the **Online Course Engagement Dataset** available on Kaggle:  
🔗 https://www.kaggle.com/datasets/rabieelkharoua/predict-online-course-engagement-dataset

### Dataset Description
The dataset represents learner interaction patterns in online courses and includes features such as:

- User ID  
- Course Category  
- Time Spent on Course  
- Number of Videos Watched  
- Number of Quizzes Taken  
- Quiz Scores  
- Completion Rate  
- Device Type  
- Course Completion Status  

### How the Dataset Is Used
- The original dataset is **replayed as streaming events** through Apache Kafka
- Each row is treated as a **real-time student activity event**
- Spark Structured Streaming processes these events into:
  - **Silver Layer** (raw + structured streaming data)
  - **Gold Layer** (aggregated analytical metrics)

This approach allows the project to demonstrate **real-world streaming data engineering patterns**, even though the source dataset is static.

The project follows modern data engineering best practices, including layered data architecture, idempotent batch processing, checkpointed streaming, and orchestration-driven analytics, making it suitable for enterprise-scale analytics and BI workloads.

📌 Key Highlights

✔ Real-time ingestion with Kafka
✔ Fault-tolerant Spark Structured Streaming
✔ Bronze → Silver → Gold layered architecture
✔ Airflow-orchestrated batch analytics
✔ Parquet-based analytics storage
✔ Cloud-ready (AWS S3 / Azure Databricks)
✔ BI & Visualization-ready Gold tables

🧠 System Architecture
┌────────────────┐
│  Python Producer│
│ (Event Generator)│
└────────┬────────┘
         │
         ▼
┌────────────────┐
│   Apache Kafka │
│ Topic: student │
└────────┬────────┘
         │
         ▼
┌──────────────────────────────┐
│ Spark Structured Streaming   │
│ Silver Layer (Raw Parquet)   │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Spark Batch (Airflow DAG)    │
│ Structured Silver → Gold     │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ Gold Layer (Aggregated Data) │
│ Parquet on S3 / Local FS     │
└────────┬─────────────────────┘
         │
         ▼
┌──────────────────────────────┐
│ BI / Visualization Layer     │
│ (Power BI / Tableau / Superset│
│  / Databricks SQL)           │
└──────────────────────────────┘

🗂 Project Structure
STRATUS/
├── airflow/
│   └── dags/
│       └── student_pipeline_dag.py
├── spark/
│   ├── silver_streaming.py
│   ├── silver_map_to_structured.py
│   ├── gold_aggregation.py
│   └── gold_batch.py
├── producer/
│   └── student_producer.py
├── data/
│   ├── silver/
│   ├── gold/
│   └── checkpoints/
├── start_project.sh
├── reset_project.sh
├── stop_project.sh
└── README.md

⚙️ Technology Stack
Layer	Technology
Data Ingestion	Apache Kafka
Stream Processing	Apache Spark Structured Streaming
Batch Processing	Apache Spark
Orchestration	Apache Airflow
Storage	Parquet (Local FS / Amazon S3)
Language	Python
Deployment	Bash Automation
BI (Planned)	Power BI / Tableau / Superset
🧩 Data Architecture
🟡 Bronze Layer

Raw event data published to Kafka

No transformation

High-throughput ingestion

⚪ Silver Layer

Spark Structured Streaming

Schema-less JSON → MapType

Fault-tolerant with checkpoints

Stored as Parquet

🟢 Gold Layer

Airflow-triggered Spark batch jobs

Business-level aggregations

Optimized for analytics & reporting

Stored in Parquet (partition-friendly)

🚀 How to Run the Project
1️⃣ Clone Repository
git clone https://github.com/Querbog/STRATUS.git
cd STRATUS

2️⃣ Reset (Optional – Clean Run)
chmod +x reset_project.sh
./reset_project.sh


✔ Deletes Kafka topic
✔ Clears checkpoints
✔ Cleans Silver & Gold layers

3️⃣ Start Full Pipeline
chmod +x start_project.sh
./start_project.sh


This automatically starts:

ZooKeeper

Kafka Broker

Spark Silver Streaming

Airflow Webserver

Airflow Scheduler

4️⃣ Start Producer
cd producer
python student_producer.py


This simulates real-time student activity events.

5️⃣ Trigger Airflow DAG

Open: http://localhost:8080

Unpause student_pipeline_dag

Trigger manually or let scheduler handle it

6️⃣ Verify Output
Silver Layer
spark.read.parquet("data/silver").show()

Gold Layer
spark.read.parquet("data/gold").show()

📊 Visualization Layer (Future Integration)

The Gold layer is BI-ready and designed for direct consumption by analytics tools.

Supported Visualization Options
Tool	Integration
Power BI	Read Parquet from S3
Tableau	External table via S3
Apache Superset	SQL on Parquet
Databricks SQL	Native Parquet analytics
AWS Athena	External table over S3
Visualization Use-Cases

Course engagement trends

Completion ratio analysis

Average time spent per category

User performance benchmarking

☁️ Cloud Deployment (Planned & Supported)
Amazon S3

Replace local paths with s3a://

Spark writes Gold tables in batches

Airflow triggers periodic refresh

Azure Databricks

Silver streaming runs as Databricks Job

Gold aggregation via Databricks Workflows

Databricks SQL for BI dashboards

🧠 Design Decisions

✔ Streaming and batch decoupled
✔ Idempotent batch analytics
✔ Checkpoint-backed fault tolerance
✔ Parquet for columnar analytics
✔ Airflow for orchestration, not streaming
✔ Cloud-native architecture

🔮 Future Enhancements

Delta Lake for ACID guarantees

Schema evolution handling

Data quality checks

Alerting & monitoring

CI/CD for DAGs

Real-time dashboard layer

🎯 Why STRATUS?

STRATUS reflects real-world data engineering practices, not toy examples.
It demonstrates skills in:

Streaming systems

Batch analytics

Orchestration

Cloud-ready pipelines

Analytics-first design

This project is interview-ready, enterprise-oriented, and scalable.

👤 Author

Querbog

📌 GitHub: https://github.com/Querbog

📌 Project: STRATUS
