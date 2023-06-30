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

###0630 작업
# 방탈출 매장 데이터 리스트
room_escape_list = [
    {
        "theme": "LUCKY",
        "name": "도어이스케이프 레드 신논현점",
        "address": "서울특별시 서초구 서초동 1302-24",
        "grade": 8.45,
        "difficulty": 6,
        "review_num": 684
    },
    {
        "theme": "그림자 없는 상자",
        "name": "방탈출, 단편선",
        "address": "서울특별시 강남구 봉은사로4길 36",
        "grade": 9.27,
        "difficulty": 4,
        "review_num": 954
    },
    {
        "theme": "꼬레아 우라",
        "name": "코드케이 홍대점",
        "address": "서울특별시 마포구 상수동 86-22번지 3층 301호",
        "grade": 9.13,
        "difficulty": 8,
        "review_num": 1701
    },
    {
        "theme": "섀도우",
        "name": "지구별방탈출 홍대라스트시티점",
        "address": "서울 마포구 홍익로 10 (서교푸르지오) 상가건물 지하2층 지구별 방탈출",
        "grade": 9.00,
        "difficulty": 2,
        "review_num": 204
    },
    {
        "theme": "호텔 레토",
        "name": "호텔 레토",
        "address": "서울시 성동구 연무장5길 18 지하1층 101호(성수동2가)",
        "grade": 9.21,
        "difficulty": 8,
        "review_num": 1103
    },
    {
        "theme": "튜링테스트",
        "name": "이스케이프샾 건대점",
        "address": "서울 광진구 능동로 129-1 2층, 3층",
        "grade": 8.13,
        "difficulty": 10,
        "review_num": 223
    }
]


@app.get("/room_escape")
async def search_room_escape(
        theme: Optional[str] = Query(None, description="테마"),
        address: Optional[str] = Query(None, description="매장 주소를 바탕으로 검색"),
        name: Optional[str] = Query(None, description="매장명"),
        min_grade: Optional[float] = Query(None, ge=0, le=10, description="최소 별점"),
        max_grade: Optional[float] = Query(None, ge=0, le=10, description="최대 별점"),
        min_difficulty: Optional[int] = Query(None, ge=0, le=10, description="최소 난이도"),
        max_difficulty: Optional[int] = Query(None, ge=0, le=10, description="최대 난이도")
) -> List[dict]:
    results = []
    for room in room_escape_list:
        if room["theme"] and theme is not None and room["theme"] != theme:
            continue
        if room["address"] and address is not None and room["address"].find(address) == -1:
            continue
        if room["name"] and name is not None and room["name"] != name:
            continue
        if room["grade"] and min_grade is not None and room["grade"] < min_grade:
            continue
        if room["grade"] and max_grade is not None and room["grade"] > max_grade:
            continue
        if room["difficulty"] and min_difficulty is not None and room["difficulty"] < min_difficulty:
            continue
        if room["difficulty"] and max_difficulty is not None and room["difficulty"] > max_difficulty:
            continue
        results.append(room)
    return results

theme_park_list = [
    {
        "name": "에버랜드",
        "address": "경기도 용인 처인구 포곡읍 에버랜드로 199",
        "grade": 4.5,
        "review_num": 1817,
        "reviews": ["진짜 친구들이랑 갔는데 완전 재밌음 ㅋㅋ", "너무 재밌어요 ㅋㅋㅋㅋㅋ 꼭 추천 합니다.", "놀이기구도 다 재밌고 넓고 아이들이랑 같이 가면 좋은곳 먹거리 많고 맛있고 한번가면 또 가고 싶음 아이들 있으면 한번 가는것도 좋을것 같음"]
    },
    {
        "name": "롯데월드",
        "address": "서울 송파구 올림픽로 240",
        "grade": 4.0,
        "review_num": 3340,
        "reviews": ["날씨도 좋고 실내도 있어서 더 재미있게 놀았다!", "아이가 정말 너무너무 행복해 했어요", "직원분이 친절하셔서 더웅 재미있던 롯데월드"]
    },
    {
        "name": "레고랜드 코리아",
        "address": "강원도 춘천 하중도길 128",
        "grade": 5.0,
        "review_num": 104,
        "reviews": ["레고랜드에서 즐겁고 알차게 보냈어요", "아이들이 좋아해요", "레고랜드 마치 장난감나라의 주인공이 된 것 같아요!"]
    },
    {
        "name": "한국민속촌",
        "address": "경기도 용인 기흥구 민속촌로 90",
        "grade": 4.5,
        "review_num": 765,
        "reviews": ["재방문의사 100프로", "데이트 코스로도 최고", "옛한국적인 모습을 볼 수 있는 곳."]
    },
    {
        "name": "에코랜드 테마파크",
        "address": "제주특별자치도 제주시, 조천읍 번영로 1278-169",
        "grade": 4.0,
        "review_num": 352,
        "reviews": ["가족여행으로 제격", "애들과 함께라면 하루정도는 애코랜드에서 시간을 보내는것도 좋을듯하다", "힐링 힐링 그리고 다채로운 추억남김"]
    }
]

@app.get("/themepark")
async def search_theme_park(
    name: Optional[str] = Query(None, description="테마파크명"),
    ctprvNm: str = Query(..., description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    min_grade: Optional[float] = Query(None, ge=0, le=5, description="최소 평점"),
    max_grade: Optional[float] = Query(None, ge=0, le=5, description="최대 평점"),
) -> List[dict]:
    results = []
    for theme_park in theme_park_list:
        if theme_park["name"] and name is not None and theme_park["name"] != name:
            continue
        if theme_park["address"] and sgngNm is not None and theme_park["address"].find(sgngNm) == -1:
            continue
        if theme_park["grade"] and min_grade is not None and theme_park["grade"] < min_grade:
            continue
        if theme_park["grade"] and max_grade is not None and theme_park["grade"] > max_grade:
            continue
        results.append(theme_park)
    return results

bicycle_list = [
    {
        "type": "MTB",
        "brand": "도마스",
        "name": "2022 도마스 아드레날린 2.1 MTB 27.5",
        "price": 410000,
        "colors": ["매트 블랙", "글로시 다크그레이", "글로시 옐로우"],
        "review_num": 667
    },
    {
        "type": "MTB",
        "brand": "비앙키",
        "name": "2023 비앙키 듀엘 27.S MTB",
        "price": 1150000,
        "colors": ["블랙", "체레스트"],
        "review_num": 6
    },
    {
        "type": "미니벨로",
        "brand": "알톤",
        "name": "2023 알톤 힐라리스 20 접이식 미니벨로",
        "price": 490000,
        "colors": ["블랙", "다크그레이", "화이트"],
        "review_num": 11
    },
    {
        "type": "미니벨로",
        "brand": "첼로",
        "name": "2023 첼로 토모 SE 9 접이식 9단 미니벨로",
        "price": 890000,
        "colors": ["다크베리", "다크 카멜레온"],
        "review_num": 0
    },
    {
        "type": "전기자전거",
        "brand": "알톤",
        "name": "2023 알톤 벤조 24 전기자전거 24",
        "price": 1150000,
        "colors": ["매트 블랙", "매트 베이지"],
        "review_num": 5
    },
    {
        "type": "전기자전거",
        "brand": "퀄리스포츠",
        "name": "2023 퀄리 볼트S 750W 전동스쿠터",
        "price": 2100000,
        "colors": ["블랙", "그레이", "그린"],
        "review_num": 7
    }
]

@app.get("/bicycle")
async def search_bicycle(
    type: Optional[str] = Query(None, description="타입"),
    brand: Optional[str] = Query(None, description="브랜드"),
    name: Optional[str] = Query(None, description="모델명"),
    min_price: Optional[int] = Query(None, ge=0, description="최소 가격"),
    max_price: Optional[int] = Query(None, ge=0, description="최대 가격"),
    color: Optional[str] = Query(None, description="색상")
) -> List[dict]:
    results = []
    for bicycle in bicycle_list:
        if type is not None and bicycle["type"] != type:
            continue
        if brand is not None and bicycle["brand"] != brand:
            continue
        if name is not None and bicycle["name"] != name:
            continue
        if min_price is not None and bicycle["price"] < min_price:
            continue
        if max_price is not None and bicycle["price"] > max_price:
            continue
        if color is not None and color not in bicycle["colors"]:
            continue
        results.append(bicycle)
    return results

seoul_bike_list = [
    {
        "name": "사당역 5번출구 대여소",
        "address": "서울 관악구 남현동 1060-12",
        "bike_num": 0,
        "smallbike_num": 3,
        "subway_station": "사당역"
    },
    {
        "name": "서울도시건축전시관 대여소",
        "address": "서울 중구 태평로1가 60-20",
        "bike_num": 26,
        "smallbike_num": 5,
        "subway_station": "시청역"
    },
    {
        "name": "광화문 S타워 앞 대여소",
        "address": "서울 종로구 신문로1가 5-4",
        "bike_num": 71,
        "smallbike_num": 6,
        "subway_station": "광화문역"
    },
    {
        "name": "롯데호텔 대여소",
        "address": "서울 중구 을지로1가 180-6",
        "bike_num": 4,
        "smallbike_num": 0,
        "subway_station": "을지로입구역"
    },
    {
        "name": "청계광장 옆 대여소",
        "address": "서울 중구 태평로1가 2-2",
        "bike_num": 14,
        "smallbike_num": 2,
        "subway_station": "광화문역"
    },
    {
        "name": "관악구청교차로 대여소",
        "address": "서울 관악구 관악로 153",
        "bike_num": 0,
        "smallbike_num": 2,
        "subway_station": "서울대입구역"
    }
]

@app.get("/seoul_bike")
async def search_seoul_bike(
    gu: Optional[str] = Query(None, description="서울시 행정구역명(ex: 강남구, 중구 등)"),
    name: Optional[str] = Query(None, description="대여소 이름"),
    min_bike: Optional[int] = Query(None, ge=0, description="최소 일반 따릉이 수"),
    max_bike: Optional[int] = Query(None, ge=0, description="최대 일반 따릉이 수"),
    min_smallbike: Optional[int] = Query(None, ge=0, description="최소 새싹 따릉이 수"),
    max_smallbike: Optional[int] = Query(None, ge=0, description="최대 새싹 따릉이 수"),
) -> List[dict]:
    results = []
    for seoul_bike in seoul_bike_list:
        if gu is not None and gu != seoul_bike["gu"]:
            continue
        if name is not None and name != seoul_bike["name"]:
            continue
        if min_bike is not None and seoul_bike["bike_num"] < min_bike:
            continue
        if max_bike is not None and seoul_bike["bike_num"] > max_bike:
            continue
        if min_smallbike is not None and seoul_bike["smallbike_num"] < min_smallbike:
            continue
        if max_smallbike is not None and seoul_bike["smallbike_num"] > max_smallbike:
            continue
        results.append(seoul_bike)
    return results

gyeonggi_bus_list = [
    {
        "num": "4000",
        "type": "공항",
        "starting_point": "동수원공항버스정류장",
        "terminal": "인천공항3층출국장(T2)",
        "bus_stops": ["동수원공항버스정류장", "못골사거리", "북수원TG", "안산IC", "연수JC", "제1여객터미널", "인천공항3층출국장(T2)"]
    },
    {
        "num": "11",
        "type": "용인시 마을",
        "starting_point": "죽전역.신세계백화점",
        "terminal": "미금역.2001아울렛",
        "bus_stops": ["죽전역.신세계백화점", "정평중학교", "주공아파트", "초입마을사거리", "동천동현대홈타운1차아파트", "미금역.2001아울렛"]
    },
    {
        "num": "4300",
        "type": "공항",
        "starting_point": "동수원공항버스정류장",
        "terminal": "김포공항국내선(12번홈)",
        "bus_stops": ["동수원공항버스정류장", "창룡문사거리", "호계종합시장", "비산교", "석수IC", "안현JC", "송내IC", "서운JC", "김포공항국내선(12번홈)"]
    },
    {
        "num": "M5115",
        "type": "광역급행",
        "starting_point": "상현역",
        "terminal": "서울역버스환승센터(6번승강장)(중)",
        "bus_stops": ["상현역", "광교중앙.경기도청.아주대역환승센터(지하1층)", "경기대수원캠퍼스후문", "죽전", "금토JC", "양재IC", "한남오거리", "서울백병원.국가인권위.안중근활동터(중)","서울역버스환승센터(6번승강장)(중)"]
    },
    {
        "num": "M5342",
        "type": "광역급행",
        "starting_point": "수원버스터미널",
        "terminal": "잠실광역환승센터",
        "bus_stops": ["수원버스터미널", "수원아이파크시티.선일초교", "삼성2차아파트", "동수원TG", "죽전", "판교IC", "장지역.가든파이브", "가락시장.가락시장역","잠실광역환승센터"]
    },
    {
        "num": "370",
        "type": "성남시 일반",
        "starting_point": "고등마을아파트",
        "terminal": "더샵판교퍼스트파크",
        "bus_stops": ["고등마을아파트", "성남고등공공주택지구.서편", "시흥사거리", "유라코퍼레이션.SK케미칼", "웰츠타워", "서현역.AK플라자", "정자사거리", "더샵판교퍼스트파크"]
    }
]

@app.get("/gyeonggi_bus")
async def search_gyeonggi_bus(
    num: Optional[str] = Query(None, description="노선 번호"),
    type: str = Query(..., description="노선 유형(ex: 공항, 광역급행, 용인시 마을 등)"),
    starting_point: Optional[str] = Query(None, description="기점"),
    terminal: Optional[str] = Query(None, description="종점"),
    bus_stop: Optional[str] = Query(None, description="정류장명(주요 경유지를 바탕으로 검색합니다)")
) -> List[dict]:
    results = []
    for bus in gyeonggi_bus_list:
        if num is not None and num != bus["num"]:
            continue
        if type is not None and type != bus["type"]:
            continue
        if starting_point is not None and starting_point != bus["starting_point"]:
            continue
        if terminal is not None and terminal != bus["terminal"]:
            continue
        if bus_stop is not None and bus_stop not in bus["bus_stops"]:
            continue
        results.append(bus)
    return results

typhoon_data = [
    {
        "num": 1,
        "name": "볼라벤",
        "eng_name": "BOLAVEN",
        "naming_cntry": "라오스",
        "influence": "없음",
        "generationDt": "2018.01.03",
        "extinctionDt": "2018.01.04",
        "desc": "제1호 태풍 볼라벤(BOLAVEN)은 라오스에서 제출한 이름으로 고원의 이름임."
    },
    {
        "num": 8,
        "name": "바비",
        "eng_name": "BAVI",
        "naming_cntry": "베트남",
        "influence": "직접영향",
        "generationDt": "2020.08.22",
        "extinctionDt": "2020.08.27",
        "desc": "제8호 태풍 바비(BAVI)는 베트남에서 제출한 이름으로 산맥의 이름임."
    },
    {
        "num": 9,
        "name": "마이삭",
        "eng_name": "MAYSAK",
        "naming_cntry": "캄보디아",
        "influence": "상륙",
        "generationDt": "2020.08.28",
        "extinctionDt": "2020.09.03",
        "desc": "제9호 태풍 마이삭(MAYSAK)은 캄보디아에서 제출한 이름으로 나무의 한 종류임."
    },
    {
        "num": 10,
        "name": "하이선",
        "eng_name": "HAISHEN",
        "naming_cntry": "중국",
        "influence": "상륙",
        "generationDt": "2020.09.01",
        "extinctionDt": "2020.09.07",
        "desc": "제10호 태풍 하이선(HAISHEN)은 중국에서 제출한 이름으로 바다의 신을 의미함."
    },
    {
        "num": 1,
        "name": "말라카스",
        "eng_name": "MALAKAS",
        "naming_cntry": "필리핀",
        "influence": "없음",
        "generationDt": "2022.04.08",
        "extinctionDt": "2022.04.16",
        "desc": "제1호 태풍 말라카스(MALAKAS)는 필리핀에서 제출한 이름으로 강력함을 의미함."
    },
    {
        "num": 2,
        "name": "메기",
        "eng_name": "MEGI",
        "naming_cntry": "한국",
        "influence": "없음",
        "generationDt": "2022.04.10",
        "extinctionDt": "2022.04.12",
        "desc": "제2호 태풍 메기(MEGI)는 한국에서 제출한 이름으로 메기를 의미함."
    },
    {
        "num": 3,
        "name": "차바",
        "eng_name": "CHABA",
        "naming_cntry": "태국",
        "influence": "없음",
        "generationDt": "2022.06.30",
        "extinctionDt": "2022.07.03",
        "desc": "제3호 태풍 차바(CHABA)는 태국에서 제출한 이름으로 꽃의 한 종류임."
    },
    {
        "num": 4,
        "name": "에어리",
        "eng_name": "AERE",
        "naming_cntry": "미국",
        "influence": "직접영향",
        "generationDt": "2022.07.01",
        "extinctionDt": "2022.07.05",
        "desc": "제4호 태풍 에어리(AERE)는 미국에서 제출한 이름으로 폭풍을 의미함."
    }
]

@app.get("/typhoon")
async def search_typhoon(
    num: Optional[int] = Query(None, description="호수"),
    name: Optional[str] = Query(None, description="태풍 이름"),
    influence: Optional[str] = Query(None, description="영향도(ex: 없음, 직접영향, 상륙 등)"),
    startDt: Optional[str] = Query(None, description="최소 발생연도(m~n년 사이에 발생한 태풍 검색 시 사용. 발생날짜를 바탕으로 검색.)"),
    endDt: Optional[str] = Query(None, description="최대 발생연도(m~n년 사이에 발생한 태풍 검색 시 사용. 발생날짜를 바탕으로 검색.)"),
    naming_cntry: Optional[str] = Query(None, description="작명 국가")
) -> List[dict]:
    results = []
    for typhoon in typhoon_data:
        if num is not None and num != typhoon["num"]:
            continue
        if name is not None and name != typhoon["name"]:
            continue
        if influence is not None and influence != typhoon["influence"]:
            continue
        if startDt is not None and startDt > typhoon["generationDt"]:
            continue
        if endDt is not None and endDt < typhoon["generationDt"]:
            continue
        if naming_cntry is not None and naming_cntry != typhoon["naming_cntry"]:
            continue
        results.append(typhoon)
    return results


particulate_matter_data = [
    {
        "ctprvNm": "서울특별시",
        "sgngNm": "은평구",
        "grade": "양호",
        "density": 17,
        "fine_density": 16
    },
    {
        "ctprvNm": "서울특별시",
        "sgngNm": "서대문구",
        "grade": "좋음",
        "density": 16,
        "fine_density": 7
    },
    {
        "ctprvNm": "서울특별시",
        "sgngNm": "중구",
        "grade": "좋음",
        "density": 13,
        "fine_density": 13
    },
    {
        "ctprvNm": "서울특별시",
        "sgngNm": "양천구",
        "grade": "나쁨",
        "density": 74,
        "fine_density": 10
    },
    {
        "ctprvNm": "서울특별시",
        "sgngNm": "동작구",
        "grade": "보통",
        "density": 42,
        "fine_density": 11
    },
    {
        "ctprvNm": "서울특별시",
        "sgngNm": "광진구",
        "grade": "좋음",
        "density": 20,
        "fine_density": 13
    }
]

@app.get("/particulate_matter")
async def search_particulate_matter(
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    grade: Optional[str] = Query(None, description="등급"),
    min_density: Optional[float] = Query(None, gt=0, description="최소 미세먼지 농도"),
    max_density: Optional[float] = Query(None, gt=0, description="최대 미세먼지 농도"),
    min_fine_density: Optional[float] = Query(None, gt=0, description="최소 초미세먼지 농도"),
    max_fine_density: Optional[float] = Query(None, gt=0, description="최대 초미세먼지 농도")
) -> List[dict]:
    results = []
    for data in particulate_matter_data:
        if ctprvNm is not None and ctprvNm != data["ctprvNm"]:
            continue
        if sgngNm is not None and sgngNm != data["sgngNm"]:
            continue
        if grade is not None and grade != data["grade"]:
            continue
        if min_density is not None and min_density > data["density"]:
            continue
        if max_density is not None and max_density < data["density"]:
            continue
        if min_fine_density is not None and min_fine_density > data["fine_density"]:
            continue
        if max_fine_density is not None and max_fine_density < data["fine_density"]:
            continue
        results.append(data)
    return results

convenience_device_data = [
    {
        "line": 1,
        "name": "서울역",
        "locker": 3,
        "cvlisMchn": 1,
        "atm": 0,
        "vndngMchn": 1,
        "autoCamera": 1,
        "exchangeKiosk": 0
    },
    {
        "line": 1,
        "name": "시청역",
        "locker": 2,
        "cvlisMchn": 1,
        "atm": 0,
        "vndngMchn": 1,
        "autoCamera": 0,
        "exchangeKiosk": 0
    },
    {
        "line": 1,
        "name": "종각역",
        "locker": 2,
        "cvlisMchn": 2,
        "atm": 1,
        "vndngMchn": 1,
        "autoCamera": 1,
        "exchangeKiosk": 0
    },
    {
        "line": 2,
        "name": "을지로입구역",
        "locker": 2,
        "cvlisMchn": 1,
        "atm": 0,
        "vndngMchn": 1,
        "autoCamera": 1,
        "exchangeKiosk": 2
    },
    {
        "line": 2,
        "name": "홍대입구역",
        "locker": 5,
        "cvlisMchn": 2,
        "atm": 0,
        "vndngMchn": 1,
        "autoCamera": 1,
        "exchangeKiosk": 2
    },
    {
        "line": 2,
        "name": "신촌역",
        "locker": 3,
        "cvlisMchn": 3,
        "atm": 1,
        "vndngMchn": 1,
        "autoCamera": 1,
        "exchangeKiosk": 1
    },
    {
        "line": 3,
        "name": "경복궁역",
        "locker": 2,
        "cvlisMchn": 1,
        "atm": 0,
        "vndngMchn": 1,
        "autoCamera": 1,
        "exchangeKiosk": 1
    },
    {
        "line": 3,
        "name": "안국역",
        "locker": 2,
        "cvlisMchn": 1,
        "atm": 0,
        "vndngMchn": 1,
        "autoCamera": 1,
        "exchangeKiosk": 1
    }
]

@app.get("/convenience_device")
async def search_convenience_device(
    line: Optional[int] = Query(None, description="호선"),
    name: Optional[str] = Query(None, description="역명"),
    min_locker: Optional[int] = Query(None, ge=0, description="물품보관함 수"),
    max_locker: Optional[int] = Query(None, ge=0, description="물품보관함 수"),
    min_atm: Optional[int] = Query(None, ge=0, description="현급지급기 수"),
    max_atm: Optional[int] = Query(None, ge=0, description="현급지급기 수"),
    min_cvlisMchn: Optional[int] = Query(None, ge=0, description="무인민원발급기 수"),
    max_cvlisMchn: Optional[int] = Query(None, ge=0, description="무인민원발급기 수"),
    min_vndngMchn: Optional[int] = Query(None, ge=0, description="위생용품자판기 수"),
    max_vndngMchn: Optional[int] = Query(None, ge=0, description="위생용품자판기 수"),
    min_autoCamera: Optional[int] = Query(None, ge=0, description="자동사진기 수"),
    max_autoCamera: Optional[int] = Query(None, ge=0, description="자동사진기 수"),
    min_exchangeKiosk: Optional[int] = Query(None, ge=0, description="무인환전키오스크 수"),
    max_exchangeKiosk: Optional[int] = Query(None, ge=0, description="무인환전키오스크 수"),
) -> List[dict]:
    results = []
    for data in convenience_device_data:
        if line is not None and line != data["line"]:
            continue
        if name is not None and name != data["name"]:
            continue
        if min_locker is not None and min_locker > data["locker"]:
            continue
        if max_locker is not None and max_locker < data["locker"]:
            continue
        if min_atm is not None and min_atm > data["atm"]:
            continue
        if max_atm is not None and max_atm < data["atm"]:
            continue
        if min_cvlisMchn is not None and min_cvlisMchn > data["cvlisMchn"]:
            continue
        if max_cvlisMchn is not None and max_cvlisMchn < data["cvlisMchn"]:
            continue
        if min_vndngMchn is not None and min_vndngMchn > data["vndngMchn"]:
            continue
        if max_vndngMchn is not None and max_vndngMchn < data["vndngMchn"]:
            continue
        if min_autoCamera is not None and min_autoCamera > data["autoCamera"]:
            continue
        if max_autoCamera is not None and max_autoCamera < data["autoCamera"]:
            continue
        if min_exchangeKiosk is not None and min_exchangeKiosk > data["exchangeKiosk"]:
            continue
        if max_exchangeKiosk is not None and max_exchangeKiosk < data["exchangeKiosk"]:
            continue
        results.append(data)
    return results

element_data = [
    {"num": 1, "symbol": "H", "name": "수소", "eng_name": "Hydrogen", "group": 1, "period": 1},
    {"num": 2, "symbol": "He", "name": "헬륨", "eng_name": "Helium", "group": 18, "period": 1},
    {"num": 3, "symbol": "Li", "name": "리튬", "eng_name": "Lithium", "group": 1, "period": 2},
    {"num": 4, "symbol": "Be", "name": "베릴륨", "eng_name": "Beryllium", "group": 2, "period": 2},
    {"num": 5, "symbol": "B", "name": "붕소", "eng_name": "Boron", "group": 13, "period": 2},
    {"num": 6, "symbol": "C", "name": "탄소", "eng_name": "Carbon", "group": 14, "period": 2},
    {"num": 7, "symbol": "N", "name": "질소", "eng_name": "Nitrogen", "group": 15, "period": 2},
    {"num": 8, "symbol": "O", "name": "산소", "eng_name": "Oxygen", "group": 16, "period": 2},
    {"num": 9, "symbol": "F", "name": "플루오린", "eng_name": "Fluorine", "group": 17, "period": 2},
    {"num": 10, "symbol": "Ne", "name": "네온", "eng_name": "Neon", "group": 18, "period": 2},
]

@app.get("/element")
async def search_element(
    num: Optional[int] = Query(None, description="원자 번호"),
    symbol: Optional[str] = Query(None, description="기호(ex: H, He, Li 등)"),
    name: Optional[str] = Query(..., description="원소명"),
    group: Optional[int] = Query(None, ge=1, le=18, description="족"),
    period: Optional[int] = Query(None, ge=1, le=7, description="주기"),
) -> List[dict]:
    results = []
    for data in element_data:
        if num is not None and num != data["num"]:
            continue
        if symbol is not None and symbol != data["symbol"]:
            continue
        if name is not None and name != data["name"]:
            continue
        if group is not None and group != data["group"]:
            continue
        if period is not None and period != data["period"]:
            continue
        results.append(data)
    return results

grad_project_data = [
    {
        "name": "Vegan",
        "team_members": ["김민준", "이서연"],
        "professor": "Park",
        "year": 2022,
        "semester": 2,
        "language": ["Java", "R"],
        "desc": "비건지향인들을 위한 앱 서비스"
    },
    {
        "name": "Welfare",
        "team_members": ["장서준", "임도윤", "구예준"],
        "professor": "Lee",
        "year": 2022,
        "semester": 2,
        "language": ["Java", "Python"],
        "desc": "복지 정보를 얻을 수 있는 챗봇 서비스"
    },
    {
        "name": "Tagg",
        "team_members": ["류지우", "김하윤", "박민서"],
        "professor": "Na",
        "year": 2022,
        "semester": 2,
        "language": ["C", "C++", "Java"],
        "desc": "최저가 쇼핑 검색 모바일 앱"
    },
    {
        "name": "Dot",
        "team_members": ["서채원", "이준서"],
        "professor": "Kim",
        "year": 2022,
        "semester": 1,
        "language": ["Java", "Python", "PHP"],
        "desc": "점자 번역 애플리케이션"
    },
    {
        "name": "Food",
        "team_members": ["심우진", "이수아", "김지호"],
        "professor": "Jang",
        "year": 2022,
        "semester": 1,
        "language": ["Java", "Python"],
        "desc": "식단 관리 모바일 앱"
    },
    {
        "name": "Sign Lang",
        "team_members": ["김건우", "심지아", "구선우"],
        "professor": "Lim",
        "year": 2022,
        "semester": 1,
        "language": ["Python"],
        "desc": "수화 통역 애플리케이션"
    },
]

@app.get("/grad_project")
async def search_grad_project(
    name: Optional[str] = Query(..., description="프로젝트명"),
    student: Optional[str] = Query(None, description="팀원명"),
    professor: Optional[str] = Query(None, description="담당 교수명"),
    year: Optional[int] = Query(None, description="연도"),
    semester: Optional[int] = Query(None, ge=1, le=2, description="학기"),
    language: Optional[str] = Query(None, description="사용 언어"),
) -> List[dict]:
    results = []
    for data in grad_project_data:
        if name is not None and name != data["name"]:
            continue
        if student is not None and student not in data["team_members"]:
            continue
        if professor is not None and professor != data["professor"]:
            continue
        if year is not None and year != data["year"]:
            continue
        if semester is not None and semester != data["semester"]:
            continue
        if language is not None and language not in data["language"]:
            continue
        results.append(data)
    return results

olympic_data = [
    {
        "type": "하계",
        "country": "영국",
        "city": "런던",
        "openingDt": "2012-07-27",
        "closingDt": "2021-08-12",
        "slogan": "Inspire a Generation (시대에게 영감을)"
    },
    {
        "type": "하계",
        "country": "브라질",
        "city": "리우데자네이루",
        "openingDt": "2016-08-05",
        "closingDt": "2016-08-21",
        "slogan": "Um mundo novo (새로운 세계)"
    },
    {
        "type": "하계",
        "country": "일본",
        "city": "도쿄",
        "openingDt": "2021-07-23",
        "closingDt": "2021-08-08",
        "slogan": "感動で、私たちはひとつになる (감동으로 우리는 하나가 된다)"
    },
    {
        "type": "동계",
        "country": "러시아",
        "city": "소치",
        "openingDt": "2014-02-07",
        "closingDt": "2014-02-23",
        "slogan": "Жаркие. Зимние. Твои (열기, 시원함을, 당신에게)"
    },
    {
        "type": "동계",
        "country": "대한민국",
        "city": "평창",
        "openingDt": "2018-02-09",
        "closingDt": "2018-02-25",
        "slogan": "하나된 열정 (Passion. Connected.)"
    },
    {
        "type": "동계",
        "country": "중국",
        "city": "베이징",
        "openingDt": "2022-02-04",
        "closingDt": "2022-02-20",
        "slogan": "一起向未来 (함께하는 미래로)"
    },
]

@app.get("/olympic")
async def search_olympic(
    type: Optional[str] = Query(..., description="분류"),
    country: Optional[str] = Query(None, description="개최국"),
    city: Optional[str] = Query(None, description="도시"),
    strtYr: Optional[str] = Query(None, description="최소 개최 연도(개회일을 바탕으로 검색)"),
    endYr: Optional[str] = Query(None, description="최대 개최 연도(개회일을 바탕으로 검색)")
) -> List[dict]:
    results = []
    for data in olympic_data:
        if type is not None and type != data["type"]:
            continue
        if country is not None and country != data["country"]:
            continue
        if city is not None and city != data["city"]:
            continue
        if strtYr is not None and strtYr > data["openingDt"]:
            continue
        if endYr is not None and endYr < data["openingDt"]:
            continue
        results.append(data)
    return results

silver_town_data = [
    {
        "name": "서울시니어스 서울타워",
        "address": "서울특별시 중구 다산로 72",
        "households": 138,
        "phone": "02-2254-1221",
        "cnstrYr": 1998
    },
    {
        "name": "노블레스타워",
        "address": "서울특별시 성북구 종암로 90",
        "households": 239,
        "phone": "02-910-6090",
        "cnstrYr": 2008
    },
    {
        "name": "더클래식500",
        "address": "서울특별시 광진구 능동로 90",
        "households": 380,
        "phone": "02-2218-5526",
        "cnstrYr": 2009
    },
    {
        "name": "삼성노블카운티",
        "address": "경기도 용인시 기흥구 하갈동 490",
        "households": 553,
        "phone": "031-208-8000",
        "cnstrYr": 2001
    },
    {
        "name": "스프링카운티자이",
        "address": "경기도 용인시 기흥구 동백죽전대로 333",
        "households": 1345,
        "phone": "031-8067-6017",
        "cnstrYr": 2019
    },
    {
        "name": "유당마을",
        "address": "경기도 수원시 장안구 수일로 191번길 26",
        "households": 247,
        "phone": "031-242-0079",
        "cnstrYr": 1988
    },
]

@app.get("/silver_town")
async def search_silver_town(
    ctprvNm: str = Query(..., description="시도명"),
    sgngNm: Optional[str] = Query(None, description="시군구명"),
    name: Optional[str] = Query(None, description="시설명"),
    min_households: Optional[int] = Query(None, description="최소 세대수"),
    max_households: Optional[int] = Query(None, description="최대 세대수")
) -> List[dict]:
    results = []
    for data in silver_town_data:
        if ctprvNm != data["address"].split()[0]:
            continue
        if sgngNm is not None and sgngNm != data["address"].split()[1]:
            continue
        if name is not None and name != data["name"]:
            continue
        if min_households is not None and min_households > data["households"]:
            continue
        if max_households is not None and max_households < data["households"]:
            continue
        results.append(data)
    return results

personality_test_data = [
    {
        "company": "삼성",
        "name": "GSAT",
        "q_num": 50,
        "time": 60,
        "subjects": ["수리논리", "추리"]
    },
    {
        "company": "SK그룹",
        "name": "SKCT",
        "q_num": 450,
        "time": 145,
        "subjects": ["실행역량", "인지역량", "심층역량"]
    },
    {
        "company": "CJ그룹",
        "name": "CJAT",
        "q_num": 80,
        "time": 100,
        "subjects": ["언어", "수리", "추리", "공간 지각"]
    },
    {
        "company": "KT",
        "name": "KT 종합인적성검사",
        "q_num": 85,
        "time": 90,
        "subjects": ["언어적 사고", "수리적 사고", "문제해결"]
    },
    {
        "company": "LG",
        "name": "LG Way Fit Test",
        "q_num": 243,
        "time": 60,
        "subjects": ["언어이해", "언어추리", "자료해석", "창의수리", "인성검사"]
    },
]

@app.get("/personality_test")
async def search_personality_test(
    company: str = Query(..., description="기업명"),
    name: Optional[str] = Query(None, description="시험명"),
    min_questions: Optional[int] = Query(None, description="최소 문항수"),
    max_questions: Optional[int] = Query(None, description="최대 문항수"),
    min_time: Optional[int] = Query(None, description="최소 시험시간 (단위: 분)"),
    max_time: Optional[int] = Query(None, description="최대 시험시간 (단위: 분)"),
    subject: Optional[str] = Query(None, description="과목명")
) -> List[dict]:
    results = []
    for data in personality_test_data:
        if company != data["company"]:
            continue
        if name is not None and name != data["name"]:
            continue
        if min_questions is not None and min_questions > data["q_num"]:
            continue
        if max_questions is not None and max_questions < data["q_num"]:
            continue
        if min_time is not None and min_time > data["time"]:
            continue
        if max_time is not None and max_time < data["time"]:
            continue
        if subject is not None and subject not in data["subjects"]:
            continue
        results.append(data)
    return results

air_purifier_data = [
    {
        "name": "노블 공기청정기(50㎡)",
        "brand": "coway",
        "contract_period": 72,
        "monthly_fee": 34900,
        "grade": 4.9,
        "review_num": 415
    },
    {
        "name": "듀얼클린 가습공기청정기",
        "brand": "coway",
        "contract_period": 36,
        "monthly_fee": 30400,
        "grade": 4.9,
        "review_num": 128
    },
    {
        "name": "아이콘 공기청정기",
        "brand": "coway",
        "contract_period": 36,
        "monthly_fee": 35900,
        "grade": 4.9,
        "review_num": 52
    },
    {
        "name": "퓨리케어 공기청정기 10평",
        "brand": "LG",
        "contract_period": 60,
        "monthly_fee": 13900,
        "grade": 5.0,
        "review_num": 16
    },
    {
        "name": "퓨리케어 360° 공기청정기 알파 오브제컬렉션 35평 (펫 필터)",
        "brand": "LG",
        "contract_period": 60,
        "monthly_fee": 44900,
        "grade": 5.0,
        "review_num": 13
    },
    {
        "name": "퓨리케어 에어로타워 오브제컬렉션_선풍+온풍",
        "brand": "LG",
        "contract_period": 60,
        "monthly_fee": 37900,
        "grade": 5.0,
        "review_num": 2
    },
]

@app.get("/air_purifier")
async def search_air_purifier(
    name: Optional[str] = Query(None, description="제품명"),
    brand: Optional[str] = Query(None, description="브랜드"),
    min_contract_period: int = Query(..., description="최소 약정 기간 (단위: 개월)"),
    max_contract_period: Optional[int] = Query(None, description="최대 약정 기간 (단위: 개월)"),
    min_fee: Optional[int] = Query(None, description="최소 월 렌탈료"),
    max_fee: Optional[int] = Query(None, description="최대 월 렌탈료"),
    min_grade: Optional[float] = Query(None, description="최소 평점"),
    max_grade: Optional[float] = Query(None, description="최대 평점"),
):
    results = []
    for data in air_purifier_data:
        if name and name != data["name"]:
            continue
        if brand and brand != data["brand"]:
            continue
        if data["contract_period"] < min_contract_period:
            continue
        if max_contract_period and data["contract_period"] > max_contract_period:
            continue
        if min_fee and data["monthly_fee"] < min_fee:
            continue
        if max_fee and data["monthly_fee"] > max_fee:
            continue
        if min_grade and data["grade"] < min_grade:
            continue
        if max_grade and data["grade"] > max_grade:
            continue
        results.append(data)
    return results

samsungsvc_data = [
    {
        "name": "을지로휴대폰센터",
        "address": "서울 중구 을지로 51 교원내외빌딩 5층",
        "congestion": "혼잡",
        "products": ["스마트폰", "태블릿", "웨어러블기기"],
        "subway_station": "을지로입구역"
    },
    {
        "name": "용산센터",
        "address": "서울 용산구 한강대로 314 삼성스토어 용산 2층",
        "congestion": "혼잡",
        "products": ["스마트폰", "태블릿", "웨어러블기기", "노트북", "PC", "모니터", "프린터", "TV", "홈시어터", "오디오", "DVD", "카메라", "캠코더", "오븐/전자레인지", "기타 소형가전"],
        "subway_station": "숙대입구역"
    },
    {
        "name": "삼선교휴대폰센터",
        "address": "서울 성북구 동소문로 47 삼성스토어 삼선교 2층",
        "congestion": "혼잡",
        "products": ["스마트폰", "태블릿", "웨어러블기기"],
        "subway_station": "한성대입구역"
    },
    {
        "name": "홍대휴대폰센터",
        "address": "서울 마포구 양화로 171 삼성스토어 홍대 4층",
        "congestion": "혼잡",
        "products": ["스마트폰", "태블릿", "웨어러블기기", "노트북", "PC", "모니터", "프린터"],
        "subway_station": "홍대입구역"
    },
    {
        "name": "성남센터",
        "address": "경기 성남시 수정구 산성대로 81 삼성스토어 성남 3층",
        "congestion": "혼잡",
        "products": ["스마트폰", "태블릿", "웨어러블기기", "PC", "노트북", "모니터", "프린터", "TV", "홈시어터", "오디오", "DVD", "오븐/전자레인지", "더 플레이트 인덕션(휴대용)", "기타 소형가전"],
        "subway_station": "모란역"
    },
    {
        "name": "분당휴대폰센터",
        "address": "경기 성남시 분당구 황새울로311번길 28 라포르테블랑서현 1층",
        "congestion": "혼잡",
        "products": ["스마트폰", "태블릿", "웨어러블기기", "노트북", "PC", "모니터", "프린터"],
        "subway_station": "서현역"
    }
]

@app.get("/samsungsvc")
async def search_samsungsvc(
    ctprvNm: str = Query(..., description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="센터명"),
    congestion: Optional[str] = Query(None, description="혼잡도"),
    item: Optional[str] = Query(None, description="제품명(수리 제품을 바탕으로 검색)"),
) -> List[dict]:
    results = []
    for data in samsungsvc_data:
        if ctprvNm and ctprvNm != data["address"].split()[0]:
            continue
        if sgngNm and sgngNm != data["address"].split()[1]:
            continue
        if name and name != data["name"]:
            continue
        if congestion and congestion != data["congestion"]:
            continue
        if item and item not in data["products"]:
            continue
        results.append(data)
    return results

waterpark_data = [
    {
        "name": "캐리비안 베이",
        "address": "경기도 용인시 처인구 포곡읍 에버랜드로 199",
        "grade": 4.0,
        "review_num": 237,
        "reviews": ["완전 꿀잼임", "어린아이에게도 좋은 워터파크", "좁은데 사람이 너무 많아요"]
    },
    {
        "name": "설악 워터피아",
        "address": "강원도 속초시 미시령로2983번길 111",
        "grade": 4.0,
        "review_num": 91,
        "reviews": ["넘 좋아요", "아이들과 함께 가기 좋은 곳", "한적하게 물놀이 가능합니다."]
    },
    {
        "name": "롯데워터파크",
        "address": "경상남도 김해시 장유로 555",
        "grade": 4.0,
        "review_num": 34,
        "reviews": ["부산,경남 최대 롯데워터파크", "언제나 즐거운곳", "놀기 좋아요"]
    },
    {
        "name": "경주 캘리포니아비치",
        "address": "경상북도 경주시 보문로 544",
        "grade": 4.0,
        "review_num": 25,
        "reviews": ["아이들이 잘 놀아요.", "여름 휴가로 연인과 친구들과 가기에 좋습니다.", "이곳을 이용하면 놀이동산을 같이 이용할 수 있다는 장점이 있습니다"]
    },
    {
        "name": "비발디파크 오션월드",
        "address": "강원도 홍천군 서면 한치골길 262",
        "grade": 4.0,
        "review_num": 107,
        "reviews": ["Good but parking was really bad.", "비내리는 겨울에도 놀기 좋은 곳", "신나게 하루 놀았어요"]
    }
]

@app.get("/waterpark")
async def search_waterpark(
    name: Optional[str] = Query(None, description="워터파크명"),
    ctprvNm: str = Query(..., description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    min_grade: Optional[float] = Query(None, ge=0, le=5, description="최소 평점"),
    max_grade: Optional[float] = Query(None, ge=0, le=5, description="최대 평점")
) -> List[dict]:
    results = []
    for data in waterpark_data:
        if name and name != data["name"]:
            continue
        if ctprvNm and ctprvNm not in data["address"]:
            continue
        if sgngNm and sgngNm not in data["address"]:
            continue
        if min_grade and data["grade"] < min_grade:
            continue
        if max_grade and data["grade"] > max_grade:
            continue
        results.append(data)
    return results

post_office_data = [
    {
        "name": "광화문우체국",
        "address": "서울 종로구 종로 6 (서린동)",
        "phone": "02-3703-9011",
        "fund_sale": True,
        "atm": True
    },
    {
        "name": "우정총국",
        "address": "서울 종로구 우정국로 59 (견지동)",
        "phone": "02-734-8369",
        "fund_sale": False,
        "atm": False
    },
    {
        "name": "서울중앙우체국",
        "address": "서울 중구 소공로 70 (충무로1가)",
        "phone": "02-6450-1114",
        "fund_sale": True,
        "atm": True
    },
    {
        "name": "서울도봉우체국",
        "address": "서울 도봉구 노해로 150",
        "phone": "02-3499-3600",
        "fund_sale": True,
        "atm": False
    },
    {
        "name": "서수원우체국",
        "address": "경기 수원시 권선구 호매실로 22-55(탑동)",
        "phone": "031-8020-0702",
        "fund_sale": False,
        "atm": True
    },
    {
        "name": "성남우체국",
        "address": "경기 성남시 수정구 산성대로 301",
        "phone": "031-743-0014",
        "fund_sale": True,
        "atm": True
    },
    {
        "name": "인천연수동우체국",
        "address": "인천 연수구 비류대로 436 (연수동)",
        "phone": "032-812-2105",
        "fund_sale": False,
        "atm": True
    }
]

@app.get("/post_office")
async def search_post_office(
    ctprvNm: str = Query(..., description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="우체국명"),
    fund_sale: Optional[bool] = Query(None, description="펀드 판매 여부"),
    atm: Optional[bool] = Query(None, description="365코너 설치 여부")
) -> List[dict]:
    results = []
    for data in post_office_data:
        if ctprvNm and ctprvNm not in data["address"]:
            continue
        if sgngNm and sgngNm not in data["address"]:
            continue
        if name and name != data["name"]:
            continue
        if fund_sale is not None and fund_sale != data["fund_sale"]:
            continue
        if atm is not None and atm != data["atm"]:
            continue
        results.append(data)
    return results

national_park_data = [
    {
        "name": "지리산국립공원",
        "num": 1,
        "address": "경상남도 산청군 시천면 남명로 376",
        "desc": "지리산은 언제나 어머니 품처럼 깊고 따뜻합니다. 노고단에서 천왕봉에 이르는 25킬러미터 종주길은 누구나 한 번쯤 가보고 싶어하는 탐방로입니다.",
        "courses": [
            "노고단 코스",
            "정령치-바래봉 코스",
            "만복대 코스",
            "화엄계곡 코스",
            "피아골 코스",
            "반야봉 코스",
            "불일폭포 코스"
        ]
    },
    {
        "name": "경주국립공원",
        "num": 2,
        "address": "경상북도 경주시 천북남로 12",
        "desc": "경주시의 8개 자연생태ㆍ문화유산지구를 국립공원으로 지정한 것입니다. 불국사와 석굴암 등 우리가 잘 알고 있는 문화재들이 국립공원에 속해 있습니다.",
        "courses": [
            "관음사 코스",
            "신선사 코스",
            "암곡 코스",
            "삼불사 코스",
            "용장골 코스",
            "불국사 코스",
            "삼릉 코스"
        ]
    },
    {
        "name": "계룡산국립공원",
        "num": 3,
        "address": "충청남도 공주시 반포면 동학사1로 327-6",
        "desc": "풍수지리상 명산으로 이름난 계룡산은 능선이 마치 닭벼슬을 쓴 용의 모습을 닮아 이름지어졌다고 합니다. 대전 도심과 가까워 많은 시민이 찾고 있는 최고의 자연휴양지입니다.",
        "courses": [
            "신원사 코스",
            "동학사 코스",
            "수통골 코스",
            "갑사 코스",
            "천정 코스"
        ]
    },
    {
        "name": "한려해상국립공원",
        "num": 4,
        "address": "경상남도 사천시 사천대로 173(실안동 888)",
        "desc": "한려해상은 거제 지심도에서 여수 오동도까지 300리 뱃길을 따라 크고 작은 섬들을 국립공원으로 지정한 우리나라 최초의 해상국립공원입니다.",
        "courses": [
            "금산 1코스",
            "금산자연관찰로",
            "해금강 코스",
            "소매물도 등대길 코스",
            "지심도 코스",
            "야소 ~ 망산 코스",
            "진두 ~ 덮을개 코스"
        ]
    },
    {
        "name": "설악산국립공원",
        "num": 5,
        "address": "강원도 속초시 설악산로 833",
        "desc": "기암괴석으로 둘러싸인 협곡을 흐르는 물줄기와 바위틈 곳곳에서 자라는 나무들이 한 데 어우러져 설악산의 멋진 풍경을 만들어냅니다.",
        "courses": [
            "울산바위 코스",
            "남교리 코스",
            "대승폭포 코스",
            "대청봉 코스(한계령)",
            "비룡폭포(토왕폭전망대)",
            "대청봉 코스(설악동)"
        ]
    },
    {
        "name": "속리산국립공원",
        "num": 6,
        "address": "충청북도 보은군 속리산면 법주사로 84",
        "desc": "'속세를 떠난다'는 속리산은 조선 세조 이야기에 담겨있는 문장대와 정이품송, 법주사가 있습니다. 법주사에는 팔상전과 석연지 등 국보와 보물이 많아 탐방가치가 높습니다.",
        "courses": [
            "장성봉 코스",
            "칠보산 코스",
            "도명산2 코스",
            "장각동 코스",
            "문장대1 코스",
            "군자산 코스",
            "도명산1 코스",
            "옥녀봉 코스",
            "대야산 코스",
            "묘봉 코스",
            "백악산 코스",
            "불목이옛길"
        ]
    }
]

@app.get("/national_park")
async def search_national_park(
    ctprvNm: str = Query(..., description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="국립공원명"),
    num: Optional[int] = Query(None, description="호수"),
    course: Optional[str] = Query(None, description="코스명(탐방 코스를 바탕으로 검색)")
):
    results = []
    for item in data:
        if ctprvNm is not None and ctprvNm != item[2]:
            continue
        if sgngNm is not None and sgngNm != item[3]:
            continue
        if name is not None and name != item[0]:
            continue
        if num is not None and num != item[1]:
            continue
        if course is not None and course not in item[4]:
            continue
        results.append({
            "name": item[0],
            "num": item[1],
            "address": item[2],
            "desc": item[3],
            "courses": item[4]
        })
    return results


whiskey_data = [
    {
        "name": "Jack Daniel's Gentleman Jack",
        "type": "Tennessee Whiskey",
        "cask": ["American Oak"],
        "abv": 40,
        "flavors": ["Vanilla", "Coal", "Sweet", "Smooth", "Spice"]
    },
    {
        "name": "Teeling Blackpitts",
        "type": "Single Malt",
        "cask": ["Bourbon cask", "Sauternes"],
        "abv": 46,
        "flavors": ["Pineapple", "Smoke", "Pear", "Fruit", "Yellow"]
    },
    {
        "name": "Brenne Cuvee Speciale",
        "type": "Single Malt",
        "cask": ["Cognac", "European Oak"],
        "abv": 40,
        "flavors": ["Bubblegum", "Sweet", "Vanilla", "Banana", "Candy"]
    },
    {
        "name": "Midleton Barry Crockett Legacy",
        "type": "Single Pot Still",
        "cask": ["Bourbon cask"],
        "abv": 46,
        "flavors": ["Fruit", "Delicate", "Light", "Honey", "Toffee"]
    },
    {
        "name": "Tomatin Decades",
        "type": "Single Malt",
        "cask": ["Bourbon cask", "Sherry"],
        "abv": 46,
        "flavors": ["Fruit", "Vanilla", "Cream", "Oak", "Apple"]
    },
    {
        "name": "W.L. Weller 12 Year Old",
        "type": "Bourbon",
        "cask": ["American Oak"],
        "abv": 45,
        "flavors": ["Vanilla", "Sweet", "Spice", "Oak", "Apple"]
    },
    {
        "name": "Maker’s Mark 46",
        "type": "Bourbon",
        "cask": ["American Oak"],
        "abv": 47,
        "flavors": ["Vanilla", "Sweet", "Apple", "Bourbon", "Light"]
    }
]

@app.get("/whiskey")
async def search_whiskey(
    name: Optional[str] = Query(None, description="제품명"),
    type: Optional[str] = Query(None, description="유형(ex: Single Malt, Bourbon 등)"),
    cask: Optional[str] = Query(None, description="캐스크"),
    min_abv: float = Query(..., description="최소 도수 (단위: %)"),
    max_abv: Optional[float] = Query(None, description="최대 도수 (단위: %)")
):
    results = []
    for item in whiskey_data:
        if name is not None and name != item["name"]:
            continue
        if type is not None and type != item["type"]:
            continue
        if cask is not None and cask not in item["cask"]:
            continue
        if item["abv"] < min_abv:
            continue
        if max_abv is not None and item["abv"] > max_abv:
            continue
        results.append({
            "name": item["name"],
            "type": item["type"],
            "cask": item["cask"],
            "abv": item["abv"],
            "flavors": item["flavors"]
        })
    return results

spcl_high_school_data = [
    {
        "name": "국립국악고등학교",
        "establishment": "국립",
        "type": "예술계열",
        "gender": "공학",
        "address": "서울특별시 강남구 개포로22길 65 (개포동)",
        "phone": "02-3460-0500",
        "url": "https://gugak.sen.hs.kr/"
    },
    {
        "name": "서울공연예술고등학교",
        "establishment": "사립",
        "type": "예술계열",
        "gender": "공학",
        "address": "서울특별시 구로구 오리로22나길 16-26 (궁동)",
        "phone": "02-3281-9760",
        "url": "https://www.sopa.hs.kr/"
    },
    {
        "name": "대원외국어고등학교",
        "establishment": "사립",
        "type": "외국어계열",
        "gender": "공학",
        "address": "서울특별시 광진구 용마산로22길 26 (중곡동)",
        "phone": "02-2204-1530",
        "url": "http://www.dwfl.hs.kr/"
    },
    {
        "name": "이화여자외국어고등학교",
        "establishment": "사립",
        "type": "외국어계열",
        "gender": "여",
        "address": "서울특별시 중구 통일로4길 30 (순화동)",
        "phone": "02-2176-1992",
        "url": "https://ewha-gfh.hs.kr/"
    },
    {
        "name": "서울로봇고등학교",
        "establishment": "공립",
        "type": "마이스터고",
        "gender": "공학",
        "address": "서울특별시 강남구 광평로20길 63 (일원동)",
        "phone": "02-2226-2141",
        "url": "https://srobot.sen.hs.kr/"
    },
    {
        "name": "한성과학고등학교",
        "establishment": "공립",
        "type": "과학계열",
        "gender": "공학",
        "address": "서울특별시 서대문구 통일로 279-79 (현저동)",
        "phone": "02-6917-0000",
        "url": "https://hansungsh.sen.hs.kr/"
    },
    {
        "name": "서울국제고등학교",
        "establishment": "공립",
        "type": "국제계열",
        "gender": "공학",
        "address": "서울특별시 종로구 성균관로13길 40 (명륜1가)",
        "phone": "02-743-9385",
        "url": "https://sghs.sen.hs.kr/"
    },
    {
        "name": "서울체육고등학교",
        "establishment": "공립",
        "type": "체육계열",
        "gender": "공학",
        "address": "서울특별시 송파구 강동대로 232 (방이동)",
        "phone": "02-2140-9801",
        "url": "https://seoul-ph.sen.hs.kr/"
    }
]

@app.get("/spcl_high_school")
def search_specialized_high_school(
    gu: str = Query(..., description="서울시 행정구역명(ex: 강남구, 중구 등)"),
    establishment: Optional[str] = Query(None, description="설립 구분(ex: 국립, 사립, 공립)"),
    school_type: Optional[str] = Query(None, description="유형(ex: 예술계열, 과학계열, 외국어계열, 마이스터고, 국제계열, 체육계열)"),
    gender: Optional[str] = Query(None, description="성별(ex: 공학, 여, 남)"),
    name: Optional[str] = Query(None, description="학교명"),
):
    results = []
    for item in spcl_high_school_data:
        if gu and gu not in item["address"]:
            continue
        if establishment and establishment != item["establishment"]:
            continue
        if school_type and school_type != item["type"]:
            continue
        if gender and gender != item["gender"]:
            continue
        if name and name.lower() not in item["name"].lower():
            continue
        results.append({
            "name": item["name"],
            "establishment": item["establishment"],
            "type": item["type"],
            "gender": item["gender"],
            "address": item["address"],
            "phone": item["phone"],
            "url": item["url"]
        })
    return results

pet_youtube_data = [
    ["김메주와 고양이들", 622000, 1200, "오늘도 평화로운 메주네☀️", "https://www.youtube.com/c/MejooandCats"],
    ["무지막지한 막무家네 ", 534000, 327, "무지와 막지의 일상을 담은 막무家네 채널입니다 :-)", "https://www.youtube.com/@mujimakji"],
    ["Arirang은 고양이들내가 주인", 639000, 569, "혹시 개인적인 문의사항이 있으시면 aricat2488@gmail.com 이쪽으로 메일 주시면 가끔 아리가 메일을 열어봅니다.", "https://www.youtube.com/@arirang3"],
    ["MochaMilk", 1640000, 380, "모카와 우유의 일상을 함께 봐주셔서 감사합니다 :)", "https://www.youtube.com/@mochamilk"],
    ["순덕순덕", 120000, 363, "말티즈 순심, 비숑 덕선, 푸들 삼순의 행복한 유튜브 채널입니다.", "https://www.youtube.com/@sundeoksundeok"],
    ["[THE SOY]루퐁이네", 2130000, 549, "안녕하세요 쌈바요정 루디씨와 옭옭쟁이 퐁키의 유튜브채널입니다.", "https://www.youtube.com/@rupong"]
]

@app.get("/pet_youtube")
def search_pet_youtube(
    name: Optional[str] = Query(None, description="채널명"),
    min_subscribers: Optional[int] = Query(None, description="최소 구독자수", gt=0),
    max_subscribers: Optional[int] = Query(None, description="최대 구독자수", gt=0),
    min_videos: Optional[int] = Query(None, description="최소 영상수", gt=0),
    max_videos: Optional[int] = Query(None, description="최대 영상수", gt=0),
) -> List[dict]:
    results = []
    for item in pet_youtube_data:
        if name and name.lower() not in item[0].lower():
            continue
        if min_subscribers and item[1] < min_subscribers:
            continue
        if max_subscribers and item[1] > max_subscribers:
            continue
        if min_videos and item[2] < min_videos:
            continue
        if max_videos and item[2] > max_videos:
            continue
        results.append({
            "name": item[0],
            "subscribers": item[1],
            "videos": item[2],
            "desc": item[3],
            "url": item[4]
        })
    return results

spcl_edu_school_data = [
    ["서울맹학교", "국립", ["시각장애"], "서울특별시 종로구 필운대로 97", "https://bl.sen.sc.kr/"],
    ["한국구화학교", "사립", ["청각장애", "지적장애"], "서울특별시 강동구 고덕로 295-59", "https://kuhwa.sen.sc.kr/"],
    ["한빛맹학교", "사립", ["시각장애"], "서울특별시 강북구 삼양로73가길 47", "https://hanbit.sen.sc.kr/"],
    ["아름학교", "공립", ["시각장애", "지적장애"], "경기도 수원시 영통구 광교로 32", "https://areum.sc.kr/"],
    ["한국선진학교", "국립", ["지적장애"], "경기도 안산시 상록구 이호로 113", "https://seonjin.sc.kr/"],
    ["부천혜림학교", "사립", ["지적장애"], "경기도 부천시 소사구 경인로304번길 26", "https://haelim-s.goebc.kr/haelim-s/main.do"]
]

@app.get("/spcl_edu_school")
def search_special_education_school(
    ctprvNm: str = Query(..., description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="학교명"),
    establishment: Optional[str] = Query(None, description="설립 구분(ex: 국립, 사립, 공립)"),
    target: Optional[str] = Query(None, description="대상자(ex: 시각장애, 지적장애 등)"),
) -> List[dict]:
    results = []
    for item in spcl_edu_school_data:
        if ctprvNm.lower() not in item[3].lower():
            continue
        if sgngNm and sgngNm.lower() not in item[3].lower():
            continue
        if name and name.lower() not in item[0].lower():
            continue
        if establishment and establishment.lower() not in item[1].lower():
            continue
        if target and target.lower() not in [t.lower() for t in item[2]]:
            continue
        results.append({
            "name": item[0],
            "establishment": item[1],
            "target": item[2],
            "address": item[3],
            "url": item[4]
        })
    return results

online_shopping_data = [
    {
        "category": "의류",
        "name": "슬로우앤드",
        "style": ["캠퍼스룩", "심플베이직"],
        "free_shipping": False,
        "best_items": ["솔트 클린 반팔티셔츠", "세로니팅 반오픈 버튼티셔츠", "썸머 에어롱핏 데님팬츠"],
        "url": "https://www.slowand.com/"
    },
    {
        "category": "의류",
        "name": "김아홉",
        "style": ["빈티지", "유니크"],
        "free_shipping": True,
        "best_items": ["linen oatmeal pt", "sahara pleats dress", "V whisper open blouse"],
        "url": "https://www.9hope.kr/"
    },
    {
        "category": "의류",
        "name": "베이델리",
        "style": ["심플베이직", "러블리"],
        "free_shipping": True,
        "best_items": ["빈티지 우드 워싱 데님 반바지", "러블리 레이스 프릴 나시", "캔디 반팔 셔츠 원피스"],
        "url": "https://beidelli.com/"
    },
    {
        "category": "가방",
        "name": "론네바이론",
        "style": ["유니크"],
        "free_shipping": True,
        "best_items": ["타티백", "링크백", "제크백 크로스 숄더백"],
        "url": "https://lonnebyron.com/"
    },
    {
        "category": "신발",
        "name": "꼼꼼구두",
        "style": ["모던시크"],
        "free_shipping": True,
        "best_items": ["슈슈 스퀘어 리본 뮬 슬리퍼(2cm)", "릿츠 스퀘어 버클 스트랩 샌들(6.5cm)", "태그 라탄 배색 슬리퍼(1.5cm)"],
        "url": "https://ccomccomshoes.com/"
    },
    {
        "category": "신발",
        "name": "잇슈",
        "style": ["심플베이직"],
        "free_shipping": False,
        "best_items": ["2way 스퀘어 셔링 디테일 통굽 슬리퍼 샌들(4.0cm)", "사선스트랩 플랫폼 통굽슬리퍼(6.0cm)", "어글리 스포티 깍지버클 통굽 플랫폼 샌들(7.4cm)"],
        "url": "https://itshu.co.kr/"
    }
]


@app.get("/online_shopping")
async def search_online_shopping_mall(
    category: str = Query(..., description="카테고리(ex: 의류, 가방 등)"),
    name: Optional[str] = Query(None, description="쇼핑몰 이름"),
    style: Optional[str] = Query(None, description="스타일(ex: 심플베이직, 유니크 등)"),
    free_shipping: Optional[bool] = Query(None, description="무료배송 여부"),
    item: Optional[str] = Query(None, description="상품명(인기 상품을 바탕으로 검색)")
) -> List[dict]:
    results = []
    for d in online_shopping_data:
        if d["category"] == category:
            if name and d["name"] != name:
                continue
            if style and style not in d["style"]:
                continue
            if free_shipping is not None and d["free_shipping"] != free_shipping:
                continue
            if item and item not in d["best_items"]:
                continue
            results.append(d)
    return results

cleaner_data = [
    {
        "name": "LG 코드제로 오브제컬렉션 A9S",
        "brand": "LG전자",
        "category": "핸디스틱청소기",
        "wire": "무선",
        "price": 1790000,
        "colors": ["카밍베이지"]
    },
    {
        "name": "다이슨 V10 앱솔루트",
        "brand": "다이슨",
        "category": "핸디스틱청소기",
        "wire": "무선",
        "price": 1275000,
        "colors": ["블루", "코퍼", "블랙"]
    },
    {
        "name": "LG 싸이킹 K8",
        "brand": "LG전자",
        "category": "진공청소기",
        "wire": "유선",
        "price": 365000,
        "colors": ["카밍 베이지"]
    },
    {
        "name": "BESPOKE 제트 220W",
        "brand": "삼성전자",
        "category": "핸디스틱청소기",
        "wire": "무선",
        "price": 1349000,
        "colors": ["페블 그레이", "산토리니 베이지", "모닝 블루"]
    },
    {
        "name": "파워모션 4100",
        "brand": "삼성전자",
        "category": "진공청소기",
        "wire": "유선",
        "price": 259000,
        "colors": ["그리너리"]
    }
]


@app.get("/cleaner")
async def search_cleaner(
    name: Optional[str] = Query(None, description="제품명"),
    brand: Optional[str] = Query(None, description="브랜드"),
    category: Optional[str] = Query(None, description="카테고리"),
    wire: Optional[str] = Query(None, description="무선유선방식"),
    min_price: int = Query(..., description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격")
) -> List[dict]:
    results = []
    for d in cleaner_data:
        if name and d["name"] != name:
            continue
        if brand and d["brand"] != brand:
            continue
        if category and d["category"] != category:
            continue
        if wire and d["wire"] != wire:
            continue
        if min_price is not None and d["price"] < min_price:
            continue
        if max_price is not None and d["price"] > max_price:
            continue
        results.append(d)
    return results

vegan_restaurant_data = [
    {
        "name": "카페시바",
        "category": "퓨전음식",
        "address": "서울 용산구 한강대로 276-1 1층",
        "phone": "0507-1352-1339",
        "menu": ["슈프림 양념 후라이드", "비건 수제함벅 라구 파스타", "비건새우 오일 파스타", "청양 두부 꿔바로우"]
    },
    {
        "name": "두수고방",
        "category": "음식점",
        "address": "경기 수원시 영통구 광교호수공원로 80 앨리웨이광교 어라운드 라이프 3층",
        "phone": "031-548-1912",
        "menu": ["두수고방 원테이블 다이닝"]
    },
    {
        "name": "뜰안채채식뷔페",
        "category": "샐러드뷔페",
        "address": "경기 용인시 기흥구 용구대로2335번길 25",
        "phone": "031-281-5879",
        "menu": ["런치 뷔페", "디너 뷔페"]
    },
    {
        "name": "남미플랜트랩",
        "category": "퓨전음식",
        "address": "서울 서초구 방배천로4안길 55 2층",
        "phone": "02-522-1276",
        "menu": ["치즈야채 피자", "파스타베르데", "가지멜란자네피자"]
    },
    {
        "name": "거북이",
        "category": "카페/디저트",
        "address": "서울 서초구 방배천로4안길 48 1층",
        "phone": "070-4015-5314",
        "menu": ["아메리카노", "두유 크림라떼", "귀리 크림라떼"]
    },
    {
        "name": "플랜튜드 아이파크몰 용산점",
        "category": "퓨전음식",
        "address": "서울 용산구 한강대로23길 55 용산역 아이파크몰 테이스트파크 7층",
        "phone": "0507-1390-0798",
        "menu": ["트러플 감태 크림 떡볶이", "구운 알배추 컬리플라워 샐러드", "순두부 인 헬"]
    }
]


@app.get("/vegan_restaurant")
async def search_vegan_restaurant(
    ctprvNm: str = Query(..., description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    category: Optional[str] = Query(None, description="카테고리"),
    name: Optional[str] = Query(None, description="식당명"),
    menu: Optional[str] = Query(None, description="메뉴명(대표 메뉴를 바탕으로 검색)")
) -> List[dict]:
    results = []
    for d in vegan_restaurant_data:
        if ctprvNm and d["address"].startswith(ctprvNm):
            continue
        if sgngNm and sgngNm not in d["address"]:
            continue
        if category and d["category"] != category:
            continue
        if name and d["name"] != name:
            continue
        if menu and menu not in d["menu"]:
            continue
        results.append(d)
    return results

festival_data = [
    {
        "name": "서울재즈페스티벌 2023",
        "startDt": "2023-05-26",
        "endDt": "2023-05-28",
        "place": "서울특별시 송파구 올림픽로 424 올림픽공원",
        "price_fulltime": 420000,
        "price_oneday": 187000,
        "platform": ["인터파크"],
        "lineup": ["Mika", "Christopher", "AJR", "폴킴", "새소년"]
    },
    {
        "name": "월드 디제이 페스티벌 2023",
        "startDt": "2023-06-02",
        "endDt": "2023-06-04",
        "place": "경기도 과천시 광명로 181 서울랜드",
        "price_fulltime": 229000,
        "price_oneday": 119000,
        "platform": ["위메프"],
        "lineup": ["GALANTIS", "THE QREATOR", "NICKY ROMERO", "ZEDD", "VINI VICI"]
    },
    {
        "name": "뷰티풀 민트 라이프 2023",
        "startDt": "2023-05-13",
        "endDt": "2023-05-14",
        "place": "서울특별시 송파구 올림픽로 424 올림픽공원",
        "price_fulltime": 220000,
        "price_oneday": 110000,
        "platform": ["인터파크", "예스24", "위메프"],
        "lineup": ["10CM", "하현상", "LUCY", "소란", "선우정아"]
    },
    {
        "name": "해브어나이스데이 #9",
        "startDt": "2023-04-15",
        "endDt": "2023-04-16",
        "place": "서울특별시 용산구 양녕로 445 노들섬",
        "price_fulltime": 198000,
        "price_oneday": 99000,
        "platform": ["인터파크", "예스24"],
        "lineup": ["HYNN(박혜원)", "소란", "치즈", "정승환", "유다빈밴드"]
    },
    {
        "name": "러브썸 페스티벌 2023",
        "startDt": "2023-04-22",
        "endDt": "2023-04-23",
        "place": "서울특별시 송파구 올림픽로 25 잠실 올림픽주경기장",
        "price_fulltime": 198000,
        "price_oneday": 99000,
        "platform": ["예스24", "네이버"],
        "lineup": ["멜로망스", "적재", "정승환", "이적", "비투비"]
    },
    {
        "name": "피크 페스티벌 2023",
        "startDt": "2023-05-27",
        "endDt": "2023-05-28",
        "place": "서울시 마포구 한강난지로 162 난지한강공원",
        "price_fulltime": 139000,
        "price_oneday": 99000,
        "platform": ["인터파크", "예스24"],
        "lineup": ["10CM", "선우정아", "NELL", "기현", "소란"]
    }
]


@app.get("/festival")
async def search_festival(
    name: Optional[str] = Query(None, description="페스티벌명"),
    place: Optional[str] = Query(None, description="장소"),
    min_price_full: Optional[int] = Query(None, description="최소 전일권 가격"),
    max_price_full: Optional[int] = Query(None, description="최대 전일권 가격"),
    min_price_oneday: int = Query(..., description="최소 1일권 가격"),
    max_price_oneday: Optional[int] = Query(None, description="최대 1일권 가격"),
    artist: Optional[str] = Query(None, description="아티스트명(라인업을 바탕으로 검색)")
) -> List[dict]:
    results = []
    for d in festival_data:
        if name and d["name"] != name:
            continue
        if place and d["place"] != place:
            continue
        if min_price_full and d["price_fulltime"] < min_price_full:
            continue
        if max_price_full and d["price_fulltime"] > max_price_full:
            continue
        if d["price_oneday"] < min_price_oneday:
            continue
        if max_price_oneday and d["price_oneday"] > max_price_oneday:
            continue
        if artist and artist not in d["lineup"]:
            continue
        results.append(d)
    return results

disaster_alert_data = [
    {
        "type": "자연재난",
        "subclass": "호우",
        "area": "서울특별시 노원구",
        "sendingDt": "2023-06-29",
        "level": "안전안내",
        "msg": "[노원구] 하천수위 상승으로 중랑천,당현천,우이천,묵동천 출입을 금지합니다. 특히 산사태위험지역 및 지하주택 등 침수취약지역의 주민은 안전에 유의하시기 바랍니다."
    },
    {
        "type": "자연재난",
        "subclass": "산사태",
        "area": "전라북도 정읍시",
        "sendingDt": "2023-06-28",
        "level": "안전안내",
        "msg": "[정읍시청] 금일 09시경 산내면 장금리 933-1 사실재터널(산내-순창방면) 산사태로 인해 도로 통제중이니,통행차량은 국도30호선으로 우회하여 주시기 바랍니다."
    },
    {
        "type": "사회재난",
        "subclass": "교통통제",
        "area": "경기도 이천시 창전동",
        "sendingDt": "2023-06-27",
        "level": "안전안내",
        "msg": "[이천시청]설봉중(향교로 117) 공사 중 가설구조물 일부 붕괴로 17시~내일 오전 10시까지 설봉푸르지오2차입구~설봉중사거리 도로 통제 예정이오니 우회 바랍니다"
    },
    {
        "type": "자연재난",
        "subclass": "산사태",
        "area": "서울특별시",
        "sendingDt": "2023-06-29",
        "level": "안전안내",
        "msg": "[산림청] 오늘 전국에 많은 비가 예보되어 산사태 위험이 높습니다. 산림 주변 야외활동을 자제하시고 산에 있을 경우 산림 밖으로 피하시는 등 안전에 유의바랍니다."
    },
    {
        "type": "기타재난",
        "subclass": "기타",
        "area": "경기도 수원시 팔달구",
        "sendingDt": "2023-06-28",
        "level": "안전안내",
        "msg": "[경기남부경찰청] 수원시에서 배회중인 신희준씨(남, 52세)를 찾습니다 -170cm, 55kg, 파란색반팔,반바지(잠옷) vo.la/GynnF /"
    }
]

@app.get("/disaster_alert")
async def search_disaster_alert(
    type: Optional[str] = Query(None, description="재난 분류"),
    subclass: Optional[str] = Query(None, description="재난 상세"),
    ctprvNm: str = Query(..., description="시도명"),
    sgngNm: Optional[str] = Query(None, description="시군구명"),
    min_dt: Optional[str] = Query(None, description="최소 발송일"),
    max_dt: Optional[str] = Query(None, description="최대 발송일")
) -> List[dict]:
    results = []
    for item in disaster_alert_data:
        if type and item["type"] != type:
            continue
        if subclass and item["subclass"] != subclass:
            continue
        if item["area"] != ctprvNm:
            continue
        if sgngNm and item["area"] != sgngNm:
            continue
        if min_dt and item["sendingDt"] < min_dt:
            continue
        if max_dt and item["sendingDt"] > max_dt:
            continue
        results.append(item)
    return results

playlist_data = [
    {
        "title": "미소가 저절로 나오게 만드는 노래들로만 가져왔어요",
        "category": ["해외 팝", "신나는"],
        "songs_num": 13,
        "likes": 535,
        "comments": ["별로 기대 안하고 눌렀는데 미소가 번지네옇ㅎ", "진짜 넘 좋아요", "전부 다 좋아요!"]
    },
    {
        "title": "듣자마자 내적댄스 갈기는 여돌 플리",
        "category": ["국내 댄스/일렉", "신나는"],
        "songs_num": 81,
        "likes": 175,
        "comments": ["아이브짱", "대박", "내가 칮던 그런 플레이리스트"]
    },
    {
        "title": "어깨가 들썩들썩이게 하는 드라이빙 팝송",
        "category": ["해외 팝", "드라이브", "상쾌한"],
        "songs_num": 114,
        "likes": 544,
        "comments": ["이 플리 너무 좋네요", "좋은 선곡 감사합니다"]
    },
    {
        "title": "저녁 향수 뿌린 인디에 취해",
        "category": ["국내 인디", "잔잔한"],
        "songs_num": 16,
        "likes": 11,
        "comments": ["첫 곡부터 너무 좋다", "잠들기 전 듣기 좋네요"]
    },
    {
        "title": "상쾌한 아침 공기 가득 담은 청정 팝",
        "category": ["해외 팝", "아침", "상쾌한"],
        "songs_num": 22,
        "likes": 1067,
        "comments": ["좋은 팝송 찾고 있었는데 너무 좋아요!", "항상 잘 듣고 있어요"]
    }
]

@app.get("/playlist")
async def search_playlist(
    title: Optional[str] = Query(None, description="플레이리스트 제목"),
    category: Optional[str] = Query(None, description="카테고리"),
    min_songs: int = Query(..., description="최소 곡수", gt=0),
    max_songs: Optional[int] = Query(None, description="최대 곡수", gt=0),
    min_likes: Optional[int] = Query(None, description="최소 좋아요수", ge=0),
    max_likes: Optional[int] = Query(None, description="최대 좋아요수", ge=0)
) -> List[dict]:
    results = []
    for item in playlist_data:
        if title and title.lower() not in item["title"].lower():
            continue
        if category and category.lower() not in [c.lower() for c in item["category"]]:
            continue
        if item["songs_num"] < min_songs:
            continue
        if max_songs and item["songs_num"] > max_songs:
            continue
        if min_likes and item["likes"] < min_likes:
            continue
        if max_likes and item["likes"] > max_likes:
            continue
        results.append(item)
    return results

subway_data = [
    {
        "name": "써브웨이 클럽",
        "calorie": 299,
        "ingredients": ["치킨 브레스트 햄", "햄", "베이컨", "치즈", "각종 야채"],
        "desc": "고소한 베이컨, 담백한 치킨 슬라이스에 햄까지 더해진 완벽한 앙상블",
        "sauce": ["랜치", "스위트 어니언"]
    },
    {
        "name": "베지",
        "calorie": 209,
        "ingredients": ["각종 야채", "치즈"],
        "desc": "갓 구운 빵과 신선한 8가지 야채로 즐기는 깔끔한 한끼",
        "sauce": ["레드와인식초", "올리브오일"]
    },
    {
        "name": "스테이크 앤 치즈",
        "calorie": 355,
        "ingredients": ["스테이크", "치즈", "각종 야채"],
        "desc": "육즙이 쫙~풍부한 비프 스테이크의 풍미가 입안 한가득",
        "sauce": ["사우스웨스트 치폴레", "마요네즈"]
    },
    {
        "name": "스파이시 이탈리안",
        "calorie": 464,
        "ingredients": ["페퍼로니", "살라미", "치즈", "각종 야채"],
        "desc": "살라미, 페퍼로니가 입안 한가득! 쏘 핫한 이탈리아의 맛",
        "sauce": ["랜치", "스위트 어니언"]
    },
    {
        "name": "에그마요",
        "calorie": 416,
        "ingredients": ["에그마요", "치즈", "각종 야채"],
        "desc": "부드러운 달걀과 고소한 마요네즈가 만나 더 부드러운 스테디셀러",
        "sauce": ["랜치", "스위트 칠리"]
    },
    {
        "name": "쉬림프",
        "calorie": 229,
        "ingredients": ["새우", "치즈", "각종 야채"],
        "desc": "탱글한 식감이 그대로 살아있는 통새우가 5마리 들어가 한 입 베어 먹을 때 마다 진짜 새우의 풍미가 가득",
        "sauce": ["스위트 칠리", "랜치"]
    }
]

@app.get("/subway_menu")
def search_subway_menu(
    name: Optional[str] = Query(None, description="메뉴명"),
    min_calorie: float = Query(..., gt=0, description="최소 칼로리 (단위: kcal)"),
    max_calorie: Optional[float] = Query(None, gt=0, description="최대 칼로리 (단위: kcal)"),
    ingredient: Optional[str] = Query(None, description="재료(주 재료를 바탕으로 검색)"),
    sauce: Optional[str] = Query(None, description="소스(추천 소스를 바탕으로 검색)")
) -> List[dict]:
    results = []
    for item in subway_data:
        if name and name.lower() not in item["name"].lower():
            continue
        if item["calorie"] < min_calorie:
            continue
        if max_calorie and item["calorie"] > max_calorie:
            continue
        if ingredient and ingredient.lower() not in [i.lower() for i in item["ingredients"]]:
            continue
        if sauce and sauce.lower() not in [s.lower() for s in item["sauce"]]:
            continue
        results.append(item)
    return results

earthquake_data = [
    {
        "occurDt": "2023-05-15",
        "occurTm": "06:27:37",
        "magnitude": 4.5,
        "depth": 31,
        "max_intensity": "Ⅲ",
        "latitude": 37.87,
        "longitude": 129.52,
        "location": "강원 동해시 북동쪽 52km 해역"
    },
    {
        "occurDt": "2023-04-25",
        "occurTm": "15:55:55",
        "magnitude": 3.5,
        "depth": 33,
        "max_intensity": "Ⅰ",
        "latitude": 37.86,
        "longitude": 129.49,
        "location": "강원 동해시 북동쪽 50km 해역"
    },
    {
        "occurDt": "2023-01-09",
        "occurTm": "01:28:15",
        "magnitude": 3.7,
        "depth": 19,
        "max_intensity": "Ⅳ",
        "latitude": 37.74,
        "longitude": 126.20,
        "location": "인천 강화군 서쪽 25km 해역"
    },
    {
        "occurDt": "2023-04-19",
        "occurTm": "00:45:07",
        "magnitude": 2.6,
        "depth": 14,
        "max_intensity": "Ⅰ",
        "latitude": 33.09,
        "longitude": 125.42,
        "location": "제주 서귀포시 서쪽 108km 해역"
    },
    {
        "occurDt": "2023-03-03",
        "occurTm": "11:26:54",
        "magnitude": 3.0,
        "depth": 8,
        "max_intensity": "Ⅳ",
        "latitude": 35.21,
        "longitude": 127.94,
        "location": "경남 진주시 서북서쪽 16km 지역"
    },
    {
        "occurDt": "2023-02-11",
        "occurTm": "08:22:01",
        "magnitude": 2.3,
        "depth": 12,
        "max_intensity": "Ⅲ",
        "latitude": 36.52,
        "longitude": 127.85,
        "location": "충북 보은군 동북동쪽 11km 지역"
    }
]

@app.get("/earthquake")
def search_earthquake(
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    min_occurDt: Optional[str] = Query(None, description="최소 발생날짜(m~n년 사이에 발생한 지진 검색 시 사용. 발생날짜를 바탕으로 검색.)"),
    max_occurDt: Optional[str] = Query(None, description="최대 발생날짜(m~n년 사이에 발생한 지진 검색 시 사용. 발생날짜를 바탕으로 검색.)"),
    min_magnitude: Optional[float] = Query(None, ge=0, description="최소 규모"),
    max_magnitude: Optional[float] = Query(None, ge=0, description="최대 규모")
) -> List[dict]:
    results = []
    for item in earthquake_data:
        if ctprvNm and ctprvNm != item.get("location", "").split()[0]:
            continue
        if sgngNm and sgngNm != item.get("location", "").split()[1]:
            continue
        if min_occurDt and min_occurDt > item["occurDt"]:
            continue
        if max_occurDt and max_occurDt < item["occurDt"]:
            continue
        if min_magnitude and item["magnitude"] < min_magnitude:
            continue
        if max_magnitude and item["magnitude"] > max_magnitude:
            continue
        results.append(item)
    return results

upcycling_items = [
    {
        "category": "크로스백",
        "name": "누깍 Cros",
        "ingredient": "카이트 서핑 돛",
        "price": 79000,
        "offline": True
    },
    {
        "category": "지갑",
        "name": "누깍 Lompakko",
        "ingredient": "광고 현수막",
        "price": 39000,
        "offline": True
    },
    {
        "category": "토트백",
        "name": "컨티뉴 브이백",
        "ingredient": "자동차 가죽시트",
        "price": 229000,
        "offline": True
    },
    {
        "category": "크로스백",
        "name": "컨티뉴 네트 텀블러백",
        "ingredient": "폐그물",
        "price": 109000,
        "offline": True
    },
    {
        "category": "백팩",
        "name": "프라이탁 FRINGE",
        "ingredient": "트럭 방수포",
        "price": 394000,
        "offline": True
    },
    {
        "category": "크로스백",
        "name": "프라이탁 JAMIE",
        "ingredient": "트럭 방수포",
        "price": 218000,
        "offline": False
    }
]

@app.get("/upcycling_items")
async def search_upcycling_items(
    category: Optional[str] = Query(None, description="카테고리"),
    name: Optional[str] = Query(None, description="제품명"),
    ingredient: Optional[str] = Query(None, description="재료"),
    min_price: int = Query(..., description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    offline: Optional[bool] = Query(None, description="오프라인 구매 가능 여부")
):
    results = []
    for item in upcycling_items:
        if category and item["category"] != category:
            continue
        if name and item["name"] != name:
            continue
        if ingredient and item["ingredient"] != ingredient:
            continue
        if item["price"] < min_price:
            continue
        if max_price and item["price"] > max_price:
            continue
        if offline is not None and item["offline"] != offline:
            continue
        results.append(item)
    
    return results

icn_dutyfree_brands = [
    {
        "category": "명품 브랜드",
        "brand": "구찌 (GUCCI)",
        "phone": "1577-0371",
        "location": "제1여객터미널 3층 면세지역 28번 게이트 부근",
        "items": ["가방", "지갑", "액세서리"]
    },
    {
        "category": "명품 브랜드",
        "brand": "까르띠에 (CARTIER)",
        "phone": "1661-8778",
        "location": "제1여객터미널 3층 면세지역 27번 게이트 부근",
        "items": ["쥬얼리", "시계"]
    },
    {
        "category": "명품 브랜드",
        "brand": "CHANEL(샤넬)",
        "phone": "080-805-9628",
        "location": "제1여객터미널 3층 면세지역 28번 게이트 부근",
        "items": ["가방", "신발", "의류", "패션액세서리"]
    },
    {
        "category": "향수·화장품",
        "brand": "설화수",
        "phone": "032-743-2151",
        "location": "제2여객터미널 3층 면세지역 252번 게이트 근처",
        "items": ["화장품", "향수"]
    },
    {
        "category": "향수·화장품",
        "brand": "에스티로더",
        "phone": "032-743-2154",
        "location": "제2여객터미널 3층 면세지역 252번 게이트 근처",
        "items": ["화장품", "향수"]
    },
    {
        "category": "주류·담배",
        "brand": "조니워커",
        "phone": "032-743-7584",
        "location": "제2여객터미널 3층 면세지역 249번 게이트 부근",
        "items": ["위스키", "몰트 위스키", "보드카", "진"]
    },
    {
        "category": "주류·담배",
        "brand": "로얄살루트",
        "phone": "032-743-7582",
        "location": "제2여객터미널 3층 면세지역 249번 게이트 부근",
        "items": ["위스키"]
    }
]

@app.get("/icn_dutyfree")
async def search_icn_dutyfree(
    category: str = Query(..., description="카테고리(ex: 명품 브랜드, 향수·화장품, 주류·담배, 패션·액세서리 등)"),
    brand: Optional[str] = Query(None, description="브랜드명"),
    phone: Optional[str] = Query(None, description="연락처"),
    location: Optional[str] = Query(None, description="위치"),
    item: Optional[str] = Query(None, description="상품명(주요 상품을 바탕으로 검색)")
):
    results = []
    for brand_info in icn_dutyfree_brands:
        if category == brand_info["category"]:
            if (
                brand is None or brand.lower() in brand_info["brand"].lower()
            ) and (
                phone is None or phone.lower() in brand_info["phone"].lower()
            ) and (
                location is None or location.lower() in brand_info["location"].lower()
            ) and (
                item is None or any(item.lower() in i.lower() for i in brand_info["items"])
            ):
                results.append(brand_info)
    return results

####

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

# 미국 주식 데이터 리스트
us_stock_list = [
    {
        "company": "마이크로소프트",
        "ticker": "MSFT",
        "price": 339.71,
        "increase": 1.84,
        "per": 35.44,
        "eps": 6.99
    },
    {
        "company": "어도비",
        "ticker": "ADBE",
        "price": 477.58,
        "increase": 0.10,
        "per": 47.17,
        "eps": 10.50
    },
    {
        "company": "애플",
        "ticker": "AAPL",
        "price": 187,
        "increase": 3.04,
        "per": 30.25,
        "eps": 6.11
    },
    {
        "company": "코카콜라",
        "ticker": "KO",
        "price": 61.85,
        "increase": 0.42,
        "per": 25.57,
        "eps": 2.41
    },
    {
        "company": "아마존 닷컴",
        "ticker": "AMZN",
        "price": 130.15,
        "increase": 5.32,
        "per": 10.22,
        "eps": -0.27
    },
    {
        "company": "테슬라",
        "ticker": "TSLA",
        "price": 264.61,
        "increase": 5.15,
        "per": 69.87,
        "eps": 3.73
    },
    {
        "company": "알파벳 CLASS A",
        "ticker": "GOOGL",
        "price": 123.15,
        "increase": 2.6,
        "per": 27.10,
        "eps": 4.56
    }
]


@app.get("/us_stocks")
async def filter_us_stocks(
    company: Optional[str] = Query(None, description="기업명"),
    ticker: Optional[str] = Query(None, description="티커"),
    min_price: Optional[float] = Query(None, description="최소 현재가"),
    max_price: Optional[float] = Query(None, description="최대 현재가"),
    max_increase: Optional[float] = Query(None, description="최대 상승폭"),
    min_increase: Optional[float] = Query(None, description="최소 상승폭"),
    per: Optional[float] = Query(None, description="주가 수익률"),
    eps: Optional[float] = Query(None, description="earnings per share (1주당 이익)")
) -> List[dict]:
    filtered_stocks = []

    for us_stock in us_stock_list:
        if company and company != us_stock["company"]:
            continue
        if ticker and ticker != us_stock["ticker"]:
            continue
        if min_price is not None and min_price > us_stock["price"]:
            continue
        if max_price is not None and max_price < us_stock["price"]:
            continue
        if max_increase is not None and max_increase < us_stock["increase"]:
            continue
        if min_increase is not None and min_increase > us_stock["increase"]:
            continue
        if per is not None and per != us_stock["per"]:
            continue
        if eps is not None and eps != us_stock["eps"]:
            continue

        filtered_stocks.append(us_stock)

    return filtered_stocks

# 개인 캣시터 데이터 리스트
catsitter_list = [
    {
        "시터이름": "오경원",
        "이용가능지역": "성남시",
        "가격": "48000",
        "평점": 5.0,
        "예약가능여부": "N",
        "이용후기": "친절하세요.",
        "연락처": "010-7320-4633"
    },
    {
        "시터이름": "성재숙",
        "이용가능지역": "제주시",
        "가격": "65000",
        "평점": 4.2,
        "예약가능여부": "Y",
        "이용후기": "상냥하세요.",
        "연락처": "010-6252-1750"
    },
    {
        "시터이름": "손주연",
        "이용가능지역": "관악구",
        "가격": "50000",
        "평점": 4.5,
        "예약가능여부": "Y",
        "이용후기": "꼼꼼하시네요.",
        "연락처": "010-4894-5996"
    },
    {
        "시터이름": "서미연",
        "이용가능지역": "진안군",
        "가격": "52000",
        "평점": 3.0,
        "예약가능여부": "Y",
        "이용후기": "시간 약속을 잘 지키지 않으세요.",
        "연락처": "010-5982-6146"
    },
    {
        "시터이름": "배원태",
        "이용가능지역": "담양군",
        "가격": "60000",
        "평점": 4.8,
        "예약가능여부": "Y",
        "이용후기": "아주 만족스러워요.",
        "연락처": "010-1904-6208"
    }
]


@app.get("/catsitter")
async def search_catsitters(
    name: Optional[str] = Query(None, description="시터 이름"),
    area: Optional[str] = Query(None, description="이용 가능 지역"),
    min_price: Optional[str] = Query(None, description="최소 가격"),
    max_price: Optional[str] = Query(None, description="최대 가격"),
    min_rating: Optional[float] = Query(None, description="최소 평점"),
    max_rating: Optional[float] = Query(None, description="최대 평점"),
    available: Optional[str] = Query(None, description="예약 가능 여부"),
) -> List[dict]:
    filtered_catsitters = []

    for catsitter in catsitter_list:
        if name and name != catsitter["시터이름"]:
            continue
        if area and area != catsitter["이용가능지역"]:
            continue
        if min_price and float(min_price) > float(catsitter["가격"]):
            continue
        if max_price and float(max_price) < float(catsitter["가격"]):
            continue
        if min_rating and min_rating > catsitter["평점"]:
            continue
        if max_rating and max_rating < catsitter["평점"]:
            continue
        if available and available != catsitter["예약가능여부"]:
            continue

        filtered_catsitters.append(catsitter)

    return filtered_catsitters

# 개인 도그워커 데이터 리스트
dogwalker_list = [
    {
        "도그워커이름": "오경원",
        "이용가능지역": "성남시",
        "가격": "48000",
        "평점": 5.0,
        "예약가능여부": "N",
        "이용후기": "친절하세요.",
        "연락처": "010-7320-4633"
    },
    {
        "도그워커이름": "성재숙",
        "이용가능지역": "제주시",
        "가격": "65000",
        "평점": 4.2,
        "예약가능여부": "Y",
        "이용후기": "상냥하세요.",
        "연락처": "010-6252-1750"
    },
    {
        "도그워커이름": "손주연",
        "이용가능지역": "관악구",
        "가격": "50000",
        "평점": 4.5,
        "예약가능여부": "Y",
        "이용후기": "꼼꼼하시네요.",
        "연락처": "010-4894-5996"
    },
    {
        "도그워커이름": "서미연",
        "이용가능지역": "진안군",
        "가격": "52000",
        "평점": 3.0,
        "예약가능여부": "Y",
        "이용후기": "시간 약속을 잘 지키지 않으세요.",
        "연락처": "010-5982-6146"
    },
    {
        "도그워커이름": "배원태",
        "이용가능지역": "담양군",
        "가격": "60000",
        "평점": 4.8,
        "예약가능여부": "Y",
        "이용후기": "아주 만족스러워요.",
        "연락처": "010-1904-6208"
    }
]


@app.get("/dogsitter")
async def search_dogwalkers(
    name: Optional[str] = Query(None, description="도그워커 이름"),
    area: Optional[str] = Query(None, description="이용 가능 지역"),
    min_price: Optional[str] = Query(None, description="최소 가격"),
    max_price: Optional[str] = Query(None, description="최대 가격"),
    min_rating: Optional[float] = Query(None, description="최소 평점"),
    max_rating: Optional[float] = Query(None, description="최대 평점"),
    available: Optional[str] = Query(None, description="예약 가능 여부"),
) -> List[dict]:
    filtered_dogwalkers = []

    for dogwalker in dogwalker_list:
        if name and name != dogwalker["도그워커이름"]:
            continue
        if area and area != dogwalker["이용가능지역"]:
            continue
        if min_price and float(min_price) > float(dogwalker["가격"]):
            continue
        if max_price and float(max_price) < float(dogwalker["가격"]):
            continue
        if min_rating and min_rating > dogwalker["평점"]:
            continue
        if max_rating and max_rating < dogwalker["평점"]:
            continue
        if available and available != dogwalker["예약가능여부"]:
            continue

        filtered_dogwalkers.append(dogwalker)

    return filtered_dogwalkers

# 웹툰 데이터 리스트
webtoon_list = [
    {
        "작품명": "즐거우리인생",
        "작가명": "현미씨",
        "연재플랫폼": "네이버웹툰",
        "장르": "일상",
        "이용가능연령": "전체이용가",
        "완결여부": "완결"
    },
    {
        "작품명": "마라샹궈매직",
        "작가명": "쉐프님",
        "연재플랫폼": "네이버웹툰",
        "장르": "개그",
        "이용가능연령": "전체이용가",
        "완결여부": "연재중"
    },
    {
        "작품명": "카드값을숨김",
        "작가명": "유리쿠쿠다스",
        "연재플랫폼": "카카오페이지",
        "장르": "스릴러",
        "이용가능연령": "15세이상",
        "완결여부": "연재중"
    },
    {
        "작품명": "호박고구마",
        "작가명": "김상무상무",
        "연재플랫폼": "만화경",
        "장르": "드라마",
        "이용가능연령": "12세이상",
        "완결여부": "휴재중"
    },
    {
        "작품명": "아미산귀환",
        "작가명": "소인배점소이",
        "연재플랫폼": "레진코믹스",
        "장르": "무협",
        "이용가능연령": "18세이상",
        "완결여부": "연재중"
    }
]

@app.get("/webtoon_search")
def webtoon_search(
    작품명: Optional[str] = Query(None, description="검색하고자 하는 웹툰의 작품 이름"),
    작가명: Optional[str] = Query(None, description="검색하고자 하는 웹툰의 작가 이름"),
    연재플랫폼: Optional[str] = Query(None, description="검색하고자 하는 웹툰의 연재 플랫폼"),
    장르: Optional[str] = Query(None, description="검색하고자 하는 웹툰의 장르 ex) 판타지, 액션, 일상, 스릴러, 개그, 드라마, 무협 등"),
    이용가능연령: Optional[str] = Query(None, description="이용가능연령 ex) 전체이용가, 12세이상, 15세이상, 18세이상"),
    키워드: Optional[str] = Query(None, description="작품의 이름, 설명, 플랫폼, 장르, 이용가능 연령, 완결여부의 설명을 모두 포함해 검색하는 키워드")
) -> List[dict]:
    results = []
    
    for webtoon in webtoon_list:
        if 작품명 and 작품명 != webtoon["작품명"]:
            continue
        if 작가명 and 작가명 != webtoon["작가명"]:
            continue
        if 연재플랫폼 and 연재플랫폼 != webtoon["연재플랫폼"]:
            continue
        if 장르 and 장르 != webtoon["장르"]:
            continue
        if 이용가능연령 and 이용가능연령 != webtoon["이용가능연령"]:
            continue
        if 키워드 and 키워드 not in f"{webtoon['작품명']} {webtoon['작가명']} {webtoon['연재플랫폼']} {webtoon['장르']} {webtoon['이용가능연령']} {webtoon['완결여부']}":
            continue
        
        results.append(webtoon)
    
    return results

# 체육센터 데이터 리스트
sports_center_list = [
    {
        "센터명": "흑석체육센터",
        "지역구": "동작구",
        "상세주소": "서울특별시 동작구 현충로 73",
        "주요시설": "헬스장",
        "주요강습": "헬스",
        "운영시간": "06:00 ~ 22:00",
        "휴관일": "법정공휴일 및 일요일",
        "연락처": "02-823-2273"
    },
    {
        "센터명": "목동다목적체육관",
        "지역구": "중랑구",
        "상세주소": "서울특별시 중랑구 숙선옹주로 66",
        "주요시설": "기구필라테스",
        "주요강습": "필라테스",
        "운영시간": "07:00 ~ 20:00",
        "휴관일": "법정공휴일 및 토요일과 일요일",
        "연락처": "02-949-5577"
    },
    {
        "센터명": "신월문화체육센터",
        "지역구": "양천구",
        "상세주소": "서울특별시 양천구 지양로 47",
        "주요시설": "수영장",
        "주요강습": "수영",
        "운영시간": "05:00 ~ 19:00",
        "휴관일": "법정공휴일",
        "연락처": "02-2605-4093~5"
    },
    {
        "센터명": "성북구민체육관",
        "지역구": "성북구",
        "상세주소": "서울특별시 성북구 화랑로13길 144",
        "주요시설": "베드민턴장",
        "주요강습": "베드민턴",
        "운영시간": "06:00 ~ 22:00",
        "휴관일": "법정공휴일 및 일요일",
        "연락처": "02-909-3497~8"
    },
    {
        "센터명": "대현산체육관",
        "지역구": "성동구",
        "상세주소": "서울특별시 성동구 독서당로63길 44",
        "주요시설": "수영장",
        "주요강습": "아쿠아로빅",
        "운영시간": "09:00 ~ 22:00",
        "휴관일": "휴무 없음",
        "연락처": "02-2204-7681"
    }
]

@app.get("/seoul_public")
def search_seoul_public(
    센터명: Optional[str] = Query(None, description="조회하고자 하는 체육센터의 이름"),
    지역구: Optional[str] = Query(None, description="조회하고자 하는 구 이름 ex)은평구, 서초구, 마포구 등"),
    상세주소: Optional[str] = Query(None, description="조회하고자 하는 센터의 상세 주소 ex) 중랑구 신내로21길, 방이1동 방이동 439-8 등"),
    주요시설: Optional[str] = Query(None, description="센터 내 주요 시설 ex) 헬스장, 기구필라테스, 수영장 등"),
    주요강습: Optional[str] = Query(None, description="센터 내 주요 강습 프로그램 ex) 수영, 아쿠아로빅, 배드민턴, 요가, 필라테스 등")
) -> List[dict]:
    results = []
    
    for center in sports_center_list:
        if 센터명 and 센터명 != center["센터명"]:
            continue
        if 지역구 and 지역구 != center["지역구"]:
            continue
        if 상세주소 and 상세주소 != center["상세주소"]:
            continue
        if 주요시설 and 주요시설 != center["주요시설"]:
            continue
        if 주요강습 and 주요강습 != center["주요강습"]:
            continue
        
        results.append(center)
    
    return results
# 공원 데이터 리스트
park_list = [
    {
        "공원명": "북악산도시자연공원",
        "지역구": "종로구",
        "상세주소": "서울특별시 종로구 부암동 산2-1",
        "주요시설": "주차장",
        "면적": 954553,
        "문의연락처": "02-2148-2832"
    },
    {
        "공원명": "효창근린공원",
        "지역구": "용산구",
        "상세주소": "서울특별시 용산구 효창원로 177-18",
        "주요시설": "농구장",
        "면적": 171294,
        "문의연락처": "02-2199-7608"
    },
    {
        "공원명": "샘말공원",
        "지역구": "관악구",
        "상세주소": "서울특별시 관악구 대학동 산63-1일대 샘말공원",
        "주요시설": "유아숲체험장",
        "면적": 10634,
        "문의연락처": "02-879-6523"
    },
    {
        "공원명": "초안산생태공원",
        "지역구": "도봉구",
        "상세주소": "서울특별시 도봉구 창동 산24",
        "주요시설": "잔디쉼터",
        "면적": 22113,
        "문의연락처": "02-2091-3754"
    },
    {
        "공원명": "금천폭포근린공원",
        "지역구": "금천구",
        "상세주소": "서울특별시 금천구 시흥대로38길 61",
        "주요시설": "캠핑장",
        "면적": 4835,
        "문의연락처": "02-2627-1652"
    }
]

@app.get("/seoul_park")
def search_seoul_park(
    공원명: Optional[str] = Query(None, description="조회하고자 하는 공원의 이름"),
    지역구: Optional[str] = Query(None, description="조회하고자 하는 구 이름 ex)은평구, 서초구, 마포구 등"),
    상세주소: Optional[str] = Query(None, description="조회하고자 하는 공원의 상세 주소 ex) 중랑구 신내로21길, 방이1동 방이동 439-8 등"),
    주요시설: Optional[str] = Query(None, description="공원 내 주요 시설 ex) 캠핑장, 배드민턴장, 잔디쉼터 등"),
    최소면적: Optional[int] = Query(None, description="찾고자 하는 공원 면적의 최소치"),
    최대면적: Optional[int] = Query(None, description="찾고자 하는 공원 면적의 최대치")
) -> List[dict]:
    results = []
    
    for park in park_list:
        if 공원명 and 공원명 != park["공원명"]:
            continue
        if 지역구 and 지역구 != park["지역구"]:
            continue
        if 상세주소 and 상세주소 != park["상세주소"]:
            continue
        if 주요시설 and 주요시설 != park["주요시설"]:
            continue
        if 최소면적 and park["면적"] < 최소면적:
            continue
        if 최대면적 and park["면적"] > 최대면적:
            continue
        
        results.append(park)
    
    return results

# 지진 정보 데이터 리스트
earthquake_list = [
    {
        "발생일자": "2023/06/18",
        "발생시각": "23:39:16",
        "발생위치": "북한 함경북도 길주 북북서쪽 38km 지역",
        "최대진도": 1,
        "규모": 2.3
    },
    {
        "발생일자": "2023/06/17",
        "발생시각": "22:34:38",
        "발생위치": "강원 동해시 북동쪽 50km 해역",
        "최대진도": 1,
        "규모": 2.1
    },
    {
        "발생일자": "2023/06/05",
        "발생시각": "12:42:18",
        "발생위치": "전북 완주군 남쪽 15km 지역",
        "최대진도": 3,
        "규모": 2.1
    },
    {
        "발생일자": "2016/09/12",
        "발생시각": "19:44:32",
        "발생위치": "경북 경주시 남남서쪽 8.2km 지역",
        "최대진도": 5,
        "규모": 5.1
    },
    {
        "발생일자": "2017/11/15",
        "발생시각": "14:29:31",
        "발생위치": "경북 포항시 북구 북쪽 8km 지역",
        "최대진도": 6,
        "규모": 5.4
    }
]

@app.get("/earthquake")
def search_earthquake(
    검색년도: Optional[str] = Query(None, description="조회하고자 하는 지진 발생년도"),
    시도명: Optional[str] = Query(None, description="조회하고자 하는 지진 발생지역 시도 이름 ex) 창원시, 경기도 등"),
    군구명: Optional[str] = Query(None, description="조회하고자 하는 지진 발생지역 군구 이름 ex) 고성군, 무안군, 마포구 등"),
    최대진도: Optional[int] = Query(None, description="최대진도의 표기(로마 숫자가 아닌 일반 숫자로 검색) ex) 1, 2, 3 등"),
    규모: Optional[int] = Query(None, description="지진의 규모")
) -> List[dict]:
    results = []

    for earthquake in earthquake_list:
        if 검색년도 and 검색년도 != earthquake["발생일자"].split("/")[0]:
            continue
        if 시도명 and 시도명 != earthquake["발생위치"].split(" ")[0]:
            continue
        if 군구명 and 군구명 != earthquake["발생위치"].split(" ")[1]:
            continue
        if 최대진도 and 최대진도 != earthquake["최대진도"]:
            continue
        if 규모 and 규모 != earthquake["규모"]:
            continue

        results.append(earthquake)

    return results


# 복숭아 예약 농장 데이터 리스트
peach_farm_list = [
    {
        "농장명": "현철이네",
        "대표명": "신현철",
        "복숭아품종명": "신비복숭아",
        "가격": "60000",
        "예약가능여부": "Y",
        "연락처": "010-5290-5959"
    },
    {
        "농장명": "피치팜팜",
        "대표명": "노승환",
        "복숭아품종명": "납작복숭아",
        "가격": "72000",
        "예약가능여부": "Y",
        "연락처": "010-6289-6620"
    },
    {
        "농장명": "복자네",
        "대표명": "이복희",
        "복숭아품종명": "망고복숭아",
        "가격": "60000",
        "예약가능여부": "Y",
        "연락처": "010-5775-8909"
    },
    {
        "농장명": "별빛도원",
        "대표명": "권태환",
        "복숭아품종명": "마도카복숭아",
        "가격": "58000",
        "예약가능여부": "N",
        "연락처": "010-6151-6807"
    },
    {
        "농장명": "청암농원",
        "대표명": "최정화",
        "복숭아품종명": "양홍장",
        "가격": "50000",
        "예약가능여부": "Y",
        "연락처": "010-9344-9628"
    }
]

@app.get("/paech_farm")
def search_peach_farm(
    농장명: Optional[str] = Query(None, description="검색하고자 하는 농장의 이름"),
    대표명: Optional[str] = Query(None, description="검색하고자 하는 농장의 대표명"),
    복숭아품종명: Optional[str] = Query(None, description="예약하고자 하는 복숭아 품종의 이름"),
    최소가격: Optional[int] = Query(None, description="가격의 최소치"),
    최대가격: Optional[int] = Query(None, description="가격의 최대치"),
    예약가능여부: Optional[str] = Query(None, description="현재 예약이 가능한지 여부 (Y or N)"),
    키워드: Optional[str] = Query(None, description="농장명, 대표명, 복숭아품종명, 가격을 통틀어 검색하는 키워드")
):
    results = []

    for farm in peach_farm_list:
        if 농장명 and 농장명 != farm["농장명"]:
            continue
        if 대표명 and 대표명 != farm["대표명"]:
            continue
        if 복숭아품종명 and 복숭아품종명 != farm["복숭아품종명"]:
            continue
        if 최소가격 is not None and farm["가격"] < 최소가격:
            continue
        if 최대가격 is not None and farm["가격"] > 최대가격:
            continue
        if 예약가능여부 and 예약가능여부 != farm["예약가능여부"]:
            continue
        if 키워드 and 키워드 not in [farm["농장명"], farm["대표명"], farm["복숭아품종명"], str(farm["가격"])]:
            continue

        results.append(farm)

    return results

# 수영장 데이터 리스트
swimming_pool_list = [
    {
        "수영장명": "여의도실내수영장",
        "주소": "서울시 영등포구 국제금융로 79(여의도동 42-1)",
        "이용가격": "5000",
        "레일수": 7,
        "레일길이": 25,
        "연락처": "02-786-0955"
    },
    {
        "수영장명": "홍제스포츠센터",
        "주소": "서울시 서대문구 홍은중앙로 13(홍은1동 48)",
        "이용가격": "4000",
        "레일수": 5,
        "레일길이": 25,
        "연락처": "02-395-4422"
    },
    {
        "수영장명": "안양월드스포츠센터",
        "주소": "경기도 안양 만안구 안양로 329번길 108(만안구 안양3동 900-10)",
        "이용가격": "6000",
        "레일수": 6,
        "레일길이": 20,
        "연락처": "031-441-4310"
    },
    {
        "수영장명": "세종국민체육센터",
        "주소": "세종시 조치원읍 새내8길 115(조치원읍 명리 24-1)",
        "이용가격": "4200",
        "레일수": 6,
        "레일길이": 30,
        "연락처": "044-868-9885"
    },
    {
        "수영장명": "제주종합경기장 실내수영장",
        "주소": "제주시 서광로2길 24(오라1동 1165)",
        "이용가격": "8000",
        "레일수": 8,
        "레일길이": 50,
        "연락처": "064-728-3290"
    }
]

@app.get("/swimming_pool")
def search_swimming_pool(
    수영장명: Optional[str] = Query(None, description="검색하고자 하는 수영장의 이름"),
    지역: Optional[str] = Query(None, description="수영장이 위치한 지역 시,도를 검색시에 사용합니다 ex) 서울시, 고양시"),
    상세주소: Optional[str] = Query(None, description="수영장의 상세 주소입니다(도로명 표기)"),
    최소가격: Optional[int] = Query(None, description="수영장 일일권 이용 최소 가격입니다(원화 기준)"),
    최대가격: Optional[int] = Query(None, description="수영장 일일권 이용 최대가격입니다(원화 기준)"),
    최소레일수: Optional[int] = Query(None, description="수영장의 최소 레일 개수입니다"),
    최대레일수: Optional[int] = Query(None, description="수영장의 최대 레일 개수입니다"),
    최소레일길이: Optional[int] = Query(None, description="수영장의 최소 레일 길이입니다(미터 기준)"),
    최대레일길이: Optional[int] = Query(None, description="수영장의 최대 레일 길이입니다(미터 기준)")
) -> List[dict]:
    results = []

    for pool in swimming_pool_list:
        if 수영장명 and 수영장명 != pool["수영장명"]:
            continue
        if 지역 and 지역 not in pool["주소"]:
            continue
        if 상세주소 and 상세주소 not in pool["주소"]:
            continue
        if 최소가격 is not None and int(pool["이용가격"]) < 최소가격:
            continue
        if 최대가격 is not None and int(pool["이용가격"]) > 최대가격:
            continue
        if 최소레일수 is not None and pool["레일수"] < 최소레일수:
            continue
        if 최대레일수 is not None and pool["레일수"] > 최대레일수:
            continue
        if 최소레일길이 is not None and pool["레일길이"] < 최소레일길이:
            continue
        if 최대레일길이 is not None and pool["레일길이"] > 최대레일길이:
            continue

        results.append(pool)

    return results


# 독립서점 데이터 리스트
bookshop_list = [
    {
        "서점명": "책방연희",
        "대표명": "이지현",
        "주소": "서울특별시 마포구 와우산로35길 3 (서교동) 지하 1층",
        "활동내용": "독서모임",
        "운영시간": "12:00 ~ 19:00",
        "휴무일": "일요일과 법정 공휴일 휴무",
        "웹사이트": "https://www.instagram.com/chaegbangyeonhui/"
    },
    {
        "서점명": "다다르다",
        "대표명": "김승헌",
        "주소": "대전광역시 중구 중교로73번길 6 (은행동) 2층",
        "활동내용": "낭독회",
        "운영시간": "12:00 ~ 22:00",
        "휴무일": "일요일과 월요일 휴무",
        "웹사이트": "http://www.citytraveller.co.kr/"
    },
    {
        "서점명": "조용한흥분색",
        "대표명": "이신재",
        "주소": "전라북도 군산시 옥구읍 옥구남로 11 (선제리)",
        "활동내용": "전시",
        "운영시간": "11:00 ~ 20:00",
        "휴무일": "화요일 휴무",
        "웹사이트": "https://www.instagram.com/colors.ordinaryday/"
    },
    {
        "서점명": "책다방 밭",
        "대표명": "박지원",
        "주소": "전라북도 순창군 동계면 동계로 17-1 (동계면)",
        "활동내용": "독서모임",
        "운영시간": "11:00 ~ 18:00",
        "휴무일": "토요일과 일요일 휴무",
        "웹사이트": "https://www.instagram.com/batt_bookshop/"
    },
    {
        "서점명": "안녕책방",
        "대표명": "백아라",
        "주소": "제주특별자치도 제주시 인다13길 60 (아라일동) 1층",
        "활동내용": "공간대여",
        "운영시간": "11:00~17:00",
        "휴무일": "일요일과 월요일 휴무",
        "웹사이트": "https://www.instagram.com/hihi_books/"
    }
]

@app.get("/indi_library")
async def get_bookshops(
    서점명: Optional[str] = Query(None, description="검색하고자 하는 서점의 이름"),
    대표명: Optional[str] = Query(None, description="검색하고자 하는 서점의 대표명"),
    지역: Optional[str] = Query(None, description="서점이 위치한 지역 시,도를 검색시에 사용합니다 ex) 서울시, 경기도"),
    상세주소: Optional[str] = Query(None, description="서점의 상세 주소입니다(도로명 표기)"),
    활동내용: Optional[str] = Query(None, description="서점에서 진행하는 활동 설명입니다 ex) 독서모임, 낭독회, 전시 등"),
    키워드: Optional[str] = Query(None, description="서점명, 대표명, 활동내용을 통틀어 검색하는 키워드")
) -> List[dict]:
    results = []

    for bookshop in bookshop_list:
        if 서점명 and 서점명 != bookshop["서점명"]:
            continue
        if 대표명 and 대표명 != bookshop["대표명"]:
            continue
        if 지역 and 지역 not in bookshop["주소"]:
            continue
        if 상세주소 and 상세주소 not in bookshop["주소"]:
            continue
        if 활동내용 and 활동내용 != bookshop["활동내용"]:
            continue
        if 키워드 and 키워드 not in bookshop["서점명"] and 키워드 not in bookshop["대표명"] and 키워드 not in bookshop["활동내용"]:
            continue

        results.append(bookshop)

    return results

# 주말농장 데이터 리스트
weekend_farm_list = [
    {
        "농장명": "고덕주말농장",
        "주소": "서울시 강동구 고덕1동 479",
        "분양가": "120000",
        "분양면적": 15,
        "현재분양가능여부": "N",
        "연락처": "010-4214-9347"
    },
    {
        "농장명": "황금주말농장",
        "주소": "서울시 강서구 개화동 497-2",
        "분양가": "100000",
        "분양면적": 16.5,
        "현재분양가능여부": "Y",
        "연락처": "010-3790-1005"
    },
    {
        "농장명": "천수텃밭농원",
        "주소": "서울시 노원구 중계로8길 56",
        "분양가": "450000",
        "분양면적": 14,
        "현재분양가능여부": "Y",
        "연락처": "010-6426-2153"
    },
    {
        "농장명": "웰빙주말농장",
        "주소": "서울시 도봉구 두봉1동 468",
        "분양가": "110000",
        "분양면적": 13,
        "현재분양가능여부": "Y",
        "연락처": "010-6271-3264"
    },
    {
        "농장명": "청계주말농장",
        "주소": "서울시 서초구 원지동530",
        "분양가": "200000",
        "분양면적": 10,
        "현재분양가능여부": "Y",
        "연락처": "010-6273-1234"
    }
]

@app.get("/weekend_farm")
async def get_weekend_farms(
    농장명: Optional[str] = Query(None, description="검색하고자 하는 농장의 이름"),
    지역구: Optional[str] = Query(None, description="농장이 위치한 지역구를 검색시에 사용합니다 ex) 강동구, 도봉구"),
    농장주소: Optional[str] = Query(None, description="농장의 상세 주소입니다(도로명 표기)"),
    최소분양가: Optional[str] = Query(None, description="농장의 최소 분양가입니다(원화 기준)"),
    최대분양가: Optional[str] = Query(None, description="농장의 최대 분양가입니다(원화 기준)"),
    최소분양면적: Optional[int] = Query(None, description="농장의 최소분양면적입니다(제곱미터 단위)"),
    최대분양면적: Optional[int] = Query(None, description="농장의 최대분양면적입니다(제곱미터 단위)"),
    현재분양가능여부: Optional[str] = Query(None, description="현재 분양이 가능한지 여부입니다 Y or N")
) -> List[dict]:
    results = []

    for farm in weekend_farm_list:
        if 농장명 and 농장명 != farm["농장명"]:
            continue
        if 지역구 and 지역구 not in farm["주소"]:
            continue
        if 농장주소 and 농장주소 not in farm["주소"]:
            continue
        if 최소분양가 and 최소분양가 != farm["분양가"]:
            continue
        if 최대분양가 and 최대분양가 != farm["분양가"]:
            continue
        if 최소분양면적 and (not farm.get("분양면적") or farm["분양면적"] < 최소분양면적):
            continue
        if 최대분양면적 and (not farm.get("분양면적") or farm["분양면적"] > 최대분양면적):
            continue
        if 현재분양가능여부 and 현재분양가능여부 != farm["현재분양가능여부"]:
            continue

        results.append(farm)

    return results

# 향수 상품 데이터 리스트
perfume_list = [
    {
        "name": "디올",
        "type": "미스 디올 블루밍 부케 오 드 뚜왈렛",
        "brand": "오 드 뚜왈렛",
        "price": 96000,
        "capacity": 30,
        "rating": 4.5
    },
    {
        "name": "버버리",
        "type": "버버리 히어로",
        "brand": "오 드 퍼퓸",
        "price": 199000,
        "capacity": 100,
        "rating": 4.2
    },
    {
        "name": "딥티크",
        "type": "오 카피탈",
        "brand": "오 드 퍼퓸",
        "price": 255550,
        "capacity": 75,
        "rating": 4.8
    },
    {
        "name": "바이레도",
        "type": "블랑쉬",
        "brand": "오 드 퍼퓸",
        "price": 168300,
        "capacity": 50,
        "rating": 4.0
    },
    {
        "name": "조말론",
        "type": "잉글리쉬 페어 앤 프리지아",
        "brand": "오 드 코롱",
        "price": 250000,
        "capacity": 130,
        "rating": 4.7
    }
]

@app.get("/perfume")
async def filter_perfume(
    brand: Optional[str] = Query(None, description="브랜드"),
    name: Optional[str] = Query(None, description="제품명"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    type: Optional[str] = Query(None, description="향수 종류 ex) 퍼퓸, 오 드 퍼퓸, 오 드 뚜왈렛, 오 드 코롱"),
    capacity: Optional[float] = Query(None, description="용량")
) -> List[dict]:
    results = []

    for perfume in perfume_list:
        if brand and brand != perfume["brand"]:
            continue
        if name and name != perfume["name"]:
            continue
        if max_price and (not perfume.get("price") or perfume["price"] > max_price):
            continue
        if type and type != perfume["type"]:
            continue
        if capacity and (not perfume.get("capacity") or perfume["capacity"] != capacity):
            continue

        results.append(perfume)

    return results

# 영양제 정보 데이터 리스트
supplement_list = [
    {
        "name": "트루포뮬러",
        "type": "위톱",
        "brand": "알약",
        "expiration_date": 20250622,
        "price": 28900,
        "efficacy": "위건강에 도움"
    },
    {
        "name": "심플리케어",
        "type": "알파",
        "brand": "환",
        "expiration_date": 20230825,
        "price": 59800,
        "efficacy": "활력"
    },
    {
        "name": "블랙모어스",
        "type": "액티브 프로바이오틱스플러스면역건강",
        "brand": "가루",
        "expiration_date": 20240408,
        "price": 50000,
        "efficacy": "장건강도움"
    },
    {
        "name": "리얼레시피",
        "type": "홍삼젤리",
        "brand": "젤리",
        "expiration_date": 20250120,
        "price": 41900,
        "efficacy": "면역력 증진"
    },
    {
        "name": "네츄럴플러스",
        "type": "징코+오메가3",
        "brand": "알약",
        "expiration_date": 20250804,
        "price": 28600,
        "efficacy": "눈건강에 도움"
    }
]

@app.get("/supplements")
async def filter_supplements(
    brand: Optional[str] = Query(None, description="브랜드"),
    name: Optional[str] = Query(None, description="제품명"),
    type: Optional[str] = Query(None, description="종류 ex) 알약, 젤리, 가루, 액체"),
    expiration_date: Optional[int] = Query(None, description="유통기한 데이터 형식 yyyymmdd"),
    keyword: Optional[str] = Query(None, description="키워드 ex) 위 건강에 도움, 눈 건강 개선")
) -> List[dict]:
    results = []

    for supplement in supplement_list:
        if brand and brand != supplement["brand"]:
            continue
        if name and name != supplement["name"]:
            continue
        if type and type != supplement["type"]:
            continue
        if expiration_date and (not supplement.get("expiration_date") or supplement["expiration_date"] != expiration_date):
            continue
        if keyword and keyword not in supplement["efficacy"]:
            continue

        results.append(supplement)

    return results

#시계
watch_list = [
    {
        "name": "Omega",
        "size": 43.0,
        "brand": "AQUA TERRA 150M",
        "price": 38600000,
        "material": "세드나 골드 및 레더 스트랩",
        "water_resistance": "Y"
    },
    {
        "name": "TAG HEUER",
        "size": 36.0,
        "brand": "CARRERA DATE",
        "price": 4380000,
        "material": "Steel",
        "water_resistance": "Y"
    },
    {
        "name": "danielwellington",
        "size": 28.0,
        "brand": "PETITE CORNWALL",
        "price": 188000,
        "material": "Steel",
        "water_resistance": "N"
    },
    {
        "name": "ALBA",
        "size": 41.5,
        "brand": "AG8K17X1",
        "price": 135000,
        "material": "Steel",
        "water_resistance": "Y"
    },
    {
        "name": "Emporio Armani",
        "size": 43.0,
        "brand": "SPORTIVO",
        "price": 209000,
        "material": "Steel",
        "water_resistance": "Y"
    }
]

@app.get("/watch")
async def filter_watch(
    brand: Optional[str] = Query(None, description="브랜드"),
    name: Optional[str] = Query(None, description="제품명"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    material: Optional[str] = Query(None, description="시계 소재 ex) 티타늄, 골드, 스틸"),
    water_resistance: Optional[str] = Query(None, description="방수기능 유무 Y or N")
) -> List[dict]:
    results = []

    for watch in watch_list:
        if brand and brand != watch["brand"]:
            continue
        if name and name != watch["name"]:
            continue
        if max_price and (not watch.get("price") or watch["price"] > max_price):
            continue
        if material and material != watch["material"]:
            continue
        if water_resistance and water_resistance != watch["water_resistance"]:
            continue

        results.append(watch)

    return results

# 서울시 주차장 시설 정보 데이터 리스트
parking_lot_list = [
    {
        "name": "잠실종합운동장 주차장",
        "type": "공영주차장",
        "address": "서울 송파구 올림픽로 25 서울종합운동장",
        "운영시간": 24,
        "price": 1200,
        "전화번호": "02-2240-8876"
    },
    {
        "name": "성북로138 주차장",
        "type": "유료주차장",
        "address": "서울 성북구 성북로 138 주차장",
        "운영시간": 24,
        "price": 900,
        "전화번호": "0507-1387-3781"
    },
    {
        "name": "연남2 공영주차장",
        "type": "공영주차장",
        "address": "서울 마포구 동교동 147-74",
        "운영시간": 11,
        "price": 1500,
        "전화번호": "02-1234-5678"
    },
    {
        "name": "문래근린공원공영주차장",
        "type": "공영주차장",
        "address": "서울 영등포구 당산로 1",
        "운영시간": 24,
        "price": 1500,
        "전화번호": "02-2650-1435"
    },
    {
        "name": "동작대교노상공영주차장",
        "type": "공영주차장",
        "address": "서울 동작구 동작대로 335",
        "운영시간": 9,
        "price": 1560,
        "전화번호": "02-1111-2222"
    }
]

@app.get("/parking_lot")
async def filter_parking_lot(
    gu: Optional[str] = Query(None, description="지역구분_구"),
    dong: Optional[str] = Query(None, description="지역구분_동"),
    name: Optional[str] = Query(None, description="주차장 명"),
    parking_type: Optional[str] = Query(None, description="주차장 종류 ex) 공영주차장, 유료주차장, 노상주차장"),
    operating_hours: Optional[int] = Query(None, description="운영시간 데이터 형식 00시~00시"),
    min_price: Optional[int] = Query(None, description="최소가격 ex) 시간당 1200원")
) -> List[dict]:
    results = []

    for parking_lot in parking_lot_list:
        if gu and gu != parking_lot.get("gu"):
            continue
        if dong and dong != parking_lot.get("dong"):
            continue
        if name and name != parking_lot.get("name"):
            continue
        if parking_type and parking_type != parking_lot.get("type"):
            continue
        if operating_hours and operating_hours != parking_lot.get("운영시간"):
            continue
        if min_price and (not parking_lot.get("price") or parking_lot.get("price") < min_price):
            continue

        results.append(parking_lot)

    return results

# 화장품 데이터 리스트
cosmetics_list = [
    {
        "name": "비플레인",
        "type": "토너",
        "brand": "시카테롤 토너",
        "price": 24000,
        "유통기한": 250523,
        "성분": "병풀추출물"
    },
    {
        "name": "에스네이처",
        "type": "선크림",
        "brand": "아쿠아 365 유브이 선크림",
        "price": 11900,
        "유통기한": 250206,
        "성분": "판테놀"
    },
    {
        "name": "삐아",
        "type": "쿠션",
        "brand": "네버 다이 쿠션",
        "price": 10750,
        "유통기한": 240809,
        "성분": "아데노신"
    },
    {
        "name": "이즈앤트리",
        "type": "크림",
        "brand": "히알루론산 아쿠아 젤크림",
        "price": 13900,
        "유통기한": 26012,
        "성분": "소듐피씨에이"
    },
    {
        "name": "컬러그램",
        "type": "틴트",
        "brand": "쥬시 젤리 틴트",
        "price": 9800,
        "유통기한": 241230,
        "성분": "석류추출물"
    }
]

@app.get("/cosmetics")
async def filter_cosmetics(
    brand: Optional[str] = Query(None, description="브랜드"),
    name: Optional[str] = Query(None, description="화장품 명"),
    cosmetic_type: Optional[str] = Query(None, description="화장품 종류 ex) 토너, 바디로션, 립스틱, 파운데이션"),
    expiration_date: Optional[int] = Query(None, description="유통기한 데이터 형식 yymmdd"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격")
) -> List[dict]:
    results = []

    for cosmetics in cosmetics_list:
        if brand and brand != cosmetics.get("brand"):
            continue
        if name and name != cosmetics.get("name"):
            continue
        if cosmetic_type and cosmetic_type != cosmetics.get("type"):
            continue
        if expiration_date and expiration_date != cosmetics.get("유통기한"):
            continue
        if min_price and (not cosmetics.get("price") or cosmetics.get("price") < min_price):
            continue
        if max_price and (not cosmetics.get("price") or cosmetics.get("price") > max_price):
            continue

        results.append(cosmetics)

    return results

# 애견동반 가능시설 데이터 리스트
pets_list = [
    {
        "name": "스테이지28 웁시데이지",
        "type": "애견동반카페",
        "address": "서울특별시 강동구 고덕제1동 아리수로61길 105",
        "전화번호": "02-3426-1928",
        "offleash_available": "Y"
    },
    {
        "name": "서울앵무새 용산점",
        "type": "애견동반카페",
        "address": "서울특별시 용산구 한강대로62길 55 1, 2, 3층",
        "전화번호": "0507-1350-4710",
        "offleash_available": "N"
    },
    {
        "name": "콘래드 서울",
        "type": "호텔",
        "address": "서울특별시 영등포구 국제금융로 10",
        "전화번호": "02-6137-7000",
        "offleash_available": "Y"
    },
    {
        "name": "팔레드 신",
        "type": "식당",
        "address": "서울특별시 중구 퇴계로 67",
        "전화번호": "02-317-4001",
        "offleash_available": "N"
    },
    {
        "name": "도그베이 서울점",
        "type": "수영장",
        "address": "서울특별시 광진구 광나루로 441",
        "전화번호": "070-4908-5890",
        "offleash_available": "Y"
    }
]

@app.get("/pets")
async def filter_pets(
    name: Optional[str] = Query(None, description="시설 이름"),
    facility_type: Optional[str] = Query(None, description="시설 종류 ex) 식당, 쇼핑몰, 카페, 애견운동장, 수영장, 숙소"),
    gu: Optional[str] = Query(None, description="지역구분_구"),
    dong: Optional[str] = Query(None, description="지역구분_동"),
    offleash_available: Optional[str] = Query(None, description="오프리쉬 가능여부 Y or N")
) -> List[dict]:
    results = []

    for pets in pets_list:
        if name and name != pets.get("name"):
            continue
        if facility_type and facility_type != pets.get("type"):
            continue
        if gu and gu != pets.get("address").split()[1]:
            continue
        if dong and dong != pets.get("address").split()[2]:
            continue
        if offleash_available and offleash_available != pets.get("offleash_available"):
            continue

        results.append(pets)

    return results

# 질병 데이터 리스트
diseases_list = [
    {
        "nameInKorean": "급성 B형간염",
        "nameInEnglish": "Acute hepatitis B",
        "질병코드": "B16",
        "개정구분": "8차",
        "keyword": "바이러스 감염성 질환"
    },
    {
        "nameInKorean": "백선증",
        "nameInEnglish": "Dermatophytosis",
        "질병코드": "B35",
        "개정구분": "8차",
        "keyword": "피부 및 피하조직의 감염"
    },
    {
        "nameInKorean": "헌팅톤",
        "nameInEnglish": "Huntington’s disease",
        "질병코드": "G10",
        "개정구분": "8차",
        "keyword": "신경계통의 질환"
    },
    {
        "nameInKorean": "구개열",
        "nameInEnglish": "Cleft palate",
        "질병코드": "Q35",
        "개정구분": "6차",
        "keyword": "선천기형"
    },
    {
        "nameInKorean": "조기 진통",
        "nameInEnglish": "Preterm delivery",
        "질병코드": "O60",
        "개정구분": "5차",
        "keyword": "임신"
    }
]

@app.get("/diseases")
async def filter_diseases(
    name_in_english: Optional[str] = Query(None, description="질병 명 영어"),
    name_in_korean: Optional[str] = Query(None, description="질병 명 한글"),
    disease_code: Optional[str] = Query(None, description="질병코드"),
    revision_type: Optional[str] = Query(None, description="개정구분 ex) 5차, 6차, 7차, 8차"),
    keyword: Optional[str] = Query(None, description="키워드")
) -> List[dict]:
    results = []

    for disease in diseases_list:
        if name_in_english and name_in_english != disease.get("nameInEnglish"):
            continue
        if name_in_korean and name_in_korean != disease.get("nameInKorean"):
            continue
        if disease_code and disease_code != disease.get("질병코드"):
            continue
        if revision_type and revision_type != disease.get("개정구분"):
            continue
        if keyword and keyword != disease.get("keyword"):
            continue

        results.append(disease)

    return results

# 법령 데이터 리스트
law_list = [
    {
        "name": "1인 창조기업 육성에 관한 법률",
        "type": "법률",
        "공포일자": 220610,
        "시행일자": 221211,
        "제정개정구분": "일부개정"
    },
    {
        "name": "가사소송법",
        "type": "법률",
        "공포일자": 210126,
        "시행일자": 221211,
        "제정개정구분": "타법개정"
    },
    {
        "name": "각종 기념일 등에 관한 규정",
        "type": "대통령령",
        "공포일자": 230410,
        "시행일자": 230605,
        "제정개정구분": "타법개정"
    },
    {
        "name": "희귀질환관리법 시행규칙",
        "type": "보건복지부령",
        "공포일자": 230308,
        "시행일자": 230308,
        "제정개정구분": "일부개정"
    },
    {
        "name": "경영지도사 및 기술지도사에 관한 법률",
        "type": "법률",
        "공포일자": 200407,
        "시행일자": 210408,
        "제정개정구분": "제정"
    }
]

@app.get("/law")
async def filter_law(
    name: Optional[str] = Query(None, description="법령명"),
    law_type: Optional[str] = Query(None, description="법령 종류"),
    promulgation_date: Optional[int] = Query(None, description="공포일자 데이터형식 yymmdd"),
    enforcement_date: Optional[int] = Query(None, description="시행일자 데이터형식 yymmdd"),
    revision_type: Optional[str] = Query(None, description="제정·개정구분")
) -> List[dict]:
    results = []

    for law in law_list:
        if name and name != law.get("name"):
            continue
        if law_type and law_type != law.get("type"):
            continue
        if promulgation_date and promulgation_date != law.get("공포일자"):
            continue
        if enforcement_date and enforcement_date != law.get("시행일자"):
            continue
        if revision_type and revision_type != law.get("제정개정구분"):
            continue

        results.append(law)

    return results

# 보드게임 데이터 리스트
boardgame_list = [
    {
        "name": "사보타지",
        "type": "협잡",
        "min_age": 8,
        "최소_인원": 3,
        "최대_인원": 10,
        "설명": "광부들 사이에 방해꾼이 섞여 있습니다."
    },
    {
        "name": "부루마불",
        "type": "경제",
        "min_age": 7,
        "최소_인원": 2,
        "최대_인원": 4,
        "설명": "자신의 도시를 방문하면 다양한 건물을 지을 수 있습니다."
    },
    {
        "name": "뱅",
        "type": "추리",
        "min_age": 8,
        "최소_인원": 4,
        "최대_인원": 7,
        "설명": "무법자들이 보안관을 사냥하고 보안관은 무법자를 사냥합니다."
    },
    {
        "name": "할리갈리",
        "type": "순발력",
        "min_age": 6,
        "최소_인원": 2,
        "최대_인원": 6,
        "설명": "같은 과일의 개수가 보인다면 빠르게 종을 치세요."
    },
    {
        "name": "클루",
        "type": "추리",
        "min_age": 8,
        "최소_인원": 3,
        "최대_인원": 6,
        "설명": "용의자와 무기 그리고 장소를 알아내야 합니다."
    }
]

@app.get("/boardgame")
async def filter_boardgame(
    name: Optional[str] = Query(None, description="보드게임 이름"),
    game_type: Optional[str] = Query(None, description="보드게임 종류 ex) 추리, 순발력, 협잡 등"),
    min_age: Optional[int] = Query(None, description="이용가능한 최소 연령"),
    min_players: Optional[int] = Query(None, description="최소 인원"),
    max_players: Optional[int] = Query(None, description="최대 인원"),
    keyword: Optional[str] = Query(None, description="키워드")
) -> List[dict]:
    results = []

    for game in boardgame_list:
        if name and name != game.get("name"):
            continue
        if game_type and game_type != game.get("type"):
            continue
        if min_age and min_age > game.get("min_age"):
            continue
        if min_players and min_players > game.get("최소_인원"):
            continue
        if max_players and max_players < game.get("최대_인원"):
            continue
        if keyword and keyword not in game.get("설명"):
            continue

        results.append(game)

    return results

# 꽃 데이터 리스트
flower_list = [
    {
        "꽃이름": "안개꽃",
        "분류_속": "대나물속",
        "분류_과": "석죽과",
        "분류_목": "석죽목",
        "꽃말": "맑은 마음",
        "원산지": "캅카스"
    },
    {
        "꽃이름": "해당화",
        "분류_속": "장미속",
        "분류_과": "장미과",
        "분류_목": "장미목",
        "꽃말": "이끄시는 대로",
        "원산지": "중국"
    },
    {
        "꽃이름": "스타티스",
        "분류_속": "질경이속",
        "분류_과": "질경이과",
        "분류_목": "꿀풀목",
        "꽃말": "변치않는 사랑",
        "원산지": "중국"
    },
    {
        "꽃이름": "튤립",
        "분류_속": "튤립속",
        "분류_과": "백합과",
        "분류_목": "백합목",
        "꽃말": "새로운 시작",
        "원산지": "남동 유럽"
    },
    {
        "꽃이름": "수국",
        "분류_속": "수국속",
        "분류_과": "수국과",
        "분류_목": "층층나무목",
        "꽃말": "냉정",
        "원산지": "일본"
    }
]

@app.get("/flower")
async def filter_flower(
    꽃이름: Optional[str] = Query(None, description="꽃의 이름"),
    분류_속: Optional[str] = Query(None, description="꽃의 분류를 속으로 합니다"),
    분류_과: Optional[str] = Query(None, description="꽃의 분류를 과로 합니다"),
    분류_목: Optional[str] = Query(None, description="꽃의 분류를 목으로 합니다"),
    꽃말: Optional[str] = Query(None, description="꽃말"),
    원산지: Optional[str] = Query(None, description="원산지")
) -> List[dict]:
    results = []

    for flower in flower_list:
        if 꽃이름 and 꽃이름 != flower.get("꽃이름"):
            continue
        if 분류_속 and 분류_속 != flower.get("분류_속"):
            continue
        if 분류_과 and 분류_과 != flower.get("분류_과"):
            continue
        if 분류_목 and 분류_목 != flower.get("분류_목"):
            continue
        if 꽃말 and 꽃말 != flower.get("꽃말"):
            continue
        if 원산지 and 원산지 != flower.get("원산지"):
            continue

        results.append(flower)

    return results

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
