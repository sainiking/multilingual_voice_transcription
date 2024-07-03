from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

Base = declarative_base()

class Transcription(Base):
    __tablename__ = 'transcriptions'
    id = Column(Integer, primary_key=True)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime)

# Setup SQLite database
engine = create_engine('sqlite:///transcriptions.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

def save_transcription(text):
    """Save a new transcription to the database."""
    session = Session()
    new_transcription = Transcription(text=text, created_at=datetime.datetime.utcnow())  # Use utcnow() for current time
    session.add(new_transcription)
    session.commit()
    session.close()

def get_transcription_history():
    """Retrieve transcription history from the database."""
    session = Session()
    transcriptions = session.query(Transcription).order_by(Transcription.created_at.desc()).all()
    session.close()
    return transcriptions