from fastapi import FastAPI, Depends
from app.schemas import Telemetry
from app.ai_engine import analyze_ai
from app.rule_engine import evaluate_rules
from app.priority_engine import compute_priority
from app.database import Base, engine, SessionLocal
from app.models import Alert
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware



Base.metadata.create_all(bind=engine)

app = FastAPI(title="AutoSentinel AI")

templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.post("/analyze")
def analyze(data: Telemetry):

    ai_result = analyze_ai(data)
    rule_severity = evaluate_rules(data)

    priority_score = min(1.0, ai_result["fault_probability"] + rule_severity * 0.1)

    if priority_score > 0.75:
        category = "HIGH"
    elif priority_score > 0.4:
        category = "MEDIUM"
    else:
        category = "LOW"

    return {
        "prediction": ai_result["prediction"],
        "fault_probability": ai_result["fault_probability"],
        "priority_score": priority_score,
        "category": category,
        "rule_severity": rule_severity,
        "feature_contributions": ai_result["feature_contributions"]
    }


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

