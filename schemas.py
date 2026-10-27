from pydantic import BaseModel, ConfigDict, Field
class PracticeAreaCreate(BaseModel):
    name:str =Field(min_length=1)
    floor_number:int=Field(gt=1)

class ConsultantCreate(BaseModel): 
    name:str=Field(min_length=1)
    designation:str=Field(min_length=1)
    consultation_fee:int=Field(gt= 300)
    experience_years:int=Field(gt= 0)
class ConsultantUpdate(BaseModel): 
    name:str | None =Field(default=None,min_length=1)
    designation:str | None=Field(default=None,min_length=1)
    consultation_fee:int | None=Field(default=None,gt= 300)
    experience_years :int| None=Field(default=None,gt= 0)


    
class PracticeAreaOut(BaseModel):
    id:int
    name:str
    floor_number:int
    model_config = ConfigDict(from_attributes=True)

class ConsultantOut(BaseModel): 
    name:str
    designation:str
    consultation_fee:int
    experience_years:int
    model_config=ConfigDict(from_attributes=True)
class PracticeAreaWithConsultants(PracticeAreaOut):
    consultants: list[ConsultantOut]