from datetime import datetime, timezone

from sqlalchemy import TEXT, Column, DateTime, Integer

from simple_text_api.db.database import Base


class TextAnalysisResult(Base):
    __tablename__ = "text_analysis_results"
    id = Column(Integer, primary_key=True, index=True)
    original_text = Column(TEXT)
    clean_text = Column(TEXT)
    words_count = Column(Integer)
    sentence_count = Column(Integer)
    frequent_words_json = Column(TEXT)
    frequent_chars_json = Column(TEXT)
    created_at = Column(
        DateTime(timezone=True), default=lambda: datetime.now(timezone.utc)
    )
