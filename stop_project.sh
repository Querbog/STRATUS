#!/bin/bash

echo "Stopping Student Activity Pipeline..."

pkill -f silver_streaming.py
pkill -f kafka.Kafka
pkill -f zookeeper
pkill -f airflow

echo "All services stopped safely."

