import json
import os
import sys

if getattr(sys, 'frozen', False):
      BASE_DIR = os.path.dirname(sys.executable)
else:
      BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CONFIG_FILE = os.path.join(BASE_DIR, "config.json")

def load():
    with open(CONFIG_FILE, "r") as f:
        return json.load(f)
    
def save(data):
        with open(CONFIG_FILE, "w") as f:
            json.dump(data, f, indent=4)

def get(key):
        return load()[key]
    
def set(key, value):
      data = load()
      data[key] = value
      save(data)