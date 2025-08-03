# 📈 ML-Enhanced Portfolio Construction Tool

This interactive dashboard helps investors build optimized portfolios using Machine Learning and Modern Portfolio Theory (MPT). Built with Python, Scikit-learn, and Streamlit.

---

## 🚀 Features

- ✅ Asset selection using Yahoo Finance (`yfinance`)
- ✅ Technical feature engineering (volatility, momentum, moving averages)
- ✅ Return prediction using Random Forest Regressor
- ✅ Sharpe-ratio based portfolio optimization
- ✅ Interactive visualizations via Streamlit

---

## 🛠 Setup Instructions

```bash
git clone https://github.com/YOUR_USERNAME/ml-portfolio-tool.git
cd ml-portfolio-tool
pip install -r requirements.txt
streamlit run src/app.py
```

---

## 🌐 Streamlit Cloud Deployment

To deploy this on [Streamlit Cloud](https://streamlit.io/cloud):

1. Push this repo to GitHub.
2. Sign into Streamlit Cloud and create a new app.
3. Choose `src/app.py` as the entry point.
4. (Optional) Add API keys to `.streamlit/secrets.toml`.

```toml
[api]
# Example:
# alpha_vantage_key = "your_secret_key_here"
```

---

## 📄 Project Structure

```
ml_portfolio_tool/
├── data/
├── notebooks/
├── src/
│   ├── data_pipeline.py
│   ├── feature_engineering.py
│   ├── model.py
│   ├── optimizer.py
│   └── app.py
├── .streamlit/
│   ├── secrets.toml
│   └── config.toml
├── requirements.txt
└── README.md
```

---

## 📬 Questions?

Feel free to submit issues or feature suggestions!

Made with ❤️ using Python, Scikit-learn, and Streamlit.
