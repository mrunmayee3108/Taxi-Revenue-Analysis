# 🚕 Taxi Revenue Analysis & Dashboard

<p align="left">
  <img src="https://cdn.simpleicons.org/python" height="48" />
  <img src="https://cdn.simpleicons.org/pandas" height="48" />
  <img src="https://cdn.simpleicons.org/streamlit" height="48" />
  <img src="https://seaborn.pydata.org/_static/logo-wide-lightbg.svg" height="48" />
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" height="48" />
  <img src="https://cdn.simpleicons.org/scipy" height="48" />

</p>

**Python · Pandas · Statistics · Streamlit · Seaborn · Matplotlib · Scipy**


## 📘 Project Overview

This project performs **end-to-end Taxi Trip Data Analysis, Statistical Evaluation, and Interactive Dashboard Visualization** using real-world taxi trip records.

It includes:

* Cleaning and preprocessing raw taxi trip data using a **Jupyter Notebook**
* Exploratory Data Analysis (EDA) with **statistical validation**
* Applying **inferential statistics** to support business insights
* A **Streamlit dashboard** to visualize revenue and trip patterns

The project combines **data analysis + statistics + visualization** to derive reliable insights.


## 📷 Demo Screenshots

<img width="1600" height="838" alt="image" src="https://github.com/user-attachments/assets/49b480a1-19d7-4158-9d37-b51c8754f570" />


## 📁 Project Structure

```
Taxi-Revenue-Analysis/
│
├── taxi.ipynb        → Data cleaning, EDA & statistical analysis
│
├── app.py                          → Streamlit dashboard
├── requirements.txt                → Dependencies
│
└── README.md                       → Documentation
```

Here the dataset file was not uploaded due to its very large size. dataset download link is in taxi.ipynb

## 🧹 Data Cleaning, EDA & Statistical Analysis

**File:** `taxi.ipynb`

The notebook performs:

### 🔹 Data Cleaning

* Handling missing and invalid values
* Removing fare and distance outliers
* Filtering unrealistic trips
* Standardizing column names

### 🔹 Exploratory Data Analysis

* Payment type vs average fare
* Trip distance vs fare trends
* Passenger count distribution

### 🔹 Statistical Analysis

Using **SciPy** and **StatsModels**:

* Hypothesis testing to compare **Card vs Cash fares**

  * Two-sample **t-test**
* Correlation analysis between:

  * Trip distance and fare amount
* Regression analysis to:

  * Quantify impact of trip distance on fare
* Statistical validation of observed trends

The final dataset is exported as `final_taxi_data.csv`.


## 📊 Interactive Dashboard (Streamlit)

**File:** `app.py`

Dashboard features:

* Clean responsive layout using Streamlit columns
* Seaborn & Matplotlib visualizations
* Charts include:

  * **Average Fare by Payment Type**
  * **Fare Distribution (Card vs Cash)**
  * **Trip Distance vs Fare**
* Optimized plots using:
  * Transparency
  * Sampling for large datasets

Run using:

```
streamlit run app.py
```


## 🛠️ Tech Stack

### Languages & Libraries

* Python
* Pandas
* NumPy
* SciPy (`scipy.stats`)
* StatsModels (`statsmodels`)
* Matplotlib
* Seaborn
* Streamlit


## 📦 Requirements

`requirements.txt`:

```
streamlit
pandas
numpy
matplotlib
seaborn
scipy
statsmodels
```


# 🚀 How to Run the Project

## 1️⃣ Install Dependencies

```
pip install -r requirements.txt
```

## 2️⃣ Run Streamlit Dashboard

```
streamlit run app.py
```


## 🧠 Insights Discovered (Statistically Validated)

* **Card payments** have a **significantly higher average fare** than cash payments (t-test)
* Fare increases **positively with trip distance**
* Strong correlation between **distance and fare**
* Majority of trips involve **1–2 passengers**
* Statistical analysis supports encouraging **digital payments** to increase revenue


## 👥 Contributing

Pull requests are welcome.


## 📄 License

MIT License.


## 🙏 Acknowledgments

* NYC Taxi Trip Dataset (Public Dataset) (https://www.kaggle.com/datasets/elemento/nyc-yellow-taxi-trip-data?resource=download)


## ⭐ Support

If you like this project, consider giving the repository a ⭐ star on GitHub!

~ Mrunmayee Sachin Potdar
