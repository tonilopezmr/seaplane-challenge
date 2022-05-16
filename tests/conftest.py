import sys
sys.path.append("..")

import pytest
from app import app as word_ladder_app

@pytest.fixture()
def app():        
    word_ladder_app.config.update({
        "TESTING": True,
    })

    yield word_ladder_app



@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()