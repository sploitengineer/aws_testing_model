import requests
import json

url = "http://<your-ec2-public-ip>:11434/api/generate"  # EC2 public IP

payload = {
    "model": "gemma:2b", 
    "prompt": """PROMPT"""
}

resp = requests.post(url, json=payload, stream=True)

for line in resp.iter_lines():
    if line:
        data = json.loads(line.decode("utf-8"))
        if "response" in data:
            print(data["response"], end="")
