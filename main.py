from fastapi import FastAPI, Query
from typing import List, Optional
from pydantic import BaseModel

app = FastAPI()

###########
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
#########

@app.get("/mobile_app")
def filter_mobile_application(
    min_ranking: Optional[int] = Query(None, ge=1),
    max_ranking: Optional[int] = Query(None, ge=1),
    name: Optional[str] = Query(None),
    category: Optional[str] = Query(None),
    min_rating: Optional[float] = Query(None, ge=0, le=5),
    max_rating: Optional[float] = Query(None, ge=0, le=5),
    pub: Optional[str] = Query(None)
):
    filtered_apps = []
    # 여기서는 주어진 데이터를 리스트 형태로 정의했습니다.
    data = [
        [1, "NH올원뱅크", "금융", "당신을 위한 모든 금융이 한 곳에! 농협은행 모바일 뱅크. NH올원뱅크를 만나 보세요!", 3.7, "NH농협은행"],
        [2, "시티즌코난", "도구", "일선 경찰관을 위한 보이스피싱 악성 앱 순간 탐지기(구 피싱아이즈 폴리스)로서 *피싱아이즈*와 함께 운영되고 있습니다.", 4.2, "(주)인피니그루"],
        [3, "KB Pay", "금융", "KB Pay 모든 금융을 한번에, 한손에, 한눈에 담다", 4.2, "KB국민카드"],
        [4, "쿠팡플레이", "엔터테인먼트", "쿠팡플레이로 쿠팡 와우 멤버십에 시청의 즐거움을 더했어요.", 3.6, "Coupang Corp."],
        [5, "AliExpress", "쇼핑", "해외직구는 알리익스프레스!", 4.5, "Alibaba Mobile"],
        [6, "Nike", "쇼핑", "최신 운둥화와 남성 여성 키즈 의류부터 앱 전용 제품과 멤버 혜택, 운동 콘텐츠까지. 당신만을 위한 특별한 나이키를 앱에서 만나보세요.", 4.3, "Nike, Inc."],
        [7, "네이버 파파고", "도구", "똑똑한 AI 통변역기, 언어 장벽 없이 대화하는 세상을 꿈꿉니다.", 4.7, "NAVER Corp."]
    ]

    for app_data in data:
        ranking, app_name, app_category, desc, rating, app_pub = app_data
        if (
            (min_ranking is None or ranking >= min_ranking) and
            (max_ranking is None or ranking <= max_ranking) and
            (name is None or app_name.lower() == name.lower()) and
            (category is None or app_category.lower() == category.lower()) and
            (min_rating is None or rating >= min_rating) and
            (max_rating is None or rating <= max_rating) and
            (pub is None or app_pub.lower() == pub.lower())
        ):
            filtered_apps.append({
                "ranking": ranking,
                "name": app_name,
                "category": app_category,
                "desc": desc,
                "rating": rating,
                "pub": app_pub
            })

    return filtered_apps


@app.get("/credit_card")
def recommend_credit_card(
    name: Optional[str] = Query(None),
    company: Optional[str] = Query(None),
    min_annual_fee: Optional[int] = Query(None, ge=0),
    max_annual_fee: Optional[int] = Query(None, ge=0),
    min_previous: Optional[int] = Query(None, ge=0),
    max_previous: Optional[int] = Query(None, ge=0),
    card_type: Optional[str] = Query(None)
):
    filtered_cards = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["KB국민 마이위시카드", "KB국민카드", 15000, 400000, "할인"],
        ["LOCA 365 카드", "롯데카드", 20000, 500000, "할인"],
        ["신한카드 Deep Dream", "신한카드", 8000, 0, "포인트"],
        ["현대카드 M BOOST", "현대카드", 30000, 500000, "포인트"],
        ["신한카드 The CLASSIC+", "신한카드", 120000, 300000, "마일리지"],
        ["대한항공카드 030", "현대카드", 30000, 0, "마일리지"]
    ]

    for card_data in data:
        card_name, card_company, annual_fee, previous, card_type = card_data
        if (
            (name is None or card_name.lower() == name.lower()) and
            (company is None or card_company.lower() == company.lower()) and
            (min_annual_fee is None or annual_fee >= min_annual_fee) and
            (max_annual_fee is None or annual_fee <= max_annual_fee) and
            (min_previous is None or previous >= min_previous) and
            (max_previous is None or previous <= max_previous) and
            (card_type is None or card_type.lower() == card_type.lower())
        ):
            filtered_cards.append({
                "name": card_name,
                "company": card_company,
                "annual_fee": annual_fee,
                "previous": previous,
                "type": card_type
            })

    return filtered_cards

@app.get("/payable_merchant")
def filter_payable_merchant(
    sgngNm: str = Query(..., description="시군명"),
    category: Optional[str] = Query(None, description="업종"),
    name: Optional[str] = Query(None, description="매장명"),
    address: Optional[str] = Query(None, description="주소"),
    phone: Optional[str] = Query(None, description="전화번호"),
):
    filtered_merchants = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["용인시", "음료식품", "(주)뉴욕치즈케익팩토리", "경기 성남시 수정구 성남대로 1330", "031-602-0088"],
        ["용인시", "음료식품", "1253타르트", "경기 용인시 수지구 문인로54번길 3-6", "031-1111-1111"],
        ["용인시", "서적문구", "꿈꾸는마을", "경기 용인시 기흥구 서천동로43번길 9-11", "070-4645-1613"],
        ["하남시", "음료식품", "8월의홍시", "경기 하남시 조정대로 85", "031-792-8899"],
        ["과천시", "학원", "가우디미술학원", "경기 과천시 새술막길 10-13", "02-502-3222"]
    ]

    for merchant_data in data:
        merchant_sgngNm, merchant_category, merchant_name, merchant_address, merchant_phone = merchant_data
        if (
            sgngNm.lower() == merchant_sgngNm.lower() and
            (category is None or category.lower() == merchant_category.lower()) and
            (name is None or name.lower() == merchant_name.lower()) and
            (address is None or address.lower() == merchant_address.lower()) and
            (phone is None or phone.lower() == merchant_phone.lower())
        ):
            filtered_merchants.append({
                "sgngNm": merchant_sgngNm,
                "category": merchant_category,
                "name": merchant_name,
                "address": merchant_address,
                "phone": merchant_phone
            })

    return filtered_merchants

@app.get("/traditional_market")
def filter_traditional_market(
    name: Optional[str] = Query(None, description="시장 이름"),
    businessday: Optional[str] = Query(None, description="영업일"),
    dayoff: Optional[str] = Query(None, description="휴무일"),
    keyword: Optional[str] = Query(None, description="시장 주소와 설명을 바탕으로 검색하는 키워드"),
    start_time: Optional[str] = Query(None, description="영업 시작 시간"),
    end_time: Optional[str] = Query(None, description="영업 종료 시간"),
):
    filtered_markets = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["남대문시장", "서울특별시 중구 남대문시장4길 21", "일요일", "02-753-2805", "서울을 대표하는 중심 시장으로 1,700여개 품목을 판매하는 없는 게 없는 전통시장", "09:00", "17:30"],
        ["동대문종합시장", "서울특별시 중구 종로 272", "일요일", "02-2262-0114", "원단, 의류뷰자재, 액세서리, 최신 혼수용품 도소매까지. 우리나라 최대의 의류전문시장", "08:00", "19:00"],
        ["광장시장", "서울특별시 종로구 창경궁로 88", "일요일", "02-2267-0291", "다양한 먹거리, 포목과 구제 상품 등 110년 전통으로 멋과 맛이 있는 전통시장", "09:00", "23:00"],
        ["통인시장", "서울 종로구 지하문로15길 18", "일요일", "02-722-0911", "엽전으로 사먹는 도시락카페로 국내외 관광객들에게 인기 만점인 전통시장", "07:00", "21:00"],
        ["풍물시장", "서울 동대문구 천호대로4길 21", "화요일", "02-2232-3367", "현재와 과거의 공존! 아날로그 갬성 돋는 골동품을 만날 수 있는 전통시장", "10:00", "19:00"] 
    ]
    
    for market in data:
        # 필터링 조건에 맞는 시장을 찾아서 결과에 추가
        if (name is None or name == market[0]) and \
            (businessday is None or businessday == market[2]) and \
            (dayoff is None or dayoff == market[3]) and \
            (keyword is None or keyword in market[1] or keyword in market[4]) and \
            (start_time is None or start_time == market[5]) and \
            (end_time is None or end_time == market[6]):
            
            filtered_markets.append({
                "name": market[0],
                "address": market[1],
                "dayoff": market[2],
                "phone": market[3],
                "desc": market[4],
                "start_time": market[5],
                "end_time": market[6]
            })
    
    return filtered_markets

@app.get("/fonts")
def recommend_fonts(
    name: Optional[str] = Query(None, description="글꼴 이름"),
    pub: Optional[str] = Query(None, description="제작사"),
    type: Optional[str] = Query(None, description="글꼴 타입"),
    min_font_weight: Optional[int] = Query(None, description="최소 굵기 수", gt=0),
    max_font_weight: Optional[int] = Query(None, description="최대 굵기 수", gt=0)
):
    filtered_fonts = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["나눔스퀘어", "네이버", "고딕", 4, "반듯한 직선으로 제목에 잘 어울리며 모바일에서도 잘 보이는 글꼴입니다."],
        ["나눔고딕", "네이버", "고딕", 4, "나눔고딕은 문서의 본문에도 잘 쓸 수 있는 고딕 글꼴입니다. 글자 끝의 날카로운 부분을 둥글게 처리해 친근하고 부드러운 느낌입니다."],
        ["나눔손글씨 펜", "네이버", "손글씨", 1, "나눔손글씨 펜체는 깔끔한 선 처리와 생동감이 돋보입니다."],
        ["주아체", "우아한형제들", "고딕", 1, "배달의민족 주아체는 붓으로 직접 그려서 만든 손글씨 간판을 모티브로 만들었습니다. 붓으로 그려 획의 굵기가 일정하지 않고 동글동글한 느낌을 주는 서체로 옛날 간판의 푸근함과 정겨움이 묻어나는 것이 특징입니다."],
        ["강원교육모두체", "강원도교육청X헤움디자인", "명조", 2, "강원도교육청의 공식 서체입니다."],
        ["빙그레체", "빙그레", "손글씨", 2, "빙그레체는 '건강, 행복, 미소'의 컨셉이 담긴 서체로 빙그레 '바나나맛 우유' 로고 타입에서 착안하여 현대적으로 디자인 되었습니다."]
    ]
    
    # 필터링 조건에 맞는 글꼴 찾기
    for font in data:
        if (name is None or name == font[0]) and \
            (pub is None or pub == font[1]) and \
            (type is None or type == font[2]) and \
            (min_font_weight is None or font[3] >= min_font_weight) and \
            (max_font_weight is None or font[3] <= max_font_weight):
            
            filtered_fonts.append({
                "name": font[0],
                "pub": font[1],
                "type": font[2],
                "font_weight": font[3],
                "desc": font[4]
            })
    
    return filtered_fonts

@app.get("/studio_rental")
def recommend_studio(
    name: Optional[str] = Query(None, description="연습실 이름"),
    type: Optional[str] = Query(None, description="공간 유형"),
    min_rental_fee: Optional[int] = Query(None, description="최소 시간당 대관료", gt=0),
    max_rental_fee: Optional[int] = Query(None, description="최대 시간당 대관료", gt=0),
    min_size: Optional[int] = Query(None, description="최소 공간 면적(단위: 평)", gt=0),
    max_size: Optional[int] = Query(None, description="최대 공간 면적(단위: 평)", gt=0),
    min_people: Optional[int] = Query(None, description="최소 인원", gt=0),
    max_people: Optional[int] = Query(None, description="최대 인원", gt=0),
    address_keyword: Optional[str] = Query(None, description="주소를 바탕으로 검색하는 키워드")
):
    filtered_studios = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["뮤즈하버 음악스튜디오", "악기연습실", 30000, 16, 10, 20, "서울 양천구 오목로 77 3층 뮤즈하버 음악스튜디오", "0507-1302-4928"],
        ["엠와이스튜디오", "댄스연습실", 5000, 24, 1, 20, "서울 마포구 망원동 423-5 지하 1층", "02-123-4567"],
        ["VStudio", "보컬연습실", 12000, 5, 1, 9, "서울특별시 강동구 성내2동 145-10 지하층 B1", "02-000-1111"],
        ["SOBON", "댄스연습실", 9000, 15, 1, 10, "서울특별시 마포구 서교동 366-30 B1층 SOBON (쏘본)", "02-999-7777"],
        ["숲연습실", "악기연습실", 3000, 2, 1, 2, "서울 서초구 양재동 366-13 지하1층", "02-111-0000"]
    ]
    
    # 필터링 조건에 맞는 연습실 찾기
    for studio in data:
        if (name is None or name == studio[0]) and \
            (type is None or type == studio[1]) and \
            (min_rental_fee is None or studio[2] >= min_rental_fee) and \
            (max_rental_fee is None or studio[2] <= max_rental_fee) and \
            (min_size is None or studio[3] >= min_size) and \
            (max_size is None or studio[3] <= max_size) and \
            (min_people is None or studio[4] >= min_people) and \
            (max_people is None or studio[5] <= max_people) and \
            (address_keyword is None or address_keyword in studio[6]):
            
            filtered_studios.append({
                "name": studio[0],
                "type": studio[1],
                "rentalFee": studio[2],
                "size": studio[3],
                "min_people": studio[4],
                "max_people": studio[5],
                "address": studio[6],
                "phone": studio[7]
            })
    
    return filtered_studios

@app.get("/subway_station")
def search_subway_station(
    name: Optional[str] = Query(None, description="역 이름"),
    line: Optional[str] = Query(None, description="호선"),
    address: Optional[str] = Query(None, description="주소를 바탕으로 검색하는 키워드"),
    phone: Optional[str] = Query(None, description="대표번호"),
    lostproperty_phone: Optional[str] = Query(None, description="유실물센터 번호"),
    restroom: Optional[str] = Query(None, description="화장실 위치")
):
    filtered_stations = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["광교", "신분당", "경기도 수원시 영통구 대학로 55", "031-8018-7830", "031-8018-7777", "개찰구 밖"],
        ["죽전", "수인분당", "경기도 용인시 수지구 포은대로 530", "031-896-9791", "1544-7788", "개찰구 밖"],
        ["압구정", "3", "서울특별시 강남구 압구정로 지하 172", "02-6110-3361", "02-6110-3344", "개찰구 밖"],
        ["회현", "4", "서울특별시 중구 퇴계로 지하 54", "02-6110-4251", "02-6110-3344", "개찰구 안"],
        ["명동", "4", "서울특별시 중구 퇴계로 지하 126", "02-6110-4241", "02-6110-3344", "개찰구 안"],
        ["혜화", "4", "서울특별시 종로구 대학로 지하 120", "02-6110-4201", "02-6110-3344", "개찰구 밖"]
    ]
    
    # 필터링 조건에 맞는 지하철역 찾기
    for station in data:
        if (name is None or name == station[0]) and \
            (line is None or line == station[1]) and \
            (address is None or address in station[2]) and \
            (phone is None or phone == station[3]) and \
            (lostproperty_phone is None or lostproperty_phone == station[4]) and \
            (restroom is None or restroom == station[5]):
            
            filtered_stations.append({
                "name": station[0],
                "line": station[1],
                "address": station[2],
                "phone": station[3],
                "lostproperty_phone": station[4],
                "restroom": station[5]
            })
    
    return filtered_stations

@app.get("/apartment")
def search_apartment(
    name: Optional[str] = Query(None, description="아파트 이름"),
    min_household: Optional[int] = Query(None, description="최소 세대수", ge=0),
    max_household: Optional[int] = Query(None, description="최대 세대수", ge=0),
    min_block: Optional[int] = Query(None, description="최소 동 수", ge=0),
    max_block: Optional[int] = Query(None, description="최대 동 수", ge=0),
    company: Optional[str] = Query(None, description="건설사"),
    address: Optional[str] = Query(None, description="주소를 바탕으로 검색하는 키워드")
):
    filtered_apartments = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["과천푸르지오써밋", 1571, 32, "대우건설", "경기도 과천시 관문로 106"],
        ["과천자이", 2099, 27, "지에스건설", "경기도 과천시 별양로 110"],
        ["반포써밋", 764, 8, "대우건설", "서울시 서초구 고무래로 89"],
        ["래미안서초스위트", 392, 3, "삼성물산", "서울시 서초구 서운로 221"],
        ["두산위브트레지움", 98, 1, "두산건설", "서울시 서초구 서운로 194"],
        ["래미안슈르", 3143, 48, "삼성물산", "경기도 과천시 별양로 12"]
    ]
    
    # 필터링 조건에 맞는 아파트 찾기
    for apartment in data:
        if (name is None or name == apartment[0]) and \
            (min_household is None or apartment[1] >= min_household) and \
            (max_household is None or apartment[1] <= max_household) and \
            (min_block is None or apartment[2] >= min_block) and \
            (max_block is None or apartment[2] <= max_block) and \
            (company is None or company == apartment[3]) and \
            (address is None or address in apartment[4]):
            
            filtered_apartments.append({
                "name": apartment[0],
                "household": apartment[1],
                "block": apartment[2],
                "company": apartment[3],
                "address": apartment[4]
            })
    
    return filtered_apartments

@app.get("/golf_course")
def search_golf_course(
    name: Optional[str] = Query(None, description="골프장 이름"),
    type: Optional[str] = Query(None, description="이용구분 (ex: 퍼블릭, 회원제)"),
    min_holes: Optional[int] = Query(None, description="최소 홀 수", gt=0),
    max_holes: Optional[int] = Query(None, description="최대 홀 수", gt=0),
    address: Optional[str] = Query(None, description="주소를 바탕으로 검색하는 키워드"),
    phone: Optional[str] = Query(None, description="전화번호")
):
    filtered_golf_courses = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["써닝포인트", "회원제", 18, "경기 용인시 처인구 백암면 고안리 633-4", "031-329-0800"],
        ["아세코밸리", "회원제", 9, "경기 시흥시 마전로 307", "031-488-8000"],
        ["파가니카", "회원제", 18, "강원 춘천시 남면 소주고개로 145-10", "033-261-6556"],
        ["아난티클럽 서울", "퍼블릭", 27, "경기도 가평군 설악면 유명로 961-34", "031-589-3000"],
        ["오크밸리", "퍼블릭", 9, "강원도 원주시 지정면 월송리 1016", "1588-7676"],
        ["비발디파크cc", "퍼블릭", 9, "강원도 홍천군 서면 한치골길 262", "1588-4888"]
    ]
    
    # 필터링 조건에 맞는 골프장 찾기
    for golf_course in data:
        if (name is None or name == golf_course[0]) and \
            (type is None or type == golf_course[1]) and \
            (min_holes is None or golf_course[2] >= min_holes) and \
            (max_holes is None or golf_course[2] <= max_holes) and \
            (address is None or address in golf_course[3]) and \
            (phone is None or phone == golf_course[4]):
            
            filtered_golf_courses.append({
                "name": golf_course[0],
                "type": golf_course[1],
                "holes": golf_course[2],
                "address": golf_course[3],
                "phone": golf_course[4]
            })
    
    return filtered_golf_courses

@app.get("/michelin_guide")
def filter_michelin_guide(
    name: Optional[str] = Query(None, description="식당 이름"),
    category: Optional[str] = Query(None, description="카테고리"),
    grade: Optional[str] = Query(None, description="등급"),
    country: Optional[str] = Query(None, description="위치 국가"),
    address: Optional[str] = Query(None, description="주소")
):
    filtered_restaurants = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["Waterside Inn", "전통 프랑스 요리", "3스타", "Ferry Road, Bray, SL6 2AT", "영국"],
        ["Benu", "아시안", "3스타", "22 Hawthorne St., San Francisco, 94105", "미국"],
        ["가온", "한식", "3스타", "강남구 도산대로 317, 호림아트센터 M층, Seoul", "대한민국"],
        ["권숙수", "한식", "2스타", "강남구 압구정로 80길 37, 4층, Seoul", "대한민국"],
        ["Californios", "멕시칸", "2스타", "355 11th St., San Francisco, 94103", "미국"],
        ["비채나", "한식", "1스타", "송파구 올림픽로 300, 롯데월드 타워 81층, Seoul", "대한민국"]
    ]
    
    # 필터링 조건에 맞는 미쉐린 가이드 레스토랑 찾기
    for restaurant in data:
        if (name is None or name == restaurant[0]) and \
            (category is None or category == restaurant[1]) and \
            (grade is None or grade == restaurant[2]) and \
            (country is None or country == restaurant[4]) and \
            (address is None or address in restaurant[3]):
            
            filtered_restaurants.append({
                "name": restaurant[0],
                "category": restaurant[1],
                "grade": restaurant[2],
                "address": restaurant[3],
                "country": restaurant[4]
            })
    
    return filtered_restaurants

@app.get("/bundang_restroom")
def search_bundang_restroom(
    name: Optional[str] = Query(None, description="시설물 이름"),
    address: Optional[str] = Query(None, description="주소를 바탕으로 검색하는 키워드"),
    floor: Optional[int] = Query(None, description="층수"),
    start_time: Optional[str] = Query(None, description="운영 시작 시간 (ex: 06:00)"),
    end_time: Optional[str] = Query(None, description="운영 종료 시간 (ex: 23:00)"),
    phone: Optional[str] = Query(None, description="전화번호"),
    hand_dryer: Optional[str] = Query(None, description="손 건조기 유무")
):
    filtered_restrooms = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["아미고타워", "야탑로81번길 10 (야탑동)", 1, "00:00", "24:00", "622-0112", "무"],
        ["유스페이스", "대왕판교로 660 (삼평동)", 1, "06:00", "24:00", "628-6114", "유"],
        ["하나프라자", "느티로 27 (정자동)", 1, "00:00", "24:00", "719-0933", "유"],
        ["월드비터빌딩", "정자로13(정자동)", 1, "00:00", "24:00", "010-5422-7276", "무"],
        ["판교KCC웰츠타워B동", "분당내곡로155(삼평동)", 1, "00:00", "24:00", "604-1631", "유"],
        ["다운타운빌딩", "백현로 97 (수내동)", 1, "00:00", "24:00", "714-7542", "유"]
    ]
    
    # 개방화장실 검색 조건에 맞는 화장실 찾기
    for restroom in data:
        if (name is None or name == restroom[0]) and \
            (address is None or address in restroom[1]) and \
            (floor is None or floor == restroom[2]) and \
            (start_time is None or start_time == restroom[3]) and \
            (end_time is None or end_time == restroom[4]) and \
            (phone is None or phone == restroom[5]) and \
            (hand_dryer is None or hand_dryer == restroom[6]):
            
            filtered_restrooms.append({
                "name": restroom[0],
                "address": restroom[1],
                "floor": restroom[2],
                "start_time": restroom[3],
                "end_time": restroom[4],
                "phone": restroom[5],
                "hand_dryer": restroom[6]
            })
    
    return filtered_restrooms

@app.get("/ev_charging")
def search_ev_charging(
    name: Optional[str] = Query(None, description="충전소 이름"),
    address: Optional[str] = Query(None, description="주소를 바탕으로 검색하는 키워드"),
    min_charger: Optional[int] = Query(None, gt=0, description="최소 충전기수"),
    max_charger: Optional[int] = Query(None, gt=0, description="최대 충전기수"),
    speed: Optional[str] = Query(None, description="충전 속도 (ex: 급속, 완속)"),
    parking_fee: Optional[str] = Query(None, description="주차비 (ex: 무료, 유료)")
):
    filtered_charging_stations = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["광진문화예술회관", "서울특별시 광진구 능동로 76", 2, "급속", "유료"],
        ["송도체육센터", "인천광역시 연수구 송도과학로51번길 80", 1, "급속", "무료"],
        ["광진우체국", "서울특별시 광진구 강변역로 2", 10, "완속", "유료"],
        ["서울시 광진구 자양문화체육센터", "서울특별시 광진구 뚝섬로52길 66", 2, "급속", "무료"],
        ["KBS 별관 주차장", "서울특별시 영등포구 여의대방로 359", 4, "급속", "무료"],
        ["여의도국민일보빌딩", "서울특별시 영등포구 여의공원로 101 (여의도동, 국민일보빌딩)", 6, "완속", "유료"]
    ]
    
    # 전기차 충전소 검색 조건에 맞는 충전소 찾기
    for charging_station in data:
        if (name is None or name == charging_station[0]) and \
            (address is None or address in charging_station[1]) and \
            (min_charger is None or charging_station[2] >= min_charger) and \
            (max_charger is None or charging_station[2] <= max_charger) and \
            (speed is None or speed == charging_station[3]) and \
            (parking_fee is None or parking_fee == charging_station[4]):
            
            filtered_charging_stations.append({
                "name": charging_station[0],
                "address": charging_station[1],
                "charger": charging_station[2],
                "speed": charging_station[3],
                "parking_fee": charging_station[4]
            })
    
    return filtered_charging_stations

@app.get("/steam_game")
def search_steam_game(
    name: Optional[str] = Query(None, description="게임 이름"),
    genre: Optional[str] = Query(None, description="장르"),
    min_price: Optional[int] = Query(None, gt=0, description="최소 가격"),
    max_price: Optional[int] = Query(None, gt=0, description="최대 가격"),
    age: Optional[str] = Query(None, description="이용 연령"),
    keyword: Optional[str] = Query(None, description="설명을 바탕으로 검색하는 키워드")
):
    filtered_games = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        {
            "name": "PUBG: BATTLEGROUNDS",
            "genre": "FPS",
            "price": 0,
            "age": "청소년이용불가",
            "desc": "다양한 전장에서 전략적 위치를 선점하고 무기와 장비를 확보해 최후의 1인이 되기 위한 생존의 사투를 펼칩니다. 친구들과 함께 팀을 만들어 배틀로얄 건플레이 장르의 선구자인 PUBG: BATTLEGROUNDS만이 선사하는 긴장감 넘치는 경험을 위해 도전하세요."
        },
        {
            "name": "콜 오브 듀티: 모던 워페어 2",
            "genre": "FPS",
            "price": 84500,
            "age": "청소년이용불가",
            "desc": "콜 오브 듀티®: 모던 워페어 II 2022는 세계를 무대로 펼쳐지는 전례 없는 규모의 분쟁으로 플레이어를 인도합니다. 또한, 상징적인 태스크 포스 141의 오퍼레이터가 귀환합니다. 소규모 고위험 침투 전술 작전부터 고도의 기밀 임무까지, 친구와 함께 몰입도가 높은 플레이를 경험할 수 있습니다."
        },
        {
            "name": "데이브 더 다이버",
            "genre": "어드벤처",
            "price": 24000,
            "age": "12세이용가",
            "desc": "수많은 어종과 거대 생물이 가득한 아름다운 바닷속 언제 어디서 나타날 지 모르는 해양 생물들이 궁금하지 않으신가요? 위협적인 생물의 습격을 피해 싱싱한 식재료를 획득하세요. 환상적인 해양 생태계와 신비한 고대 유물. 바닷속은 수수께끼로 가득합니다."
        },
        {
            "name": "Stardew Valley",
            "genre": "인디",
            "price": 16000,
            "age": "12세이용가",
            "desc": "Stardew Valley is an open-ended country-life RPG!"
        },
        {
            "name": "좋은 피자, 위대한 피자",
            "genre": "시뮬레이션",
            "price": 11000,
            "age": "전체이용가",
            "desc": "피자 가게 하나를 운영하는게 어떤 느낌인지 궁금하세요? 저희 새로운 게임 좋은 피자, 위대한 피자로 체험해보세요! 고객님들의 수요를 만족시키고, 충분한 운영 자금도 지속하세요. 새로운 토핑과 시설들을 업그레이드 하셔서 라이벌 알리칸테와 경쟁하세요!"
        },
        {
            "name": "Football Manager 2023",
            "genre": "시뮬레이션",
            "price": 59000,
            "age": "전체이용가",
            "desc": "Football Manager 2023 헤드라인을 장식하고, 팬의 사랑을 얻어내고, 경쟁을 장악하여 엘리트 감독 대열에 합류하세요"
        }
    ]

    for game in data:
        if name and name.lower() not in game["name"].lower():
            continue
        if genre and genre.lower() not in game["genre"].lower():
            continue
        if min_price is not None and game["price"] < min_price:
            continue
        if max_price is not None and game["price"] > max_price:
            continue
        if age and age.lower() not in game["age"].lower():
            continue
        if keyword and keyword.lower() not in game["desc"].lower():
            continue
        filtered_games.append(game)

    return filtered_games

students = [
    {
        "id": "1828010",
        "name": "홍길동",
        "major": "수학과",
        "grade": 2,
        "age": 27,
        "gender": "M",
        "credit": 65
    },
    {
        "id": "2323006",
        "name": "박서준",
        "major": "통계학과",
        "grade": 1,
        "age": 27,
        "gender": "M",
        "credit": 15
    },
    {
        "id": "2227008",
        "name": "이지은",
        "major": "전자공학과",
        "grade": 2,
        "age": 27,
        "gender": "F",
        "credit": 90
    },
    {
        "id": "2085009",
        "name": "서강준",
        "major": "수학과",
        "grade": 4,
        "age": 29,
        "gender": "M",
        "credit": 120
    },
    {
        "id": "1528008",
        "name": "이태민",
        "major": "국어국문",
        "grade": 4,
        "age": 27,
        "gender": "M",
        "credit": 110
    }
]

@app.get("/student")
def search_student(
    id: Optional[str] = Query(None, description="학번"),
    name: Optional[str] = Query(None, description="이름"),
    major: Optional[str] = Query(None, description="학과"),
    grade: Optional[int] = Query(None, ge=1, le=8, description="학년"),
    age: Optional[int] = Query(None, description="나이"),
    sex: Optional[str] = Query(None, description="성별"),
    credit: Optional[int] = Query(None, description="수강학점")
):
    filtered_students = []

    for student in students:
        if id and id != student["id"]:
            continue
        if name and name != student["name"]:
            continue
        if major and major != student["major"]:
            continue
        if grade is not None and grade != student["grade"]:
            continue
        if age is not None and age != student["age"]:
            continue
        if sex and sex != student["gender"]:
            continue
        if credit is not None and credit != student["credit"]:
            continue
        filtered_students.append(student)

    return filtered_students

# 야구 경기 일정 데이터 리스트
baseball_plays = [
    {
        "match_schedule": "20230608",
        "team": "한화이글스",
        "location": "수원",
        "ticket_price": 15000,
        "seat": 50
    },
    {
        "match_schedule": "20230509",
        "team": "LG트윈스",
        "location": "사직",
        "ticket_price": 18000,
        "seat": 45
    },
    {
        "match_schedule": "20230422",
        "team": "KT",
        "location": "수원",
        "ticket_price": 18000,
        "seat": 70
    },
    {
        "match_schedule": "20230609",
        "team": "삼성라이온즈",
        "location": "잠실",
        "ticket_price": 19000,
        "seat": 80
    },
    {
        "match_schedule": "20230531",
        "team": "키움",
        "location": "고척",
        "ticket_price": 21000,
        "seat": 150
    }
]

@app.get("/baseball_play")
def search_baseball_play(
    match_schedule: Optional[str] = Query(None, description="경기날짜"),
    team: str = Query(..., description="경기 팀"),
    location: Optional[str] = Query(None, description="경기 지역"),
    ticket_price: Optional[int] = Query(None, ge=1, le=100000, description="표 가격"),
    seat: Optional[int] = Query(None, description="예매 가능 좌석")
):
    filtered_plays = []

    for play in baseball_plays:
        if match_schedule and match_schedule != play["match_schedule"]:
            continue
        if team != play["team"]:
            continue
        if location and location != play["location"]:
            continue
        if ticket_price is not None and ticket_price != play["ticket_price"]:
            continue
        if seat is not None and seat != play["seat"]:
            continue
        filtered_plays.append(play)

    return filtered_plays

# 도서관 책 데이터 리스트
library_books = [
    {
        "library": "대추골 도서관",
        "book_name": "미분적분학",
        "author": "고응일",
        "publisher": "미래출판사",
        "plot": "대학 수학 기초인 미분적분학의 이해를 돕기 위한 책으로 예제와 연습문제로 구성되어 있습니다."
    },
    {
        "library": "이화여대 중앙도서관",
        "book_name": "회귀분석",
        "author": "유재근",
        "publisher": "미래출판사",
        "plot": "대학 수학 기초인 미분적분학의 이해를 돕기 위한 책으로 예제와 연습문제로 구성되어 있습니다."
    },
    {
        "library": "국립중앙도서관",
        "book_name": "시어머니 유품정리",
        "author": "가키야 미우",
        "publisher": "문예춘추사",
        "plot": "시어머니의 유품을 정리하기 위해 시어머니 집을 청소하는 며니리의 이야기입니다."
    },
    {
        "library": "서울 도서관",
        "book_name": "소나기",
        "author": "황순원",
        "publisher": "맑은소리",
        "plot": "김유정의 소설로 사춘기 소년과 소녀에게 소나기처럼 찾아 온 아름다운 첫사랑의 내용을 서정적으로 그린 작품입니다."
    },
    {
        "library": "고려대 도서관",
        "book_name": "김유정 전집",
        "author": "김유정",
        "publisher": "강",
        "plot": "김유정 작가 소설의 작품 모음집입니다. 소낙비, 가을 등 소설 31개와 길 등 수필 12집으로 구성되어 있습니다."
    }
]

@app.get("/library")
def search_library_book(
    library: str = Query(..., description="도서관명"),
    book_name: Optional[str] = Query(None, description="책이름"),
    author: Optional[str] = Query(None, description="저자명"),
    publisher: Optional[str] = Query(None, description="출판사"),
    document_no: Optional[str] = Query(None, description="문헌번호")
):
    filtered_books = []

    for book in library_books:
        if library != book["library"]:
            continue
        if book_name and book_name != book["book_name"]:
            continue
        if author and author != book["author"]:
            continue
        if publisher and publisher != book["publisher"]:
            continue
        if document_no and document_no != book["document_no"]:
            continue
        filtered_books.append(book)

    return filtered_books

# 떡볶이 메뉴 데이터 리스트
tteokbokki_menu = [
    {
        "menu": "기름떡볶이",
        "price": 9000,
        "calories": 1100,
        "min_spicy": 2,
        "max_spicy": 4.5,
        "rating": 4
    },
    {
        "menu": "간장궁중떡볶이",
        "price": 5000,
        "calories": 900,
        "min_spicy": 1,
        "max_spicy": 4,
        "rating": 4
    },
    {
        "menu": "매운떡볶이",
        "price": 5000,
        "calories": 800,
        "min_spicy": 4,
        "max_spicy": 3,
        "rating": 3
    },
    {
        "menu": "크림떡볶이",
        "price": 13000,
        "calories": 900,
        "min_spicy": 1,
        "max_spicy": 4,
        "rating": 4
    },
    {
        "menu": "로제떡볶이",
        "price": 12000,
        "calories": 750,
        "min_spicy": 2,
        "max_spicy": 5,
        "rating": 5
    }
]

@app.get("/tteokbokki")
def search_tteokbokki_menu(
    menu: str = Query(..., description="메뉴명"),
    price: Optional[int] = Query(None, description="가격"),
    calories: Optional[int] = Query(None, description="칼로리"),
    min_spicy: Optional[int] = Query(None, description="최소 맵기", ge=0, le=5),
    max_spicy: Optional[int] = Query(None, description="최대 맵기", ge=0, le=5),
    rating: Optional[int] = Query(None, description="평점")
):
    filtered_menu = []

    for item in tteokbokki_menu:
        if menu != item["menu"]:
            continue
        if price and price != item["price"]:
            continue
        if calories and calories != item["calories"]:
            continue
        if min_spicy and min_spicy > item["min_spicy"]:
            continue
        if max_spicy and max_spicy < item["max_spicy"]:
            continue
        if rating and rating != item["rating"]:
            continue
        filtered_menu.append(item)

    return filtered_menu

# 음료 데이터 리스트
beverage_list = [
    {
        "beverage_name": "콜라",
        "price": 2000,
        "calories": 300,
        "sweetness": 4,
        "size": 350
    },
    {
        "beverage_name": "사이다",
        "price": 2000,
        "calories": 300,
        "sweetness": 4,
        "size": 350
    },
    {
        "beverage_name": "토레타",
        "price": 2500,
        "calories": 200,
        "sweetness": 3,
        "size": 500
    },
    {
        "beverage_name": "마운틴듀",
        "price": 2000,
        "calories": 300,
        "sweetness": 4,
        "size": 350
    },
    {
        "beverage_name": "웰치스",
        "price": 2000,
        "calories": 350,
        "sweetness": 4,
        "size": 350
    }
]

@app.get("/beverage")
def search_beverage(
    beverage_name: Optional[str] = Query(None, description="음료명"),
    price: Optional[int] = Query(None, description="가격"),
    calories: Optional[int] = Query(None, description="칼로리"),
    sweetness: Optional[int] = Query(None, description="단맛"),
    size: Optional[int] = Query(None, description="용량")
):
    filtered_beverage = []

    for item in beverage_list:
        if beverage_name and beverage_name != item["beverage_name"]:
            continue
        if price and price != item["price"]:
            continue
        if calories and calories != item["calories"]:
            continue
        if sweetness and sweetness != item["sweetness"]:
            continue
        if size and size != item["size"]:
            continue
        filtered_beverage.append(item)

    return filtered_beverage

# 전시 티켓 데이터 리스트
exhibition_list = [
    {
        "exhibition_name": "최지목:부재의 빚",
        "price": 0,
        "place": "챕터투",
        "exhibition_date": "20230623-20230825",
        "store": "예스24",
        "discount_rate": "0%"
    },
    {
        "exhibition_name": "CAT.ART 캣아트 고양이미술사,세계명화 이야기",
        "price": 15000,
        "place": "소피텔 앰배서더 서울호텔3층 뮤지엄209",
        "exhibition_date": "20230706-20231029",
        "store": "인터파크",
        "discount_rate": "50%"
    },
    {
        "exhibition_name": "빛의시어터 달리",
        "price": 29000,
        "place": "워커힐 호텔앤리조트",
        "exhibition_date": "20230615-20230303",
        "store": "예스24",
        "discount_rate": "30%"
    },
    {
        "exhibition_name": "에드워드 호퍼,길 위에서",
        "price": 17000,
        "place": "서울시립미술관 서소문본관",
        "exhibition_date": "20230420-20230820",
        "store": "인터파크",
        "discount_rate": "30%"
    },
    {
        "exhibition_name": "공칸 개인전,<공적이면서도 사적인(Private but Public)",
        "price": 0,
        "place": "탕 컨템포러리",
        "exhibition_date": "20230610-20230715",
        "store": "예스24",
        "discount_rate": "0%"
    }
]

@app.get("/exhibition")
def search_exhibition(
    exhibition_name: Optional[str] = Query(None, description="전시회명"),
    price: Optional[int] = Query(None, description="가격"),
    place: Optional[str] = Query(None, description="장소"),
    exhibition_date: Optional[str] = Query(None, description="전시일자"),
    store: Optional[str] = Query(None, description="판매처")
):
    filtered_exhibition = []

    for item in exhibition_list:
        if exhibition_name and exhibition_name != item["exhibition_name"]:
            continue
        if price and price != item["price"]:
            continue
        if place and place != item["place"]:
            continue
        if exhibition_date and exhibition_date != item["exhibition_date"]:
            continue
        if store and store != item["store"]:
            continue
        filtered_exhibition.append(item)

    return filtered_exhibition

# KTX 티켓 데이터 리스트
ktx_ticket_list = [
    {
        "date": "20230626",
        "departure": "서울",
        "arrival": "부산",
        "seat": "일반실",
        "price": 49500
    },
    {
        "date": "20230628",
        "departure": "서울",
        "arrival": "목포",
        "seat": "일반실",
        "price": 48500
    },
    {
        "date": "20230705",
        "departure": "수원",
        "arrival": "강릉",
        "seat": "특/우등",
        "price": 49000
    },
    {
        "date": "20230726",
        "departure": "서울",
        "arrival": "부산",
        "seat": "특/우등",
        "price": 65500
    },
    {
        "date": "20230731",
        "departure": "서울",
        "arrival": "양양",
        "seat": "일반실",
        "price": 22500
    }
]

@app.get("/ktx")
def search_ktx(
    date: Optional[str] = Query(None, description="일자"),
    departure: str = Query(..., description="출발장소"),
    arrival: str = Query(..., description="도착장소"),
    seat: Optional[str] = Query(None, description="좌석"),
    price: Optional[int] = Query(None, description="가격")
):
    filtered_tickets = []

    for ticket in ktx_ticket_list:
        if date and date != ticket["date"]:
            continue
        if departure and departure != ticket["departure"]:
            continue
        if arrival and arrival != ticket["arrival"]:
            continue
        if seat and seat != ticket["seat"]:
            continue
        if price and price != ticket["price"]:
            continue
        filtered_tickets.append(ticket)

    return filtered_tickets

# 미용실 데이터 리스트
hairshop_list = [
    {
        "shop_name": "이노헤어",
        "price": 300000,
        "hair_type": "염색",
        "region": "서울 서대문구",
        "holiday": "화-토"
    },
    {
        "shop_name": "이노헤어",
        "price": 140000,
        "hair_type": "염색",
        "region": "서울 광진구",
        "holiday": "화-토"
    },
    {
        "shop_name": "롱롱위캔드",
        "price": 35000,
        "hair_type": "커트",
        "region": "서울 서대문구",
        "holiday": "화-토"
    },
    {
        "shop_name": "박승철",
        "price": 300000,
        "hair_type": "볼륨매직",
        "region": "서울 은평구",
        "holiday": "화-일"
    },
    {
        "shop_name": "레드샵",
        "price": 200000,
        "hair_type": "영양",
        "region": "서울 서대문구",
        "holiday": "월-일"
    }
]

@app.get("/hairshop")
def search_hairshop(
    shop_name: Optional[str] = Query(None, description="미용실명"),
    price: Optional[int] = Query(None, description="가격"),
    hair_type: Optional[str] = Query(None, description="헤어종류"),
    region: Optional[str] = Query(None, description="지역"),
    holiday: Optional[str] = Query(None, description="공휴일 영업")
):
    filtered_hairshops = []

    for hairshop in hairshop_list:
        if shop_name and shop_name != hairshop["shop_name"]:
            continue
        if price and price != hairshop["price"]:
            continue
        if hair_type and hair_type != hairshop["hair_type"]:
            continue
        if region and region != hairshop["region"]:
            continue
        if holiday and holiday != hairshop["holiday"]:
            continue
        filtered_hairshops.append(hairshop)

    return filtered_hairshops

# 가방 데이터 리스트
bag_list = [
    {
        "brand": "나이키",
        "max_price": 79000,
        "color": "검정",
        "bag_type": "백팩",
        "store": "무신사",
        "age": "5%"
    },
    {
        "brand": "히어리",
        "max_price": 88200,
        "color": "실버",
        "bag_type": "핸드백",
        "store": "29cm",
        "age": 29
    },
    {
        "brand": "레니비",
        "max_price": 39000,
        "color": "아이보리",
        "bag_type": "백팩",
        "store": "29cm",
        "age": 20
    },
    {
        "brand": "스컬프터",
        "max_price": 112000,
        "color": "검정",
        "bag_type": "백팩",
        "store": "무신사",
        "age": "10%"
    },
    {
        "brand": "퐁실구름크로스백",
        "max_price": 30000,
        "color": "아이보리",
        "bag_type": "크로스백",
        "store": "98도씨",
        "age": 0
    }
]

@app.get("/bag")
def search_bag(
    brand: Optional[str] = Query(None, description="브랜드명"),
    max_price: Optional[int] = Query(None, description="최대 가격", gt=0, le=10000000),
    color: Optional[str] = Query(None, description="색깔"),
    bag_type: Optional[str] = Query(None, description="종류"),
    store: Optional[str] = Query(None, description="판매처"),
    age: Optional[int] = Query(None, description="나이")
):
    filtered_bags = []

    for bag in bag_list:
        if brand and brand != bag["brand"]:
            continue
        if max_price and max_price < bag["max_price"]:
            continue
        if color and color != bag["color"]:
            continue
        if bag_type and bag_type != bag["bag_type"]:
            continue
        if store and store != bag["store"]:
            continue
        if age and age != bag["age"]:
            continue
        filtered_bags.append(bag)

    return filtered_bags

# 야구 선수 데이터 리스트
baseball_player_list = [
    {
        "team": "한화이글스",
        "uniform_number": 64,
        "position": "내야수",
        "age": 20,
        "name": "문현빈"
    },
    {
        "team": "한화이글스",
        "uniform_number": 22,
        "position": "내야수",
        "age": 35,
        "name": "채은성"
    },
    {
        "team": "두산베어스",
        "uniform_number": 25,
        "position": "포수",
        "age": 38,
        "name": "양의지"
    },
    {
        "team": "키움히어로즈",
        "uniform_number": 3,
        "position": "내야수",
        "age": 25,
        "name": "김혜성"
    },
    {
        "team": "키움히어로즈",
        "uniform_number": 51,
        "position": "외야수",
        "age": 26,
        "name": "이정후"
    }
]

@app.get("/baseballplayer")
def search_baseball_player(
    team: Optional[str] = Query(None, description="소속팀"),
    uniform_number: Optional[int] = Query(None, description="등번호"),
    position: Optional[str] = Query(None, description="포지션명"),
    age: Optional[int] = Query(None, description="나이"),
    name: Optional[str] = Query(None, description="이름")
):
    filtered_players = []

    for player in baseball_player_list:
        if team and team != player["team"]:
            continue
        if uniform_number and uniform_number != player["uniform_number"]:
            continue
        if position and position != player["position"]:
            continue
        if age and age != player["age"]:
            continue
        if name and name != player["name"]:
            continue
        filtered_players.append(player)

    return filtered_players

# 강아지 사료 데이터 리스트
pet_food_list = [
    {
        "brandName": "스위피",
        "name": "자연식 테린 입문세트",
        "price": 46800,
        "type": "화식",
        "protein": "닭",
        "calorie": 65,
        "age": "어덜트",
        "stock": 5
    },
    {
        "brandName": "룰루키친",
        "name": "일주일 체험 키트",
        "price": 45000,
        "type": "화식",
        "protein": "소",
        "calorie": 50,
        "age": "시니어",
        "stock": 2
    },
    {
        "brandName": "포옹",
        "name": "생식선생 - 닭1kg",
        "price": 52000,
        "type": "생식",
        "protein": "닭",
        "calorie": 48,
        "age": "퍼피",
        "stock": 3
    },
    {
        "brandName": "인섹트도그",
        "name": "미니 2kg",
        "price": 19000,
        "type": "건사료",
        "protein": "밀웜",
        "calorie": 36,
        "age": "어덜트",
        "stock": 7
    },
    {
        "brandName": "스텔라앤츄이스",
        "name": "로우 코티드 키블 사료 - LID 케이지 프리 터키",
        "price": 38000,
        "type": "건사료",
        "protein": "칠면조",
        "calorie": 42,
        "age": "시니어",
        "stock": 5
    },
    {
        "brandName": "나우",
        "name": "프레쉬 스몰브리드 퍼피 2.72kg",
        "price": 29000,
        "type": "건사료",
        "protein": "닭고기, 칠면조, 연어, 청어",
        "calorie": 70,
        "age": "시니어",
        "stock": 1
    },
    {
        "brandName": "스텔라앤츄이스",
        "name": "탄탈라이즈 터키 디너패티 사료 397g",
        "price": 49000,
        "type": "동결건조",
        "protein": "칠면조",
        "calorie": 30,
        "age": "어덜트",
        "stock": 6
    },
    {
        "brandName": "빅독",
        "name": "빅바이트 사료-캥거루 490g",
        "price": 49000,
        "type": "동결건조",
        "protein": "캥거루",
        "calorie": 25,
        "age": "퍼피",
        "stock": 9
    },
    {
        "brandName": "지위픽",
        "name": "독 식품 소고기 1kg",
        "price": 80000,
        "type": "에어드라이",
        "protein": "소",
        "calorie": 65,
        "age": "어덜트",
        "stock": 5
    },
    {
        "brandName": "허즈",
        "name": "미국산 칠면조가슴살 레시피 2LB",
        "price": 53000,
        "type": "에어드라이",
        "protein": "칠면조",
        "calorie": 60,
        "age": "시니어",
        "stock": 2
    }
]

@app.get("/pet_food")
def filter_pet_food(
    brandName: Optional[str] = Query(None, description="강아지 사료 브랜드 이름"),
    name: Optional[str] = Query(None, description="강아지 사료 이름"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    type: Optional[str] = Query(None, description="강아지 사료 형태"),
    protein: Optional[str] = Query(None, description="단백질 종류"),
    calorie: Optional[float] = Query(None, description="사료의 칼로리"),
    age: Optional[str] = Query(None, description="강아지의 연령"),
    stock: Optional[int] = Query(None, description="재고 수량")
):
    filtered_pet_food = []

    for food in pet_food_list:
        if brandName and brandName != food["brandName"]:
            continue
        if name and name != food["name"]:
            continue
        if max_price and food["price"] > max_price:
            continue
        if type and type != food["type"]:
            continue
        if protein and protein != food["protein"]:
            continue
        if calorie and calorie != food["calorie"]:
            continue
        if age and age != food["age"]:
            continue
        if stock and food["stock"] < stock:
            continue
        filtered_pet_food.append(food)

    return filtered_pet_food

# 식기 데이터 리스트
dinnerware_list = [
    {
        "brandName": "덴비",
        "collection": "헤리티지",
        "origin": "영국",
        "category": "국그릇",
        "price": 30000,
        "quality": "세라믹"
    },
    {
        "brandName": "에르메스",
        "collection": "패시폴리아",
        "origin": "프랑스",
        "category": "국그릇",
        "price": 750000,
        "quality": "세라믹"
    },
    {
        "brandName": "프라우나",
        "collection": "루미너스",
        "origin": "한국",
        "category": "접시",
        "price": 80000,
        "quality": "세라믹"
    },
    {
        "brandName": "덴비",
        "collection": "임프레션",
        "origin": "영국",
        "category": "접시",
        "price": 40000,
        "quality": "세라믹"
    },
    {
        "brandName": "에르메스",
        "collection": "어워크인더가든",
        "origin": "프랑스",
        "category": "컵",
        "price": 620000,
        "quality": "유리"
    },
    {
        "brandName": "빌레로이앤보흐",
        "collection": "엘시어노바",
        "origin": "독일",
        "category": "접시",
        "price": 35000,
        "quality": "세라믹"
    },
    {
        "brandName": "프라우나",
        "collection": "제레미",
        "origin": "한국",
        "category": "티주전자",
        "price": 260000,
        "quality": "세라믹"
    },
    {
        "brandName": "빌레로이앤보흐",
        "collection": "아르테사노프로벤셜라벤더",
        "origin": "독일",
        "category": "컵",
        "price": 18000,
        "quality": "유리"
    },
    {
        "brandName": "놋담",
        "collection": "달 커트러리",
        "origin": "커트러리",
        "category": "커트러리",
        "price": 55000,
        "quality": "유기"
    },
    {
        "brandName": "놋담",
        "collection": "블랑 커트러리",
        "origin": "한국",
        "category": "커트러리",
        "price": 70000,
        "quality": "유기"
    }
]

@app.get("/dinnerware")
def filter_dinnerware(
    brandName: Optional[str] = Query(None, description="식기 브랜드 이름"),
    collection: Optional[str] = Query(None, description="식기 컬렉션 이름"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    category: Optional[str] = Query(None, description="식기 종류"),
    origin: Optional[str] = Query(None, description="식기의 원산지"),
    quality: Optional[str] = Query(None, description="식기의 재질")
):
    filtered_dinnerware = []

    for dinnerware in dinnerware_list:
        if brandName and brandName != dinnerware["brandName"]:
            continue
        if collection and collection != dinnerware["collection"]:
            continue
        if max_price and dinnerware["price"] > max_price:
            continue
        if min_price and dinnerware["price"] < min_price:
            continue
        if category and category != dinnerware["category"]:
            continue
        if origin and origin != dinnerware["origin"]:
            continue
        if quality and quality != dinnerware["quality"]:
            continue
        filtered_dinnerware.append(dinnerware)

    return filtered_dinnerware

# 키보드 데이터 리스트
keyboard_list = [
    {
        "brandName": "앱코",
        "name": "스페셜 게이밍 카일 레인보우LED",
        "structure": "기계식",
        "switch": "광축",
        "use": "용도",
        "price": 61000,
        "waterproof": "불가",
        "description": "화려한 백라이트"
    },
    {
        "brandName": "앱코",
        "name": "TOS180 블루투스 펜타그래프 키보드",
        "structure": "멤브레인",
        "switch": "",
        "use": "사무용",
        "price": 20000,
        "waterproof": "불가",
        "description": "사무용으로 적합한 저소음 키보드"
    },
    {
        "brandName": "한성",
        "name": "Gtune Rainbow 키보드",
        "structure": "기계식",
        "switch": "적축",
        "use": "게이밍",
        "price": 89000,
        "waterproof": "가능",
        "description": "타건감이 경쾌한 키보드"
    },
    {
        "brandName": "한성",
        "name": "GTune GK600",
        "structure": "기계식",
        "switch": "갈축",
        "use": "게이밍",
        "price": 50470,
        "waterproof": "가능",
        "description": "알루미늄 디자인과 보강설계로 정숙한 타건감"
    },
    {
        "brandName": "콕스",
        "name": "게이트론 LED",
        "structure": "기계식",
        "switch": "황축",
        "use": "게이밍",
        "price": 60000,
        "waterproof": "불가",
        "description": "PC방에서 가장 인기있는 가성비 키보드"
    },
    {
        "brandName": "콕스",
        "name": "CK87 PBT",
        "structure": "기계식",
        "switch": "갈축",
        "use": "게이밍",
        "price": 38000,
        "waterproof": "불가",
        "description": "훌륭한 가성비로 색이 다양한 키보드"
    },
    {
        "brandName": "녹스",
        "name": "기어 VALKAN LED 유선키보드",
        "structure": "기계식",
        "switch": "광축",
        "use": "사무용",
        "price": 75000,
        "waterproof": "가능",
        "description": "고밀도 스테인레스를 이용한 토션 스프링 채용"
    },
    {
        "brandName": "콕스",
        "name": "CK01 PBT SL",
        "structure": "기계식",
        "switch": "백축",
        "use": "사무용",
        "price": 54000,
        "waterproof": "가능",
        "description": "데스크테리어로 적합한 키보드"
    },
    {
        "brandName": "해커",
        "name": "K640 한영 이중사출",
        "structure": "기계식",
        "switch": "청축",
        "use": "게이밍",
        "price": 120000,
        "waterproof": "가능",
        "description": "무지개색의 백라이트로 게임을 더 생동감 있게"
    }
]

@app.get("/keyboard")
def filter_keyboard(
    brandName: Optional[str] = Query(None, description="키보드 브랜드 이름"),
    name: Optional[str] = Query(None, description="키보드의 상품 이름"),
    structure: Optional[str] = Query(None, description="키보드의 구조"),
    switch: Optional[str] = Query(None, description="키보드의 스위치 종류"),
    use: Optional[str] = Query(None, description="용도"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    waterproof: Optional[str] = Query(None, description="키보드의 방수 여부"),
    description: Optional[str] = Query(None, description="키보드에 대한 설명")
):
    filtered_keyboard = []

    for keyboard in keyboard_list:
        if brandName and brandName != keyboard["brandName"]:
            continue
        if name and name != keyboard["name"]:
            continue
        if structure and structure != keyboard["structure"]:
            continue
        if switch and switch != keyboard["switch"]:
            continue
        if use and use != keyboard["use"]:
            continue
        if min_price and keyboard["price"] < min_price:
            continue
        if waterproof and waterproof != keyboard["waterproof"]:
            continue
        if description and description != keyboard["description"]:
            continue
        filtered_keyboard.append(keyboard)

    return filtered_keyboard

# 수제비누 데이터 리스트
soap_list = [
    {
        "name": "태양",
        "ingredient": "노니 가루",
        "effect": "미백",
        "scent": "라벤더",
        "part": "얼굴",
        "weight": 125,
        "price": 3000
    },
    {
        "name": "바다",
        "ingredient": "밤 껍질 가루",
        "effect": "보습",
        "scent": "머스크",
        "part": "얼굴",
        "weight": 200,
        "price": 9800
    },
    {
        "name": "파도",
        "ingredient": "꿀",
        "effect": "보습",
        "scent": "머스크",
        "part": "머리",
        "weight": 95,
        "price": 7800
    },
    {
        "name": "산골",
        "ingredient": "어성초 가루",
        "effect": "진정",
        "scent": "오이",
        "part": "몸",
        "weight": 165,
        "price": 55000
    },
    {
        "name": "나무",
        "ingredient": "쌀",
        "effect": "미백",
        "scent": "바닐라",
        "part": "몸",
        "weight": 300,
        "price": 10000
    },
    {
        "name": "까만",
        "ingredient": "감자",
        "effect": "미백",
        "scent": "레몬",
        "part": "얼굴",
        "weight": 136,
        "price": 6000
    },
    {
        "name": "파티",
        "ingredient": "무화과 가루",
        "effect": "각질 제거",
        "scent": "향기",
        "part": "머리",
        "weight": 210,
        "price": 9000
    },
    {
        "name": "사랑",
        "ingredient": "티트리",
        "effect": "진정",
        "scent": "소나무",
        "part": "머리",
        "weight": 158,
        "price": 8000
    },
    {
        "name": "우정",
        "ingredient": "딸기 가루",
        "effect": "각질 제거",
        "scent": "라벤더",
        "part": "얼굴",
        "weight": 150,
        "price": 7500
    }
]

@app.get("/soap")
def filter_soap(
    name: Optional[str] = Query(None, description="비누의 상품명"),
    ingredient: Optional[str] = Query(None, description="비누에 사용된 재료"),
    effect: Optional[str] = Query(None, description="비누의 효능"),
    scent: Optional[str] = Query(None, description="비누의 향기"),
    part: Optional[str] = Query(None, description="비누의 사용 부위"),
    weight: Optional[float] = Query(None, description="비누의 무게"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격")
):
    filtered_soap = []

    for soap in soap_list:
        if name and name != soap["name"]:
            continue
        if ingredient and ingredient != soap["ingredient"]:
            continue
        if effect and effect != soap["effect"]:
            continue
        if scent and scent != soap["scent"]:
            continue
        if part and part != soap["part"]:
            continue
        if weight and weight != soap["weight"]:
            continue
        if min_price and soap["price"] < min_price:
            continue
        if max_price and soap["price"] > max_price:
            continue
        filtered_soap.append(soap)

    return filtered_soap

# 수영장 회원 데이터 리스트
member_list = [
    {
        "regDate": "2022-09-15",
        "regNum": "95",
        "name": "김유진",
        "birthday": "1997-08-13",
        "gender": "F",
        "level": "중급",
        "lockerNum": "135",
        "regMonth": 9,
        "attendance": "출석"
    },
    {
        "regDate": "2022-12-17",
        "regNum": "99",
        "name": "양원영",
        "birthday": "1981-05-09",
        "gender": "F",
        "level": "중급",
        "lockerNum": "203",
        "regMonth": 6,
        "attendance": "출석"
    },
    {
        "regDate": "2019-01-25",
        "regNum": "12",
        "name": "강지원",
        "birthday": "1970-06-25",
        "gender": "M",
        "level": "고급",
        "lockerNum": "253",
        "regMonth": 40,
        "attendance": "결석"
    },
    {
        "regDate": "2023-01-11",
        "regNum": "135",
        "name": "장이서",
        "birthday": "2000-05-06",
        "gender": "F",
        "level": "초급",
        "lockerNum": "87",
        "regMonth": 5,
        "attendance": "결석"
    },
    {
        "regDate": "2023-05-16",
        "regNum": "166",
        "name": "윤동희",
        "birthday": "2001-08-30",
        "gender": "M",
        "level": "기초",
        "lockerNum": "66",
        "regMonth": 1,
        "attendance": "출석"
    },
    {
        "regDate": "2023-06-08",
        "regNum": "185",
        "name": "정수아",
        "birthday": "1978-12-25",
        "gender": "F",
        "level": "기초",
        "lockerNum": "41",
        "regMonth": 1,
        "attendance": "출석"
    },
    {
        "regDate": "2021-12-02",
        "regNum": "45",
        "name": "도원영",
        "birthday": "1990-07-16",
        "gender": "F",
        "level": "고급",
        "lockerNum": "2",
        "regMonth": 15,
        "attendance": "출석"
    },
    {
        "regDate": "2023-03-03",
        "regNum": "146",
        "name": "이도하",
        "birthday": "1992-04-26",
        "gender": "M",
        "level": "초급",
        "lockerNum": "88",
        "regMonth": 3,
        "attendance": "결석"
    },
    {
        "regDate": "2022-02-07",
        "regNum": "88",
        "name": "안강훈",
        "birthday": "1999-01-02",
        "gender": "M",
        "level": "중급",
        "lockerNum": "16",
        "regMonth": 12,
        "attendance": "출석"
    }
]


@app.get("/swim_member")
async def filter_swim_member(
    regDate: Optional[str] = Query(None, description="등록일"),
    regNum: Optional[str] = Query(None, description="회원 등록번호"),
    name: Optional[str] = Query(None, description="회원 이름"),
    birthday: Optional[str] = Query(None, description="생년월일"),
    gender: Optional[str] = Query(None, description="성별"),
    level: Optional[str] = Query(None, description="급수 ex. 기초, 초급, 중급, 고급"),
    lockerNum: Optional[int] = Query(None, description="사물함 번호"),
    regMonth: Optional[int] = Query(None, description="등록 개월 수"),
    attendance: Optional[str] = Query(None, description="출석 여부")
) -> List[dict]:
    filtered_members = []

    for member in member_list:
        if regDate and regDate != member["regDate"]:
            continue
        if regNum and regNum != member["regNum"]:
            continue
        if name and name != member["name"]:
            continue
        if birthday and birthday != member["birthday"]:
            continue
        if gender and gender != member["gender"]:
            continue
        if level and level != member["level"]:
            continue
        if lockerNum and lockerNum != member["lockerNum"]:
            continue
        if regMonth and regMonth != member["regMonth"]:
            continue
        if attendance and attendance != member["attendance"]:
            continue
        filtered_members.append(member)

    return filtered_members

# 세계 맥주 데이터 리스트
world_beer_list = [
    {
        "name": "창",
        "country": "태국",
        "EXPDate": "2023-12-25",
        "category": "라거",
        "degree": 5.0,
        "price": 3200
    },
    {
        "name": "벡스",
        "country": "독일",
        "EXPDate": "2024-01-09",
        "category": "라거",
        "degree": 0,
        "price": 5000
    },
    {
        "name": "버드와이저",
        "country": "미국",
        "EXPDate": "2023-09-01",
        "category": "라거",
        "degree": 4.5,
        "price": 3600
    },
    {
        "name": "기네스",
        "country": "아일랜드",
        "EXPDate": "2025-08-13",
        "category": "흑맥주",
        "degree": 7.0,
        "price": 4500
    },
    {
        "name": "코젤다크",
        "country": "체코",
        "EXPDate": "2023-03-10",
        "category": "흑맥주",
        "degree": 5.6,
        "price": 4200
    },
    {
        "name": "호가든",
        "country": "벨기에",
        "EXPDate": "2025-01-09",
        "category": "밀맥주",
        "degree": 4.9,
        "price": 3800
    },
    {
        "name": "1664블랑",
        "country": "프랑스",
        "EXPDate": "2023-09-30",
        "category": "과일맥주",
        "degree": 5.5,
        "price": 4500
    },
    {
        "name": "하이네켄",
        "country": "네덜란드",
        "EXPDate": "2024-03-25",
        "category": "라거",
        "degree": 6.0,
        "price": 4100
    },
    {
        "name": "포엑스 골드",
        "country": "호주",
        "EXPDate": "2024-09-29",
        "category": "라거",
        "degree": 3.5,
        "price": 3750
    }
]


@app.get("/world_beer")
async def filter_world_beer(
    name: Optional[str] = Query(None, description="상품명"),
    country: Optional[str] = Query(None, description="원산지"),
    EXPDate: Optional[str] = Query(None, description="유통기한"),
    category: Optional[str] = Query(None, description="카테고리"),
    min_degree: Optional[float] = Query(None, description="최저 도수"),
    max_degree: Optional[float] = Query(None, description="최고 도수"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격")
) -> List[dict]:
    filtered_beers = []

    for beer in world_beer_list:
        if name and name != beer["name"]:
            continue
        if country and country != beer["country"]:
            continue
        if EXPDate and EXPDate != beer["EXPDate"]:
            continue
        if category and category != beer["category"]:
            continue
        if min_degree is not None and beer["degree"] < min_degree:
            continue
        if max_degree is not None and beer["degree"] > max_degree:
            continue
        if min_price is not None and beer["price"] < min_price:
            continue
        if max_price is not None and beer["price"] > max_price:
            continue
        filtered_beers.append(beer)

    return filtered_beers

# 원데이 클래스 데이터 리스트
one_day_class_list = [
    {
        "name": "마크라메 강좌",
        "teacher": "김사라",
        "category": "공예",
        "limit": 5,
        "price": 37000,
        "location": "서울 공예협회 104호",
        "description": "매듭으로 만드는 팔찌와 키링"
    },
    {
        "name": "지중해식 요리 강좌",
        "teacher": "강유진",
        "category": "요리",
        "limit": 4,
        "price": 60000,
        "location": "강유진 요리연구가 사무실 1Room",
        "description": "남프랑스 레시피로 만드는 샐러드와 연어스테이크"
    },
    {
        "name": "라탄 강좌",
        "teacher": "고미연",
        "category": "공예",
        "limit": 10,
        "price": 40000,
        "location": "한국 라탄협회 본사 403호",
        "description": "라탄으로 만드는 컵받침과 휴지 케이스"
    },
    {
        "name": "아이패드 프로크리에이트 강좌",
        "teacher": "한영석",
        "category": "미술",
        "limit": 7,
        "price": 30000,
        "location": "디지털드로잉 협회 2층",
        "description": "하루만에 이모티콘 만들기"
    },
    {
        "name": "젤네일 강좌",
        "teacher": "유영지",
        "category": "뷰티",
        "limit": 15,
        "price": 35000,
        "location": "라룸 네일",
        "description": "집에서도 따라할 수 있는 쉬운 셀프 젤네일"
    },
    {
        "name": "오일파스텔 드로잉 강좌",
        "teacher": "김은지",
        "category": "미술",
        "limit": 6,
        "price": 40000,
        "location": "하늘구름 미술학원",
        "description": "자연의 색감을 풍부하게 표현하는 오일파스텔의 매력으로"
    }
]


@app.get("/oneday_class")
async def filter_one_day_class(
    name: Optional[str] = Query(None, description="클래스 이름"),
    teacher: Optional[str] = Query(None, description="강사 이름"),
    category: str = Query(..., description="카테고리를 나타냅니다. ex. 공예, 요리, 미술, 뷰티, 플라워"),
    min_limit: Optional[int] = Query(None, description="최소 정원"),
    min_price: Optional[int] = Query(None, description="최저 가격"),
    location: Optional[str] = Query(None, description="장소"),
    description: Optional[str] = Query(None, description="설명")
) -> List[dict]:
    filtered_classes = []

    for one_day_class in one_day_class_list:
        if name and name != one_day_class["name"]:
            continue
        if teacher and teacher != one_day_class["teacher"]:
            continue
        if category != one_day_class["category"]:
            continue
        if min_limit is not None and one_day_class["limit"] < min_limit:
            continue
        if min_price is not None and one_day_class["price"] < min_price:
            continue
        if location and location != one_day_class["location"]:
            continue
        if description and description != one_day_class["description"]:
            continue
        filtered_classes.append(one_day_class)

    return filtered_classes

# 캐릭터 굿즈 데이터 리스트
character_goods_list = [
    {
        "name": "최고심",
        "author": "최고심",
        "category": "가방",
        "price": 50000,
        "stock": 5
    },
    {
        "name": "레니니",
        "author": "라인프렌즈",
        "category": "키링",
        "price": 9000,
        "stock": 60
    },
    {
        "name": "브니니",
        "author": "라인프렌즈",
        "category": "인형",
        "price": 23000,
        "stock": 25
    },
    {
        "name": "라이언",
        "author": "카카오프렌즈",
        "category": "엽서",
        "price": 2500,
        "stock": 203
    },
    {
        "name": "어피치",
        "author": "카카오프렌즈",
        "category": "키링",
        "price": 12000,
        "stock": 100
    },
    {
        "name": "샐리니",
        "author": "라인프렌즈",
        "category": "엽서",
        "price": 2000,
        "stock": 300
    },
    {
        "name": "시나모롤",
        "author": "산리오",
        "category": "키링",
        "price": 18000,
        "stock": 3
    }
]


@app.get("/character_goods")
async def filter_character_goods(
    name: Optional[str] = Query(None, description="캐릭터 이름"),
    author: Optional[str] = Query(None, description="작가 이름"),
    category: Optional[str] = Query(None, description="카테고리"),
    min_price: Optional[int] = Query(None, description="최저 가격"),
    max_price: Optional[int] = Query(None, description="최고 가격"),
    min_stock: Optional[int] = Query(None, description="최저 재고")
) -> List[dict]:
    filtered_goods = []

    for character_goods in character_goods_list:
        if name and name != character_goods["name"]:
            continue
        if author and author != character_goods["author"]:
            continue
        if category and category != character_goods["category"]:
            continue
        if min_price is not None and character_goods["price"] < min_price:
            continue
        if max_price is not None and character_goods["price"] > max_price:
            continue
        if min_stock is not None and character_goods["stock"] < min_stock:
            continue
        filtered_goods.append(character_goods)

    return filtered_goods

# 장난감 렌탈샵 데이터 리스트
toy_rental_list = [
    {
        "brandName": "코리아보드게임즈",
        "productName": "폴짝폴짝 개구리 사탕먹기",
        "age": 8,
        "category": "보드게임",
        "duration": 6,
        "price": 8720
    },
    {
        "brandName": "타요",
        "productName": "타요RC카",
        "age": 4,
        "category": "완구",
        "duration": 3,
        "price": 7000
    },
    {
        "brandName": "요미몬",
        "productName": "터치식 키즈탭",
        "age": 2,
        "category": "전자기기",
        "duration": 2,
        "price": 12000
    },
    {
        "brandName": "뽀롱뽀롱 뽀로로",
        "productName": "노래하는 청소 돌돌이",
        "age": 5,
        "category": "완구",
        "duration": 3,
        "price": 5000
    },
    {
        "brandName": "바다통상",
        "productName": "소프트 촉감볼 촉감각 발달 완구 8p",
        "age": 0,
        "category": "완구",
        "duration": 10,
        "price": 15000
    },
    {
        "brandName": "릴라코",
        "productName": "어린이 플레이하우스",
        "age": 6,
        "category": "텐트",
        "duration": 12,
        "price": 19000
    },
    {
        "brandName": "윈펀",
        "productName": "똑똑한 무선 강아지 친구",
        "age": 1,
        "category": "완구",
        "duration": 6,
        "price": 9500
    }
]


@app.get("/toy_rental")
async def filter_toy_rental(
    brandName: Optional[str] = Query(None, description="브랜드 이름"),
    productName: Optional[str] = Query(None, description="상품명"),
    max_age: Optional[int] = Query(None, description="최대 사용 나이"),
    category: Optional[str] = Query(None, description="카테고리"),
    min_duration: Optional[int] = Query(None, description="최소 기간"),
    max_price: Optional[int] = Query(None, description="최대 가격")
) -> List[dict]:
    filtered_toys = []

    for toy_rental in toy_rental_list:
        if brandName and brandName != toy_rental["brandName"]:
            continue
        if productName and productName != toy_rental["productName"]:
            continue
        if max_age is not None and max_age < toy_rental["age"]:
            continue
        if category and category != toy_rental["category"]:
            continue
        if min_duration is not None and min_duration > toy_rental["duration"]:
            continue
        if max_price is not None and max_price < toy_rental["price"]:
            continue

        filtered_toys.append(toy_rental)

    return filtered_toys

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
