from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
from database import Base
class PracticeArea(Base):
    __tablename__="practice_areas"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False)
    floor_number =Column(Integer,nullable=False)
    consultants= relationship("Consultant",back_populates="practice_areas")
class Consultant(Base):
    __tablename__="consultants"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    designation=Column(String,nullable=False)
    consultation_fee = Column(Integer, nullable=False)
    experience_years = Column(Integer, nullable=False)
    practice_area_id = Column(
            Integer,
            ForeignKey("practice_areas.id"),
            nullable=False
        )
    practice_areas=relationship("PracticeArea",back_populates="consultants")
    