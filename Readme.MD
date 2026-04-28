# ☁️ Cloud Cost Analytics & Forecasting System

A Python-based data analytics project that simulates cloud billing data and performs cost analysis, visualization, and forecasting to generate actionable insights for cloud cost optimization.

---

## 📌 Overview

This project focuses on analyzing cloud infrastructure costs using a simulated dataset modeled on real-world cloud services such as compute, storage, and databases.

The system performs:

- Data ingestion and preprocessing  
- Exploratory data analysis (EDA)  
- Statistical analysis  
- Cost trend visualization  
- Basic forecasting using time-series techniques  
- SQL-based querying for aggregated insights  

---

## 🏗️ Architecture
```
    +---------------------+
    |  Synthetic Dataset  |
    | (dataset.py)        |
    +----------+----------+
               |
               v
    +---------------------+
    |  Data Ingestion     |
    | (Pandas - CSV Load) |
    +----------+----------+
               |
               v
    +---------------------+
    | Data Processing     |
    | Cleaning, Transform |
    +----------+----------+
               |
               v
    +---------------------+
    | Exploratory Data    |
    | Analysis (EDA)      |
    +----------+----------+
               |
    +----------+----------+
    |                     |
    v                     v
+----------------+ +----------------------+
| Visualization  | | Statistical Analysis |
| (Matplotlib)   | | Mean, Std, Trends    |
+----------------+ +----------------------+
        |_____________________|  
                  |
                  v
      +---------------------+
      | Forecasting         |
      | (Moving Average)    |
      +----------+----------+
                  |
                  v
      +---------------------+
      | SQL Layer           |
      | (SQLite Queries)    |
      +---------------------+

```

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Matplotlib  
- **Database:** SQLite (via sqlite3)  
- **Concepts:** Data Pipeline, EDA, Time-Series Analysis, Forecasting  

---

## 📂 Project Structure

```
cloud-cost-analytics-forecasting-system/
│── data/
│ └── cloud_billing_data.csv
│
│── outputs/
│ └── charts/
│
│── dataset.py # Generates synthetic dataset
│── analysis.py # Main analysis + visualization + SQL
│── cloud_cost.db # SQLite database (generated)
│── README.md
```


---

## ⚙️ Setup & Installation

### 1. Clone Repository
```
git clone <your-repo-link>
cd cloud-cost-analytics-forecasting-system
```


### 2. Install Dependencies
```
pip install pandas numpy matplotlib
```

---

## ▶️ How to Run

### Step 1: Generate Dataset

```
python dataset.py
```

This creates:

```
data/cloud_billing_data.csv
```


---

### Step 2: Run Analysis

```
python analysis.py
```


This will:

- Perform EDA  
- Generate statistical summaries  
- Create charts (saved in `outputs/charts/`)  
- Perform forecasting  
- Run SQL queries on processed data  

---

## 📊 Key Features

### 🔹 Data Pipeline
- Ingests and processes cloud billing data
- Handles date conversion and transformations

### 🔹 Exploratory Data Analysis
- Identifies trends and patterns
- Detects cost spikes and variations

### 🔹 Visualization Dashboard
- Daily cost trend
- Monthly spending
- Service-wise cost distribution

### 🔹 Forecasting
- Uses moving averages to estimate future cloud costs

### 🔹 SQL Integration
- Stores processed data in SQLite
- Performs aggregation queries (monthly spend, top cost days)

---

## 📈 Example Insights

- Cloud costs show a gradual increase over time  
- Compute (EC2) contributes the highest cost  
- Storage (S3) grows steadily due to accumulation  
- Occasional spikes indicate abnormal usage or scaling events  

---

## 💡 Optimization Recommendations

- Implement auto-scaling and resource right-sizing  
- Use storage lifecycle policies for cost control  
- Monitor anomalies to prevent unexpected billing  
- Use forecasting for budget planning  

---

## 🚀 Future Improvements

- Automate pipeline using Airflow  
- Use real cloud billing APIs (AWS Cost Explorer)  
- Store data in data warehouse (PostgreSQL/BigQuery)  
- Build interactive dashboards (Streamlit/Power BI)  

---

## 🎯 Learning Outcomes

- Built an end-to-end data pipeline  
- Applied EDA and statistical analysis  
- Understood time-series forecasting basics  
- Integrated SQL with Python workflows  
- Connected analytics with real-world cloud problems  

---

## 👨‍💻 Author

**Saksham Joshi**  
B.Tech CSE (DevOps) | UPES  