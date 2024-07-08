from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64
from typing import List, Optional

app = FastAPI()

data = pd.read_csv("mushroom_cleaned.csv")

class StatTestRequest(BaseModel):
    test_type: str
    variables: List[str]

def preprocess_data(df):
    return df

def get_statistical_summary(df):
    summary = {
        "mean": df.mean().to_dict(),
        "median": df.median().to_dict(),
        "mode": df.mode().iloc[0].to_dict(),
        "variance": df.var().to_dict(),
        "std_dev": df.std().to_dict(),
        "range": {col: df[col].max() - df[col].min() for col in df.columns},
        "quartiles": {
            col: df[col].quantile([0.25, 0.5, 0.75]).to_dict() for col in df.columns
        },
    }
    return summary

def create_visualization(df, vis_type, variables):
    plt.figure()
    if vis_type == "histogram":
        df[variables[0]].hist()
    elif vis_type == "bar":
        df[variables[0]].value_counts().plot(kind="bar")
    elif vis_type == "scatter" and len(variables) == 2:
        df.plot.scatter(x=variables[0], y=variables[1])
    elif vis_type == "heatmap":
        sns.heatmap(df.corr(), annot=True)
    else:
        raise HTTPException(
            status_code=400, detail="Invalid visualization type or variables"
        )

    buf = BytesIO()
    plt.savefig(buf, format="png")
    plt.close()
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")

@app.get("/api/data")
def get_data():
    return data.to_dict(orient="records")

@app.get("/api/summary")
def get_summary():
    summary = get_statistical_summary(data)
    return summary

@app.get("/api/visualization")
def get_visualization(type: str, variables: List[str]):
    img_str = create_visualization(data, type, variables)
    return {"image": img_str}

@app.get("/api/correlation")
def get_correlation():
    corr_matrix = data.corr().to_dict()
    return {"correlation_matrix": corr_matrix}

@app.post("/api/stat_tests")
def perform_stat_tests(request: StatTestRequest):
    if request.test_type == "t_test" and len(request.variables) == 2:
        pass
    elif request.test_type == "chi_square" and len(request.variables) == 2:
        pass
    elif request.test_type == "anova" and len(request.variables) > 2:
        pass
    else:
        raise HTTPException(
            status_code=400, detail="Invalid test type or number of variables"
        )
    return {"results": "test results"}

@app.post("/api/preprocess")
def preprocess():
    preprocessed_data = preprocess_data(data)
    return {"status": "Preprocessing complete"}

@app.get("/api/patterns")
def detect_patterns():
    return {"patterns": "detected patterns"}

@app.get("/api/insights")
def get_insights():
    return {"insights": "key findings and recommendations"}

@app.get("/api/limitations")
def get_limitations():
    return {"limitations": "data limitations"}

@app.get("/api/future_research")
def future_research():
    return {"future_research": "suggested areas for further investigation"}
