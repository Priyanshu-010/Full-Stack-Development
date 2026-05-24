from fastapi import FastAPI
from typing import List, Any

app = FastAPI(root_path="/api/v1")

data: Any = [
  {"id": 1, "name": "Campaign 1"},
  {"id": 2, "name": "Campaign 2"}
]

@app.get("/")
async def root():
  return {"message": "Hello World"}

# Get all campaigns

@app.get("/campaigns")
async def get_campaigns():
  return {"campaigns": data}

# Get campaign by id

@app.get("/campaigns/{id}")
async def get_by_id(id: int):
  for campaign in data:
    if campaign["id"] == id:
      return {"campaign": campaign}
  return {"message": "Campaign not found"}

# Create a campaign

# Simple Way of creating a campaign

# @app.post("/campaigns")
# async def create_campaign(campaign: dict):
#   data.append(campaign)
#   return {"message": "Campaign created"}

# Other way of creating a campaign using request body as dict and assigning an id to it

@app.post("/campaigns")
async def create_campaign(body: dict[str, Any]):
  new_campaign = {
    "id": len(data) + 1,
    "name": body.get("name", "Unnamed Campaign")
  }
  data.append(new_campaign)
  return {"message": "Campaign created"}

# Update a campaign

@app.put("/campaigns/{id}")
async def update_campaign(id: int, body: dict[str, Any]):
  for index, campaign in enumerate(data):
    if campaign["id"] == id:
      updated_campaign: dict[str, Any] = {
        "id": id,
        "name": body.get("name", campaign.get("name", "Unnamed Campaign"))
      }
      data[index] = updated_campaign
      return {"message": data[index]}
  return {"message": "Campaign not found"}

# Delete a campaign

@app.delete("/campaigns/{id}")
async def delete_campaign(id: int):
  for index, campaign in enumerate(data):
    if campaign["id"] == id:
      deleted_campaign = data.pop(index)
      return {"message": f"Campaign with id {id} deleted", "campaign": deleted_campaign}
  return {"message": "Campaign not found"}
