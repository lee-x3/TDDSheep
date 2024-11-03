from urllib import response
from fastapi import FastAPI, HTTPException, status
from models.db import db
from models.models import Sheep

app = FastAPI()

@app.get("/sheep/{id}", response_model=Sheep)
def read_sheep(id: int):
    return db.get_sheep(id)

def test_add_sheet():
    #TODO: Prepare the new sheep data in a dictionary format
    new_sheep_data = {
        "id": 7,
        "name": "Cookie",
        "breed": "Suffolk",
        "sex": "ram",
    }

    #TODO: Send a POST request to the endpoint "/sheep" with the new sheep data
    # Arguments should be your endpoint and new sheep data
@app.post("/sheep", response_model=Sheep)
def add_sheep(sheep: Sheep):
    if sheep.id in db.data:
        raise HTTPException(status_code=400, detail="Sheep with this ID already exists")

    #Add the new sheep to the database
    db.data[sheep.id] = sheep
    return sheep

    #TODO: Assert that the response status code is 201(Created)
    assert response.status_code == 201

    #TODO: Assert that the response JSON matches the new sheep data
    assert response.json() == new_sheep_data


    #TODO: Verify that the sheep was actually added to the database by retrieving the new sheep by ID
    # include an assert statement to see if the new sheep data can be retrieved
    verify_response = client.get(f"/sheep/{new_sheep_data['id']}")
    assert verify_response.status_code == 200
    assert verify_response.json() == new_sheep_data
