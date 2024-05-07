from pprint import pprint
from app.db import BaseModel
class Fresh(BaseModel):
    SHEET_NAME = "freshs"
    COLUMNS = ["name", "description", "price", "url"]
    SEEDS = [
        {
            'name': 'Strawberries',
            'description': 'Juicy organic strawberries.',
            'price': 4.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/Strawberry.jpeg'
        },
        {
            'name': 'Potatoes',
            'description': 'Fresh, organic and tasty potatoes.',
            'price': 3.49,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/potatoes.jpeg'
        },
        {
            'name': 'Tomatoes',
            'description': 'Fresh, organic and juicy tomatoes.',
            'price': 129.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/tomatoes.jpeg'
        },
        {
            'name': 'Celery',
            'description': 'Crispy, crunch and healthy celeries.',
            'price': 19.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/celery.jpeg'
        },
        {
            'name': 'Oranges',
            'description': 'Juicy, citrusy and heathy oranges.',
            'price': 12.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/orange.webp'
        },
        {
            'name': 'Bananas',
            'description': 'Healty, sweet and fresh bananas.',
            'price': 3.49,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/banana.webp'
        },
        {
            'name': 'Avacadoes',
            'description': 'Creamy, tasty and full of healthy fats.',
            'price': 10.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/Avacado.jpeg'
        },
        {
            'name': 'Carrots',
            'description': 'Sweet, fresh and crunchy carrots.',
            'price': 4.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/carrots.jpeg'
        },
        {
            'name': 'Beans',
            'description': 'Green, healthy and tasty beans.',
            'price': 7.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/beans.jpeg'
        }

    ]




if __name__ == "__main__":
    print("------------")
    print("EXISTING RECORDS:")
    freshs = Fresh.all()
    print("FOUND", len(freshs), "FRESHS:")
    if any(freshs):
        for fresh in freshs:
            #breakpoint()
            pprint(dict(fresh))
    else:
        #if input("Seed freshs? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Fresh.seed()
        print("SEEDING RECORDS...")
        Fresh.seed()
        
    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    fresh = Fresh.find(1)
    print(fresh.name)
    print("------------")
    print("FILTERING RECORDS...")
    matches = Fresh.where(name="Strawberries")
    print(len(matches))
    fresh = matches[0]
    print(fresh.name)
    print("------------")
    print("CREATING NEW PRODUCT...")
    params = {
            'name': 'Cabbage',
            'description': 'Leafy, crunch and perfect for salads.',
            'price': 6.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Fresh/cabbage.webp'
    }
    Fresh.create(params)