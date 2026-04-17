from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from backend.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)

    scans = relationship("EcoScan", back_populates="user")
    product_uploads = relationship("ProductUpload", back_populates="user")
    nutrition_scans = relationship("NutritionScan", back_populates="user")
    recyclable_uploads = relationship("RecyclableUpload", back_populates="user")
    chat_interactions = relationship("ChatInteraction", back_populates="user")
    streak = relationship("Streak", back_populates="user", uselist=False)


class EcoScan(Base):
    __tablename__ = "eco_scans"

    id = Column(Integer, primary_key=True)
    item_name = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="scans")


class Streak(Base):
    __tablename__ = "streaks"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    current_streak = Column(Integer, default=0)
    longest_streak = Column(Integer, default=0)
    last_activity_date = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="streak")


class Badge(Base):
    __tablename__ = "badges"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(String)
    days_required = Column(Integer)


class UserBadge(Base):
    __tablename__ = "user_badges"

    id = Column(Integer, primary_key=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    badge_id = Column(Integer, ForeignKey("badges.id"))


class ProductUpload(Base):
    __tablename__ = "product_uploads"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    image_filename = Column(String, nullable=False)
    product_name = Column(String, nullable=False)
    category = Column(String, nullable=True)
    eco_score = Column(Integer, nullable=True)
    eco_metadata = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="product_uploads")


class RecyclableUpload(Base):
    __tablename__ = "recyclable_uploads"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    image_filename = Column(String, nullable=False)
    predicted_label = Column(String, nullable=False)
    is_recyclable = Column(Boolean, default=False, nullable=False)
    points_awarded = Column(Integer, default=0, nullable=False)
    confidence = Column(Float, default=0.0, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="recyclable_uploads")


class ChatInteraction(Base):
    __tablename__ = "chat_interactions"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    mode = Column(String, nullable=False)
    user_message = Column(Text, nullable=False)
    assistant_response = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="chat_interactions")


class NutritionScan(Base):
    __tablename__ = "nutrition_scans"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    barcode = Column(String, nullable=False)
    product_name = Column(String, nullable=False)

    energy_100g = Column(Float, default=0.0, nullable=False)
    sugar_100g = Column(Float, default=0.0, nullable=False)
    fat_100g = Column(Float, default=0.0, nullable=False)
    saturated_fat_100g = Column(Float, default=0.0, nullable=False)
    salt_100g = Column(Float, default=0.0, nullable=False)
    protein_100g = Column(Float, default=0.0, nullable=False)
    fiber_100g = Column(Float, default=0.0, nullable=False)

    nutrition_score = Column(Float, default=0.0, nullable=False)
    health_grade = Column(String, nullable=False)
    scanned_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="nutrition_scans")