# 🧪 A/B Testing for Conversion Optimization

![Python](https://img.shields.io/badge/Python-3.14-blue)
![Status](https://img.shields.io/badge/Project-Completed-brightgreen)
![Type](https://img.shields.io/badge/Type-Data%20Analysis-orange)

---

## 📌 Business Problem
A product team aims to improve conversion rates on a landing page. Two versions of the page — **Variant A (Control)** and **Variant B (New Design)** — are tested to determine which version drives better user conversions.

---

## 🎯 Objective
To evaluate whether **Variant B significantly improves conversion rates** compared to Variant A using statistical hypothesis testing and data-driven analysis.

---

## 📊 Dataset
- Simulated dataset with **8,000 users**
- Split into:
  - **Group A (Control)**
  - **Group B (Variant)**
- Features:
  - `user_id` → Unique identifier  
  - `group` → A/B test group  
  - `converted` → Conversion outcome (1 = Yes, 0 = No)

---

## 🧠 Methodology

### 1️⃣ Data Cleaning & Validation
- Checked for missing/null values  
- Verified equal distribution across groups  
- Ensured data consistency  

---

### 2️⃣ Exploratory Data Analysis (EDA)
- Calculated conversion rates for each group  
- Compared user behavior across variants  
- Visualized results using bar charts  

---

### 3️⃣ Hypothesis Testing

**Statistical Test Used:** Z-test for proportions  

#### Hypotheses:
- **H₀ (Null Hypothesis):** No difference in conversion rates  
- **H₁ (Alternative Hypothesis):** Variant B improves conversion rate  

---

## 📈 Results

| Metric              | Group A | Group B |
|--------------------|--------|--------|
| Conversion Rate    | 13.0%  | 12.6%  |

- **Z-statistic:** 0.5225  
- **P-value:** 0.6013  

👉 **Conclusion:** No statistically significant difference between the two groups  

---

## 💡 Key Insights

- Variant B does **not outperform** Variant A  
- Observed difference is **statistically insignificant**  
- UI/UX changes in Variant B **do not meaningfully impact conversions**  

---

## 🚀 Business Recommendations

- ❌ Do NOT implement Variant B  
- ✅ Retain existing version (Variant A)  
- 🔄 Test alternative design or feature changes  
- 📊 Consider increasing sample size for future experiments  

---

## 📊 Visualization

![Conversion Rates](conversion_chart.png)

- Bar chart comparing conversion rates  
- Shows minimal variation between groups  

---

## 🛠️ Tech Stack

- **Language:** Python  
- **Libraries:** Pandas, NumPy, Statsmodels, Matplotlib  
- **Concepts:** A/B Testing, Hypothesis Testing, Data Analysis, Visualization  

---

## 📂 Project Structure

