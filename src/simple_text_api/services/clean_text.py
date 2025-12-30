import re
import sys
from simple_text_api.config.conf import CHARS_TO_DEL


def clean_input(
    input: str,
) -> str:  # TODO I can assume string want be null - later in pydantic models
    input = input.strip()
    # input = re.sub(CHARS_TO_DEL, " ")
    print(input)
    return input


s = "Hello! World@"

z = clean_input(s)
