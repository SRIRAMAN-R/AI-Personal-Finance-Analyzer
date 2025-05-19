import streamlit as st
import os
from dotenv import load_dotenv
import fitz  # PyMuPDF
import google.generativeai as genai
from io import BytesIO
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import markdown
import time

# Load Gemini API Key
load_dotenv()
genai.configure(api_key="AIzaSyCwtxA1Xv4HDeskesFM-fKrYzlskSB5tmw")

# Streamlit Config
st.set_page_config(page_title="💸 UPI Analyzer", layout="wide", page_icon="💰")

# Sidebar
with st.sidebar:
    st.title("🔍 UPI Analyzer")
    st.markdown("""
Welcome to the **AI-Powered UPI Analyzer** 

📄 Upload your **UPI transaction PDF**.

🚀 This app will:
- Extract PDF text 📜
- Analyze with **AI** 🤖
- Summarize your spending 💰
- Give a downloadable financial report 📥

> No manual formatting needed. Just upload and relax.
""")

# Header
st.title("📊 AI Personal Finance Analyzer")

# PDF Text Extractor using PyMuPDF
def read_pdf_text(uploaded_file):
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text() + "\n"
    return text

# Prompt Creator
def generate_prompt(pdf_text):
    return f"""
You are a certified financial analyst.

Below is a user's UPI transaction statement extracted from a PDF:

\"\"\" 
{pdf_text} 
\"\"\" 

Please generate a **professional and user-friendly financial report** that includes the following:

---

### 1. 🧾 Executive Summary
Briefly describe the financial behavior based on the transactions.

### 2. 📅 Monthly Summary
Provide a clean overview:
- **Total Income**
- **Total Expenses**
- **Net Savings**
- **Savings Percentage**

### 3. 📊 Top 3 Spending Categories
List the top 3 categories where the user spends the most (e.g., Food, Shopping, Bills) with approximate amounts.

### 4. 🚨 Unnecessary / Irregular Expenses
Detect and list:
- Any suspicious or unusual spending
- Recurring small amounts that may be impulse buys
- Any inconsistencies in spending patterns

### 5. 💡 Budget Optimization Tips
Simple advice to reduce unnecessary expenses and save more.

### 6. 📈 Savings & Investment Suggestions
Provide beginner-friendly suggestions to build financial security.

### 7. ✅ Final Recommendations
Summarize key takeaways and next steps for the user.

---

Use bullet points, short paragraphs, and clear formatting. Keep it friendly and professional.
"""

# PDF Report Generator
def generate_report(text):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    html = markdown.markdown(text)
    flow = [Paragraph(line, styles["Normal"]) for line in html.split("\n") if line.strip()]
    doc.build(flow)
    buffer.seek(0)
    return buffer.read()

# Main Upload Area
uploaded_file = st.file_uploader("📤 Upload your UPI Transaction PDF", type="pdf")

if uploaded_file:
    with st.spinner("📄 Extracting content from your PDF..."):
        time.sleep(1)  # Just for smooth effect
        raw_text = read_pdf_text(uploaded_file)

    if len(raw_text.strip()) == 0:
        st.error("❌ No text found in the PDF. Please upload a proper UPI statement.")
    else:
        st.success("✅ File uploaded and read successfully!")

        # Ask Gemini AI
        with st.spinner("🤖 Analyzing your UPI data with AI..."):
            prompt = generate_prompt(raw_text)
            model = genai.GenerativeModel("gemini-2.0-flash")
            result = model.generate_content(prompt)
            final_report = result.text
            time.sleep(1)

        # Celebration 🎉
        st.toast("🎉 AI Analysis Complete!", icon="🤖")

        st.markdown("## ✅ Your Personalized Financial Report is Ready")
        st.markdown("Here’s your AI-generated summary of the uploaded UPI statement:")
        st.markdown(final_report)
    
        # PDF Report Download
        pdf_bytes = generate_report(final_report)
        st.download_button("📥 Download Report as PDF", data=pdf_bytes, file_name="upi_financial_report.pdf", mime="application/pdf")
