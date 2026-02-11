#!/bin/bash
set -e

echo "🚀 Starting Student Streaming Project (RESUME MODE)"

KAFKA_HOME=~/kafka
SPARK_HOME=~/spark
PROJECT_HOME=~/student_streaming_project

# -------------------------------
# 1. Start ZooKeeper
# -------------------------------
echo "▶ Starting ZooKeeper..."
gnome-terminal -- bash -c "
$KAFKA_HOME/bin/zookeeper-server-start.sh \
$KAFKA_HOME/config/zookeeper.properties
exec bash
"

sleep 5

# -------------------------------
# 2. Start Kafka Broker
# -------------------------------
echo "▶ Starting Kafka Broker..."
gnome-terminal -- bash -c "
$KAFKA_HOME/bin/kafka-server-start.sh \
$KAFKA_HOME/config/server.properties
exec bash
"

sleep 8

# -------------------------------
# 3. Start Spark Silver Streaming
# -------------------------------
echo "▶ Starting Spark Silver Streaming Consumer..."
gnome-terminal -- bash -c "
cd $PROJECT_HOME/spark
$SPARK_HOME/bin/spark-submit \
--packages org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5 \
silver_streaming.py
exec bash
"

sleep 5

# -------------------------------
# 4. Start Airflow
# -------------------------------
echo "▶ Starting Airflow (webserver + scheduler)..."
gnome-terminal -- bash -c "
conda activate airflow-tutorial
airflow webserver
exec bash
"

sleep 5

gnome-terminal -- bash -c "
conda activate airflow-tutorial
airflow scheduler
exec bash
"

echo "✅ Project started successfully"

