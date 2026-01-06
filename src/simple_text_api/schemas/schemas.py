from pydantic import BaseModel, Field


class CleanRequest(BaseModel):
    input_string: str = Field(
        description="User string to be cleaned", min_length=1, max_length=1000
    )


class CleanResponse(BaseModel):
    clean_text: str


class AnalyzeResponse(BaseModel):
    words_count: int
    sentence_count: int
    frequent_words: dict[str, int]
    frequent_chars: dict[str, int]
    original_text: str
    clean_text: str
