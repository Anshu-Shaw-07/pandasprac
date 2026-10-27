from pydantic import BaseModel,Field,ConfigDict,StrictInt
class ParentCreate(BaseModel):
    name:str=Field(min_length=1)
    region:str=Field(min_length=1)
class ChildCreate(BaseModel):
    batch_name:str=Field(min_length=1)
    crop_type:str=Field(min_length=1)
    expected_yield_kg:StrictInt=Field(ge=0)
    area_hectares:StrictInt=Field(ge=1)
class ParentOut(BaseModel):
    id:StrictInt
    name:str=Field(min_length=1)
    region:str=Field(min_length=1)
    model_config=ConfigDict(from_attributes=True)
class ChildOut(BaseModel):
    id:StrictInt
    batch_name:str=Field(min_length=1)
    crop_type:str=Field(min_length=1)
    expected_yield_kg:StrictInt=Field(ge=0)
    area_hectares:StrictInt=Field(ge=1)
    model_config=ConfigDict(from_attributes=True)
class ParentWithChildren(ParentOut):
    crop:list[ChildOut]










