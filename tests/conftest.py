import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from simple_text_api.config.conf import DATABASE_TEST_URL

from simple_text_api.db.models import (
    TextAnalysisResult,
)  # noqa

# We need to import this since import = running code, then SQLAlchemy sees the class that inherits from Base and adds info about this table to metadata. Without this import Base would not know whitch table to create
from simple_text_api.db.database import (
    Base,
)  # Important ! We need to use the same BASE as in production database since our db model inherits from it and knows the models


@pytest.fixture
def user_input_clean_text() -> str:
    return "data science data is powerful. machine learing will change the world."


@pytest.fixture
def dirty_user_input() -> str:
    return "  Data,   Science! Is  Powerful?  "


@pytest.fixture
def very_dirty_user_input() -> str:
    return "\n@Data!!!  sciEnce??\t is () powerful [] {}\n"


@pytest.fixture
def dirty_user_input_many_sentences() -> str:
    return "Hello!!!  This is first sentence.\n\nSecond one??  And third: sentence! @Really."


engine_test = create_engine(
    DATABASE_TEST_URL, connect_args={"check_same_thread": False}
)

SessionLocalTest = sessionmaker(autoflush=False, autocommit=False, bind=engine_test)

Base.metadata.create_all(bind=engine_test)


def get_test_db():
    db_test = SessionLocalTest()
    try:
        yield db_test
    finally:
        db_test.close()


# TODO !! 1. take care of conftest beeing importet many times 2. DO not use new database - use tempraty file since tests will populate this db adn can leave some junks 3. create fixture to get_tst_db and do not import to test_api ( thas antypattern) 4. dependency_pvverride hsoub be set in fixture with yeld and to clean up resources ehen finshed or when errror occured 5. Hace fixture on TestClient in fastapi 6. Create a test that will check if data in tetst_table / file are popualted after calling the endpoint
