#!/usr/bin/python3
import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from KEO.main import app

if __name__ == "__main__":
    app.run()