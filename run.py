"""
Runner for Browser History Manager inside dsa1 folder
Usage: python run.py or python app.py
"""

import os
import sys

# Ensure dsa1 directory is current working directory
current_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(current_dir)
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from app import app

if __name__ == "__main__":
    print("\n" + "=" * 50)
    print("  Browser History Manager — Flask Web Server")
    print("  Open in browser: http://127.0.0.1:5000")
    print("=" * 50 + "\n")
    app.run(debug=True, host="127.0.0.1", port=5000)
