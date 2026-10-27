from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class Farm(Base):
    __tablename__="farm"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    region=Column(String,nullable=False)
    crop=relationship("Crop",back_populates="farm")
class Crop(Base):
    __tablename__="crop"
    id=Column(Integer,primary_key=True,index=True)
    batch_name=Column(String,nullable=False)
    crop_type=Column(String,nullable=False)
    expected_yield_kg =Column(Integer,nullable=False)
    area_hectares =Column(Integer,nullable=False)
    farm_id=Column(Integer,ForeignKey("farm.id"))
    farm=relationship("Farm",back_populates="crop")




