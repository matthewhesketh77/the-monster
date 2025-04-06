import json
import requests
import os

# === CONFIG ===
LLM_ENDPOINT = "http://localhost:1234/v1/completions"
MODEL_NAME = "deepseek-coder:6.7b"
MAX_TOKENS = 1000
TEMPERATURE = 0.7

# === Read user prompt ===
user_input = input("\n💬 What would you like The Monster to do?\n> ")

# === Format prompt for LM Studio ===
prompt = f"""
You are The Monster AI.
You live on the local machine.
Your job is to complete real tasks, such as reading and writing files, running Python plugins, improving your own code, or performing maintenance.

Your tools include:
- Reflections and memory files
- Plugin system in the /plugins folder
- Self-evolving code loop

Respond ONLY with valid executable Python code.
Do NOT include:
- Task descriptions
- Markdown formatting
- Explanations or comments
Start immediately with valid Python (e.g., import statements or def ...).

User: {user_input}
"""

# === Send prompt to local LLM ===
response = requests.post(LLM_ENDPOINT, json={
    "model": MODEL_NAME,
    "prompt": prompt,
    "max_tokens": MAX_TOKENS,
    "temperature": TEMPERATURE
})

# === Extract raw code from response ===
try:
    code = response.json()["choices"][0]["text"].strip()
except Exception as e:
    print("❌ Failed to parse LLM response:", e)
    exit()

# === Clean: remove non-code lines ===
clean_lines = []
skip = False
for line in code.splitlines():
    stripped = line.strip()
    if stripped.lower().startswith("answer:"):
        continue
    if stripped.startswith("```"):
        skip = not skip
        continue
    if not skip and stripped:
        clean_lines.append(line)

clean_code = "\n".join(clean_lines)

# === Save cleaned code to file ===
with open("brain_chat_output.py", "w") as f:
    f.write(clean_code)

print("\n✅ Code generated and saved to brain_chat_output.py")

# === Ask to run ===
run = input("\n▶️ Do you want to run this code now? (y/n): ").strip().lower()
if run == "y":
    print("\n🚀 Executing brain_chat_output.py...\n")
    os.system("python3 brain_chat_output.py")
else:
    print("👀 You can review or edit brain_chat_output.py manually.")

