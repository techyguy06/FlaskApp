# Third party modules
import pytest

# First party modules
from app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_status_code(client):
    rv = client.post("/convert", json={"alpha":["A", "h", "H", "x"]}, content_type='application/json')
    assert rv.status_code == 200, "status code not ok"

def test_empty_convert_input(client):
    rv = client.post("/convert", json={"alpha":[]}, content_type='application/json')
    assert "please provide valid data" not in rv, "empty input test case failed"

def test_positive_convert_case(client):
    rv = client.post("/convert", json={"alpha":["A", "b"]}, content_type='application/json')
    assert rv.json == {"ascii_values": '{"0":650,"1":980}'}, "positive convert case failed"

