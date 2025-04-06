import json
import requests

def load_prompt():
    with open("brain_input.txt", "r") as f:
        return f.read()

def save_output(code):
    with open("brain_output.txt", "w") as f:
        f.write(code)

def send_to_llm(prompt):
    # Replace with your local DeepSeek or LM Studio endpoint
    url = "http://localhost:1234/v1/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": prompt,
        "model": "deepseek-coder:6.7b",
        "max_tokens": 1000,
        "stop": None,
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()["choices"][0]["text"]

def evolve():
    prompt = load_prompt()
    result = send_to_llm(prompt)
    save_output(result)
    print("New brain output written to brain_output.txt")

if __name__ == "__main__":
    evolve()

