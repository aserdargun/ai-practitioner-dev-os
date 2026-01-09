# Month 10: Streaming & Big Data

## Why It Matters

ML at scale requires processing large datasets and real-time streams. This month teaches distributed computing and streaming—skills for enterprise-scale ML systems.

**Job Relevance**: Big data skills are essential for Data Engineers and ML Engineers at large companies. Spark and Kafka are industry standards.

---

## Prerequisites

- Month 01-09 completed
- Python proficiency
- SQL mastery
- Cloud experience

---

## Learning Goals

### Tier 2 Focus (Consolidation)
- Airflow for batch orchestration
- Data pipelines at scale

### Tier 3 Focus
- Apache Kafka for streaming
- Apache Spark for distributed computing
- Kinesis for AWS streaming
- Real-time ML inference
- Data lakes and warehouses

---

## Main Project: Real-Time ML Pipeline

Build a streaming ML system that:
1. Ingests events via Kafka
2. Processes with Spark Streaming
3. Runs real-time inference
4. Stores results in data lake
5. Provides batch analytics
6. Monitors throughput and latency

### Deliverables

1. **`streaming/`** - Kafka producers and consumers
2. **`spark/`** - Spark jobs
3. **`inference/`** - Real-time model serving
4. **`batch/`** - Batch processing jobs
5. **`monitoring/`** - Pipeline monitoring
6. **`docs/`** - Architecture documentation

### Definition of Done

- [ ] Kafka topic producing/consuming works
- [ ] Spark job processes streaming data
- [ ] Real-time inference integrated
- [ ] Results stored in data lake
- [ ] Batch analytics job running
- [ ] Throughput metrics visible
- [ ] End-to-end latency <1s

---

## Week-by-Week Plan

### Week 1: Kafka Fundamentals

**Focus**: Event streaming basics.

- Kafka architecture
- Topics, partitions, consumers
- Producer patterns
- Consumer groups
- Docker Kafka setup

**Milestone**: Kafka producing and consuming events.

### Week 2: Spark for Big Data

**Focus**: Distributed processing.

- Spark architecture
- RDDs and DataFrames
- Transformations and actions
- Spark SQL
- PySpark development

**Milestone**: Spark job processing batch data.

### Week 3: Streaming Integration

**Focus**: Real-time processing.

- Spark Streaming
- Kafka-Spark integration
- Windowing operations
- Real-time inference
- State management

**Milestone**: Streaming pipeline with ML inference.

### Week 4: Production & Monitoring

**Focus**: Reliability at scale.

- Data lake storage (S3/ADLS)
- Batch analytics with Spark
- Pipeline monitoring
- Error handling
- Performance tuning

**Milestone**: Complete streaming platform with monitoring.

---

## Stretch Goals

- Add exactly-once semantics
- Implement feature store integration
- Build real-time dashboard
- Add schema registry
- Implement backpressure handling

---

## Claude Prompts

### Planning
```
/plan-week
```

### Architecture Design
```
As the Researcher, design a streaming architecture for real-time fraud detection.
```

### Spark Optimization
```
/debug-learning

My Spark job is slow. Here's the code...
```

### Kafka Best Practices
```
As the Researcher, what are Kafka best practices for ML event streaming?
```

### Review
```
/harden

Review my streaming pipeline for reliability and performance.
```

---

## How to Publish

### Demo Script
```bash
# Start Kafka and Spark
docker-compose up -d

# Start producer (simulates events)
python streaming/producer.py

# Watch Spark process events
spark-submit spark/streaming_job.py

# Check results
python batch/query_results.py
```

### Write-Up Topics
- Building real-time ML pipelines
- Kafka for ML event streaming
- Spark for distributed processing
- Batch vs streaming trade-offs

---

## Resources

- [Apache Kafka Documentation](https://kafka.apache.org/documentation/)
- [Apache Spark Documentation](https://spark.apache.org/docs/latest/)
- [PySpark Guide](https://spark.apache.org/docs/latest/api/python/)
- [Confluent Kafka Tutorials](https://developer.confluent.io/)

---

## Month Evaluation

At month end, run:
```bash
python .claude/path-engine/evaluate.py --month 10
```
