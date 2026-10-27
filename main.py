from fastapi import FastAPI ,Depends,HTTPException
from sqlalchemy.orm import Session
from database import get_db,enigne,Base
from models import Farm,Crop
import schemas as s
Base.metadata.create_all(bind=enigne)
app=FastAPI()
@app.post("/farms",response_model=s.ParentOut,status_code=201)
def create_farm(farm:s.ParentCreate,db:Session=Depends(get_db)):
    item=Farm(**farm.model_dump())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
@app.post("/farms/{parent_id}/crop_batches",response_model=s.ChildCreate,status_code=201)
def createcrop(parent_id:int,crops:s.ChildCreate,db:Session=Depends(get_db)):
    parent=db.get(Farm,parent_id)
    if parent is None:
        raise HTTPException(status_code=404,detail="parent not found")
    item=Crop(**crops.model_dump(),farm_id=parent_id)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item
@app.get("/farms/{parent_id}",response_model=s.ParentWithChildren,status_code=200)
def getcrop(parent_id:int,
            crop_type:str|None=None,
            sort:str|None=None,db:Session=Depends(get_db)):
    parent=db.get(Farm,parent_id)
    if parent is None:
        raise HTTPException(status_code=404,detail="parent not found")
    crops=list(parent.crop)
    if crop_type is not None and crop_type.strip():
      crops=  [c for c in crops if  c.crop_type==crop_type]
    if sort is not None:
        if sort not in {"batch_name","expected_yield_kg"}:
            raise HTTPException(status_code=404,detail="parent not found")
    if sort =="batch_name":
        crops.sorted(crops,key=lambda c:c.batch_name)
    if sort =="expected_yield_kg":
        crops.sortred(crops,key=lambda c:c.expected_yield_kg)
    return {
        "id": parent.id,
        "name": parent.name,
        "region": parent.region,
        "crop": crops
    }
@app.put("/farms/{parent_id}/crop_batches/{child_id}",response_model=s.ChildOut)
def updatecrop(parent_id:int,child_id:int,data:s.ChildCreate,db:Session=Depends(get_db)):
    parent=db.get(Farm,parent_id)
    if parent is None:
        raise HTTPException(status_code=404)
    child=db.get(Crop,child_id)
    if child is None or child.farm_id!=parent_id:
        raise HTTPException(status_code=404)
    child.batch_name=data.batch_name
    child.crop_type=data.crop_type
    child.area_hectares=data.area_hectares
    child.expected_yield_kg=data.expected_yield_kg
    db.commit()
    db.refresh(child)
    return child
    
    
    



