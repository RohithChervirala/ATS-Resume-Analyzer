# ATS-Resume-Analyzer
<p align="center">

  <!-- Tech Stack -->
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-UI-red?logo=streamlit" />
  <img src="https://img.shields.io/badge/Groq-Mixtral8x7b-green" />
  <img src="https://img.shields.io/badge/AI-Resume Analyzer-purple?logo=ai" />

  <!-- Status and Popularity -->
  <img src="https://img.shields.io/github/stars/RohithChervirala/ATS-Resume-Analyzer?style=social" />
  <img src="https://img.shields.io/github/last-commit/RohithChervirala/ATS-Resume-Analyzer" />
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" />

  <!-- Contributions -->
  <img src="https://img.shields.io/badge/PRs-Welcome-green?logo=github" />
  <img src="https://img.shields.io/badge/Maintained-Yes-brightgreen" />

</p>

This project is a Streamlit-based ATS Resume Analyzer that evaluates resumes and compares them with a given job description using free LLMs (Groq Mixtral-8x7B/Gemini alternative). It highlights missing skills, generates ATS score, keyword match, optimization suggestions, and provides a complete structured analysis  improve resume selection chances.

# 🧠 ATS Resume Analyzer | AI-Powered Resume Evaluation

This is an AI-powered **ATS Resume Analyzer** that compares resumes with job descriptions and gives ATS score, skill gap analysis, missing keywords, and professional improvement suggestions.

Built using **Streamlit + Groq Mixtral-8x7B (Free LLM)** — No paid API required!

---

## 🚀 Features

| Feature | Description |
|--------|-------------|
| 📄 Upload PDF Resume | Extracts text using PyPDF2 |
| 📝 Add Job Description | Model compares resume vs JD |
| 🏆 ATS Score | Gives selection probability 0–100 |
| 🔍 Skill Match | Shows matched & missing skills |
|🔑 Keywords Extraction| Helps improve resume ranking |
|⚡ Free LLM Support | Uses Groq API Mixtral-8x7B |
|🛠 Clean UI | Built with Streamlit |

---

## 🛠 Tech Stack

| Component | Used |
|----------|-------|
| Backend / AI | Groq Mixtral-8x7B |
| UI | Streamlit |
| Text Extraction | PyPDF2 |
| Environment | .env |

---

## 📥 Installation Steps

```bash
git clone https://github.com/your-username/ATS-Resume-Analyzer.git
cd ATS-Resume-Analyzer

pip install -r requirements.txt
