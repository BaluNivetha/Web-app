from pprint import pprint

from app.db import BaseModel

class Product(BaseModel):

    SHEET_NAME = "products"

    COLUMNS = ["name", "description", "price", "url"]

    SEEDS = [
        {
            'name': 'Strawberries',
            'description': 'Buy 2 boxes of Strawberries and get 1 box for free!',
            'price': 4.99,
            'url': 'https://picsum.photos/id/1080/360/200'
        },
        {
            'name': 'Avocado',
            'description': 'Buy 1 Avocado @ $2 off, buy 3 Avocado @ $5 off.',
            'price': 3.49,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/Avacado.jpeg?raw=true'
        },
        {
            'name': 'Salmon',
            'description': 'Buy 1 filet of Salmon and  get 1 Salmon Filet free!',
            'price': 19.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/salmon.jpeg?raw=true'
        },
        {
            'name': 'Beans',
            'description': 'Buy 1lb beans and get $3 off on carrots.',
            'price': 3.49,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/beans.jpeg?raw=true'
        },
        {
            'name': 'Meatballs',
            'description': 'Buy 1lb meatballs and get $5 off on seasoning kit',
            'price': 3.49,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/meatbals.jpeg?raw=true'
        },
        {
            'name': 'Chicken Sausage',
            'description': 'Buy 10 Chicken Sausages and get 2 Chicken Sausages for free!',
            'price': 3.49,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/chicken%20sausage.jpeg?raw=true'
        },
        {
          'name': 'Celery',
            'description': 'Buy 1lb Celery and get 30 days trial with blender!',
            'price': 3.49,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/celery.jpeg?raw=true'
        },
        {
            'name': 'Banana',
            'description': 'Buy 10 banana and get cubed pineapples for 50% off!',
            'price': 3.49,
            'url': 'https://raw.githubusercontent.com/BaluNivetha/Web-app/main/pictures/Fresh/banana.webp'
        }
    ]




if __name__ == "__main__":

    print("------------")
    print("EXISTING RECORDS:")
    products = Product.all()
    print("FOUND", len(products), "PRODUCTS:")
    if any(products):
        for product in products:
            #breakpoint()
            pprint(dict(product))
    else:
        #if input("Seed products? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Product.seed()
        print("SEEDING RECORDS...")
        Product.seed()

    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    product = Product.find(1)
    print(product.name)

    print("------------")
    print("FILTERING RECORDS...")
    matches = Product.where(name="Strawberries")
    print(len(matches))
    product = matches[0]
    print(product.name)

    print("------------")
    # print("CREATING NEW PRODUCT...")
    # params = {
    #     "name": "Blueberries",
    #     "price":3.99,
    #     "description":"organic blues",
    #     "url": "https://images.unsplash.com/photo-1498557850523-fd3d118b962e?q=80&w=2938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
    # }
    # Product.create(params)
