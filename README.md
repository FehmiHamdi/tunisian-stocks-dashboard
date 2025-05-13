# 📈 Tunisian Stock Market Dashboard

A **Streamlit-powered web app** that visualizes historical stock data from the Tunisian market. This project was built to explore and present financial data interactively using Python, pandas, and Plotly.

## 🚀 Features

- 📊 Visualize **closing prices** over time for Tunisian companies  (2010 --> 2022)
- 📉 View **daily trading volume** with optional bar charts  
- 🔎 **Interactive sidebar** to select companies by name  
- 📅 Clean and simple interface using Streamlit  
- ✅ Filterable data and visual exploration  

## 📂 Project Structure

```
tunisian-stock-dashboard/
├── app/
│   └── dashboard.py           # Streamlit dashboard app
├── data/
│   ├── ALL_DATA_cleaned.csv   # Historical stock data
│   └── stock_list.csv         # Company names and tickers
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .gitignore                 # Ignored files
```

## 🛠️ Technologies Used

- **Python** 🐍  
- **Streamlit** – frontend web UI  
- **Pandas** – data manipulation  
- **Plotly** – interactive charts  

## ▶️ Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/tunisian-stock-dashboard.git
cd tunisian-stock-dashboard
```

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
streamlit run app/dashboard.py
```

## 📸 Screenshot

![Preview of the dashboard](preview.png)

## 📌 Notes

- Make sure the `data/` folder contains the CSV files:  
  - `ALL_DATA_cleaned.csv` (historical stock prices)  
  - `stock_list.csv` (tickers and company names)  
- The dashboard is intended for educational and demonstration purposes.

## 📬 Contact

Feel free to reach out via GitHub if you have any suggestions or feedback.

---

**Made with ❤️ by a Software Development Student passionate about Data Science and AI**
