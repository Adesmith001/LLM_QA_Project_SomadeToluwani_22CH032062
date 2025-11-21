# LLM Question-and-Answering System

**Author:** Somade Toluwani  
**Matric Number:** 22CH032062  
**Course:** CSC415 - Natural Language Processing  

## Project Overview

This project implements a Question-and-Answering system using Groq's LLM API (Llama 3.3 70B model). It includes both a CLI application and a modern web-based GUI with a clean, chat-style interface.

## Features

✅ **CLI Application** (`LLM_QA_CLI.py`)
- Interactive command-line interface
- Natural language question preprocessing (lowercasing, tokenization, punctuation removal)
- Real-time LLM query and response display

✅ **Web GUI** (`app.py` + `templates/index.html`)
- Modern chat-style interface
- Real-time question processing visualization
- Collapsible preprocessing details (tokens, processed text)
- Smooth animations and responsive design
- Built with Flask framework

✅ **LLM Integration**
- Uses Groq API with Llama 3.3 70B Versatile model
- Free tier available (no credit card required)
- Fast response times and high-quality answers

## Project Structure

```
LLM_QA_Project_Somade_22CH032062/
├── LLM_QA_CLI.py                    # CLI application
├── app.py                            # Flask web application
├── requirements.txt                  # Python dependencies
├── vercel.json                       # Vercel deployment config
├── LLM_QA_hosted_webGUI_link.txt    # Deployment URLs
├── .env.example                      # Environment variable template
├── .gitignore                        # Git ignore rules
├── README.md                         # This file
├── static/
│   └── style.css                     # Web GUI styling
└── templates/
    └── index.html                    # Web GUI HTML template
```

## Setup Instructions

### 1. Get Groq API Key (Free)

1. Visit [https://console.groq.com/](https://console.groq.com/)
2. Sign up for a free account
3. Navigate to API Keys section
4. Create a new API key and copy it

### 2. Local Setup

```powershell
# Clone or navigate to the project directory
cd "c:\Users\USER\Documents\Covenant Univerisity\400 lvl\Alpha Semester\CSC415\22CH032062_SOMADE_TOLUWANI_NLP"

# Create virtual environment
python -m venv venv

# Activate virtual environment
.\venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt

# Create .env file
Copy-Item .env.example .env

# Edit .env and add your Gemini API key
notepad .env
```

Add your API key to `.env`:
```
GROQ_API_KEY=your_actual_groq_api_key_here
```

### 3. Run CLI Application

```powershell
python LLM_QA_CLI.py
```

### 4. Run Web Application Locally

```powershell
python app.py
```

Then open your browser and visit: `http://localhost:5000`

## Deployment to Vercel

### Prerequisites
- GitHub account
- Vercel account (free tier available)

### Steps

1. **Push to GitHub**
   ```powershell
   git init
   git add .
   git commit -m "Initial commit: LLM Q&A System"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
   git push -u origin main
   ```

2. **Deploy to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Sign in with GitHub
   - Click "New Project"
   - Import your repository
   - Configure environment variable:
     - Key: `GROQ_API_KEY`
     - Value: Your Groq API key
   - Click "Deploy"

3. **Update submission file**
   - Edit `LLM_QA_hosted_webGUI_link.txt`
   - Add your Vercel deployment URL
   - Add your GitHub repository URL

## Technologies Used

- **Backend:** Flask (Python web framework)
- **Frontend:** HTML, CSS, JavaScript
- **LLM API:** Groq (Llama 3.3 70B Versatile)
- **Deployment:** Vercel
- **NLP Processing:** Custom preprocessing (tokenization, lowercasing)

## API Features

### Preprocessing Steps
1. **Lowercasing:** Convert all text to lowercase
2. **Tokenization:** Split text into individual words
3. **Punctuation Removal:** Remove punctuation (except question marks for context)
4. **Whitespace Normalization:** Remove extra spaces

### LLM Configuration
- **Model:** llama-3.3-70b-versatile
- **API:** Groq
- **Free tier:** Available (no credit card required)

## Usage Examples

### CLI
```
Enter your question: What is the capital of France?

[Original Question]: What is the capital of France?
[Processed Question]: what is the capital of france?
[Tokens]: ['what', 'is', 'the', 'capital', 'of', 'france?']

[Querying LLM API...]

============================================================
ANSWER:
============================================================
The capital of France is Paris.
============================================================
```

### Web GUI
1. Open the web application
2. See the welcome message with chat interface
3. Type your question in the chat input
4. Press Enter or click the send button
5. View the AI-generated answer
6. Click "View preprocessing details" to see tokens and processed text

## Troubleshooting

### API Key Issues
- Ensure `.env` file exists in project root
- Verify API key is correct (no extra spaces)
- Check Groq console for API key status and quota

### Deployment Issues
- Verify `GROQ_API_KEY` is set in Vercel environment variables
- Check Vercel deployment logs for errors
- Ensure `vercel.json` configuration is correct

### Local Testing
```powershell
# Test if Flask is installed
python -c "import flask; print(flask.__version__)"

# Test if Groq is installed
python -c "import groq; print('Groq installed')"

# Test if environment variables load
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print('API Key loaded:', bool(os.getenv('GROQ_API_KEY')))"
```

## Why Groq API?

✅ **Free tier** - No credit card required  
✅ **Fast** - Extremely fast inference speeds  
✅ **Reliable** - High uptime and availability  
✅ **Powerful** - Llama 3.3 70B model with excellent performance  
✅ **Easy to use** - Simple API interface  
✅ **Vercel compatible** - Works seamlessly with serverless deployment  
✅ **Python 3.8+ support** - Compatible with older Python versions  

## License

This project is for educational purposes as part of CSC415 coursework.

## Contact

**Student:** Somade Toluwani  
**Matric Number:** 22CH032062  
**Institution:** Covenant University  

---

**Note:** Remember to never commit your `.env` file or expose your API keys publicly!
