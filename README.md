# 💰 AI-Powered UPI Financial Analyzer

**An AI-powered Streamlit web app to analyze UPI transaction PDFs (PhonePe, Paytm) and provide personalized financial advice using Google Gemini LLM.**

---

## 🧾 Problem Statement

Develop an AI-powered application that processes UPI transaction statements from multiple apps (Paytm, GPay, PhonePe, etc.) and generates actionable insights and personalized financial advice using LLMs.

The system must:
- Extract transaction details from varied PDF formats
- Structure the data into a consistent format
- Analyze spending behavior
- Deliver tailored recommendations via an interactive dashboard or downloadable report

---

## 📌 Project Description

This project allows users to:
- Upload UPI transaction statements (PDFs) from **PhonePe** or **Paytm**
- Automatically **extract** and **analyze** transaction data
- Generate a **detailed financial report** using **Google Gemini LLM**
- Download the insights as a **PDF report**
- Works entirely on the browser using **Streamlit**

---

## 🚀 Project Flow

1. **PDF Upload**
   - Users upload UPI transaction PDFs via the Streamlit interface.

2. **Text Extraction**
   - Uses **PyMuPDF (fitz)** to extract all text content from the PDF.

3. **AI Report Generation**
   - Sends the extracted text to **Google Gemini** using a structured financial prompt.
   - Gemini generates a multi-section report: summary, insights, spending tips, and investment suggestions.

4. **PDF Report Download**
   - The LLM report is converted into a downloadable PDF using ReportLab.

---

## 🌐 Live Demo

✅ Try it live on **Hugging Face Spaces**:  
🔗 [https://huggingface.co/spaces/sriramanr/AI_Personal_Finance_Analyzer](https://huggingface.co/spaces/sriramanr/AI_Personal_Finance_Analyzer)

---

## 🧪 Tech Stack

- Python
- Streamlit
- Google Gemini API (`google.generativeai`)
- PyMuPDF (`fitz`)
- ReportLab (PDF generation)
- Markdown

---

## 📦 Installation

Before running the project, install the required packages using `pip`:

```bash
pip install -r requirements.txt
```
## 🌐 How to Host on Streamlit Cloud

1. **Prepare the repo**
   - Add the following files:
     - `app.py`
     - `requirements.txt`

2. **requirements.txt**
   ```txt
    streamlit
    pandas
    matplotlib
    seaborn
    google-generativeai
    reportlab
    markdown
    python-dotenv
    pymupdf
   ```

3. **Push to GitHub**

4. **Visit: [https://share.streamlit.io](https://share.streamlit.io)**
   - Connect your GitHub repo
   - Set main file as `app.py`

---
