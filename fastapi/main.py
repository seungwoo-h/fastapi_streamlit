import json
import pandas as pd
from io import BytesIO
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import FastAPI, File
from pydantic import BaseModel

app = FastAPI(
    title='test',
    description='This is a demo connecting streamlit with fastapi',
)

def convert_to_dataframe(data):
    return pd.read_csv(data)

def process(data):
    data['new_column'] = 0 
    return data

@app.post("/csv")
def process_csv(file: bytes = File(...)):
    df = convert_to_dataframe(BytesIO(file))
    df = process(df) # 데이터 처리
    # Reponse 보내기 위해 Json으로 변환
    json_data = df.to_json(orient='records')
    response =  JSONResponse(json.loads(json_data))
    return response

class MerchName(BaseModel):
    merch_name: str
    
def get_prediction(text):
    return "음식점"

@app.post("/inference")
def inference_single(inp: MerchName):
    pred = get_prediction(inp.merch_name)
    return pred