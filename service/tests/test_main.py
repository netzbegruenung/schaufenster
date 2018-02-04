import falcon
from falcon import testing
import pytest
from api.main import app

@pytest.fixture
def client():
    return testing.TestClient(app)


def test_get_events_no_ical_url(client):
    """
    No ical URL given  bad request
    """
    response = client.simulate_get('/events/')
    assert response.status == falcon.HTTP_BAD_REQUEST
    # TODO: assertion for response format

def test_get_events(client):
    response = client.simulate_get('/events/', params={
        "ical_url": "http://www.webcal.fi/cal.php?id=75&rid=ics&wrn=0&wp=12&wf=55"
    })
    assert response.status == falcon.HTTP_OK
