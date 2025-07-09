from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from llama_cpp import Llama

app = FastAPI()

# Mount static files (CSS/JS if needed)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Set up Jinja2 templates
templates = Jinja2Templates(directory="templates")

# Load the model once
llm = Llama(
    model_path="./models/llama-2-7b-chat.Q4_K_M.gguf",
    n_ctx=2048,
    n_threads=8,
    n_gpu_layers=20
)

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.post("/ask")
async def ask(request: Request):
    data = await request.json()
    prompt = data["message"]

    response = llm(prompt=prompt, max_tokens=256)
    return {"response": response["choices"][0]["text"].strip()}
