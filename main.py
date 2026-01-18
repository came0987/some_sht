from fastapi import FastAPI, HTTPException
from engine import run_pipeline
from schema import Pipeline
from pydantic import ValidationError

app = FastAPI(title="ML Pipeline Engine")

@app.post("/run")
def run_pipeline_endpoint(pipeline: Pipeline):
    try:
        results = run_pipeline(pipeline.dict())
        return {
            "status": "ok",
            "results": serialize_results(results)
        }

    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
