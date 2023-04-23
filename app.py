from fastapi import FastAPI
import interface as pred
import json

app=FastAPI(
                title="PriceAPI",
                version="1.0",
                contact={
                            "name": "v1c4r10us",
                            "email": "v1c4r10us.29@gmail.com",
                },
                license_info={
                            "name": "Apache 2.0",
                            "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
                }
            )

@app.get('/')
def welcome():
    return {'version': 'v1.0', 'published':'2023', 'contributors': 'Asami Cuéllar & Edgard Huanca', 'github':'https://github.com/v1c4r10us/pf_scrapper', 'documentation':'web-production-7526.up.railway.app/docs'}

@app.get('/get_actual_price')
def get_actual_price():
    return {'Arroz largo': pred.predict_price()}
