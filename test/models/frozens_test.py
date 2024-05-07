from datetime import datetime
from app.models.frozen import Frozen
from conftest import GOOGLE_SHEETS_TEST_DOCUMENT_ID
def test_frozens(model_context):
    # model context ensures tests are using data from the test document:
    assert Frozen.service.document_id == GOOGLE_SHEETS_TEST_DOCUMENT_ID
    # DESTROY ALL:
    Frozen.destroy_all()
    # SEED RECORDS:
    Frozen.seed()
    # FIND ALL:
    frozens = Frozen.all()
    assert len(frozens) == 3
    # CREATE
    frozen = Frozen.find(1)
    assert frozen.id == 1
    assert frozen.name == "Meatballs"
    assert frozen.price == '$17.99'
    assert isinstance(frozen.created_at, datetime)