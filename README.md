# 📦 Supply Chain & Logistics Analytics

An end-to-end **Data Science and Business Analytics project** focused on analyzing supply chain operations, sales performance, profitability, logistics efficiency, product performance, and regional business performance.

The project includes a complete **Jupyter Notebook analysis**, an interactive **Streamlit dashboard**, and a detailed **PDF business report**.

---

## 📌 Project Overview

The **Supply Chain & Logistics Analytics** project analyzes supply chain transaction data to identify important business patterns and performance indicators.

The analysis covers:

- Sales and revenue performance
- Profitability and profit margins
- Product and category performance
- Logistics and delivery performance
- Shipping mode analysis
- Regional and geographic performance
- Market performance
- Delivery delays
- Loss-making products
- Interactive filtering and data exploration

The final solution provides both **analytical insights** and an **interactive dashboard** that allows users to explore the data dynamically.

---

## 🎯 Project Objectives

The main objectives of this project are to:

- Analyze overall sales and profitability.
- Measure business performance using key KPIs.
- Identify high-performing and low-performing products.
- Analyze category and market performance.
- Evaluate logistics and delivery efficiency.
- Compare different shipping modes.
- Analyze regional and geographic performance.
- Identify delivery delays and operational issues.
- Provide business insights and recommendations.
- Build an interactive dashboard for business users.
- Provide a detailed analytical report.

---

## 📊 Key Business KPIs

The dashboard provides an executive overview containing KPIs such as:

- **Total Sales**
- **Total Profit**
- **Total Records / Orders**
- **Profit Margin**
- **Units Sold**
- **Average Order Value**
- **Average Delivery Delay**
- **Delayed Orders**

These KPIs dynamically update based on the filters selected by the user.

---

## 🔍 Dashboard Filters

Users can interactively filter the dashboard using:

- **Market**
- **Order Region**
- **Category**
- **Shipping Mode**
- **Delivery Performance**

All relevant KPIs, charts, and filtered data update according to the selected filters.

---

## 📈 Dashboard Analysis

The Streamlit dashboard follows a structured business-analysis workflow.

### Executive Overview

Provides a high-level summary of:

- Sales
- Profit
- Orders / records
- Profit margin
- Units sold
- Average order value
- Delivery delay
- Delayed orders

### Business Insights & Recommendations

The dashboard provides consolidated business insights based on the analyzed sales, profitability, logistics, product, and regional performance.

### Sales & Revenue Analysis

Analyzes:

- Sales by category
- Revenue performance
- Sales trends and comparisons
- Sales contribution across business segments

### Profitability Analysis

Analyzes:

- Total profit
- Profit margins
- Profit by category
- Profit by product
- Profitability comparisons

### Logistics & Delivery Performance

Analyzes:

- Delivery performance
- Delivery status
- Delivery delays
- Regional delivery performance
- Shipping efficiency

### Shipping Mode Analysis

Compares different shipping modes based on:

- Sales
- Profit
- Delivery performance
- Average delivery delay
- Operational efficiency

### Product & Category Performance

Analyzes:

- Top products by sales
- Top products by profit
- Loss-making products
- Category sales
- Category profitability
- Category profit margins

### Regional & Geographic Performance

Analyzes:

- Sales by region
- Profit by region
- Order volume by region
- Regional profitability
- Regional sales vs. profit
- Geographic business performance

### Market Performance

Compares business performance across different markets.

### Filtered Data Explorer

Allows users to inspect the filtered dataset directly inside the dashboard.

The filtered data can also be downloaded as a **CSV file**.

---

## 🔄 Dashboard Workflow

The dashboard follows this analytical flow:

```text
Data Loading
     ↓
Sidebar Filters
     ↓
Filtered Dataset
     ↓
Executive Overview
     ↓
Business Insights & Recommendations
     ↓
Sales & Revenue Analysis
     ↓
Profitability Analysis
     ↓
Logistics & Delivery Analysis
     ↓
Shipping Mode Analysis
     ↓
Product & Category Analysis
     ↓
Regional & Geographic Analysis
     ↓
Market Performance
     ↓
Filtered Data Explorer
     ↓
CSV Download
```

---

## 🗂️ Project Structure

```text
Supply-Chain-Logistics-Analytics/
│
├── data/
│   ├── raw/
│   │   ├── DataCoSupplyChainDataset.csv
│   │   └── DescriptionDataCoSupplyChain.csv
│   │
│   └── processed/
│       └── supply_chain_cleaned.csv
│
├── notebook/
│   └── Supply_Chain_Logistics_Analytics.ipynb
│
├── dashboard/
│   └── app.py
│
├── images/
│   ├── sales_analysis.png
│   ├── logistics_analysis.png
│   ├── product_analysis.png
│   ├── regional_analysis.png
│   └── dashboard_overview.png
│
├── reports/
│   └── Supply_Chain_Logistics_Analytics_Report.pdf
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 🛠️ Technology Stack

### Programming Language

- Python

### Data Analysis

- Pandas
- NumPy

### Data Visualization

- Plotly
- Matplotlib
- Seaborn

### Dashboard

- Streamlit

### Development Environment

- Jupyter Notebook
- VS Code

### Documentation & Reporting

- Markdown
- PDF Report

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Armi-123/Supply-Chain-Logistics-Analytics.git
```

Move into the project directory:

```bash
cd Supply-Chain-Logistics-Analytics
```

---

### 2. Create a Virtual Environment

#### Windows

```bash
python -m venv venv
```

Activate the environment:

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv
```

Activate the environment:

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Run the Streamlit Dashboard

From the project root directory:

```bash
streamlit run dashboard/app.py
```

The Streamlit application will open in your browser.

The dashboard provides interactive filters, KPI cards, business analysis charts, filtered data exploration, and CSV download functionality.

---

## 📓 Run the Jupyter Notebook

The complete analysis notebook is located at:

```text
notebook/Supply_Chain_Logistics_Analytics.ipynb
```

Open the notebook using Jupyter Notebook, JupyterLab, or VS Code.

Run the notebook cells sequentially to reproduce:

- Data loading
- Data preparation
- Exploratory data analysis
- KPI calculations
- Sales analysis
- Profitability analysis
- Logistics analysis
- Product analysis
- Regional analysis
- Business insights
- Visualizations

---

## 📋 Data Preparation

The project uses separate raw and processed data directories.

### Raw Data

The original dataset files are stored inside:

```text
data/raw/
```

These include:

```text
DataCoSupplyChainDataset.csv
DescriptionDataCoSupplyChain.csv
```

### Processed Data

The cleaned dataset used for analysis and dashboard development is stored inside:

```text
data/processed/supply_chain_cleaned.csv
```

The processed dataset is prepared for downstream analysis and dashboard visualization.

---

## 📊 Data Exploration Highlights

The project allows users to move from high-level business KPIs to detailed business analysis.

For example:

```text
Total Sales
     ↓
Category Sales
     ↓
Product Sales
     ↓
Product Profit
     ↓
Loss-Making Products
```

Logistics analysis follows a similar structure:

```text
Delivery Performance
     ↓
Shipping Mode
     ↓
Delivery Delay
     ↓
Regional Delivery Performance
```

Regional analysis can be explored through:

```text
Regional Sales
     ↓
Regional Profit
     ↓
Order Volume
     ↓
Regional Sales vs Profit
```

This structure makes the dashboard useful for both **business overview** and **detailed investigation**.

---

## 💡 Business Insights

The project focuses on identifying actionable insights from multiple business dimensions, including:

- Sales performance
- Profitability
- Product performance
- Category performance
- Logistics efficiency
- Delivery performance
- Shipping modes
- Regional performance
- Market performance
- Loss-making products

These insights help identify areas of strong performance as well as potential operational and financial improvement opportunities.

---

## 📄 Project Report

A detailed PDF report is available at:

```text
reports/Supply_Chain_Logistics_Analytics_Report.pdf
```

The report contains:

- Executive Summary
- Dataset & Data Preparation
- Executive Overview
- Business Insights
- Sales & Revenue Analysis
- Profitability Analysis
- Logistics & Delivery Analysis
- Shipping Mode Analysis
- Product & Category Analysis
- Regional & Geographic Analysis
- Interactive Filtering
- Business Recommendations
- Dashboard Architecture
- Technology Stack
- Conclusion

---

## 📸 Dashboard Preview

Dashboard screenshots are stored inside:

```text
images/
```

Recommended screenshots include:

- `dashboard_overview.png`
- `sales_analysis.png`
- `logistics_analysis.png`
- `product_analysis.png`
- `regional_analysis.png`

These images provide visual examples of the interactive dashboard and analytical sections.

---

## 📥 Filtered Data Download

The dashboard includes a **Filtered Data Explorer**.

After applying filters, users can:

1. View the filtered records.
2. Explore the selected data directly in the dashboard.
3. Download the filtered dataset as a CSV file.

This provides an easy way to export data for further analysis or reporting.

---

## 📌 Use Cases

This project can support:

- Supply chain performance monitoring
- Sales performance analysis
- Profitability analysis
- Product portfolio analysis
- Category performance analysis
- Logistics performance monitoring
- Shipping mode comparison
- Regional business analysis
- Market performance analysis
- Delivery performance monitoring
- Business decision support
- Operational performance review

---

## 🔮 Future Improvements

Possible future enhancements include:

- Automated scheduled reporting
- Advanced sales forecasting
- Demand forecasting
- Inventory optimization
- Real-time supply chain data integration
- Anomaly detection
- Advanced logistics optimization
- Automated email reports
- Role-based dashboard access
- Cloud deployment
- Advanced predictive analytics

---

## 👨‍💻 Project Type

```text
Data Science
Business Analytics
Supply Chain Analytics
Data Visualization
Interactive Dashboard
```
---

## 🏁 Conclusion

The **Supply Chain & Logistics Analytics** project demonstrates an end-to-end Data Science and Business Analytics workflow, starting from raw supply chain data and progressing through data preparation, exploratory analysis, business analysis, visualization, and interactive dashboard development.

The final solution provides a consolidated view of:

- Sales
- Revenue
- Profitability
- Products
- Categories
- Shipping
- Logistics
- Markets
- Regions
- Delivery performance

The interactive Streamlit dashboard allows users to dynamically filter the data, monitor key performance indicators, investigate business performance, explore detailed records, and download filtered datasets.

The project combines **analytical thinking, data visualization, business insights, and practical reporting** to provide a complete supply chain analytics solution suitable for a Data Science and Business Analytics portfolio.

---

## ⭐ If You Find This Project Useful

Feel free to explore the **analysis, interactive dashboard, visualizations, and detailed PDF report** included in this repository.