import json
import os

CONFIG_FILE = "config.json"

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