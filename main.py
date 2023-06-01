from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# 가상의 쥬얼리 상품 데이터
jewelry_data = [
    {"category": "earring", "brand": "ABC jewelry", "price": 100000, "gemstone": "diamond", "inventory": 5},
    {"category": "necklace", "brand": "XYZ accessories", "price": 80000, "gemstone": "ruby", "inventory": 3},
    {"category": "bracelet", "brand": "DEF gems", "price": 120000, "gemstone": "emerald", "inventory": 8},
    {"category": "ring", "brand": "GHI jewelers", "price": 150000, "gemstone": "sapphire", "inventory": 2},
    {"category": "earring", "brand": "JKL designs", "price": 90000, "gemstone": "amethyst", "inventory": 6},
    {"category": "necklace", "brand": "MNO gems", "price": 110000, "gemstone": "topaz", "inventory": 4},
    {"category": "bracelet", "brand": "PQR accessories", "price": 95000, "gemstone": "aquamarine", "inventory": 7},
    {"category": "ring", "brand": "STU jewelers", "price": 130000, "gemstone": "opal", "inventory": 1},
    {"category": "earring", "brand": "VWX jewelry", "price": 85000, "gemstone": "pearl", "inventory": 9},
    {"category": "necklace", "brand": "YZA designs", "price": 75000, "gemstone": "garnet", "inventory": 5}
]

# 쥬얼리 상품 필터링 API 엔드포인트
@app.get("/jewelry")
async def filter_jewelry(
    category: str = Query(default=None),
    brand: str = Query(default=None),
    min_price: int = Query(default=None, ge=0),
    max_price: int = Query(default=None, ge=0),
    gemstone: str = Query(default=None)
):
    filtered_items = jewelry_data

    if category:
        filtered_items = [item for item in filtered_items if item["category"].lower() == category.lower()]

    if brand is not None:
        filtered_items = [item for item in filtered_items if item["brand"].lower() == brand.lower()]

    if min_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] >= min_price]

    if max_price is not None:
        filtered_items = [item for item in filtered_items if item["price"] <= max_price]

    if gemstone is not None:
        filtered_items = [item for item in filtered_items if gemstone.lower() in item["gemstone"].lower()]

    return filtered_items

car_rental_data = [
    {"vehicle_type": "SUV", "model": "Kia Sportage", "mileage": 10.5, "daily_rental_fee": 90000, "available": True, "location": "서울특별시 강남구"},
    {"vehicle_type": "Sedan", "model": "Hyundai Sonata", "mileage": 12.3, "daily_rental_fee": 80000, "available": True, "location": "서울특별시 마포구"},
    {"vehicle_type": "SUV", "model": "Toyota RAV4", "mileage": 11.8, "daily_rental_fee": 95000, "available": False, "location": "서울특별시 서초구"},
    {"vehicle_type": "Sedan", "model": "Kia K5", "mileage": 13.2, "daily_rental_fee": 75000, "available": True, "location": "서울특별시 송파구"},
    {"vehicle_type": "SUV", "model": "Hyundai Tucson", "mileage": 10.9, "daily_rental_fee": 88000, "available": True, "location": "서울특별시 영등포구"},
    {"vehicle_type": "Sedan", "model": "Toyota Camry", "mileage": 12.8, "daily_rental_fee": 82000, "available": False, "location": "서울특별시 종로구"},
    {"vehicle_type": "SUV", "model": "Kia Sorento", "mileage": 11.5, "daily_rental_fee": 92000, "available": True, "location": "서울특별시 중구"},
    {"vehicle_type": "Sedan", "model": "Hyundai Elantra", "mileage": 13.5, "daily_rental_fee": 78000, "available": True, "location": "서울특별시 강서구"},
    {"vehicle_type": "SUV", "model": "Mazda CX-5", "mileage": 10.2, "daily_rental_fee": 93000, "available": False, "location": "서울특별시 도봉구"},
    {"vehicle_type": "Sedan", "model": "Honda Accord", "mileage": 12.1, "daily_rental_fee": 79000, "available": True, "location": "서울특별시 성북구"}
]

@app.get("/car_rental")
async def filter_car_rental(
    location: str = Query(default=None),
    model: str = Query(default=None),
    vehicle_type: str = Query(default=None),
    min_mileage: float = Query(default=None, ge=0.0),
    max_rental_fee: int = Query(default=None, ge=0),
    available: bool = Query(default=None)
):
    filtered_items = car_rental_data

    if location:
        filtered_items = [item for item in filtered_items if location.lower() in item["location"].lower()]

    if model is not None:
        filtered_items = [item for item in filtered_items if model.lower() in item["model"].lower()]

    if vehicle_type is not None:
        filtered_items = [item for item in filtered_items if vehicle_type.lower() == item["vehicle_type"].lower()]

    if min_mileage is not None:
        filtered_items = [item for item in filtered_items if item["mileage"] >= min_mileage]

    if max_rental_fee is not None:
        filtered_items = [item for item in filtered_items if item["daily_rental_fee"] <= max_rental_fee]

    if available is not None:
        filtered_items = [item for item in filtered_items if item["available"] == available]

    return filtered_items
