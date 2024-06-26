
from app.models.fresh import Fresh
from app.models.frozen import Frozen
from app.models.product import Product

# tests for each page (update the tests if you change the page contents):


def test_home_page(test_client):
    response = test_client.get("/")
    assert response.status_code == 200
    assert b"<h1>Welcome to Superstore!</h1>" in response.data


def test_about_page(test_client):
    response = test_client.get("/about")
    assert response.status_code == 200
    assert b"<h1>Welcome to Superstore!</h1>" in response.data

    
def test_products_page(test_client):
    # setup (seed database with some products):
    Product.destroy_all()
    Product.seed()

    products = Product.all()
    assert len(products) == 8

    # given certain products in the database,
    # we expect to see corresponding information on the page:
    response = test_client.get("/products")
    assert response.status_code == 200
    # assert b"<h1>Everyday Deals</h1>" in response.data
    # assert b"Textbook" in response.data
    # assert b"Cup of Tea" in response.data
    # assert b"Strawberries" in response.data

    # clean up (clear products sheet):
    Product.destroy_all()




def test_freshs_page(test_client):
    # setup (seed database with some freshs):
    Fresh.destroy_all()
    Fresh.seed()
    freshs = Fresh.all()
    assert len(freshs) == 9
    # given certain freshs in the database,
    # we expect to see corresponding information on the page:
    response = test_client.get("/freshs")
    assert response.status_code == 200
    # assert b"<h1>Fresh Produce</h1>" in response.data
    # assert b"Textbook" in response.data
    # assert b"Cup of Tea" in response.data
    # assert b"Strawberries" in response.data
    # clean up (clear freshs sheet):
    Fresh.destroy_all()





def test_frozens_page(test_client):
    # setup (seed database with some frozens):
    Frozen.destroy_all()
    Frozen.seed()
    frozens = Frozen.all()
    assert len(frozens) == 9
    # given certain frozens in the database,
    # we expect to see corresponding information on the page:
    response = test_client.get("/frozens")
    assert response.status_code == 200
    # assert b"<h1>Frozen Products</h1>" in response.data
    # assert b"Strawberries" in response.data
    # clean up (clear frozens sheet):
    Frozen.destroy_all()