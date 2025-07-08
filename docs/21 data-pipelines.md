# Data Pipelines in Python

A **data pipeline** is a sequence of processing steps that transform and transport data from source to destination.

Python is a popular language for building pipelines thanks to:
- Rich ecosystem (Pandas, Airflow, Prefect, etc.)
- First-class functions and generators
- Async and multiprocessing support
- Simple glue code for I/O systems

---

## 🧠 Core Pipeline Concepts

| Concept        | Description                                            |
|----------------|--------------------------------------------------------|
| Source         | Where data comes from (DB, file, API, etc.)            |
| Transform      | Process or enrich data                                 |
| Sink           | Final destination (storage, dashboard, ML model, etc.) |
| Orchestration  | Managing execution order, dependencies, retries        |
| Monitoring     | Logging, metrics, failure alerts                       |

---

## 🧩 Pipeline Patterns

### 1. Functional Chaining (Streaming)

```python
def read_file(path):
    with open(path) as f:
        for line in f:
            yield line.strip()

def parse(line):
    ...

def transform(record):
    ...

def write_sink(record):
    ...

for line in read_file("data.txt"):
    record = parse(line)
    transformed = transform(record)
    write_sink(transformed)
```

- ✅ Memory-efficient (streaming)
- ✅ Easy to parallelize
- ❌ Error handling can get tricky

---

### 2. Batch Pipeline with Pandas

```python
import pandas as pd

df = pd.read_csv("input.csv")
df["total"] = df["qty"] * df["price"]
df = df[df["total"] > 1000]
df.to_csv("output.csv")
```

- ✅ Very concise
- ❌ Not memory efficient for large datasets

---

### 3. DAG-based Pipeline (Airflow/Prefect)

```python
@task
def extract(): ...

@task
def transform(data): ...

@task
def load(data): ...

with Flow("etl") as flow:
    data = extract()
    transformed = transform(data)
    load(transformed)
```

- ✅ Retry support, scheduling, monitoring
- ✅ Production-grade orchestration
- ❌ More boilerplate/setup

---

## 🔁 Stream Processing

### With Generators

```python
def pipeline():
    for line in read_file():
        if is_valid(line):
            yield transform(line)
```

Use generators for:
- Lazy evaluation
- Low memory usage
- Real-time ingestion

---

## ⚙️ Parallelism & Concurrency

### Multithreading with `concurrent.futures`

```python
from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor() as executor:
    results = list(executor.map(transform, records))
```

### Multiprocessing

```python
from multiprocessing import Pool

with Pool(4) as pool:
    results = pool.map(transform, records)
```

### Async Pipelines (I/O Bound)

```python
import aiofiles
import asyncio

async def process():
    async with aiofiles.open("data.txt") as f:
        async for line in f:
            await transform(line)
```

---

## 🧰 Common Libraries for Pipelines

| Tool       | Use Case                        |
|------------|---------------------------------|
| **Pandas**     | In-memory, tabular batch data       |
| **Airflow**    | DAG-based pipeline orchestration    |
| **Prefect**    | Modern replacement for Airflow      |
| **Luigi**      | Simple dependency DAGs              |
| **Dagster**    | Data-aware pipelines, type-safe     |
| **Dask**       | Scalable parallel Pandas/Numpy      |
| **Ray**        | Distributed, actor-based compute     |
| **PySpark**    | Distributed ETL, big data            |
| **Streamz**    | Real-time stream pipelines           |

---

## 🧱 Building a Reusable Pipeline Framework

```python
class Step:
    def run(self, data):
        raise NotImplementedError

class Pipeline:
    def __init__(self, steps):
        self.steps = steps

    def run(self, data):
        for step in self.steps:
            data = step.run(data)
        return data
```

Usage:

```python
class MultiplyByTwo(Step):
    def run(self, x): return x * 2

class AddFive(Step):
    def run(self, x): return x + 5

pipeline = Pipeline([MultiplyByTwo(), AddFive()])
print(pipeline.run(3))  # 11
```

---

## 🔐 Error Handling

### Per-step try/except

```python
def safe_transform(record):
    try:
        return transform(record)
    except Exception as e:
        log_error(e)
        return None
```

### Retry Decorators

```python
from tenacity import retry, stop_after_attempt

@retry(stop=stop_after_attempt(3))
def call_api(): ...
```

---

## 🧪 Testing Pipelines

- **Unit test individual steps**
- Use **mock data** for integration testing
- For Airflow/Prefect:
  - Use test DAGs
  - Validate idempotency
  - Simulate failures

---

## 📈 Monitoring and Metrics

| Tool         | Use                            |
|--------------|---------------------------------|
| Logging      | Track step-by-step activity     |
| Prometheus   | Metrics + Grafana dashboards    |
| OpenTelemetry| Tracing, span correlation       |
| Airflow UI   | Built-in DAG and task logs      |
| Prefect Cloud| Logs, metrics, alerts           |

---

## 🧨 Pitfalls and Anti-Patterns

### 1. Loading entire dataset in memory

Use streaming or chunked reads:

```python
pd.read_csv("huge.csv", chunksize=10_000)
```

### 2. Tight coupling between steps

Decouple with:
- Clear I/O contracts
- Class- or function-based steps

### 3. No retry logic for I/O

Use retries with backoff for:
- External APIs
- DB/network calls

### 4. No monitoring or logging

You can't debug what you can't see.

---

## 🧬 Real-World Use Cases

| Domain       | Example                          |
|--------------|-----------------------------------|
| Data Science | CSV → Pandas → cleaned DataFrame |
| Web Scraping | URL list → HTML → parsed data    |
| ML Training  | Data ingest → feature eng → model|
| Analytics    | Logs → Kafka → DB or dashboard   |
| Finance      | CSV → validate → calculate → DB  |

---

## ✅ Summary

| Feature          | Options / Tools                        |
|------------------|----------------------------------------|
| Execution style   | Streaming, Batch, DAG                  |
| Parallelism       | Threads, multiprocessing, async        |
| Orchestration     | Airflow, Prefect, Luigi, Dagster       |
| Libraries         | Pandas, PySpark, Dask, Streamz         |
| Error handling    | `try/except`, `tenacity`, retry logic  |
| Monitoring        | Logs, metrics, tracing, dashboards     |

---

## 📚 Further Reading

- [Airflow Documentation](https://airflow.apache.org/)
- [Prefect Docs](https://docs.prefect.io/)
- [Streamz for real-time pipelines](https://streamz.readthedocs.io/)
- [Pandas User Guide](https://pandas.pydata.org/docs/)
- [Dask for Scalable Data](https://docs.dask.org/en/stable/)
- [Dagster Docs](https://docs.dagster.io/)

