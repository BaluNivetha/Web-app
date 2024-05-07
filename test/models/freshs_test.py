from datetime import datetime
from app.models.fresh import Fresh
from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID
def test_freshs(model_context):
    # model context ensures tests are using data from the test document:
    assert Fresh.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
    # DESTROY ALL:
    Fresh.destroy_all()
    # SEED RECORDS:
    Fresh.seed()
    # FIND ALL:
    freshs = Fresh.all()
    assert len(freshs) == 3
    # CREATE
    fresh = Fresh.find(1)
    assert fresh.id == 1
    assert fresh.name == "Strawberries"
    assert fresh.price == 4.99
    assert isinstance(fresh.created_at, datetime)