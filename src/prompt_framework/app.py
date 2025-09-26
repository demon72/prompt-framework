from fastapi import FastAPI
import yaml
from pathlib import Path

app = FastAPI(title="Prompt Framework v0.0.1")

PROMPT_FILE = Path("data/prompts.yaml")

def load_prompts():
    if PROMPT_FILE.exists():
        return yaml.safe_load(PROMPT_FILE.read_text(encoding="utf-8"))
    return []

@app.get("/")
def root():
    return {"status": "ok", "framework": "v0.0.1"}

@app.get("/prompts")
def get_prompts():
    return load_prompts()

@app.get("/prompt/{prompt_id}")
def get_prompt(prompt_id: str):
    prompts = load_prompts()
    for p in prompts:
        if p.get("id") == prompt_id:
            return p
    return {"error": f"Prompt {prompt_id} not found"}
