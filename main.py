from fastapi import FastAPI, Query
from typing import List
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float

inventory = []  # 임시로 아이템을 저장하는 리스트

@app.post("/items/")
async def create_item(item: Item):
    inventory.append(item)
    return {"message": "Item created successfully"}

@app.get("/items/")
async def get_items():
    return inventory

#mobile app
all_apps = [
    {1,"NH올원뱅크","금융","당신을 위한 모든 금융이 한 곳에! 농협은행 모바일 뱅크. NH올원뱅크를 만나 보세요!", 3.7, "NH농협은행"},
{2,"시티즌코난","도구","일선 경찰관을 위한 보이스피싱 악성 앱 순간 탐지기(구 피싱아이즈 폴리스)로서 *피싱아이즈*와 함께 운영되고 있습니다.", 4.2, "(주)인피니그루"},
{3,"KB Pay","금융","KB Pay 모든 금융을 한번에, 한손에, 한눈에 담다", 4.2, "KB국민카드"},
{4,"쿠팡플레이","엔터테인먼트","쿠팡플레이로 쿠팡 와우 멤버십에 시청의 즐거움을 더했어요.", 3.6, "Coupang Corp."},
{5,"AliExpress","쇼핑","해외직구는 알리익스프레스!", 4.5, "Alibaba Mobile"},
{6,"Nike","쇼핑","최신 운둥화와 남성 여성 키즈 의류부터 앱 전용 제품과 멤버 혜택, 운동 콘텐츠까지. 당신만을 위한 특별한 나이키를 앱에서 만나보세요.", 4.3, "Nike, Inc."},
{7,"네이버 파파고","도구","똑똑한 AI 통변역기, 언어 장벽 없이 대화하는 세상을 꿈꿉니다.", 4.7, "NAVER Corp."}
]

@app.get("/mobile_app")
async def filter_mobile_app(
    min_ranking: int = Query(default=None, description="Minimum ranking"),
    max_ranking: int = Query(default=None, description="Maximum ranking"),
    name: str = Query(default=None, description="App name"),
    category: str = Query(default=None, description="Category"),
    min_rating: float = Query(default=None, ge=0, le=5, description="Minimum rating"),
    max_rating: float = Query(default=None, ge=0, le=5, description="Maximum rating"),
    pub: str = Query(default=None, description="Developer/Publisher")
):
    filtered_apps = []

    # Placeholder code to demonstrate the filtering logic
    for app in all_apps:
        if (
            (min_ranking is None or app["ranking"] >= min_ranking) and
            (max_ranking is None or app["ranking"] <= max_ranking) and
            (name is None or app["name"].lower() == name.lower()) and
            (category is None or app["category"].lower() == category.lower()) and
            (min_rating is None or app["rating"] >= min_rating) and
            (max_rating is None or app["rating"] <= max_rating) and
            (pub is None or app["pub"].lower() == pub.lower())
        ):
            filtered_apps.append(app)

    return filtered_apps






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

#가상의 자동차 렌트 상품 데이터
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

#가상의 SNS 계정 정보 DB

sns_accounts = [
    {"user_id": "user1", "username": "John Doe", "followers": 500, "following": 300, "posts": 100, "likes": 2000, "comments": 500, "bio": "Passionate photographer"},
    {"user_id": "user2", "username": "Jane Smith", "followers": 1000, "following": 500, "posts": 200, "likes": 4000, "comments": 1000, "bio": "Food lover and travel enthusiast"},
    {"user_id": "user3", "username": "David Johnson", "followers": 800, "following": 600, "posts": 150, "likes": 3000, "comments": 800, "bio": "Fitness freak and adventure seeker"},
    {"user_id": "user4", "username": "Emily Davis", "followers": 1200, "following": 900, "posts": 180, "likes": 5000, "comments": 1200, "bio": "Bookworm and aspiring writer"},
    {"user_id": "user5", "username": "Michael Wilson", "followers": 300, "following": 200, "posts": 50, "likes": 1000, "comments": 300, "bio": "Music lover and concert goer"},
    {"user_id": "user6", "username": "Sarah Brown", "followers": 700, "following": 400, "posts": 120, "likes": 2500, "comments": 600, "bio": "Fashion enthusiast and beauty junkie"},
    {"user_id": "user7", "username": "Christopher Lee", "followers": 1500, "following": 1200, "posts": 250, "likes": 6000, "comments": 1500, "bio": "Tech geek and gadget lover"},
    {"user_id": "user8", "username": "Olivia Taylor", "followers": 900, "following": 700, "posts": 160, "likes": 3500, "comments": 900, "bio": "Nature lover and outdoor adventurer"},
    {"user_id": "user9", "username": "Daniel Martin", "followers": 400, "following": 250, "posts": 80, "likes": 1500, "comments": 400, "bio": "Coffee addict and early riser"},
    {"user_id": "user10", "username": "Sophia Anderson", "followers": 600, "following": 350, "posts": 100, "likes": 2000, "comments": 600, "bio": "Art lover and creative soul"}
]

@app.get("/sns_accounts")
async def filter_sns_accounts(
    min_followers: int = Query(default=None, ge=0),
    min_following: int = Query(default=None, ge=0),
    min_likes: int = Query(default=None, ge=0),
    user_id: str = Query(default=None),
    username: str = Query(default=None),
):
    filtered_accounts = sns_accounts

    if min_followers is not None:
        filtered_accounts = [account for account in filtered_accounts if account["followers"] >= min_followers]

    if min_following is not None:
        filtered_accounts = [account for account in filtered_accounts if account["following"] >= min_following]

    if min_likes is not None:
        filtered_accounts = [account for account in filtered_accounts if account["likes"] >= min_likes]

    if user_id is not None:
        filtered_accounts = [account for account in filtered_accounts if account["user_id"].lower() == user_id.lower()]

    if username is not None:
        filtered_accounts = [account for account in filtered_accounts if username.lower() in account["username"].lower()]

    return filtered_accounts

#건강관리 센터 회원 정보
health_center_members = [
    {"id": 1, "name": "John Doe", "gender": "M", "age": 30, "height": 180, "weight": 75, "blood_pressure": "120/80", "heart_rate": 70},
    {"id": 2, "name": "Jane Smith", "gender": "F", "age": 45, "height": 165, "weight": 68, "blood_pressure": "130/85", "heart_rate": 75},
    {"id": 3, "name": "David Johnson", "gender": "M", "age": 50, "height": 175, "weight": 80, "blood_pressure": "125/82", "heart_rate": 72},
    {"id": 4, "name": "Emily Davis", "gender": "F", "age": 35, "height": 160, "weight": 55, "blood_pressure": "118/78", "heart_rate": 68},
    {"id": 5, "name": "Michael Wilson", "gender": "M", "age": 55, "height": 170, "weight": 70, "blood_pressure": "130/90", "heart_rate": 78},
    {"id": 6, "name": "Sarah Brown", "gender": "F", "age": 40, "height": 155, "weight": 58, "blood_pressure": "122/80", "heart_rate": 65},
    {"id": 7, "name": "Christopher Lee", "gender": "M", "age": 60, "height": 175, "weight": 85, "blood_pressure": "135/88", "heart_rate": 75},
    {"id": 8, "name": "Olivia Taylor", "gender": "F", "age": 50, "height": 165, "weight": 60, "blood_pressure": "120/80", "heart_rate": 70},
    {"id": 9, "name": "Daniel Martin", "gender": "M", "age": 45, "height": 180, "weight": 78, "blood_pressure": "125/85", "heart_rate": 72},
    {"id": 10, "name": "Sophia Anderson", "gender": "F", "age": 55, "height": 160, "weight": 65, "blood_pressure": "130/90", "heart_rate": 75}
]

@app.get("/health_center_members")
async def filter_health_center_members(
    name: str = Query(default=None),
    gender: str = Query(default=None, regex="^[MF]$"),
    age: int = Query(default=None, ge=0),
    age_range: str = Query(default=None),
    weight_range: str = Query(default=None),
    height_range: str = Query(default=None)
):
    filtered_members = health_center_members

    if name is not None:
        filtered_members = [member for member in filtered_members if name.lower() in member["name"].lower()]

    if gender is not None:
        filtered_members = [member for member in filtered_members if member["gender"].lower() == gender.lower()]

    if age is not None:
        filtered_members = [member for member in filtered_members if member["age"] == age]

    if age_range is not None:
        age_min, age_max = map(int, age_range.split("-"))
        filtered_members = [member for member in filtered_members if age_min <= member["age"] <= age_max]

    if weight_range is not None:
        weight_min, weight_max = map(int, weight_range.split("-"))
        filtered_members = [member for member in filtered_members if weight_min <= member["weight"] <= weight_max]

    if height_range is not None:
        height_min, height_max = map(int, height_range.split("-"))
        filtered_members = [member for member in filtered_members if height_min <= member["height"] <= height_max]

    return filtered_members

#약 처방 기록
pharmacy_prescriptions = [
    {"id": 1, "prescriber_age": 45, "prescriber_gender": "M", "medicine": "타이레놀", "prescription_date": "2022-01-01", "prescribing_doctor": "Dr. John Doe"},
    {"id": 2, "prescriber_age": 35, "prescriber_gender": "F", "medicine": "이기탄", "prescription_date": "2022-02-15", "prescribing_doctor": "Dr. Jane Smith"},
    {"id": 3, "prescriber_age": 50, "prescriber_gender": "M", "medicine": "게보린", "prescription_date": "2022-03-10", "prescribing_doctor": "Dr. David Johnson"},
    {"id": 4, "prescriber_age": 40, "prescriber_gender": "F", "medicine": "타이레놀", "prescription_date": "2022-04-05", "prescribing_doctor": "Dr. Emily Davis"},
    {"id": 5, "prescriber_age": 55, "prescriber_gender": "M", "medicine": "이기탄", "prescription_date": "2022-05-20", "prescribing_doctor": "Dr. Michael Wilson"},
    {"id": 6, "prescriber_age": 30, "prescriber_gender": "F", "medicine": "게보린", "prescription_date": "2022-06-15", "prescribing_doctor": "Dr. Sarah Brown"},
    {"id": 7, "prescriber_age": 60, "prescriber_gender": "M", "medicine": "타이레놀", "prescription_date": "2022-07-01", "prescribing_doctor": "Dr. Christopher Lee"},
    {"id": 8, "prescriber_age": 50, "prescriber_gender": "F", "medicine": "이기탄", "prescription_date": "2022-08-12", "prescribing_doctor": "Dr. Olivia Taylor"},
    {"id": 9, "prescriber_age": 45, "prescriber_gender": "M", "medicine": "게보린", "prescription_date": "2022-09-05", "prescribing_doctor": "Dr. Daniel Martin"},
    {"id": 10, "prescriber_age": 55, "prescriber_gender": "F", "medicine": "타이레놀", "prescription_date": "2022-10-20", "prescribing_doctor": "Dr. Sophia Anderson"}
]

@app.get("/pharmacy_prescriptions")
async def filter_pharmacy_prescriptions(
    age: int = Query(default=None, ge=0),
    gender: str = Query(default=None, regex="^[MF]$"),
    medicine: str = Query(default=None),
    prescription_date: str = Query(default=None),
):
    filtered_prescriptions = pharmacy_prescriptions

    if age is not None:
        filtered_prescriptions = [prescription for prescription in filtered_prescriptions if prescription["prescriber_age"] == age]

    if gender is not None:
        filtered_prescriptions = [prescription for prescription in filtered_prescriptions if prescription["prescriber_gender"].lower() == gender.lower()]

    if medicine is not None:
        filtered_prescriptions = [prescription for prescription in filtered_prescriptions if medicine.lower() in prescription["medicine"].lower()]

    if prescription_date is not None:
        filtered_prescriptions = [prescription for prescription in filtered_prescriptions if prescription["prescription_date"] == prescription_date]

    return filtered_prescriptions

#스트리밍 영상 조회

streaming_videos = [
    {"title": "Queen Live concert 220701", "channel": "Queen fantube", "views": 100000, "likes": 5000, "comments": 100, "shares": 50, "duration": "05:30"},
    {"title": "Queen Live concert 220708", "channel": "Queen fantube", "views": 50000, "likes": 2000, "comments": 50, "shares": 20, "duration": "10:45"},
    {"title": "Queen Live Under pressure", "channel": "Queen fantube", "views": 80000, "likes": 3000, "comments": 80, "shares": 30, "duration": "03:15"},
    {"title": "Queen Live Don't stop me now", "channel": "Queen fantube", "views": 120000, "likes": 8000, "comments": 200, "shares": 100, "duration": "08:20"},
    {"title": "Queen fan meeting", "channel": "Queen fantube", "views": 60000, "likes": 2500, "comments": 70, "shares": 40, "duration": "06:50"},
    {"title": "Summer concert queen", "channel": "Summer concert Official", "views": 90000, "likes": 4000, "comments": 120, "shares": 60, "duration": "07:30"},
    {"title": "Summer concert oasis", "channel": "Summer concert Official", "views": 150000, "likes": 10000, "comments": 300, "shares": 150, "duration": "12:15"},
    {"title": "Summer concert Adel", "channel": "Summer concert Official", "views": 70000, "likes": 3500, "comments": 90, "shares": 35, "duration": "04:40"},
    {"title": "Summer concert GOD", "channel": "Summer concert Official", "views": 110000, "likes": 6000, "comments": 150, "shares": 75, "duration": "09:05"},
    {"title": "Summer concert IU", "channel": "Summer concert Official", "views": 100000, "likes": 5000, "comments": 100, "shares": 50, "duration": "06:10"}
]

@app.get("/streaming_videos")
async def filter_streaming_videos(
    title: str = Query(...),
    channel: str = Query(default=None),
    min_views: int = Query(default=None, ge=0),
    min_likes: int = Query(default=None, ge=0),
    duration_start: str = Query(default=None, regex="^\d{2}:\d{2}$"),
    duration_end: str = Query(default=None, regex="^\d{2}:\d{2}$")
):
    if title:
        filtered_videos = [video for video in streaming_videos if title.lower() in video["title"].lower()]

    if channel is not None:
        filtered_videos = [video for video in filtered_videos if channel.lower() == video["channel"].lower()]

    if min_views is not None:
        filtered_videos = [video for video in filtered_videos if video["views"] >= min_views]

    if min_likes is not None:
        filtered_videos = [video for video in filtered_videos if video["likes"] >= min_likes]

    if duration_start and duration_end:
        filtered_videos = [video for video in filtered_videos if duration_start <= video["duration"] <= duration_end]

    return filtered_videos

# 가상의 스포츠 경기 일정
sports_schedule = [
    {"date": "2023-06-01", "time": "14:00", "sport": "Football", "league": "Premier League", "home_team": "Manchester United", "away_team": "Chelsea", "venue": "Old Trafford"},
    {"date": "2023-06-01", "time": "17:30", "sport": "Football", "league": "La Liga", "home_team": "Real Madrid", "away_team": "Barcelona", "venue": "Santiago Bernabeu"},
    {"date": "2023-06-02", "time": "19:00", "sport": "Football", "league": "Bundesliga", "home_team": "Bayern Munich", "away_team": "Borussia Dortmund", "venue": "Allianz Arena"},
    {"date": "2023-06-02", "time": "20:30", "sport": "Football", "league": "Serie A", "home_team": "Juventus", "away_team": "AC Milan", "venue": "Allianz Stadium"},
    {"date": "2023-06-03", "time": "15:00", "sport": "Football", "league": "Ligue 1", "home_team": "Paris Saint-Germain", "away_team": "Olympique Marseille", "venue": "Parc des Princes"},
    {"date": "2023-06-03", "time": "18:00", "sport": "Football", "league": "Eredivisie", "home_team": "Ajax", "away_team": "PSV Eindhoven", "venue": "Johan Cruyff Arena"},
    {"date": "2023-06-04", "time": "13:30", "sport": "Football", "league": "Premier League", "home_team": "Liverpool", "away_team": "Manchester City", "venue": "Anfield"},
    {"date": "2023-06-04", "time": "16:00", "sport": "Football", "league": "La Liga", "home_team": "Atletico Madrid", "away_team": "Sevilla", "venue": "Wanda Metropolitano"},
    {"date": "2023-06-05", "time": "20:00", "sport": "Football", "league": "Bundesliga", "home_team": "RB Leipzig", "away_team": "Bayer Leverkusen", "venue": "Red Bull Arena"},
    {"date": "2023-06-05", "time": "21:30", "sport": "Football", "league": "Serie A", "home_team": "Inter Milan", "away_team": "Napoli", "venue": "San Siro"}
]

@app.get("/sports_schedule")
async def filter_sports_schedule(
    date: str = Query(default=None),
    sport: str = Query(default=None),
    team: str = Query(default=None),
    league: str = Query(default=None)
):
    filtered_schedule = sports_schedule

    if date is not None:
        filtered_schedule = [game for game in filtered_schedule if game["date"] == date]

    if sport is not None:
        filtered_schedule = [game for game in filtered_schedule if sport.lower() in game["sport"].lower()]

    if team is not None:
        filtered_schedule = [game for game in filtered_schedule if team.lower() in game["home_team"].lower() or team.lower() in game["away_team"].lower()]

    if league is not None:
        filtered_schedule = [game for game in filtered_schedule if league.lower() in game["league"].lower()]

    return filtered_schedule

# 야구선수 타자 기록
season_records = [
    {"id": 1, "player_name": "Kim", "position": "1B", "avg": 0.305, "obp": 0.400, "slg": 0.550, "rbi": 100, "runs": 95, "stolen_bases": 20, "home_runs": 35},
    {"id": 2, "player_name": "Lee", "position": "2B", "avg": 0.290, "obp": 0.380, "slg": 0.500, "rbi": 80, "runs": 75, "stolen_bases": 10, "home_runs": 20},
    {"id": 3, "player_name": "Park", "position": "1B", "avg": 0.320, "obp": 0.420, "slg": 0.550, "rbi": 90, "runs": 85, "stolen_bases": 15, "home_runs": 25},
    {"id": 4, "player_name": "Choi", "position": "2B", "avg": 0.280, "obp": 0.370, "slg": 0.480, "rbi": 70, "runs": 65, "stolen_bases": 5, "home_runs": 15},
    {"id": 5, "player_name": "Kang", "position": "1B", "avg": 0.300, "obp": 0.390, "slg": 0.520, "rbi": 85, "runs": 80, "stolen_bases": 12, "home_runs": 22},
    {"id": 6, "player_name": "Yoo", "position": "2B", "avg": 0.275, "obp": 0.360, "slg": 0.500, "rbi": 75, "runs": 70, "stolen_bases": 8, "home_runs": 18},
    {"id": 7, "player_name": "Jung", "position": "1B", "avg": 0.290, "obp": 0.380, "slg": 0.490, "rbi": 80, "runs": 75, "stolen_bases": 10, "home_runs": 20},
    {"id": 8, "player_name": "Ha", "position": "1B", "avg": 0.280, "obp": 0.370, "slg": 0.480, "rbi": 70, "runs": 65, "stolen_bases": 5, "home_runs": 15},
    {"id": 9, "player_name": "Chung", "position": "2B", "avg": 0.275, "obp": 0.360, "slg": 0.500, "rbi": 75, "runs": 70, "stolen_bases": 8, "home_runs": 18}
]

@app.get("/season_records")
async def filter_season_records(
    player_name: str = Query(default=None),
    position: str = Query(default=None),
    min_avg: float = Query(default=None, ge=0.0),
    min_obp: float = Query(default=None, ge=0.0),
    min_slg: float = Query(default=None, ge=0.0),
    min_rbi: int = Query(default=None, ge=0),
    min_runs: int = Query(default=None, ge=0),
    min_stolen_bases: int = Query(default=None, ge=0),
    min_home_runs: int = Query(default=None, ge=0)
):
    filtered_records = season_records

    if player_name is not None:
        filtered_records = [record for record in filtered_records if player_name.lower() in record['player_name'].lower()]

    if position is not None:
        filtered_records = [record for record in filtered_records if position == record['position']]

    if min_avg is not None:
        filtered_records = [record for record in filtered_records if record['avg'] >= min_avg]

    if min_obp is not None:
        filtered_records = [record for record in filtered_records if record['obp'] >= min_obp]

    if min_slg is not None:
        filtered_records = [record for record in filtered_records if record['slg'] >= min_slg]

    if min_rbi is not None:
        filtered_records = [record for record in filtered_records if record['rbi'] >= min_rbi]

    if min_runs is not None:
        filtered_records = [record for record in filtered_records if record['runs'] >= min_runs]

    if min_stolen_bases is not None:
        filtered_records = [record for record in filtered_records if record['stolen_bases'] >= min_stolen_bases]

    if min_home_runs is not None:
        filtered_records = [record for record in filtered_records if record['home_runs'] >= min_home_runs]

    return filtered_records

#야구 투수 기록
pitcher_stats = [
    {"id": 1, "name": "Kim", "games": 30, "innings": 180.1, "wins": 15, "losses": 5, "strikeouts": 200, "home_runs_allowed": 10, "era": 2.50},
    {"id": 2, "name": "Lee", "games": 28, "innings": 170.2, "wins": 12, "losses": 8, "strikeouts": 180, "home_runs_allowed": 15, "era": 3.20},
    {"id": 3, "name": "Park", "games": 32, "innings": 200.0, "wins": 18, "losses": 3, "strikeouts": 220, "home_runs_allowed": 12, "era": 2.10},
    {"id": 4, "name": "Choi", "games": 25, "innings": 150.0, "wins": 10, "losses": 7, "strikeouts": 160, "home_runs_allowed": 8, "era": 3.50},
    {"id": 5, "name": "Kang", "games": 27, "innings": 165.2, "wins": 14, "losses": 6, "strikeouts": 190, "home_runs_allowed": 11, "era": 2.80},
    {"id": 6, "name": "Yoo", "games": 29, "innings": 175.1, "wins": 11, "losses": 9, "strikeouts": 170, "home_runs_allowed": 13, "era": 3.00},
    {"id": 7, "name": "Jung", "games": 26, "innings": 155.0, "wins": 9, "losses": 8, "strikeouts": 150, "home_runs_allowed": 10, "era": 3.30},
    {"id": 8, "name": "Ha", "games": 31, "innings": 190.2, "wins": 16, "losses": 4, "strikeouts": 210, "home_runs_allowed": 9, "era": 2.40}
]

@app.get("/pitcher_stats")
async def filter_pitcher_stats(
    name: str = Query(default=None),
    min_innings: float = Query(default=None, ge=0.0),
    max_era: float = Query(default=None, le=10.0),
    min_wins: int = Query(default=None, ge=0),
    max_losses: int = Query(default=None, le=20),
    min_strikeouts: int = Query(default=None, ge=0),
    max_home_runs_allowed: int = Query(default=None, le=30)
):
    filtered_stats = pitcher_stats

    if name is not None:
        filtered_stats = [stat for stat in filtered_stats if name.lower() in stat['name'].lower()]

    if min_innings is not None:
        filtered_stats = [stat for stat in filtered_stats if stat['innings'] >= min_innings]

    if max_era is not None:
        filtered_stats = [stat for stat in filtered_stats if stat['era'] <= max_era]

    if min_wins is not None:
        filtered_stats = [stat for stat in filtered_stats if stat['wins'] >= min_wins]

    if max_losses is not None:
        filtered_stats = [stat for stat in filtered_stats if stat['losses'] <= max_losses]

    if min_strikeouts is not None:
        filtered_stats = [stat for stat in filtered_stats if stat['strikeouts'] >= min_strikeouts]

    if max_home_runs_allowed is not None:
        filtered_stats = [stat for stat in filtered_stats if stat['home_runs_allowed'] <= max_home_runs_allowed]

    return filtered_stats

# 악보 상품 조회

sheet_music = [
    {"id": 1, "title": "Classical Sonata", "instrument": "Piano", "difficulty": 4.5, "price": 25, "rating": 4.2, "genre": "Classical"},
    {"id": 2, "title": "Jazz Improvisation", "instrument": "Saxophone", "difficulty": 3.2, "price": 18, "rating": 4.5, "genre": "Jazz"},
    {"id": 3, "title": "Rock Riffs", "instrument": "Guitar", "difficulty": 2.8, "price": 20, "rating": 4.0, "genre": "Rock"},
    {"id": 4, "title": "Pop Ballad", "instrument": "Piano", "difficulty": 2.1, "price": 15, "rating": 4.8, "genre": "Pop"},
    {"id": 5, "title": "Folk Songs", "instrument": "Violin", "difficulty": 3.5, "price": 22, "rating": 4.3, "genre": "Folk"},
    {"id": 6, "title": "Blues Guitar", "instrument": "Guitar", "difficulty": 3.9, "price": 19, "rating": 4.1, "genre": "Blues"},
    {"id": 7, "title": "Broadway Showtunes", "instrument": "Piano", "difficulty": 3.0, "price": 24, "rating": 4.4, "genre": "Broadway"},
    {"id": 8, "title": "Country Fiddle", "instrument": "Violin", "difficulty": 2.5, "price": 17, "rating": 4.6, "genre": "Country"}
]

@app.get("/sheet_music")
async def filter_sheet_music(
    title: str = Query(default=None),
    instrument: str = Query(default=None),
    min_difficulty: float = Query(default=None, ge=0.0),
    max_difficulty: float = Query(default=None, le=5.0),
    min_price: int = Query(default=None, ge=0),
    genre: str = Query(default=None),
    min_rating: float = Query(default=None, ge=0.0)
):
    filtered_music = sheet_music

    if title is not None:
        filtered_music = [music for music in filtered_music if title.lower() in music['title'].lower()]

    if instrument is not None:
        filtered_music = [music for music in filtered_music if instrument.lower() == music['instrument'].lower()]

    if min_difficulty is not None:
        filtered_music = [music for music in filtered_music if music['difficulty'] >= min_difficulty]

    if max_difficulty is not None:
        filtered_music = [music for music in filtered_music if music['difficulty'] <= max_difficulty]

    if min_price is not None:
        filtered_music = [music for music in filtered_music if music['price'] >= min_price]

    if genre is not None:
        filtered_music = [music for music in filtered_music if genre.lower() == music['genre'].lower()]

    if min_rating is not None:
        filtered_music = [music for music in filtered_music if music['rating'] >= min_rating]

    return filtered_music

# 헬스장 기구 데이터
gym_equipment = [
    {"id": 1, "name": "Treadmill", "type": "Cardio", "brand": "good health", "weight_capacity": 150, "price": 2000000, "availability": True, "rating": 4.5},
    {"id": 2, "name": "Bench Press", "type": "Strength", "brand": "nice body", "weight_capacity": 250, "price": 1500000, "availability": True, "rating": 4.2},
    {"id": 3, "name": "Dumbbells", "type": "Strength", "brand": "good health", "weight_capacity": 50, "price": 500000, "availability": False, "rating": 4.8},
    {"id": 4, "name": "Elliptical", "type": "Cardio", "brand": "good health", "weight_capacity": 180, "price": 2500000, "availability": True, "rating": 4.1},
    {"id": 5, "name": "Leg Press", "type": "Strength", "brand": "nice body", "weight_capacity": 300, "price": 3000000, "availability": True, "rating": 4.3}
]

# 헬스장 기구 조회 API
@app.get("/gym_equipment")
async def get_gym_equipment(
    type: str = Query(default=None),
    brand: str = Query(default=None),
    min_weight_capacity: int = Query(default=None, ge=0),
    max_price: int = Query(default=None, ge=0),
    availability: bool = Query(default=None)
):
    filtered_equipment = gym_equipment

    if type is not None:
        # 유형 필터링
        filtered_equipment = [equipment for equipment in filtered_equipment if type.lower() == equipment['type'].lower()]

    if brand is not None:
        # 브랜드 필터링
        filtered_equipment = [equipment for equipment in filtered_equipment if brand.lower() == equipment['brand'].lower()]

    if min_weight_capacity is not None:
        # 최소 중량 수용력 필터링
        filtered_equipment = [equipment for equipment in filtered_equipment if equipment['weight_capacity'] >= min_weight_capacity]

    if max_price is not None:
        # 최대 가격 필터링
        filtered_equipment = [equipment for equipment in filtered_equipment if equipment['price'] <= max_price]

    if availability is not None:
        # 사용 가능 여부 필터링
        filtered_equipment = [equipment for equipment in filtered_equipment if equipment['availability'] == availability]

    return filtered_equipment

# 호텔 예약 데이터
hotels = [
    {"id": 1, "name": "paradise", "region": "Seoul", "area": 50, "price": 100000, "competition_rate": 0.8, "cooking_available": True, "satisfaction": 4.5},
    {"id": 2, "name": "luxury home", "region": "Busan", "area": 70, "price": 150000, "competition_rate": 0.6, "cooking_available": False, "satisfaction": 4.2},
    {"id": 3, "name": "beautiful day", "region": "Seoul", "area": 60, "price": 120000, "competition_rate": 0.7, "cooking_available": True, "satisfaction": 4.8},
    {"id": 4, "name": "my home", "region": "Busan", "area": 40, "price": 80000, "competition_rate": 0.9, "cooking_available": True, "satisfaction": 4.1},
    {"id": 5, "name": "grand paradise", "region": "Seoul", "area": 55, "price": 95000, "competition_rate": 0.5, "cooking_available": False, "satisfaction": 4.3}
]

# 호텔 예약 API
@app.get("/hotels")
async def get_hotels(
    region: str = Query(default=None),
    min_area: int = Query(default=None, ge=0),
    max_price: int = Query(default=None, ge=0),
    max_competition_rate: float = Query(default=None, ge=0, le=1)
):
    filtered_hotels = hotels

    if region is not None:
        # 지역 필터링
        filtered_hotels = [hotel for hotel in filtered_hotels if region.lower() == hotel['region'].lower()]

    if min_area is not None:
        # 최소 면적 필터링
        filtered_hotels = [hotel for hotel in filtered_hotels if hotel['area'] >= min_area]

    if max_price is not None:
        # 최대 가격 필터링
        filtered_hotels = [hotel for hotel in filtered_hotels if hotel['price'] <= max_price]

    if max_competition_rate is not None:
        # 최대 경쟁율 필터링
        filtered_hotels = [hotel for hotel in filtered_hotels if hotel['competition_rate'] <= max_competition_rate]

    return filtered_hotels

# 영상 조회 데이터
videos = [
    {"id": 1, "title": "Movie 1", "genre": "Action", "duration": 120, "release_year": 2010, "rating": 4.5, "language": "English"},
    {"id": 2, "title": "TV Show 1", "genre": "Drama", "duration": 60, "release_year": 2015, "rating": 4.2, "language": "Korean"},
    {"id": 3, "title": "Movie 2", "genre": "Comedy", "duration": 90, "release_year": 2018, "rating": 3.8, "language": "Spanish"},
    {"id": 4, "title": "TV Show 2", "genre": "Sci-Fi", "duration": 45, "release_year": 2020, "rating": 4.7, "language": "English"},
    {"id": 5, "title": "Movie 3", "genre": "Thriller", "duration": 110, "release_year": 2019, "rating": 4.1, "language": "French"}
]

# 영상 조회 API
@app.get("/videos")
async def get_videos(
    title: str = Query(default=None),
    genre: str = Query(default=None),
    min_duration: int = Query(default=None, ge=0),
    min_rating: float = Query(default=None, ge=0),
    language: str = Query(default=None)
):
    filtered_videos = videos

    if title is not None:
        # 제목 필터링
        filtered_videos = [video for video in filtered_videos if title.lower() in video['title'].lower()]

    if genre is not None:
        # 장르 필터링
        filtered_videos = [video for video in filtered_videos if genre.lower() == video['genre'].lower()]

    if min_duration is not None:
        # 최소 상영 시간 필터링
        filtered_videos = [video for video in filtered_videos if video['duration'] >= min_duration]

    if min_rating is not None:
        # 최소 평점 필터링
        filtered_videos = [video for video in filtered_videos if video['rating'] >= min_rating]

    if language is not None:
        # 언어 필터링
        filtered_videos = [video for video in filtered_videos if language.lower() == video['language'].lower()]

    return filtered_videos

# 정수기 렌탈 상품 데이터
water_purifiers = [
    {"id": 1, "name": "AquaMax", "manufacturer": "ABC Company", "ice_capability": True, "monthly_rental_fee": 50000, "contract_period": 12, "size" : 100},
    {"id": 2, "name": "PureFlow", "manufacturer": "ABC Company", "ice_capability": False, "monthly_rental_fee": 45000, "contract_period": 24, "size" : 80},
    {"id": 3, "name": "CrystalClear", "manufacturer": "ABC Company", "ice_capability": True, "monthly_rental_fee": 55000, "contract_period": 18, "size" : 90},
    {"id": 4, "name": "AquaSafe", "manufacturer": "LMN Industries", "ice_capability": True, "monthly_rental_fee": 48000, "contract_period": 12, "size" : 120},
    {"id": 5, "name": "PureTaste", "manufacturer": "LMN Industries", "ice_capability": False, "monthly_rental_fee": 52000, "contract_period": 24, "size" : 140}
]

# 정수기 렌탈 상품 조회 API
@app.get("/water_purifiers")
async def get_water_purifiers(
    name: str = Query(default=None),
    manufacturer: str = Query(default=None),
    ice_capability: bool = Query(default=None),
    min_rental_fee: int = Query(default=None, ge=0),
    max_contract_period: int = Query(default=None, ge=0)
):
    filtered_purifiers = water_purifiers

    if name is not None:
        # 이름 필터링
        filtered_purifiers = [purifier for purifier in filtered_purifiers if name.lower() in purifier['name'].lower()]

    if manufacturer is not None:
        # 제조사 필터링
        filtered_purifiers = [purifier for purifier in filtered_purifiers if manufacturer.lower() == purifier['manufacturer'].lower()]

    if ice_capability is not None:
        # 얼음 기능 필터링
        filtered_purifiers = [purifier for purifier in filtered_purifiers if ice_capability == purifier['ice_capability']]

    if min_rental_fee is not None:
        # 최소 월렌탈료 필터링
        filtered_purifiers = [purifier for purifier in filtered_purifiers if purifier['monthly_rental_fee'] >= min_rental_fee]

    if max_contract_period is not None:
        # 최대 약정기간 필터링
        filtered_purifiers = [purifier for purifier in filtered_purifiers if purifier['contract_period'] <= max_contract_period]

    return filtered_purifiers

# 여행지 정보 데이터
destinations = [
    {"id": 1, "name": "Paris", "country": "France", "continent": "Europe", "attractions": ["Eiffel Tower", "Louvre Museum"], "description": "Beautiful city known for its art and culture.", "expense":100},
    {"id": 2, "name": "Bali", "country": "Indonesia", "continent": "Asia", "attractions": ["Ubud", "Tanah Lot Temple"], "description": "Tropical paradise with stunning beaches and rich cultural heritage.", "expense":90},
    {"id": 3, "name": "Cape Town", "country": "South Africa", "continent": "Africa", "attractions": ["Table Mountain", "Robben Island"], "description": "Scenic city with diverse wildlife and natural beauty.", "expense":80},
    {"id": 4, "name": "New York City", "country": "United States", "continent": "North America", "attractions": ["Statue of Liberty", "Times Square"], "description": "Vibrant metropolis known for its iconic landmarks and bustling atmosphere.", "expense":140},
    {"id": 5, "name": "Sydney", "country": "Australia", "continent": "Oceania", "attractions": ["Sydney Opera House", "Bondi Beach"], "description": "Cosmopolitan city with stunning beaches and a thriving arts scene.", "expense":120}
]

# 여행지 조회 API
@app.get("/destinations")
async def get_destinations(
    name: str = Query(default=None),
    country: str = Query(default=None),
    continent: str = Query(default=None),
    description: str = Query(default=None)
):
    filtered_destinations = destinations

    if name is not None:
        # 여행지명 필터링
        filtered_destinations = [dest for dest in filtered_destinations if name.lower() in dest['name'].lower()]

    if country is not None:
        # 국가 필터링
        filtered_destinations = [dest for dest in filtered_destinations if country.lower() == dest['country'].lower()]

    if continent is not None:
        # 대륙 필터링
        filtered_destinations = [dest for dest in filtered_destinations if continent.lower() == dest['continent'].lower()]

    if description is not None:
        # 설명 필터링
        filtered_destinations = [dest for dest in filtered_destinations if description.lower() in dest['description'].lower()]

    return filtered_destinations

bakery_products = [
    {"id": 1, "name": "Croissant", "price": 2000, "ingredients": ["Flour", "Butter", "Yeast"], "expiration_date": "2023-06-15", "calories": 200, "allergens": ["Milk", "Eggs"], "additional_options": ["Chocolate Filling", "Almond Topping"]},
    {"id": 2, "name": "Baguette", "price": 3000, "ingredients": ["Flour", "Water", "Yeast", "Salt"], "expiration_date": "2023-06-15", "calories": 150, "allergens": [], "additional_options": ["Whole Wheat", "Seeds"]},
    {"id": 3, "name": "Cupcake", "price": 1500, "ingredients": ["Flour", "Sugar", "Butter", "Eggs", "Milk"], "expiration_date": "2023-06-15", "calories": 250, "allergens": ["Milk", "Eggs", "Wheat"], "additional_options": ["Frosting", "Sprinkles"]},
    {"id": 4, "name": "Pain au Chocolat", "price": 2500, "ingredients": ["Flour", "Butter", "Yeast", "Chocolate"], "expiration_date": "2023-06-15", "calories": 300, "allergens": ["Milk", "Eggs", "Soy"], "additional_options": []},
    {"id": 5, "name": "Muffin", "price": 1800, "ingredients": ["Flour", "Sugar", "Butter", "Eggs", "Milk"], "expiration_date": "2023-06-15", "calories": 220, "allergens": ["Milk", "Eggs", "Wheat"], "additional_options": ["Blueberry", "Chocolate Chip"]},
]

@app.get("/bakery_products")
async def filter_bakery_products(
    name: str = Query(default=None),
    max_price: int = Query(default=None, ge=0),
    ingredients: str = Query(default=None),
    expiration_date: str = Query(default=None),
    allergens: str = Query(default=None)
):
    filtered_products = bakery_products

    if name is not None:
        filtered_products = [product for product in filtered_products if name.lower() in product['name'].lower()]

    if max_price is not None:
        filtered_products = [product for product in filtered_products if product['price'] <= max_price]

    if ingredients is not None:
        filtered_products = [product for product in filtered_products if ingredients.lower() in [ingredient.lower() for ingredient in product['ingredients']]]

    if expiration_date is not None:
        filtered_products = [product for product in filtered_products if expiration_date == product['expiration_date']]

    if allergens is not None:
        filtered_products = [product for product in filtered_products if allergens.lower() in [allergen.lower() for allergen in product['allergens']]]

    return filtered_products

piano_products = [
    {"id": 1, "name": "Yamaha U1 Acoustic Piano", "brand": "Yamaha", "price": 5000, "keys": 88, "user_level": "Intermediate", "material": "Wood", "color": "Black", "additional_features": ["Soft-Close Fallboard", "Practice Pedal"]},
    {"id": 2, "name": "Steinway Model D Grand Piano", "brand": "Yamaha", "price": 10000, "keys": 88, "user_level": "Professional", "material": "Wood", "color": "Ebony", "additional_features": ["Sostenuto Pedal", "Adjustable Bench"]},
    {"id": 3, "name": "Kawai KDP110 Digital Piano", "brand": "Roland", "price": 2000, "keys": 88, "user_level": "Beginner", "material": "Wood", "color": "Rosewood", "additional_features": ["Bluetooth Connectivity", "Built-in Metronome"]},
    {"id": 4, "name": "Casio PX-S3000 Privia Digital Piano", "brand": "Casio", "price": 1500, "keys": 88, "user_level": "Intermediate", "material": "Plastic", "color": "White", "additional_features": ["Weighted Keys", "Built-in Speakers"]},
    {"id": 5, "name": "Roland RD-2000 Stage Piano", "brand": "Roland", "price": 3000, "keys": 88, "user_level": "Professional", "material": "Wood", "color": "Red", "additional_features": ["MIDI Connectivity", "Dual Sound Engines"]},
]

@app.get("/piano_products")
async def filter_piano_products(
    name: str = Query(default=None),
    brand: str = Query(default=None),
    max_price: int = Query(default=None, ge=0),
    min_keys: int = Query(default=None, ge=0),
    max_keys: int = Query(default=None, ge=0),
    color: str = Query(default=None)
):
    filtered_products = piano_products

    if name is not None:
        filtered_products = [product for product in filtered_products if name.lower() in product['name'].lower()]

    if brand is not None:
        filtered_products = [product for product in filtered_products if brand.lower() == product['brand'].lower()]

    if max_price is not None:
        filtered_products = [product for product in filtered_products if product['price'] <= max_price]

    if min_keys is not None:
        filtered_products = [product for product in filtered_products if product['keys'] >= min_keys]

    if max_keys is not None:
        filtered_products = [product for product in filtered_products if product['keys'] <= max_keys]

    if color is not None:
        filtered_products = [product for product in filtered_products if color.lower() == product['color'].lower()]

    return filtered_products

sandwich_menu = [
    {"id": 1, "name": "BLT Sandwich", "price": 8000, "ingredients": ["Bacon", "Lettuce", "Tomato", "Mayonnaise"], "allergens": ["tomato"], "calories": 450, "weight":500},
    {"id": 2, "name": "Turkey Club Sandwich", "price": 9000, "ingredients": ["Turkey", "Bacon", "Lettuce", "Tomato", "Mayonnaise"], "allergens": ["tomato"], "calories": 520, "weight":500},
    {"id": 3, "name": "Veggie Delight Sandwich", "price": 7500, "ingredients": ["Lettuce", "Tomato", "Cucumber", "Onion", "Avocado", "Mayonnaise"], "allergens": ["tomato"], "calories": 380, "weight":500},
    {"id": 4, "name": "Chicken Caesar Wrap", "price": 8500, "ingredients": ["Grilled Chicken", "Romaine Lettuce", "Parmesan Cheese", "Caesar Dressing"], "allergens": ["Gluten"], "calories": 420, "weight":500},
    {"id": 5, "name": "Tuna Salad Sandwich", "price": 7500, "ingredients": ["Tuna", "Mayonnaise", "Celery", "Onion", "Lettuce", "Tomato"], "allergens": ["tomato"], "calories": 320, "weight":500},
    {"id": 6, "name": "Ham and Cheese Croissant", "price": 8500, "ingredients": ["Ham", "Cheese", "Croissant"], "allergens": ["Gluten", "Dairy"], "calories": 400, "weight":500},
]

@app.get("/sandwich_menu")
async def filter_sandwich_menu(
    name: str = Query(default=None),
    max_price: int = Query(default=None, ge=0),
    include_ingredients: str = Query(default=None),
    include_allergens: str = Query(default=None),
    min_calories: int = Query(default=None, ge=0)
):
    filtered_menu = sandwich_menu

    if name is not None:
        filtered_menu = [menu for menu in filtered_menu if name.lower() in menu['name'].lower()]

    if max_price is not None:
        filtered_menu = [menu for menu in filtered_menu if menu['price'] <= max_price]

    if include_ingredients is not None:
        include_ingredients_list = include_ingredients.split(",")
        filtered_menu = [menu for menu in filtered_menu if any(ingredient.lower() in menu['ingredients'] for ingredient in include_ingredients_list)]

    if include_allergens is not None:
        include_allergens_list = include_allergens.split(",")
        filtered_menu = [menu for menu in filtered_menu if any(allergen.lower() in menu['allergens'] for allergen in include_allergens_list)]

    if min_calories is not None:
        filtered_menu = [menu for menu in filtered_menu if menu['calories'] >= min_calories]

    return filtered_menu

used_cars = [
    {"id": 1, "manufacturer": "Hyundai", "model": "Sonata", "year": 2018, "price": 15000, "mileage": 50000, "fuel_type": "Gasoline", "transmission": "Automatic"},
    {"id": 2, "manufacturer": "Toyota", "model": "Camry", "year": 2017, "price": 18000, "mileage": 60000, "fuel_type": "Gasoline", "transmission": "Automatic"},
    {"id": 3, "manufacturer": "Hyundai", "model": "Civic", "year": 2016, "price": 12000, "mileage": 40000, "fuel_type": "Gasoline", "transmission": "Manual"},
    {"id": 4, "manufacturer": "Toyota", "model": "Focus", "year": 2015, "price": 10000, "mileage": 70000, "fuel_type": "Gasoline", "transmission": "Automatic"},
    {"id": 5, "manufacturer": "Hyundai", "model": "Cruze", "year": 2017, "price": 14000, "mileage": 55000, "fuel_type": "Gasoline", "transmission": "Automatic"},
    {"id": 6, "manufacturer": "Toyota", "model": "Altima", "year": 2019, "price": 20000, "mileage": 30000, "fuel_type": "Gasoline", "transmission": "Automatic"},
]

@app.get("/used_cars")
async def filter_used_cars(
    manufacturer: str = Query(default=None),
    model: str = Query(default=None),
    min_year: int = Query(default=None, ge=0),
    max_price: int = Query(default=None, ge=0),
    min_mileage: int = Query(default=None, ge=0)
):
    filtered_used_cars = used_cars

    if manufacturer is not None:
        filtered_used_cars = [car for car in filtered_used_cars if manufacturer.lower() in car['manufacturer'].lower()]

    if model is not None:
        filtered_used_cars = [car for car in filtered_used_cars if model.lower() in car['model'].lower()]

    if min_year is not None:
        filtered_used_cars = [car for car in filtered_used_cars if car['year'] >= min_year]

    if max_price is not None:
        filtered_used_cars = [car for car in filtered_used_cars if car['price'] <= max_price]

    if min_mileage is not None:
        filtered_used_cars = [car for car in filtered_used_cars if car['mileage'] >= min_mileage]

    return filtered_used_cars

laptops = [
    {"id": 1, "product_name": "Dell XPS 13", "brand": "Dell", "price": 1599, "cpu": "Intel Core i7", "ram": 16, "storage": 512, "graphics": "Intel Iris Xe"},
    {"id": 2, "product_name": "MacBook Pro", "brand": "Apple", "price": 1999, "cpu": "Apple M1", "ram": 16, "storage": 512, "graphics": "Apple M1"},
    {"id": 3, "product_name": "HP Spectre x360", "brand": "HP", "price": 1399, "cpu": "Intel Core i5", "ram": 8, "storage": 256, "graphics": "Intel Iris Xe"},
    {"id": 4, "product_name": "Lenovo ThinkPad X1 Carbon", "brand": "Lenovo", "price": 1699, "cpu": "Intel Core i7", "ram": 16, "storage": 1, "graphics": "Intel Iris Xe"},
    {"id": 5, "product_name": "ASUS ROG Zephyrus G14", "brand": "ASUS", "price": 1499, "cpu": "AMD Ryzen 9", "ram": 16, "storage": 1, "graphics": "NVIDIA GeForce RTX 3060"},
    {"id": 6, "product_name": "Acer Swift 3", "brand": "Acer", "price": 899, "cpu": "AMD Ryzen 5", "ram": 8, "storage": 512, "graphics": "AMD Radeon Graphics"},
]

@app.get("/laptops")
async def filter_laptops(
    product_name: str = Query(default=None),
    brand: str = Query(default=None),
    max_price: int = Query(default=None, ge=0),
    min_ram: int = Query(default=None, ge=0),
    min_storage: int = Query(default=None, ge=0)
):
    filtered_laptops = laptops

    if product_name is not None:
        filtered_laptops = [laptop for laptop in filtered_laptops if product_name.lower() in laptop['product_name'].lower()]

    if brand is not None:
        filtered_laptops = [laptop for laptop in filtered_laptops if brand.lower() == laptop['brand'].lower()]

    if max_price is not None:
        filtered_laptops = [laptop for laptop in filtered_laptops if laptop['price'] <= max_price]

    if min_ram is not None:
        filtered_laptops = [laptop for laptop in filtered_laptops if laptop['ram'] >= min_ram]

    if min_storage is not None:
        filtered_laptops = [laptop for laptop in filtered_laptops if laptop['storage'] >= min_storage]

    return filtered_laptops
