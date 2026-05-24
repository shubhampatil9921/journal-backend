from sqlalchemy import Column, Integer, String, Float, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base

class ExerciseSession(Base):
    __tablename__ = "exercise_sessions"

    id = Column(Integer, primary_key=True, index=True)
    daily_log_id = Column(Integer, ForeignKey("daily_logs.id"), nullable=False)
    type = Column(String(50), nullable=False)  # cycling, running, walking, other
    distance_km = Column(Float, nullable=True)
    duration_mins = Column(Float, nullable=True)
    active_calories = Column(Float, nullable=True)
    notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    daily_log = relationship("DailyLog", back_populates="sessions")