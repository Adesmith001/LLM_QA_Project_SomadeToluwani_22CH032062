"""
Vercel-optimized version of the Flask app
"""
from app import app

# Vercel requires the app to be named 'app' or exported
application = app

if __name__ == '__main__':
    app.run()