from pprint import pprint
from app.db import BaseModel
class Frozen(BaseModel):
    SHEET_NAME = "frozens"
    COLUMNS = ["name", "description", "price", "url"]
    SEEDS = [
        {
            'name': 'Chicken Breast',
            'description': 'Fat-free and organic chicken breast',
            'price': '$14.99',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/Chicken-breast.png?raw=true'
        },
        {
            'name': 'Chicken Thighs',
            'description': 'Tasty, healthy and protein filled.',
            'price': '$13.49',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/chicken%20thigh.webp?raw=true'
        },
        {
            'name': 'Salmon',
            'description': 'De-boned, fresh water Salmon.',
            'price': '$29.99',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/salmon.jpeg?raw=true'
        },
        {
            'name': 'Grounf Beef',
            'description': 'Healthy and tasty groound meat.',
            'price': '$12.99',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/ground%20beef.jpeg?raw=true'
        },
        {
            'name': 'Pork Belly',
            'description': 'Soft, fatty and tasty pork belly.',
            'price': '$13.49',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/prok%20belly.jpeg?raw=true'
        },
        {
            'name': 'Chicken sausage',
            'description': 'Ground chicken and spices sausage.',
            'price': '$10.99',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/chicken%20sausage.jpeg?raw=true'
        },
        {
            'name': 'Pepperoni',
            'description': 'Salty, fresh and fatty pepperoni.',
            'price': '$4.99',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/pepperoni.jpeg?raw=true'
        },
        {
            'name': 'Meatballs',
            'description': 'Healthy meatballs perfect for pasta.',
            'price': '$17.99',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/meatbals.jpeg?raw=true'
        },
        {
            'name': 'Shrimp',
            'description': 'De-veined, Tail-Off Medium shrimp.',
            'price': '$19.99',
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/shrimp.jpeg?raw=true'
        }
    ]
if __name__ == "__main__":
    print("------------")
    print("EXISTING RECORDS:")
    frozens = Frozen.all()
    print("FOUND", len(frozens), "FROZENS:")
    if any(frozens):
        for frozen in frozens:
            #breakpoint()
            pprint(dict(frozen))
    else:
        #if input("Seed frozens? (Y/N)? ").upper() == "Y":
        #    print("SEEDING RECORDS...")
        #    Frozen.seed()
        print("SEEDING RECORDS...")
        Frozen.seed()
    print("------------")
    print("FIND RECORD GIVEN ITS IDENTIFIER...")
    frozen = Frozen.find(1)
    print(frozen.name)
    print("------------")
    print("FILTERING RECORDS...")
    matches = Frozen.where(name="Strawberries")
    print(len(matches))
    frozen = matches[0]
    print(frozen.name)
    print("------------")
    print("CREATING NEW PRODUCT...")
    params = {
            'name': 'Frozen Turkey',
            'description': 'Fat-free, frozen turkey.',
            'price': 6.99,
            'url': 'https://github.com/BaluNivetha/Web-app/blob/main/pictures/Frozen/turkey.jpeg?raw=true'
    }
    Frozen.create(params)