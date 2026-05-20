"""API interface — FastAPI endpoint for claim analysis."""


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from kaji.flow import KajiFlow

app = FastAPI(title="KajiSF-DJ API")


class AnalysisRequest(BaseModel):
    claim: str
    domain: str = "general"


class AnalysisResponse(BaseModel):
    verdict: str = ""
    confidence: float = 0.0
    report: str = ""


@app.post("/analyse", response_model=AnalysisResponse)
async def analyse(req: AnalysisRequest) -> AnalysisResponse:
    try:
        flow = KajiFlow()
        result = flow.kickoff(inputs={"claim": req.claim, "domain": req.domain})
        report = result.raw if hasattr(result, "raw") else str(result)
        return AnalysisResponse(report=report)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
