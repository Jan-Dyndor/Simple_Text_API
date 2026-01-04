from fastapi import FastAPI
from simple_text_api.services.clean_text import clean_input
from simple_text_api.services.text_analysis import (
    count_sentences,
    count_words,
    most_frequent_char,
    most_frequent_words,
)
from simple_text_api.schemas.schemas import CleanRequest, CleanResponse, AnalyzeResponse

app = FastAPI()


@app.get("/health")
def health_check() -> dict:
    return {"Status": "OK"}


@app.post("/clean_text", response_model=CleanResponse)
def clean_text(text: CleanRequest) -> CleanResponse:
    clean = clean_input(text.input_string)
    return CleanResponse(clean_text=clean)


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_text(text: CleanRequest) -> AnalyzeResponse:
    clean_str = clean_input(text.input_string)
    words_count = count_words(clean_str)
    sentence_count = count_sentences(clean_str)
    frequent_words = most_frequent_words(clean_str)
    frequent_chars = most_frequent_char(clean_str)
    return AnalyzeResponse(
        words_count=words_count,
        sentence_count=sentence_count,
        frequent_words=frequent_words,
        frequent_chars=frequent_chars,
        orginal_text=text.input_string,
        clean_text=clean_str,
    )
