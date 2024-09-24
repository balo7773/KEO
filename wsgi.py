#!/usr/bin/python3
import os
import sys

project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_dir)

from KEO.main import app

if __name__ == '__main__':
    app.run(debug=True)