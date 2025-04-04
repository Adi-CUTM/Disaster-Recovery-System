from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+mysqlconnector://root:kali@localhost/cyber_defense"

try:
    engine = create_engine(DATABASE_URL)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    print("✅ Database connected successfully!")
except Exception as e:
    print(f"❌ Database connection failed: {e}")
