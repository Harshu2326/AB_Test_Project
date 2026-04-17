# 🧪 A/B Testing for Conversion Optimization

A real-world simulation of an A/B test used by product teams to make data-driven decisions on conversion optimization.

---

## 📌 Problem
A product team aims to improve landing page conversions. Two versions are tested:
- **Variant A** (current version)
- **Variant B** (new version)

The goal is to determine whether the new design leads to higher user conversions.

---

## 🎯 Objective
Analyze user conversion data and determine whether **Variant B significantly outperforms Variant A** using statistical testing.

---

## 📊 Dataset
- **8,000 simulated users**

**Features:**
- `user_id` → Unique identifier  
- `group` → A / B test group  
- `converted` → (0 = No, 1 = Yes)

---

## ⚙️ Approach
- Cleaned and validated dataset  
- Calculated conversion rates for both groups  
- Performed **Z-test for proportions**

**Hypothesis:**
- **H₀:** No difference in conversion rates  
- **H₁:** Variant B improves conversions  

---

## 📈 Results

**Conversion Rate:**
- Variant A: **13.0%**
- Variant B: **12.6%**

**Statistical Test:**
- Z-statistic: **0.5225**  
- P-value: **0.6013**

👉 **Conclusion:** No statistically significant difference between the two groups  

---

## 💡 Insight
Variant B does **not improve conversions and should not be implemented based on statistical evidence**.  
The observed difference is due to random variation, not a meaningful change in user behavior.

---

## 🚀 Recommendation
- ❌ Do **not** implement Variant B  
- ✅ Retain current version (Variant A)  
- 🔄 Test more impactful changes in future experiments  

---

## 📊 Visualization
![Conversion Rates](conversion_chart.png)

---

## 🛠️ Tech Stack
- Python  
- Pandas  
- NumPy  
- Statsmodels  
- Matplotlib  

---

## ▶️ Run the Project

```bash
git clone https://github.com/Harshu2326/AB_Test_Project.git
cd AB_Test_Project
pip install -r requirements.txt
python main.py

