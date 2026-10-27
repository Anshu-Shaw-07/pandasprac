from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,declarative_base
url="sqlite:///./farm_batches.db"
enigne=create_engine(url,connect_args={"check_same_thread":False})
SessionLocal=sessionmaker(autocommit=False,autoflush=False,bind=enigne)
Base=declarative_base()
def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()
        

   
 


