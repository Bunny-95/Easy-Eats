from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.restaurant import Restaurant
from app.models.menu_item import MenuItem

router = APIRouter(prefix="/restaurants", tags=["Restaurants"])


@router.get("/")
def get_restaurants(db: Session = Depends(get_db)):
    return db.query(Restaurant).all()


@router.get("/{restaurant_id}")
def get_restaurant(restaurant_id: int, db: Session = Depends(get_db)):
    restaurant = db.query(Restaurant).filter(
        Restaurant.id == restaurant_id
    ).first()

    menu = db.query(MenuItem).filter(
        MenuItem.restaurant_id == restaurant_id
    ).all()

    return {
        "restaurant": restaurant,
        "menu": menu
    }


@router.post("/seed")
def seed_data(db: Session = Depends(get_db)):
    if db.query(Restaurant).first():
        return {"message": "Data already exists"}

    r1 = Restaurant(
        owner_id=1,
        name="Campus Cafe",
        category="Snacks",
        is_open=True
    )

    r2 = Restaurant(
        owner_id=1,
        name="Easy Bites",
        category="Meals",
        is_open=True
    )

    r3 = Restaurant(
    owner_id=1,
    name="Coffee Corner",
    category="Coffee",
    is_open=True
)

    db.add_all([r1, r2, r3])
    db.commit()

    db.refresh(r1)
    db.refresh(r2)
    db.refresh(r3)

    items = [
        MenuItem(
            restaurant_id=r1.id,
            name="Sandwich",
            price=50,
            prep_time=5
        ),
        MenuItem(
            restaurant_id=r1.id,
            name="Tea",
            price=15,
            prep_time=2
        ),
        MenuItem(
            restaurant_id=r2.id,
            name="Veg Meal",
            price=90,
            prep_time=10
        ),
        MenuItem(
            restaurant_id=r2.id,
            name="Burger",
            price=70,
            prep_time=7
        ),
        MenuItem(
    restaurant_id=r3.id,
    name="Cold Coffee",
    price=60,
    prep_time=3
),
MenuItem(
    restaurant_id=r3.id,
    name="Latte",
    price=80,
    prep_time=4
)
    ]

    db.add_all(items)
    db.commit()

    return {"message": "Seed data added"}