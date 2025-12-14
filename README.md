# NIRT Bhopal - AI Admission Assistant

A branded AI-powered response bot for **NRI Institute of Research and Technology, Bhopal**, designed to answer student queries about courses, fees, and admissions.

## 🎓 College Details
- **Institute**: NRI Institute of Research and Technology (NIRT).
- **Location**: Raisen Road, Bhopal.
- **AI Model**: Google Gemini 2.0 (Python).

## 🚀 Features
- **Smart Chatbot**: Responds to branding-specific queries (Fees, Eligibility).
- **Dedicated Fees Page**: Tabular view of Tuition, Exam, and Hostel fees.
- **Course Catalog**: Detailed list of B.Tech, M.Tech, and MBA programs.
- **Modern UI**: Dark/Light mode, responsive, professional layout.

## 🛠️ Setup Instructions

### 1. Install Dependencies
```bash
cd PS32_Response_Bot
pip install -r requirements.txt
```

### 2. Configure API Key
Add your key to `.env` or run:
[PowerShell]
```powershell
$env:GEMINI_API_KEY="your_actual_api_key"
```

### 3. Initialize Data
This populates the database with NIRT specific course and fee structure.
```bash
python seed.py
```

### 4. Run Application
```bash
python run.py
```
Visit **http://127.0.0.1:5000**

## 💰 Fees Structure (Quick View)
| Course | Fee (Per Year) |
|--------|---------------|
| B.Tech (CSE) | ₹70,000 |
| B.Tech (AI) | ₹75,000 |
| MBA | ₹65,000 |
| **Hostel** | ~₹60,000 |
| **Admission** | ~₹5,000 |

## 🤖 AI Prompt
The AI is strictly instructed to act as an assistant for NIRT Bhopal and uses the local database for factual consistency.
