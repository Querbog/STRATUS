#!/bin/bash
set -e

echo "🧹 Resetting Student Streaming Project (CLEAN MODE)"

KAFKA_HOME=~/kafka
PROJECT_HOME=~/student_streaming_project

TOPIC=student_activity
CHECKPOINT_DIR=$PROJECT_HOME/data/checkpoints/student_activity
SILVER_DIR=$PROJECT_HOME/data/silver
GOLD_DIR=$PROJECT_HOME/data/gold

# ---- DELETE SPARK OUTPUT ----
echo "▶ Removing Spark output directories"
rm -rf "$CHECKPOINT_DIR"
rm -rf "$SILVER_DIR"
rm -rf "$GOLD_DIR"

# ---- DELETE KAFKA TOPIC ----
echo "▶ Deleting Kafka topic (if exists)"
$KAFKA_HOME/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --delete \
  --topic $TOPIC || true

sleep 3

# ---- RECREATE TOPIC ----
echo "▶ Creating Kafka topic"
$KAFKA_HOME/bin/kafka-topics.sh \
  --bootstrap-server localhost:9092 \
  --create \
  --topic $TOPIC \
  --partitions 1 \
  --replication-factor 1

echo "✅ Reset complete"

