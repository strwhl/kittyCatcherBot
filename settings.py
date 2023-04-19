import os

with open('.env', 'r') as file:
    line = file.readline()
    try:
        os.environ[line[:line.find("=")]] = line[line.find("=") + 1:]
    except ValueError:
        pass

OPENAI_API_KEY = os.environ['OPENAI_API_KEY']