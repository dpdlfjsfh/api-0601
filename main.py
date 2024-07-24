from fastapi import FastAPI, Query, HTTPException, Body, Request
from typing import List, Optional, Dict
from pydantic import BaseModel

app = FastAPI()

result_oos = [
  {
    "Step SEQ": 1,
    "EINECN No": "AB000100",
    "EINECN Title": "ECO123456-X",
    "PPID": "설명 관련 정보 입니다. 수십자 수준입니다.",
    "1": "영어와 숫자, 특수문자 조합",
    "2": "O",
    "3": "O",
    "4": "O",
    "5": None,
    "6": None,
    "7": None,
    "8": None,
    "9": None,
    "10": None,
    "11": None,
    "12": None,
    "13": None,
    "14": None,
    "15": None,
    "16": None,
    "17": None,
    "18": None,
    "19": None,
    "20": None,
    "21": None,
    "22": None,
    "23": None,
    "24": None,
    "25": None
  },
  {
    "Step SEQ": 2,
    "EINECN No": "AB001000",
    "EINECN Title": "ECO123457-X",
    "PPID": "설명 관련 정보 입니다. 수십자 수준입니다.",
    "1": "영어와 숫자, 특수문자 조합",
    "2": "O",
    "3": "O",
    "4": "O",
    "5": "O",
    "6": "O",
    "7": "O",
    "8": "O",
    "9": "O",
    "10": "O",
    "11": "O",
    "12": "O",
    "13": "O",
    "14": "O",
    "15": "O",
    "16": "O",
    "17": "O",
    "18": "O",
    "19": "O",
    "20": "O",
    "21": "O",
    "22": "O",
    "23": "O",
    "24": "O",
    "25": "O"
  },
  {
    "Step SEQ": 3,
    "EINECN No": "AB010000",
    "EINECN Title": "ECO123458-X",
    "PPID": "설명 관련 정보 입니다. 수십자 수준입니다.",
    "1": "영어와 숫자, 특수문자 조합",
    "2": "O",
    "3": "O",
    "4": "O",
    "5": "O",
    "6": None,
    "7": None,
    "8": None,
    "9": None,
    "10": None,
    "11": None,
    "12": None,
    "13": None,
    "14": None,
    "15": None,
    "16": None,
    "17": None,
    "18": None,
    "19": None,
    "20": None,
    "21": None,
    "22": None,
    "23": None,
    "24": None,
    "25": None
  },
  {
    "Step SEQ": 4,
    "EINECN No": "AB100000",
    "EINECN Title": "ECO123459-X",
    "PPID": "설명 관련 정보 입니다. 수십자 수준입니다.",
    "1": "영어와 숫자, 특수문자 조합",
    "2": "O",
    "3": "O",
    "4": "O",
    "5": "O",
    "6": "O",
    "7": "O",
    "8": "O",
    "9": "O",
    "10": "O",
    "11": "O",
    "12": "O",
    "13": "O",
    "14": "O",
    "15": "O",
    "16": "O",
    "17": "O",
    "18": "O",
    "19": "O",
    "20": "O",
    "21": "O",
    "22": "O",
    "23": "O",
    "24": "O",
    "25": "O"
  },
  {
    "Step SEQ": 5,
    "EINECN No": "AB100100",
    "EINECN Title": "ECO123460-X",
    "PPID": "설명 관련 정보 입니다. 수십자 수준입니다.",
    "1": "영어와 숫자, 특수문자 조합",
    "2": "O",
    "3": "O",
    "4": "O",
    "5": "O",
    "6": "O",
    "7": None,
    "8": None,
    "9": None,
    "10": None,
    "11": None,
    "12": None,
    "13": None,
    "14": None,
    "15": None,
    "16": None,
    "17": None,
    "18": None,
    "19": None,
    "20": None,
    "21": None,
    "22": None,
    "23": None,
    "24": None,
    "25": None
  },
  {
    "Step SEQ": 6,
    "EINECN No": "AB101000",
    "EINECN Title": "ECO123461-X",
    "PPID": "설명 관련 정보 입니다. 수십자 수준입니다.",
    "1": "영어와 숫자, 특수문자 조합",
    "2": "O",
    "3": "O",
    "4": "O",
    "5": "O",
    "6": "O",
    "7": None,
    "8": None,
    "9": None,
    "10": None,
    "11": None,
    "12": None,
    "13": None,
    "14": None,
    "15": None,
    "16": None,
    "17": None,
    "18": None,
    "19": None,
    "20": None,
    "21": None,
    "22": None,
    "23": None,
    "24": None,
    "25": None
  }
]
@app.get("/oosTest")
async def get_available_slots(LotID: str):
    return result_oos



available_slots = {
    "2024-07-19 14:00": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "2024-07-19 15:00": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    # 추가적인 시간대와 타석 정보
}

# 예약된 타석 정보
booked_slots = {}

class ReservationRequest(BaseModel):
    date_time: str
    slot_number: int

@app.get("/available_slots/")
async def get_available_slots(date_time: str):
    if date_time in available_slots:
        return {"available_slots": available_slots[date_time]}
    else:
        raise HTTPException(status_code=200, detail="해당 시간에 예약 가능한 타석이 없습니다.")

@app.post("/reserve_slot/")
async def reserve_slot(reservation: ReservationRequest):
    date_time = reservation.date_time
    slot_number = reservation.slot_number

    if date_time not in available_slots:
        raise HTTPException(status_code=200, detail="해당 시간에 예약 가능한 타석이 없습니다.")
    
    if slot_number > 10 :
        raise HTTPException(status_code=200, detail="해당 타석은 이미 예약되었습니다.")
    
    if slot_number <= 10:
        return '예약완료!'





perform_data = [
  {
    "공연_이름": "햄릿의 귀환",
    "공연_일자": "2024-08-15",
    "공연_시간": "19:30",
    "출연_배우": ["김민수", "이지원", "박성훈"],
    "S좌석_가격": 80000,
    "A좌석_가격": 60000,
    "B좌석_가격": 40000,
    "공연_예약가능_여부": True,
    "STEP_SEQ ": "AB000101",
    "예매_시작_일자": "2024-07-20",
    "공연장": "세종문화회관",
    "공연_장르": "연극",
    "공연_길이": "150분",
    "intermission": "15분",
    "관람_연령": "12세 이상",
    "특별_할인": "학생 20% 할인"
  },
  {
    "공연_이름": "오페라의 유령",
    "공연_일자": "2024-09-01",
    "공연_시간": "14:00",
    "출연_배우": ["최재훈", "송미란", "정태우"],
    "S좌석_가격": 120000,
    "A좌석_가격": 90000,
    "B좌석_가격": 70000,
    "공연_예약가능_여부": True,
    "STEP_SEQ ": "AB000102",
    "예매_시작_일자": "2024-08-01",
    "공연장": "세종문화회관",
    "공연_장르": "뮤지컬",
    "공연_길이": "180분",
    "intermission": "20분",
    "관람_연령": "8세 이상",
    "특별_할인": "조기예매 10% 할인"
  },
  {
    "공연_이름": "백조의 호수",
    "공연_일자": "2024-10-10",
    "공연_시간": "20:00",
    "출연_배우": ["이수진", "김태희", "박준호"],
    "S좌석_가격": 100000,
    "A좌석_가격": 80000,
    "B좌석_가격": 60000,
    "공연_예약가능_여부": False,
    "STEP_SEQ ": "AB000103",
    "예매_시작_일자": "2024-09-01",
    "공연장": "세종문화회관",
    "공연_장르": "발레",
    "공연_길이": "135분",
    "intermission": "15분",
    "관람_연령": "전체 관람가",
    "특별_할인": "65세 이상 30% 할인"
  },
  {
    "공연_이름": "재즈의 밤",
    "공연_일자": "2024-11-05",
    "공연_시간": "21:00",
    "출연_배우": ["박재범", "이소라", "최백호"],
    "S좌석_가격": 70000,
    "A좌석_가격": 50000,
    "B좌석_가격": 30000,
    "공연_예약가능_여부": True,
    "STEP_SEQ ": "AB000104",
    "예매_시작_일자": "2024-10-01",
    "공연장": "세종문화회관",
    "공연_장르": "재즈 콘서트",
    "공연_길이": "120분",
    "intermission": "없음",
    "관람_연령": "19세 이상",
    "특별_할인": "커플 티켓 10% 할인"
  },
  {
    "공연_이름": "국악의 향연",
    "공연_일자": "2024-12-20",
    "공연_시간": "18:00",
    "출연_배우": ["김덕수", "송소희", "안숙선"],
    "S좌석_가격": 50000,
    "A좌석_가격": 40000,
    "B좌석_가격": 30000,
    "공연_예약가능_여부": True,
    "STEP_SEQ ": "AB000105",
    "예매_시작_일자": "2024-11-15",
    "공연장": "세종문화회관",
    "공연_장르": "국악",
    "공연_길이": "90분",
    "intermission": "10분",
    "관람_연령": "전체 관람가",
    "특별_할인": "외국인 20% 할인"
  }
]

@app.get("/perform_inform")

async def perform(
    location: Optional[str] = Query(None),
):

    if location == "세종문화회관":
        return perform_data


@app.get("/restaurant_inform/{station1}")
async def get_restaurant_inform_1(station1: str):
    return {"message": f"맛집! {station1}"}

@app.get("/restaurant_inform/{station1}/{station2}")
async def get_restaurant_inform_2(station1: str, station2: str):
    return {"message": f"맛집! {station1} 와 {station2} 근처"}

@app.get("/restaurant_inform/{station1}/{station2}/{station3}")
async def get_restaurant_inform_3(station1: str, station2: str, station3: str):
    return {"message": f"맛집! {station1}, {station2}, {station3}"}



@app.get("/socartest")
async def socar(
    location: Optional[str] = Query(None),
    car_type: Optional[str] = Query(None),
    price: Optional[str] = Query(None),
    color: Optional[str] = Query(None),
):
    if location == None:
        return '빌리고 싶은 장소를 확인해주세요.'
    if location == '전주역' and car_type == '경차' and price == '10만원대' and color == '빨강':
        return '전주역에서 빌릴 수 있는 10만원대 빨간 경차 소개해드리겠습니다.'
    elif location == '전주역' and car_type == '경차' and price == '10만원대':
        return '전주역에서 빌릴 수 있는 10만원대 경차 소개해드리겠습니다.'
    elif location == '전주역' and car_type == '경차' :
        return '전주역에서 빌릴 수 있는 경차 소개해드리겠습니다.'
    elif location == '전주역':
        return '{"차량 이름" : "싼타페"}'
    else:
        return '죄송합니다. 해당 차량 정보를 찾을 수 없습니다. 자세한 문의는 고객센터 1212-4545-7878로 문의 부탁드립니다.'

@app.get("/carpricesearch")
async def socar(
    car_name: Optional[str] = Query(None)
):
    if car_name == '싼타페':
        return '2500만원'



@app.get("/AICC")
async def aicc(
    category: Optional[str] = Query(None),
    third_party: Optional[str] = Query(None),
    matching_state: Optional[str] = Query(None),
    elapsed_8hr: Optional[str] = Query(None),
    elapsed_2day: Optional[str] = Query(None),
    exclusion_reason: Optional[str] = Query(None),
    correction_state: Optional[str] = Query(None)
):
    if category == '가격비교 매칭 방법':
        if third_party == 'T':
            return '11번가, 쿠팡 상품의 가격비교 매칭은 해당 오픈마켓/종합몰 담당자에게 매칭 요청해주시기 바랍니다.'
        else:
            return '가격비교 매칭 방법은 http://imgshopping.naver.net/admin/notice/g98cytj1o5y.png 를 참조해주세요.'
    elif category == '가격비교 노출 안됨':
        if matching_state == '완료':
            if elapsed_8hr == 'T':
                return '상담사 연결'
            else:
                return '업데이트 반영까지 8시간이 걸릴 수 있습니다. 8시간 이상 지나도 반영이 안 된다면 상담사 연결해 드리겠습니다.'
        elif matching_state == '추천중':
            if elapsed_2day == 'T':
                return '상담사 연결'
            else:
                return '매칭 결과 안내까지 2일이 소요될 수 있습니다. 2일이 지나도 반영이 안 된다면 상담사 연결해 드리겠습니다.'
        elif matching_state == '반려':
            return '1. 다른 옵션이 포함된 모음 상품명 2. 1개 또는 몇 개 단위 배송비 부과 상품 3. 원부와 사이즈,용량,수량이 다른 상품일 수 있습니다. 자세한 매칭 기준은 https://help.pay.naver.com/faq/content.help?faqId=13388를 참조해주세요.'
        else:
            return '가격비교 매칭을 요청했는데 노출이 안된다면 매칭 상태를 확인해주세요. 매칭 상태는 https://adcenter.shopping.naver.com/member/login/form.nhn?targetUrl=%2Fiframe%2Fproduct%2Fmanage%2Fservice%2Flist.nhn 에서 확인할 수 있습니다.'
    elif category == '가격비교 제외 상품':
        if exclusion_reason == '원부 내 포함대상 아님':
            if correction_state == 'T':
                return '상담원 연결'
            else:
                return '상품 기본정보(대표 이미지, 제조사, 브랜드, 상품명, 상품코드) 불일치, 여러 상품을 취급하는 모음전 상품은 매칭이 불가합니다. 다음의 사항을 수정 하셨다면 상담원 연결 도와드리겠습니다.'
        elif exclusion_reason == '원부 배송비 기준 위반':
            if correction_state == 'T':
                return '상담원 연결'
            else:
                return '수량 단위로 배송비가 발생하거나, 가격비교 배송비 조건을 초과한 배송비 상품은 가격비교에서 제외됩니다. 다음의 사항을 수정 하셨다면 상담원 연결 도와드리겠습니다.'
        elif exclusion_reason == '원부 설치비 기준 위반':
            if correction_state == 'T':
                return '상담원 연결'
            else:
                return '에어컨, 보일러, 온수기 등 설치가 필요한 상품은 상품명에 "기본설치비 포함" 및 상세페이지에 추가비용 정보를 표기하지 않으면 매칭이 불가합니다. 설치 상품군 서비스 기준은 https://adcenter.shopping.naver.com/board/notice_detail.nhn?page=1&noticeType=&noticeSeq=274384&srchKey=cont&srchVal=%EC%84%A4%EC%B9%98%EB%B9%84를 참조해주세요. 다음의 사항을 수정 하셨다면 상담원 연결 도와드리겠습니다.'
        elif exclusion_reason == '원부기준 위반_기타':
            if correction_state == 'T':
                return '상담원 연결'
            else:
                return '가격비교 매칭 가이드에 맞지 않은 상품은 가격비교에 노출할 수 없습니다. 제외된 사유는 https://adcenter.shopping.naver.com/board/notice_detail.nhn?page=1&noticeType=&noticeSeq=276064&srchKey=ttl&srchVal=%EB%A7%A4%EC%B9%AD 링크 내 첨부파일을 통해 확인 가능합니다. 다음의 사항을 수정 하셨다면 상담원 연결 도와드리겠습니다.'
        elif exclusion_reason == '원부 비대상 상품군':
            if correction_state == 'T':
                return '상담원 연결'
            else:
                return '가격비교를 서비스하지 않는 상품군으로 매칭이 불가능합니다. 상품 타입 : 중고, 리퍼, 전시, 반품, 스크래치 판매 방식 : 대여, 도매, 할부, 예약판매, 구매대행'
        elif exclusion_reason is not None :
            return '가격비교 제외 사유를 정확히 입력해주세요. 사유 : 원부 내 포함대상 아님, 원부 배송비 기준 위반, 원부 설치비 기준 위반, 원부기준 위반_기타, 원부 비대상 상품군'
        else:
            return '가격비교 제외 사유를 확인해주세요. '
    else:
        return '정의 되지 않은 상담 영역입니다.'


@app.get("/zoo_animal")
def read_zoo_animal():
    return []

@app.post("/zoo_animal")
def create_zoo_animal():
    return []

@app.get("/apartment_complex")
def read_zoo_anima1l():
    return []

@app.post("/apartment_complex")
def create_zoo_animal1():
    return []

@app.get("/spread_jam_search")
def read_zoo_animal2():
    return []

@app.post("/spread_jam_search")
def create_zoo_anima2l():
    return []

@app.get("/terrace_cafe_search")
def read_zoo_animal3():
    return []

@app.post("/terrace_cafe_search")
def create_zoo_anima3l():
    return []

@app.get("/naeil_baeum_card")
def read_zoo_animal4():
    return []

@app.post("/naeil_baeum_card")
def create_zoo_animal4():
    return []

@app.get("/yoga_pilates_class_reservation")
def read_zoo_animal5():
    return []

@app.post("/yoga_pilates_class_reservation2")
def create_zoo_animal5():
    return []

#지하철역 이름
@app.get("/find_station")
async def find_station(
    landmark : Optional[str] = Query(
        None,
    )
):
    # 데이터에서 검색 조건에 맞는 항목 필터링
    filtered_data = [{"station_name":"정자역"}]
    return filtered_data

@app.get("/station_time")
async def station_time(
    station_name : Optional[str] = Query(
        None,
    )
):
    # 데이터에서 검색 조건에 맞는 항목 필터링
    filtered_data = []
    if station_name == '정자역':
        filtered_data = [{"station_name":"정자역", "time": ['17:00','17:10']}]
    return filtered_data


#벌크 테스트
strawberry_data = [
  {
    "food_name": "빈츠 딸기 프로마쥬",
    "food_type": "과자",
    "food_brand": "롯데제과",
    "food_keywords": [
      "딸기",
      "초콜릿",
      "쿠키",
      "2024년",
      "핑크",
      "봄",
      "빈츠"
    ],
    "food_price": 4500,
    "release_date": "2024-02-10",
    "review_rating": 4.3
  },
  {
    "food_name": "몽쉘 딸기 생크림 케이크",
    "food_type": "과자",
    "food_brand": "롯데제과",
    "food_keywords": [
      "딸기",
      "초콜릿",
      "케이크",
      "2024년",
      "딸기잼",
      "봄",
      "몽쉘"
    ],
    "food_price": 6500,
    "release_date": "2024-02-12",
    "review_rating": 4.5
  },
  {
    "food_name": "딸기라떼 카스타드",
    "food_type": "과자",
    "food_brand": "롯데제과",
    "food_keywords": [
      "딸기",
      "딸기라떼",
      "케이크",
      "2024년",
      "카스타드",
      "봄"
    ],
    "food_price": 5500,
    "release_date": "2024-02-11",
    "review_rating": 4.4
  },
  {
    "food_name": "딸기라떼 명가 찰떡파이",
    "food_type": "과자",
    "food_brand": "롯데제과",
    "food_keywords": [
      "딸기",
      "찰떡",
      "찰떡파이",
      "딸기라떼",
      "2024년",
      "핑크",
      "봄"
    ],
    "food_price": 7650,
    "release_date": "2024-02-06",
    "review_rating": 4.3
  },
  {
    "food_name": "팔도 봄 에디션 딸기 비빔면",
    "food_type": "라면",
    "food_brand": "팔도",
    "food_keywords": [
      "딸기",
      "비빔면",
      "딸기맛",
      "2024년",
      "상큼",
      "봄"
    ],
    "food_price": 5500,
    "release_date": "2024-02-05",
    "review_rating": 4.2
  },
  {
    "food_name": "딸기 블라썸 붕어싸만코",
    "food_type": "빙과",
    "food_brand": "빙그레",
    "food_keywords": [
      "딸기",
      "벚꽃",
      "붕어싸만코",
      "2024년",
      "아이스크림",
      "봄",
      "핑크",
      "편의점신상"
    ],
    "food_price": 2200,
    "release_date": "2024-03-02",
    "review_rating": 4.7
  },
  {
    "food_name": "딸기 글레이즈드 도넛",
    "food_type": "베이커리",
    "food_brand": "크리스피크림",
    "food_keywords": [
      "딸기",
      "도넛",
      "2024년",
      "핑크",
      "봄"
    ],
    "food_price": 2500,
    "release_date": "2024-03-15",
    "review_rating": 4.9
  },
  {
    "food_name": "상큼한 딸기크림을 토핑한 스트로베리 피그 도넛",
    "food_type": "베이커리",
    "food_brand": "크리스피크림",
    "food_keywords": [
      "딸기",
      "초콜릿",
      "딸기크림",
      "도넛",
      "동물모양",
      "2024년",
      "핑크",
      "봄"
    ],
    "food_price": 3900,
    "release_date": "2024-03-13",
    "review_rating": 4.1
  },
  {
    "food_name": "생딸기 마스카포네 도넛",
    "food_type": "베이커리",
    "food_brand": "노티드",
    "food_keywords": [
      "딸기",
      "생딸기",
      "도넛",
      "2024년",
      "크림치즈",
      "봄",
      "마스카포네"
    ],
    "food_price": 5200,
    "release_date": "2024-03-21",
    "review_rating": 4.6
  },
  {
    "food_name": "스트로베리 자스민티",
    "food_type": "음료",
    "food_brand": "노티드",
    "food_keywords": [
      "딸기",
      "자스민",
      "차",
      "2024년",
      "핑크",
      "봄",
      "허브티",
      "아이스티",
      "논카페인"
    ],
    "food_price": 6800,
    "release_date": "2024-03-06",
    "review_rating": 4.3
  }
]

@app.get("/limited_edition_strawberry_food_search")
async def searchLimitedEditionStrawberryFood(
    food_name: Optional[str] = Query(
        None,
    ),
    food_type: Optional[str] = Query(
        None,
        description="과자, 라면, 빙과, 베이커리, 음료 중 하나를 선택하세요"
    ),
    food_brand: Optional[str] = Query(
        None,
    ),
    food_keywords: List[str] = Query(
        None,
        description="한글로 띄어쓰기 없이 제품키워드를 입력하세요"
    )
):
    # 데이터에서 검색 조건에 맞는 항목 필터링
    filtered_data = []
    for item in strawberry_data:
        if (food_name is None or food_name == item["food_name"]) \
                and (food_type is None or food_type == item["food_type"]) \
                and (food_brand is None or food_brand == item["food_brand"]) \
                and (food_keywords is None or all(keyword in item["food_keywords"] for keyword in food_keywords)):
            filtered_data.append(item)
    return filtered_data

# 무형문화제 데이터
intangible_cultural_heritage_data = [    {
        "name": "판소리",
        "main_category": "전통공연",
        "subcategory": "음악",
        "designated_date": "1964.12.28",
        "location": "기타",
        "introduction": "판소리는 한 명의 소리꾼이 고수(북치는 사람)의 장단에 맞추어 창(소리), 말(아니리), 몸짓(너름새)을 섞어가며 긴 이야기를 엮어가는 것을 말한다."
    },
    {
        "name": "양주별산대놀이",
        "main_category": "전통공연",
        "subcategory": "연희",
        "designated_date": "1964.12.07",
        "location": "경기도 양주시",
        "introduction": "양주별산대놀이는 경기도 양주군 주내면 유양리 지역에서 전승되는 산대놀이 계통의 탈놀이다."
    },
    {
        "name": "자수장",
        "main_category": "전통기술",
        "subcategory": "공예",
        "designated_date": "1984.10.15",
        "location": "부산광역시 금정구",
        "introduction": "자수(刺繡)는 여러 색깔의 실을 바늘에 꿰어 바탕천에 무늬를 수놓아 나타내는 조형활동이다."
    },
    {
        "name": "주철장",
        "main_category": "전통기술",
        "subcategory": "공예",
        "designated_date": "2001.03.12",
        "location": "충청북도 진천군",
        "introduction": "주철장이란 인류가 오랫동안 사용하였던 쇠를 녹여서 각종 기물을 만드는 장인을 말한다."
    },
    {
        "name": "사직대제",
        "main_category": "의례의식",
        "subcategory": "그 밖의 의식의례",
        "designated_date": "2000.10.19",
        "location": "서울특별시 종로구",
        "introduction": "사직대제는 땅과 곡식의 신에게 드리는 국가적인 제사로, 사(社)는 땅의 신, 직(稷)은 곡식의 신을 의미한다. 예로부터 나라를 세우면 먼저 조상에게 제사를 지내고 이와 함께 땅과 곡식의 신에게 백성이 편안하게 살 수 있도록 풍요를 기원하는 사직제를 올렸다."
    },
    {
        "name": "강강술래",
        "main_category": "전통공연",
        "subcategory": "음악",
        "designated_date": "1966.02.15",
        "location": "전라남도 진도군",
        "introduction": "강강술래는 노래와 춤이 하나로 어우러진 부녀자들의 집단놀이이다."
    },
    {
        "name": "강릉단오제",
        "main_category": "전통놀이",
        "subcategory": "축제",
        "designated_date": "1967.01.16",
        "location": "강원도 강릉시",
        "introduction": "강릉단오제는 우리나라에서 가장 역사가 깊은 축제로, 마을을 지켜주는 대관령 산신을 제사하고, 마을의 평안과 농사의 번영, 집안의 태평을 기원한다."
    },
    {
        "name": "한산모시짜기",
        "main_category": "전통기술",
        "subcategory": "공예",
        "designated_date": "1967.01.16",
        "location": "충청남도 서천군",
        "introduction": "한산모시는 우리나라의 미를 상징하는 여름 전통옷감으로 역사적 가치가 높아 제작기술을 보호하고자 국가무형유산으로 지정했다."
    },
    {
        "name": "북청사자놀음",
        "main_category": "전통공연",
        "subcategory": "연희",
        "designated_date": "1967.03.31",
        "location": "서울특별시",
        "introduction": "북청사자놀음은 대사의 묘미나 풍자적인 측면보다는 사자춤의 묘기와 흥겨움이 중심이 되어 다른 사자춤사위보다 교묘하고 힘찬 동작이 특징이다."
    },
    {
        "name": "줄타기",
        "main_category": "전통공연",
        "subcategory": "연희",
        "designated_date": "1976.06.16",
        "location": "경기도 과천시",
        "introduction": "줄타기는 공중에 맨 줄 위에서 재미있는 이야기와 발림을 섞어가며 여러 가지 재주를 보여주는 놀이이다."
    },
    {
        "name": "종묘제례",
        "main_category": "의례의식",
        "subcategory": "그 밖의 의식의례",
        "designated_date": "1975.05.09",
        "location": "서울특별시 종로구",
        "introduction": "종묘제례란 조선시대 역대 왕과 왕비의 신위를 모셔 놓은 사당(종묘)에서 지내는 제사를 말한다."
    },
    {
        "name": "제주민요",
        "main_category": "전통공연",
        "subcategory": "음악",
        "designated_date": "1989.12.01",
        "location": "제주특별자치도 서귀포시",
        "introduction": "제주민요는 일하면서 부르는 노동요가 많고 부녀자들이 부르는 민요가 흔하다는 점에서 주목된다. 노랫말도 특이한 제주도 사투리를 많이 사용하고 있으며, 경기지역 민요보다 구슬프다."
    },
    {
        "name": "영산줄다리기",
        "main_category": "전통놀이",
        "subcategory": "놀이",
        "designated_date": "1969.02.11",
        "location": "경상남도 창녕군",
        "introduction": "영산줄다리기는 경상남도 창녕군 영산면에서 전승되는 민속놀이로 현재는 3·1문화제 행사의 하나로 줄다리기를 하고 있다."
    },
    {
        "name": "연등회",
        "main_category": "전통놀이",
        "subcategory": "축제",
        "designated_date": "2012.04.06",
        "location": "서울특별시 종로구",
        "introduction": "연등회는 관불의식, 연등행렬, 회향의 형식으로 진행되며 연등행렬 때 동원되는 등(燈)이 다양하고 다채롭다."
    },
    {
        "name": "번와장",
        "main_category": "전통기술",
        "subcategory": "건축",
        "designated_date": "2008.10.21",
        "location": "기타",
        "introduction": "번와장'이란 지붕의 기와를 잇는 장인을 말한다."
    }
]

@app.get("/intangible_cultural_heritage")
async def filterIntangibleCulturalHeritage(
    name: Optional[str] = Query(
        None,
        description="문화재명을 한글로 적어주세요 (ex. 판소리, 양주별산대놀이, 주철장)"
    ),
    main_category: str = Query(
        ...,
        description="대분류를 한글로 적어주세요 (ex. 전통공연, 전통기술, 의례의식)"
    ),
    subcategory: Optional[str] = Query(
        None,
        description="소분류를 한글로 적어주세요 (ex. 음악, 공예, 그 밖의 의식의례)"
    ),
    designated_date: Optional[str] = Query(
        None,
        description="지정일을 1964.12.28 형식으로 적어주세요"
    ),
    location: Optional[str] = Query(
        None,
        description="소재지를 한글로 적어주세요 (ex. 기타, 경기도 양주시, 부산광역시 금정구, 충청북도 진천군)"
    )
):
    # 데이터에서 검색 조건에 맞는 항목 필터링
    filtered_data = []
    for item in intangible_cultural_heritage_data:
        if (name is None or name == item["name"]) \
                and main_category == item["main_category"] \
                and (subcategory is None or subcategory == item["subcategory"]) \
                and (designated_date is None or designated_date == item["designated_date"]) \
                and (location is None or location == item["location"]):
            filtered_data.append(item)
    return filtered_data

cooking_receipe_data = [  {
    "creator": "뇨리사",
    "food_classification": [
      "음료"
    ],
    "cook_name": "셀러리 주스",
    "ingredients": [
      "셀러리",
      "물",
      "바나나",
      "사과",
      "레몬"
    ],
    "time": 5,
    "receipe": "1. 셀러리는 깨끗하게 씻어서 잎은 떼어내고 줄기만  갈기 좋은 크기로 자릅니다. 2. 사과는 껍질을 벗긴 후 역시 갈리 좋은 크기로 잘라둡니다. 3. 믹서 용기에 물을 붓고 잘라둔 셀러리와 사과를 넣어요. 그 위에 바나나도 뚝뚝 잘라 넣습니다. 4. 레몬은 껍질은 벗기고 씨를 발라낸 후 과육만 넣어요. 5. 재료들이 곱게 갈릴 때까지 믹서를 돌린 후 컵에 담아요. ",
    "views": 12902
  },
  {
    "creator": "히트주부",
    "food_classification": [
      "죽"
    ],
    "cook_name": "버섯 굴죽",
    "ingredients": [
      "쌀",
      "굴",
      "버섯",
      "물",
      "참기름",
      "국간장",
      "소금",
      "후추"
    ],
    "time": 30,
    "receipe": "1. 굴은 굵은 소금을 뿌려서 껍질을 골라내고 살살 씻어서 건져둡니다. 2. 냄비에 참기름과 쌀, 물 한큰술을 넣고 기름이 잘 섞이도록 살살 볶아요. 찹쌀을 섞거나 쌀알을 다져서 넣으면 더 촉촉한 느낌이 납니다. 3. 물 5컵을 넣고 쌀알이 완전히 떠오를때까지 끓여요. 4. 물기를 뺀 굴과 다진 버섯을 냄비에 넣고 물 1컵을 추가해서 살짝 더 끓여요. 5. 국간장으로는 색만 내고 소금, 후추로 간해요.   ",
    "views": 14319
  },
  {
    "creator": "프로쿠커",
    "food_classification": [
      "매일반찬"
    ],
    "cook_name": "두부 조림",
    "ingredients": [
      "두부",
      "대파",
      "실고추",
      "들기름"
    ],
    "time": 15,
    "receipe": "1. 두부를 3 ×4.5 ×0.8㎝ 정도로 잘라서 소금을 뿌려 물기를 잠시 뺀 후 면보나 키친타올로 닦아서 준비해요.  2. 두부 물기가 빠질 동안 양념 재료를 섞고 실고추와 채썬 대파를 1~2㎝ 길이로 잘라둡니다.  3. 팬에 기름을 두른 후 두부를 넣고 한쪽이 완전히 노릇노릇하게 될때까지 중간불에 두었다 뒤집어요. 빨리 뒤집지말고 한쪽면이 단단해질때까지 기다려야 부서지지않아요.  4. 두부에 양념장을 조금씩 올리고 약불~중불에서 천천히 조려요.  5. 수분이 반정도 줄어들면 실고추와 채썬 파를 올려요. 처음부터 넣으면 색이 이쁘지않아요. 6. 센불로 잠깐 올려서 남은 수분을 날려줍니다",
    "views": 24031
  },
  {
    "creator": "금손곰손",
    "food_classification": [
      "매일반찬"
    ],
    "cook_name": "고기전",
    "ingredients": [
      "쇠고기 다짐육",
      "양파",
      "당근",
      "밀가루",
      "달걀",
      "식용유",
      "마늘",
      "국간장",
      "참기름"
    ],
    "time": 35,
    "receipe": "1. 채소는 다져서 준비해요. 2. 식용유를 제외한 채소, 고기, 양념, 달걀, 밀가루를 모두 섞어요.  3. 팬에 기름을 두르고 데운 후 재료를 한수저씩 떠서 팬에 놓아요. 중간에 한번 뒤집어주세요. 4. 고기가 주재료라 약한 불에서 천천히 익혀야 타지않고 보기좋아요.",
    "views": 13714
  },
  {
    "creator": "라이프쿠커",
    "food_classification": [
      "저장음식",
      "매일반찬"
    ],
    "cook_name": "두릅장아찌",
    "ingredients": [
      "두릅",
      "물",
      "국간장",
      "식초",
      "설탕",
      "소주",
      "청양고추"
    ],
    "time": 10,
    "receipe": "1. 두릅의 딱딱한 끝부분을 잘라내고 겉껍질을 떼어낸 후 씻어요. 2. 소금을 약간 넣은 끓는 물에 두릅의 줄기부터 넣어 30초 정도 먼저 데쳐요. 3. 두릅을 모두 넣고 줄기를 먼저 넣은 시간부터 총 3분 정도 데쳐줍니다.4. 건져서 찬물에 빨리 헹궈야 숨이 죽지 않고 아삭해요. 5. 두릅의 물기를 빼고 꼭 짜두세요. 6. 소스를 끓여서 한 김 식혀둡니다. 7. 용기에 두릅을 담고 소스를 넣어 3일간 숙성시킨 후 먹어요. 용기가 넓으면 소스가 더 필요하니 유념하세요.",
    "views": 4908
  },
  {
    "creator": "마카롱언니",
    "food_classification": [
      "가족",
      "초대요리",
      "매일반찬"
    ],
    "cook_name": "치킨 너겟",
    "ingredients": [
      "닭 안심살",
      "마요네즈",
      "시리얼",
      "마늘",
      "소금",
      "후추",
      "생각가루"
    ],
    "time": 50,
    "receipe":"1. 고기는 물에 한번 씻어서 물기를 빼두세요. 안심은 기름이 거의 없어 냄새가 나지않아 우유에 담가두지 않아도 괜찮아요.  2. 안심을 2등분 합니다. 이때 힘줄이 보이면 잘라내 줍니다. 힘줄을 제거하면 더 부드럽게 먹을 수 있어요. 3. 한입 크기로 자른 고기에 소금, 후추, 생강가루로 밑간을 합니다. 4. 마요네즈에 다진 마늘을 섞은 후 고기에 버무립니다.  5. 시리얼을 지퍼백에 넣고 방망이나 병으로 성글게 밀어요. 조금 크게 부숴야 바삭하게 씹히는 느낌이 좋아요. 6. 마요네즈에 버무린 고기에다 부순 시리얼을  골고루  묻혀요.  7. 오븐팬에 고기끼리 닿지않게 놓아요. 8. 200℃로 예열한 오븐에서 20분간 구워요. 중간에 한번 뒤집어주어야 앞뒤로 바삭하게 구워져요.",
    "views":54336
  },
  {"creator": "빨간모자",
    "food_classification": [
      "국",
      "가족"
    ],
    "cook_name": "버섯 들깨탕",
    "ingredients": [
      "느타리버섯",
      "말린 표고버섯",
      "대파",
      "멸치다시마",
      "국간장",
      "들깨가루",
      "쌀가루",
      "소금",
      "멸치",
      "다시마"
    ],
    "time": 30,
    "receipe": "1. 물 5~6컵에 멸치를 넣어 육수를 만든 후 다시마를 넣어요. 2. 5분 후 불을 끄고 다시마는 건져내고 육수 4컵을 준비해요. 3. 말린 표고버섯은 물에 불려서 썰고 느타리버섯은 가늘게 찢어요. 표고버섯은 말린 후 물에 불리는게 향과 맛이 더 좋지만 말린게 없으면 생표고를 사용해도 됩니다. 4. 육수 4컵에 국간장을 넣어 간을 미리 맞추고 버섯을 넣어요. 혹시, 싱거우면 소금을 넣어주세요.  5. 들깨가루와 쌀가루를 국물에 섞어요. 채를 사용하면 뭉치지않게 잘 풀어집니다. 쌀가루를 넣으면 영양면에서도 보완이 되고 식사대용으로 먹을 수 있습니다. 쌀가루를 넣은 후에는 타지않게 바닥을 저어주는게 좋아요. 6. 한소큼 끓으면 어슷하게 썬 대파를 넣어줍니다.",
    "views": 73456
  },
  {
    "creator": "지갑텅명",
    "food_classification": [
      "가족",
      "초대요리",
      "매일반찬"
    ],
    "cook_name": "새우 춘권",
    "ingredients": [
      "춘권피",
      "달걀",
      "식용유",
      "새우살",
      "양파",
      "당근",
      "풋고추",
      "녹말가루",
      "소금",
      "후추"
    ],
    "time": 120,
    "receipe": "1. 춘권피는 냉동실에서 꺼내 살짝 녹여두고 달걀은 잘 풀어둡니다. 2. 춘권피 가장자리에 붓이나 손으로 달걀물을 바른 후 중간에 속재료를 넣고 한쪽 모서리로 덮어요. 3. 잘 말아준 뒤 잠시 잘 붙도록 둡니다. 5. 170~180℃로 데운 기름에 춘권을 튀긴 후 키친타월에 밭쳐 기름을 빼요. 6. 초간장이나 스위트칠리소스, 해선장 등을 곁들이면 잘 어울려요.",
    "views": 36434
  },
  {
    "creator": "사랑맘",
    "food_classification": [
      "찌개",
      "가족"
    ],
    "cook_name": "참치 김치찌개",
    "ingredients": [
      "참치캔",
      "김치",
      "고추장",
      "참기름",
      "참치액",
      "두부"
    ],
    "time": 18,
    "receipe": "1. 김치를 먹기좋게 자르고 고추장과 기름을 넣어서 중간불에서 잘 어우러지게 볶아요. 2. 참치캔의 기름은 버리고 참치만 건져둬요. 올리브유에 담긴 참치는 그 기름으로 볶으세요. 3. 김치에 고추장과 기름이 잘 섞였으면 물을 붓고 끓여요. 4. 김치가 완전히 익으면 참치를 넣고 맛이 어우러지게 5분 정도만 더 끓여요. 5. 혹, 싱거우면 김칫국물 (참치액이나 조미료) 등으로 간을 맞춰주세요.",
    "views": 3923
  },
  {
    "creator": "유지누나",
    "food_classification": [
      "국",
      "미역"
    ],
    "cook_name": "들깨 미역국",
    "ingredients": [
      "미역",
      "들기름",
      "물",
      "국간장",
      "들깨가루",
      "마늘"
    ],
    "time": 10,
    "receipe": "1. 불린 미역은 먹기 좋게 잘라요.  2. 냄비에 미역과 들기름, 국간장, 마늘을 넣고 중간불에서 양념이 섞이도록 잠시 볶아요.  3. 뜨물(물)을 넣고 10분 정도 미역이 부드러워질때까지 끓여요. 뜨물을 넣으면 육수를 따로 내지않아도 맛있어요. 4. 소금으로 간을 맞춰요.  5. 거피한 들깨가루를 체에 걸러 국물에 풀어주세요. 걸쭉한게 좋으면 들깨가루를 더 넣어도 됩니다.  ",
    "views": 342284
  },
  {
    "creator": "빵덕후",
    "food_classification": [
      "간식"
    ],
    "cook_name": "전 남친 토스트",
    "ingredients": [
      "식삥",
      "크림치즈",
      "블루베리잼"
    ],
    "time": 2,
    "receipe": "1. 먼저 식빵을 토스터나 프라이팬에 노릇노릇하게 구워줍니다. 2. 구워진 식빵에 크림치즈를 골고루 펴발라줍니다. 3. 크림치즈에 위에 블루베리잼을 바릅니다. 4. 전자렌지에 넣어 10초간 돌려 완성합니다.",
    "views": 645453
  },
  {
    "creator": "카랑카랑",
    "food_classification": [
      "간식"
    ],
    "cook_name": "소떡소떡",
    "ingredients": [
      "떡볶이떡",
      "비엔나 소시지",
      "꼬치",
      "식용유",
      "허니머스터드",
      "케첩",
      "고추장",
      "물엿",
      "맛술",
      "핫소스"
    ],
    "time": 20,
    "receipe": "1. 단단한 떡볶이 떡은 끓는 물에 데쳐서 부드럽게 만들어요. 소시지도 데쳐서 기름기를 빼는게 좋아요. 2. 떡과 소시지를 체에 밭쳐 물기를 말려요.  3. 나무 꼬치에 소시지와 떡을 차례로 끼워요. 4. 기름을 넉넉하게 넣은 팬에서 튀기듯이 앞뒤를 구워요. 떡을 튀기면 튀어올라 화상을 입을 수 있으니 굽는게 안전합니다.  5. 소스를 팬에서 졸이거나 전자레인지에 1분 정도 돌려서 걸쭉하게 만들어요.6. 취향에 따라 소스와 허니머스터드 소스를 발라서 먹어요.",
    "views": 132221
  },
  {
    "creator": "두시의쿠킹",
    "food_classification": [
      "간식"
    ],
    "cook_name": "감말랭이",
    "ingredients": [
      "감"
    ],
    "time": 300,
    "receipe": "1. 감의 껍질을 벗긴 후 반으로 갈라요. 2. 꼭지를 떼어주고 씨도 보이는대로 빼줍니다. 3. 말리기 좋은 크기로 잘라줍니다. 4. 감을 건조기에 고루 깔아주세요.감끼리 겹쳐지지않게 놓아야 더 빨리 마릅니다. 5. 온도는 70℃로 맞춰놓고 시간은 10~20시간 사이로 감의 양에 따라 조절해요. 8. 감이 다 마르면 건조기를 끈 다음 감말랭이가 식으면 그릇이나 지퍼백에 담아 냉동실에 보관해요.",
    "views": 6654
  },
  {
    "creator": "이선주요리교실",
    "food_classification": [
      "기타",
      "소스"
    ],
    "cook_name": "발사믹 양파조림",
    "ingredients": [
      "양파",
      "포도씨오일",
      "발사믹비니거",
      "소금",
      "후추"
    ],
    "time": 40,
    "receipe": "1. 양파를 최대한 가늘게 썰어줍니다. 두께가 비슷해야 익는 속도가 같아지니 채칼을 사용하면 편해요. 2. 포도씨유를 두르고 약불에서 한동안 볶아 부드럽게 숨을 죽여요. 3. 양파가 부드럽게 볶아졌으면 발사믹비니거를 넣고 더 볶아줍니다.(총 40분 정도 소요됨) 4. 소금, 후추로 간해요. 5. 불을 끈 후 덜어내지말고 그대로 두고 뜸을 더 들인 후 용기에 담는게 좋아요.",
    "views": 248543
  },
  {
    "creator": "하사랑",
    "food_classification": [
      "저장음식"
    ],
    "cook_name": "동치미",
    "ingredients": [
      "총각무",
      "쪽파",
      "마늘",
      "생강",
      "지고추"
    ],
    "time": 100,
    "receipe": "1. 김장때 나오는 작은 달랑무를 소금에 굴려서 쪽파와 함께 하룻 동안 통에 담아둡니다. 달랑무가 없으면  큰무 하나를 토막낸 후 쪽파와 함께 소금을 그냥 고루 발라두세요. 2. 하루가 지난 후  생수에 소금으로 간을 짭짤하게 맞춰둡니다. 3. 지고추와 편으로 썬 마늘과 생강,  파프리카나 배, 감 등을 배보자기에 담아 모두 넣어요. 4. 실온에 하루정도 두었다가 김치냉장고에 넣어요.  5. 일주일 후부터 먹을 수 있습니다.",
    "views": 63454
  }
]

@app.get("/cooking_receipe")
async def filterCookingReceipe(
    creator: Optional[str] = Query(
        None,
        description="창작자를 한글로 적어주세요(ex. 꿀키, 양순맘)"
    ),
    food_classification: str = Query(
        ...,
        description="음식 분류를 한글로 적어주세요(ex. 밥, 죽, 면, 매일반찬, 저장음식, 소스, 양념장, 가족, 초대요리, 국, 찌개, 전골, 간식, 음료, 기타)"
    ),
    cook_name: Optional[str] = Query(
        None,
        description="요리명을 한글로 적어주세요(ex. 당근라페, 계란버섯전, 전 남친 토스트)"
    ),
    ingredients: Optional[str] = Query(
        None,
        description="재료를 한글로 적어주세요(ex. 당근, 버섯, 홀그레인머스타드, 시금치, 간장, 설탕)"
    ),
    time: Optional[int] = Query(
        None,
        ge=0,
        description="소요시간(단위: 분)은 0이상의 정수로 적어주세요."
    )
):
    # 데이터에서 검색 조건에 맞는 항목 필터링
    filtered_data = []
    for item in cooking_receipe_data:
        if (creator is None or creator == item["creator"]) \
                and food_classification in item["food_classification"] \
                and (cook_name is None or cook_name == item["cook_name"]) \
                and (ingredients is None or all(ingredient in item["ingredients"] for ingredient in ingredients.split(','))) \
                and (time is None or time == item["time"]):
            filtered_data.append(item)
    return filtered_data



#나이키 테스트
nikes = [    {
        "intent": "추천",
        "product_type": "신발",
        "category": "런닝",
        "gender": None,
        "color": None,
        "product_name": None,
        "answer": "나이키 러닝화 추천'에 대해 찾아볼게요!\n\n1. 인피니티 런 4\n나이키 리액트 폼보다 13% 더 높은 에너지 반환력을 갖춘 새로운 나이키 리액트X 폼으로 제작되어 상쾌하고 탄력 있는 발걸음이 유지되며, 지지력 있는 쿠셔닝을 적용해 러닝 시 안정적인 자세를 유지할 수 있도록 도와줍니다.\n\n2. 페가수스 40\n나이키 페가수스 40은 기존의 페가수스 모델을 업그레이드한 제품으로, 더욱 편안하고 안정적인 러닝을 할 수 있도록 설계되었습니다. 리액트 폼을 적용하여 부드럽고 탄력 있는 쿠셔닝을 제공하며, 발 중앙 부분에 아치를 지지해 주는 디자인이 적용되어 안정적인 러닝을 할 수 있도록 도와줍니다.\n\n3. 인빈서블 3\n줌X 폼을 적용하여 부드럽고 탄력 있는 쿠셔닝을 제공하며, 발 중앙 부분에 아치를 지지해 주는 디자인이 적용되어 안정적인 러닝을 할 수 있도록 도와줍니다.",
        "card": ["인피니티 런 4","페가수스 40"],
        "bubble": ["인빈서블3 알려줘", "페가수스 40 알려줘", "인피니티 런 4 알려줘"]
    },
             {
        "intent": "정보",
        "product_type": "신발",
        "category": "런닝",
        "gender": None,
        "color": None,
        "product_name": "인피니티런4",
        "answer": "나이키 인피니티 런 4'에 대해 알려드릴게요.\n\n나이키 인피니티 런 4는 지지력 있는 쿠셔닝을 적용한 제품입니다. 나이키 리액트 폼보다 13% 더 높은 에너지 반환력을 갖춘 새로운 나이키 리액트X 폼으로 제작되어 더욱 상쾌하고 탄력 있는 발걸음을 유지할 수 있습니다. 플라이니트와 리액트X 폼이 어우러진 부드러운 갑피의 지지력과 통기성으로 자신감 있는 러닝을 만들어줘요.",
        "card": ["인피니티 런 4"],
        "bubble": ["인피니티 런 4 사이즈 알려줘", "인피니티 런 4 특징 알려줘", "인피니티 런 4 소재 알려줘"]
    },
             {
        "intent": "정보",
        "product_type": "신발",
        "category": "런닝",
        "gender": "남성",
        "color": "오렌지",
        "product_name": "알파플라이2",
        "answer": "'나이키 알파플라이 2 남성 로드 레이싱화 사이즈'에 대해 찾아볼게요!\n\n나이키 알파플라이 2 남성 로드 레이싱화는 사이즈 250 ~ 310까지 있습니다.\n정확한 정보는 [제품 상세 페이지](https://www.nike.com/kr/t/%EC%95%8C%ED%8C%8C%ED%94%8C%EB%9D%BC%EC%9D%B4-2-%EB%82%A8%EC%84%B1-%EB%A1%9C%EB%93%9C-%EB%A0%88%EC%9D%B4%EC%8B%B1%ED%99%94-tL7CEVL8/DN3555-600)에서 확인해 주세요",
        "card": ["나이키 알파플라이 2 남성 로드 레이싱화"],
        "bubble": ["나이키 알파플라이 2 남성 로드 레이싱화 색상 알려줘", "나이키 알파플라이 2 남성 로드 레이싱화 소재 알려줘", "나이키 알파플라이 2 남성 로드 레이싱화 특징 알려줘"]
    }
            ]

@app.get("/nike_test")
async def search_nikes(
    intent: str,
    product_type: Optional[str] = None,
    category: Optional[str] = None,
    gender: Optional[str] = None,
    color: Optional[str] = None,
    product_name: Optional[str] = None,
):
    # 필터링된 결과를 저장할 리스트
    filtered_nikes = []
    
    for nike in nikes:
        # 각 필터에 대한 조건 확인
        if (
            (intent is None or nike['intent'] == intent) and
            (product_type is None or nike['product_type'] == product_type) and
            (category is None or nike['category'] == category) and
            (gender is None or nike['gender'] == gender) and
            (color is None or nike['color'] == color) and
            (product_name is None or nike['product_name'] == product_name)
        ):

            filtered_nikes.append(nike)

    
    return filtered_nikes


#240305 테스트
rag_data = [{
        "category": "Security Monitoring",
        "context": "[['Security Monitoring Managed 서비스가 무엇인가요?', 'Security Monitoring Managed 서비스는 네이버 서비스를 외부의 공격으로부터 안전하게 보호하고 있  는 보안전문 인력이 네이버 클라우드 플랫폼 고객의 서비스를 24시간 365일 보호하는 보안관제 서비스예요.\nSecurity Monitoring Basic 서비스에서 보다 강화  된 모니터링을 원하는 고객에게 유료로 제공되는 서비스로 탐지/차단 서비스 및 분석 서비스를 추가로 제공해요.'], ['Security Monitoring Managed 서비스에   서 주간/월간 보고서를 제공하나요?', 'Security Monitoring Managed는 보다 강화된 모니터링을 원하는 고객에게 유료로 제공되는 서비스로 탐지/차단 서비스   별 주간/월간 보고서를 제공하고 있어요.'], ['WAF를 통해 차단된 것 같은데 예외 처리하려면 어떻게 해야하나요?', 'Security Monitoring에서 WAF를 통해 차   단되었을 때 예외 처리하려면,  아래 두 항목을 포함하여 [고객지원 > 문의하기]로 접수해 주세요.\n\n1. 예외 처리가 필요한 탐지 이벤트\n2. 예외 처리가 필  요한 Request URL\n3. 예외 처리가 필요한 Source IP\n\n자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['모의 침투 테스트란 무엇인가요?', '모의 침투   테스트란, 네이버 클라우드 플랫폼 상에 구성한 고객의 서비스 및 리소스에 대한 보안 수준을 평가하기 위해 실제 공격과 유사한 행위를 수행하는 것을 의미해  요.\n\n다만, 고객은 네이버 클라우드 플랫폼의 인프라 또는 네이버 클라우드 플랫폼 서비스 자체에 대한 보안 평가를 수행할 수 없어요.\n\n모의 침투 테스트  와 관련하여 상세한 정책과 사전 신청을 원하시는 경우, 아래 링크의 모의 침투 테스트 지원 정책 및 신청서를 참고해 주세요.'], ['모의 침투 테스트를 하기   위한 네이버 클라우드 플랫폼의 지원 정책은 무엇인가요?', '네이버 클라우드 플랫폼은 고객의 보안인증 및 감사를 위한 혹은 자체 계획에 따른 모의 침투 테   스트 진행을 지원하고 있어요.\n\n다만, 테스트 전 반드시 당사에 사전 신청을 해 주셔야 해요. 상세한 내용 및 사전 신청서의 양식은 아래 버튼을 눌러 확인   해 주세요.'], ['IPS V2 보안 이벤트 발생 시 어떻게 인지할 수 있나요?', 'Managed 서비스 이용 시 Security Monitoring IPS 이벤트가 발생하는 경우 Notification Setting에 설정된 정보로 이벤트 정보를 안내하고 있어요.\n상세 정보는 Console에서 확인하실 수 있어요.\n\nClassic 플랫폼 이용 시 [네이버 클라우드   플랫폼 > Console > Security Monitoring > Notification Setting > IPS(V1)]에서 안내받고자 하는 담당자를 설정할 수 있어요.\n\nVPC 플랫폼 이용 시 [네이  버 클라우드 플랫폼 > Console > Security Monitoring > Notification Setting > IPS(V2)]에서 안내받고자 하는 담당자를 설정할 수 있어요.\n\n자세한 내용은   아래 버튼을 눌러 확인해 주세요.'], ['Anti-DDoS 보안 이벤트 발생 시 어떻게 인지할 수 있나요?', 'Security Monitoring Anti-DDoS 이벤트 발생 시 Managed 고객에게는 Notification Setting에 설정된 정보로 이벤트 정보를 안내하고 있어요.\n\n자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['WAF 보안 이벤   트 발생 시 어떻게 인지할 수 있나요?', 'Security Monitoring WAF 이벤트 발생 시 Managed 고객에게는 Notification Setting에 설정된 정보로 이벤트 정보를   안내하고 있어요.\n\n자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['IDS 보안 이벤트 발생 시 어떻게 인지할 수 있나요?', 'Security Monitoring IDS    이벤트 발생 시 Managed 고객에게는 Notification Setting에 설정된 정보로 이벤트 정보를 간략하게 안내하고 있어요.\n\n자세한 내용은 아래 버튼을 눌러 확   인해 주세요.'], ['기본으로 제공되는 무료 보안 서비스는 무엇인가요?', 'Classic 플랫폼에서는 IDS, Anti-Virus(Window에 한해) 서비스를 무료로 제공하며,\nVPC 플랫폼에서는 IDS 서비스를 무료로 제공해요. (Anti-Virus는 무료로 제공하지 않아요.)\n\n무료 보안 서비스에 대한 더 자세한 내용은 아래 버튼을 눌러   확인해 주세요.'], ['IPS V2 서비스를 사용 시 주의사항은 무엇인가요?', 'IPS(V2) 서비스 사용 시 주의사항에 대해 알려 드릴게요.'], ['Security Monitoring의 IPS V2는 무엇인가요?', 'Security Monitoring의 IPS(V2)는 VPC 플랫폼에서 제공하며 Host 기반의 인바운드/아웃바운드 트래픽을 모니터링하여 의심스러운   활동을 탐지하고 차단해요.\n\nIPS는 24시간 365일 모니터링하고 공격에 대해 실시간 차단함으로써 안전하게 서비스가 운영될 수 있도록 지원해요.\n\nIPS(V2)에서 제공하는 서비스에 대한 자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['Anti-Virus 서비스를 사용 시 주의사항은 무엇인가요?', 'Anti-Virus 서비  스를 사용 시 주의사항에 대해 알려드릴게요.'], ['Anti-Virus 보안 이벤트 발생 시 어떻게 인지할 수 있나요?', 'Security Monitoring Anti-Virus 이벤트 발   생 시 Managed 고객에게는 Notification Setting에 설정된 정보로 이벤트 정보를 안내하고 있어요. 상세 정보는 Console에서 확인해 주세요.\n\n※ Security Monitoring에는 Basic과 Managed 서비스가 있으며,\nBasic 서비스를 사용하시는 경우 보안 이벤트가 발생했을 때 정보를 받아볼 이메일을 별도로 설정할 수 없으  며, 로그인 ID로 정보를 보내드려요.\nManaged 서비스를 사용하시는 경우 Notification Setting 메뉴에서 정보를 받아볼 이메일을 설정할 수 있으며, 별도 설   정을 하지 않으신 경우에는 로그인 ID로 정보를 보내드려요.\n\n자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['WAF 모니터링 대상은 어떻게 되나요?',   '\u200bWAF는 HTTP/HTTPS 표준 프로토콜을 사용하는 웹 서비스에 대해서만 모니터링할 수 있어요.\nLoad Balancer 설정된 서비스 모니터링을 위해서 Load Balancer Protocol 을 반드시 HTTP/HTTPS로 설정하셔야 해요. (TCP, SSL로 설정 시 WAF 서비스를 제공받을 수 없습니다.)'], ['OS 커널을 업데이트 할 경우 Security Monitoring에 영향이 있나요?', '고객이 임의로 OS 커널을 업데이트할 경우, Security Monitoring 서비스가 정상적으로 제공되지 않을 수 있어요.\n커널 업  데이트가 필요한 경우 호환 커널 리스트를 참고해 주세요.'], ['Security Monitoring의 IPS가 뭐야?', 'IPS(Intrusion Prevention System)란 고객의 서비스로   인입되는 공격을 탐지/차단하는 보안 솔루션으로, 24시간*365일 모니터링하여 고객의 서비스가 안전하게 운영될 수 있도록 지원하고 있어요.'], ['Security Monitoring의 보고서는 언제 발송돼?', '침입행위가 탐지될 경우 이를 분석하여 고객의 서비스에 위협이 된다고 판단되면 보고서를 발송해요.'], ['Security Monitoring에서 탐지된 공격정보는 어디서 확인해?', 'Security Monitoring에서 탐지된 공격정보는 [콘솔 > Security Monitoring > Dashboard] 에서 확인할 수 있  어요.'], ['Security Monitoring에서 침해사고 기술 지원이 뭐야?', '침해사고 기술 지원은 고객 서비스에 침해사고가 발생하면 대응 전문가가 침해사고에 대   한 분석을 수행하고, 원인을 파악해 차후 동일한 피해가 발생하지 않도록 지원하는 서비스예요.'], ['Security Monitoring에서 Anti-Virus 패턴 업데이트 주기   알려줘', '백신 패턴은 매일 새벽 1시에 업데이트 되며, 실시간 모니터링에 즉시 반영돼요.'], ['Security Monitoring의 Anti-Virus가 뭐야?', 'Anti-Virus는   고객이 운영 중인 서버에 악성코드를 실시간으로 탐지하고 격리/삭제 조치함으로써 고객의 서비스가 안정적으로 운영될 수 있도록 지원해요.\n플랫폼 환경에   따라 Anti-Virus(V1), Anti-Virus(V2)로 구분되며, Classic 환경에서 제공하는 서비스는 Anti-Virus(V1), VPC 환경에서 제공하는 서비스는 Anti-Virus(V2)라고   해요.\n\n더 자세한 내용은 아래 버튼을 눌러 확인해 주세요.'], ['Security Monitoring의 WAF가 뭐야?', 'WAF(Web Application Firewall)는 Web 기반(HTTP/HTTPS) 트래픽을 모니터링하여 공격 트래픽을 탐지 및 차단하는 보안 솔루션이에요.\n\nWAF에서 제공하는 서비스에 대한 자세한 내용은 아래 버튼을 눌러 확인   해 주세요.']]"
                }
           ]

@app.get("/rag_test")
async def get_rag_test(
    category: Optional[str] = Query(None, description="Location of the rental car")
) -> List[dict]:
    filtered_rag = rag_data

    if category:
        filtered_rag = [rag for rag in filtered_rag if rag["category"] == category]
    return filtered_rag


rag_data2 = [{
        "category": "Security Monitoring",
        "context": "Security Monitoring에는 Basic 서비스와 Managed 서비스가 있으며, 서비스 구분에 따라 제공하는 기능 및 이용 요금이 상이합니다. Security Monitoring Managed가 플랫폼별로 제공하는 보안 서비스는 다음과 같습니다. 사용자 환경이 VPC인지 Classic인지에 따라 동일한 서비스여도 일부 기능에 차이가 있을 수 있습니다. 이용 중인 플랫폼을 먼저 확인한 후 상세 설명을 참고해 주십시오.  참고  •	Security Monitoring 개념의 원활한 이해를 위해 다음 용어에 유의해 주십시오.  o	V1: Classic 환경을 일컫는 약어  o	V2: VPC 환경을 일컫는 약어  •	Security Monitoring 개념 학습 전 보안 서비스별 주의 사항도 사전에 반드시 숙지해야 합니다. 보안 서비스별 주의 사항은 Security Monitoring 사용 준비를 참조해 주십시오.  VPC  VPC 환경에서 Security Monitoring Managed가 제공하는 IDS, Anti-Virus, Anti-DDoS, WAF, IPS 기능을 설명합니다.  IDS(V2)  사용자의 서비스로 인입되는 공격을 실시간 탐지합니다. 24시간 365일 모니터링함으로써 사용자의 서비스가 안전하게 운영될 수 있도록 지원합니다. 제공하는 기능은 다음과 같습니다.  •	보안 사고 의심 이벤트 발생 시 탐지 및 분석 보고서 전달  •	최신 공격 위협에 대해서 지속적인 탐지 정책 설정 및 패턴 업데이트 적용  •	사용자 요청 시 탐지 예외 처리 제공  •	주간, 월간 보고서 제공  Anti-Virus(V2)  악성코드를 탐지하고 방어합니다. 사용자가 운영 중인 서버에 악성코드를 실시간으로 탐지하고 격리 및 삭제 조치함으로써 사용자의 서비스가 안정적으로 운영될 수 있도록 지원합니다. 제공하는 기능은 다음과 같습니다.  •	바이러스, 스파이웨어의 격리 및 삭제  •	악성코드 의심 이벤트 발생 시 분석 보고서 제공  •	Windows/Linux용 서버 백신 제공  •	특정 파일 및 폴더에 대한 예외 처리 제공  •	최신 탐지 패턴 자동 업데이트  •	네이버 클라우드 플랫폼 콘솔에서 탐지 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공  참고  Anti-Virus 백신 패턴은 매일 새벽 1시에 업데이트되며, 실시간 모니터링에 즉시 반영됩니다.  Anti-DDoS(V2)  사용자의 서비스로 인입되는 DDoS 공격을 24시간 365일 모니터링하여 탐지 및 차단함으로써 사용자의 서비스가 안정적으로 운영될 수 있도록 지원합니다. Full Packet Analysis 방식으로 빠르고 정확한 공격 탐지가 가능합니다. 제공하는 기능은 다음과 같습니다.  •	다단계 필터를 통한 다양한 유형의 DDoS 공격으로부터 보호  •	사용자별 특화된 보호 대상(Zone)을 생성하여 별도 정책으로 공격을 감지  •	사용자 특화 공격에 대한 분석 및 차단 룰 생성, 등록을 지원  •	정상적인 대량 트래픽을 유발하는 Source IP(NAT IP) 별도 관리 및 오탐 방지  •	학습을 통한 사용자 맞춤형 임계치 설정 제공  •	주간, 월간 보고서 제공  WAF(V2)  웹 공격을 전문적으로 탐지하고 방어합니다. HTTP, HTTPS의 웹 기반 트래픽을 모니터링하여 사용자의 웹 서비스로 공격이 인입될 경우 WAF 전용 솔루션을 통해 탐지하고 방어함으로써 즉각적인 대응이 가능하도록 지원합니다. VPC 환경에서 WAF는 Reverse Proxy 방식으로 사용자별 별도의 WAF 플랫폼을 제공하며, 안정적인 서비스를 위해 기본적으로 이중화 구조를 갖추고 있습니다. WAF VM과 사용자 서비스 Load Balancer 간의 통신은 HTTP 80 port 공인 통신을 사용합니다.  위 내용을 토대로 VPC 환경에서의 WAF 서비스 구성을 도식화하면 다음과 같습니다.    WAF는 기본적으로 탐지 모드와 차단 모드로 운영됩니다. 약 1개월 동안 탐지 모드로 운영한 다음 탐지 이벤트를 분석하여 차단 정책과 차단 모드 변경 일정을 사용자에게 제안하는 방식입니다. 이러한 방식으로 인해 탐지 모드로 운영되는 동안 네이버 클라우드 플랫폼 콘솔에서는 확인되는 로그는 없으며, 차단 모드로 변경된 후 차단된 로그만 제공하게 됩니다.  WAF에서 제공하는 기능은 다음과 같습니다.  •	접근 권한 취약점 탐지 및 차단  •	암호화 오류 탐지 및 차단  •	보안 설정 오류 탐지 및 차단  •	어플리케이션 취약점 탐지 및 차단  •	SSRF, XSS, CSRF, Injection 탐지 및 차단  •	Cookie 변조 및 도용 방지 등 다양한 웹 공격 탐지 및 차단  •	고객사 환경에 적합한 차단 정책 설정 및 관리  •	IP 및 URL 예외 기능 제공  •	주기적인 보안 정책 업데이트 제공  •	네이버 클라우드 플랫폼 콘솔에서 차단 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공  IPS(V2)  호스트 기반의 Inbound, Outbound 트래픽을 24시간 365일 모니터링하여 의심스러운 활동을 탐지하고 차단하여 사용자의 서비스를 안전하게 운영될 수 있도록 지원합니다. IPS는 기본적으로 탐지 모드와 차단 모드로 운영됩니다. 약 1개월 동안 탐지 모드로 운영한 다음 탐지 이벤트를 분석하여 차단 정책과 차단 모드 변경 일정을 사용자에게 제안하는 방식입니다. 이러한 방식으로 인해 탐지 모드로 운영되는 동안 네이버 클라우드 플랫폼 콘솔에서는 확인되는 로그는 없으며, 차단 모드로 변경된 후 차단된 로그만 제공하게 됩니다.  IPS에서 제공하는 기능은 다음과 같습니다.  •	운영체제별, 애플리케이션별, 서버 용도별 맞춤형 탐지 및 차단 정책 기능 제공  •	가상 패치(virtual patching) 제공을 통해 취약한 버전의 애플리케이션이 패치될 때까지 시스템을 보호하여 제로데이 공격으로부터 VM 보호  •	IPS 탐지 및 차단 정책의 주기적인 업데이트  •	호스트의 애플리케이션에 대해 주기적인 스캔 및 탐지 정책 적용을 통해 취약점으로부터 VM 보호  •	네이버 클라우드 플랫폼 콘솔에서 차단 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공  Classic  Classic 환경에서 Security Monitoring Managed가 제공하는 IDS, Anti-Virus, Anti-DDoS, WAF, IPS 기능을 설명합니다.  IDS(V1)  VPC 환경의 IDS 지원 내용과 동일합니다. 이 페이지의 VPC > IDS(V2)를 참조해 주십시오.  Anti-Virus(V1)  VPC 환경의 Anti-Virus 지원 내용과 동일합니다. 이 페이지의 VPC > Anti-Virus(V2)를 참조해 주십시오.  Anti-DDoS(V1)  VPC 환경의 Anti-DDoS 지원 내용과 동일합니다. 이 페이지의 VPC > Anti-DDoS(V2)를 참조해 주십시오.  WAF(V1)  웹 공격을 전문적으로 탐지하고 방어합니다. HTTP, HTTPS의 웹 기반 트래픽을 모니터링하여 사용자의 웹 서비스로 공격이 인입될 경우 WAF 전용 솔루션을 통해 탐지하고 방어함으로써 즉각적인 대응이 가능하도록 지원합니다. WAF는 기본적으로 탐지 모드와 차단 모드로 운영됩니다. 약 1개월 동안 탐지 모드로 운영한 다음 탐지 이벤트를 분석하여 차단 정책과 차단 모드 변경 일정을 사용자에게 제안하는 방식입니다. 이러한 방식으로 인해 탐지 모드로 운영되는 동안 네이버 클라우드 플랫폼 콘솔에서는 확인되는 로그는 없으며, 차단 모드로 변경된 후 차단된 로그만 제공하게 됩니다.  WAF에서 제공하는 기능은 다음과 같습니다.  •	접근 권한 취약점 탐지 및 차단  •	암호화 오류 탐지 및 차단  •	보안 설정 오류 탐지 및 차단  •	어플리케이션 취약점 탐지 및 차단  •	SSRF, XSS, CSRF, Injection 탐지 및 차단  •	Cookie 변조 및 도용 방지 등 다양한 웹 공격 탐지 및 차단  •	고객사 환경에 적합한 차단 정책 설정 및 관리  •	IP 및 URL 예외 기능 제공  •	주기적인 보안 정책 업데이트 제공  •	네이버 클라우드 플랫폼 콘솔에서 차단 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공  IPS(V1)  네트워크 기반의 Inbound, Outbound 트래픽을 24시간 365일 모니터링하여 의심스러운 활동을 탐지하고 차단하여 사용자의 서비스를 안전하게 운영될 수 있도록 지원합니다. IPS는 기본적으로 탐지 모드와 차단 모드로 운영됩니다. 약 1개월 동안 탐지 모드로 운영한 다음 탐지 이벤트를 분석하여 차단 정책과 차단 모드 변경 일정을 사용자에게 제안하는 방식입니다. 이러한 방식으로 인해 탐지 모드로 운영되는 동안 네이버 클라우드 플랫폼 콘솔에서는 확인되는 로그는 없으며, 차단 모드로 변경된 후 차단된 로그만 제공하게 됩니다.  IPS에서 제공하는 기능은 다음과 같습니다.  •	실시간 트래픽 분석을 통해서 악의적인 유해 트래픽 탐지 차단  •	사용자별 차단 정책 제공  o	시그니처 기반 방어  o	Application 방어  o	프로토콜 기반 방어  o	도메인 차단  o	유해 사이트/URL 기반 차단  •	패턴 기반의 차단 예외 처리 제공  •	IP 차단 예외 처리 제공  •	IPS 탐지 및 차단 정책의 주기적인 업데이트  •	네이버 클라우드 플랫폼 콘솔에서 차단 정보 확인 및 대시보드 제공  •	주간, 월간 보고서 제공"
                }
           ]

@app.get("/rag_test2")
async def get_rag_test(
    category: Optional[str] = Query(None, description="Location of the rental car")
) -> List[dict]:
    filtered_rag = rag_data2

    if category:
        filtered_rag = [rag for rag in filtered_rag if rag["category"] == category]
    return filtered_rag


#240226 테스트
new_books = [    {
        "title": "위대한 개츠비",
        "year": 1925,
        "country_code": 1,
        "author": "프란시스 스콧 피츠제럴드",
        "publisher": "차이크",
        "rating": 8.9,
        "price": 15000,
        "genre_code": 1,
        "reviews": ["로맨틱한 분위기가 가득한 명작", "최고의 소설 중 하나"]
    },
    {
        "title": "1984",
        "year": 1949,
        "country_code": 1,
        "author": "조지 오웰",
        "publisher": "한국출판사",
        "rating": 9.2,
        "price": 12000,
        "genre_code": 1,
        "reviews": ["거장의 예언, 끝없는 경고", "현실적인 비전"]
    },
    {
        "title": "미움받을 용기",
        "year": 2013,
        "country_code": 81,
        "author": "기히로 시모노",
        "publisher": "북하우스",
        "rating": 8.5,
        "price": 18000,
        "genre_code": 1,
        "reviews": ["자신을 다시 발견하는 여정", "위로와 용기를 주는 책"]
    },
    {
        "title": "반지의 제왕",
        "year": 1954,
        "country_code": 1,
        "author": "J.R.R. 톨킨",
        "publisher": "팬텀",
        "rating": 9.8,
        "price": 25000,
        "genre_code": 1,
        "reviews": ["환상의 세계로 초대하는 대작", "마법같은 모험"]
    },
    {
        "title": "죽은 시인의 사회",
        "year": 1989,
        "country_code": 1,
        "author": "피터 위어",
        "publisher": "대한출판사",
        "rating": 9.0,
        "price": 16000,
        "genre_code": 1,
        "reviews": ["자유와 열정을 논하는 명작", "파워풀한 메시지"]
    },
    {
        "title": "동물농장",
        "year": 1945,
        "country_code": 1,
        "author": "조지 오웰",
        "publisher": "로지",
        "rating": 8.7,
        "price": 11000,
        "genre_code": 1,
        "reviews": ["유쾌하면서도 경쾌한 이야기", "사회 비판의 걸작"]
    },
    {
        "title": "토지",
        "year": 1935,
        "country_code": 82,
        "author": "박경리",
        "publisher": "현대문학",
        "rating": 9.5,
        "price": 20000,
        "genre_code": 1,
        "reviews": ["한국 문학의 걸작", "희망과 우정의 이야기"]
    },
    {
        "title": "데미안",
        "year": 1919,
        "country_code": 1,
        "author": "헤르만 헤세",
        "publisher": "서양문고",
        "rating": 8.8,
        "price": 17000,
        "genre_code": 1,
        "reviews": ["내면의 탐색과 성장", "청춘의 명작"]
    },
    {
        "title": "사랑의 불시착",
        "year": 2016,
        "country_code": 82,
        "author": "박지은",
        "publisher": "샘터",
        "rating": 9.3,
        "price": 22000,
        "genre_code": 1,
        "reviews": ["감동과 재미를 모두 잡은 대작", "눈을 뗄 수 없는 몰입도"]
    },
    {
        "title": "빨간 머리 앤",
        "year": 1908,
        "country_code": 1,
        "author": "루시 모드 몽고메리",
        "publisher": "문학동네",
        "rating": 8.6,
        "price": 13000,
        "genre_code": 1,
        "reviews": ["꿈과 용기의 이야기", "사랑스러운 캐릭터들"]
    },
        {
        "title": "꽃을 보듯 너를 본다",
        "year": 1992,
        "country_code": 82,
        "author": "나태주",
        "publisher": "문학동네",
        "rating": 9.2,
        "price": 16000,
        "genre_code": 2,
        "reviews": ["감성을 자극하는 시집", "시를 통해 세상을 본다"]
    },
    {
        "title": "어떻게 말해줘야 할까",
        "year": 2018,
        "country_code": 82,
        "author": "윤정비",
        "publisher": "시인정글",
        "rating": 9.0,
        "price": 18000,
        "genre_code": 2,
        "reviews": ["마음을 담은 시의 향연", "어떤 말로 표현할까 고민되는 감정을 담은 시"]
    },
    {
        "title": "우리 집에 가는 길",
        "year": 2005,
        "country_code": 82,
        "author": "하태완",
        "publisher": "샘터",
        "rating": 8.8,
        "price": 15000,
        "genre_code": 2,
        "reviews": ["일상의 아름다움을 느낄 수 있는 시집", "마음이 따뜻해지는 시"]
    },
    {
        "title": "내 마음의 숲",
        "year": 2010,
        "country_code": 82,
        "author": "정호승",
        "publisher": "행복한 어린이",
        "rating": 8.5,
        "price": 14000,
        "genre_code": 2,
        "reviews": ["힐링되는 시집", "자연과 함께하는 시"]
    },
    {
        "title": "봄이 오나요",
        "year": 2015,
        "country_code": 82,
        "author": "이해인",
        "publisher": "봄봄",
        "rating": 9.5,
        "price": 20000,
        "genre_code": 2,
        "reviews": ["봄의 따뜻함을 느낄 수 있는 시집", "꽃 향기처럼 달콤한 시"]
    },
    {
        "title": "오늘의 기분",
        "year": 2008,
        "country_code": 82,
        "author": "이상철",
        "publisher": "무드",
        "rating": 8.9,
        "price": 17000,
        "genre_code": 2,
        "reviews": ["하루를 마무리하는 시집", "감성을 자극하는 달콤한 시"]
    },
    {
        "title": "너의 뒤에 서서",
        "year": 2019,
        "country_code": 82,
        "author": "손히",
        "publisher": "서현",
        "rating": 9.2,
        "price": 19000,
        "genre_code": 2,
        "reviews": ["사랑을 담은 시집", "눈물과 웃음을 함께하는 시"]
    },
    {
        "title": "한 뼘의 자유",
        "year": 2002,
        "country_code": 82,
        "author": "홍현희",
        "publisher": "오늘의 책",
        "rating": 8.7,
        "price": 18000,
        "genre_code": 2,
        "reviews": ["자유로움을 노래하는 시집", "희망의 메시지를 전하는 시"]
    },
    {
        "title": "여름날",
        "year": 2017,
        "country_code": 82,
        "author": "박희진",
        "publisher": "희망",
        "rating": 9.0,
        "price": 16000,
        "genre_code": 2,
        "reviews": ["여름의 시원함을 담은 시집", "더운 여름을 시원하게 해주는 시"]
    },
    {
        "title": "소리없는 아우성",
        "year": 2007,
        "country_code": 82,
        "author": "정재승",
        "publisher": "소나무",
        "rating": 8.8,
        "price": 15000,
        "genre_code": 2,
        "reviews": ["감동과 울림을 주는 시집", "작은 소리에서 큰 울림을 느끼는 시"]
    },
    {
        "title": "김정은의 불편한 진실",
        "year": 2020,
        "country_code": 82,
        "author": "이선희",
        "publisher": "한국출판사",
        "rating": 8.7,
        "price": 18000,
        "genre_code": 3,
        "reviews": ["북한에 대한 새로운 시각을 제시하는 책", "김정은의 인간적인 면을 다룬 책"]
    },
    {
        "title": "여행의 이유",
        "year": 2015,
        "country_code": 82,
        "author": "김영하",
        "publisher": "북한산",
        "rating": 9.1,
        "price": 20000,
        "genre_code": 3,
        "reviews": ["여행의 진정한 의미를 찾아가는 여정", "인생을 바꿀 수 있는 책"]
    },
    {
        "title": "삶과 죽음에 대하여",
        "year": 2018,
        "country_code": 82,
        "author": "조용필",
        "publisher": "다산북스",
        "rating": 8.8,
        "price": 17000,
        "genre_code": 3,
        "reviews": ["인생의 가치에 대해 다시 생각하게 만드는 책", "삶과 죽음에 대한 깊은 인사이트를 제공하는 책"]
    },
    {
        "title": "우리들의 무지개",
        "year": 2019,
        "country_code": 82,
        "author": "이영철",
        "publisher": "모아씨엔씨",
        "rating": 8.9,
        "price": 19000,
        "genre_code": 3,
        "reviews": ["다양성과 포용에 대한 메시지를 전하는 책", "우리 사회의 미래를 엿보는 책"]
    },
    {
        "title": "나의 하루",
        "year": 2017,
        "country_code": 82,
        "author": "서울시립",
        "publisher": "세계문학",
        "rating": 8.6,
        "price": 16000,
        "genre_code": 3,
        "reviews": ["일상의 아름다움을 발견하는 책", "작은 것들에 감사하는 마음을 심는 책"]
    },
    {
        "title": "무모한 도전",
        "year": 2016,
        "country_code": 82,
        "author": "김영민",
        "publisher": "노란별",
        "rating": 8.5,
        "price": 15000,
        "genre_code": 3,
        "reviews": ["포기하지 않는 열정을 보여주는 책", "성공과 실패 사이의 비밀을 말해주는 책"]
    },
    {
        "title": "한 걸음 더",
        "year": 2021,
        "country_code": 82,
        "author": "강호동",
        "publisher": "성안당",
        "rating": 8.4,
        "price": 14000,
        "genre_code": 4,
        "reviews": ["자기계발의 길을 찾아가는 책", "한 발 더 나아가는 비결을 알려주는 책"]
    },
        {
        "title": "부의 시나리오",
        "year": 2018,
        "country_code": 1,
        "author": "이제니",
        "publisher": "성인당",
        "rating": 8.9,
        "price": 18000,
        "genre_code": 4,
        "reviews": ["부자가 되기 위한 실전 가이드", "재무 교육의 바이블"]
    },
    {
        "title": "죽음에 관하여",
        "year": 1999,
        "country_code": 1,
        "author": "베르테르스만",
        "publisher": "문학동네",
        "rating": 9.2,
        "price": 20000,
        "genre_code": 4,
        "reviews": ["인생의 가치를 깊이 생각하게 하는 책", "생의 진정한 의미를 찾아가는 여정"]
    },
    {
        "title": "코스모스",
        "year": 1980,
        "country_code": 1,
        "author": "칼 세이건",
        "publisher": "사이언스북스",
        "rating": 8.8,
        "price": 17000,
        "genre_code": 3,
        "reviews": ["우주에 대한 감탄을 자아내는 책", "과학을 통해 세계를 이해하는 철학적인 접근"]
    },
    {
        "title": "인생의 가치",
        "year": 2015,
        "country_code": 1,
        "author": "팀 클라인",
        "publisher": "빅픽처스프레스",
        "rating": 9.0,
        "price": 19000,
        "genre_code": 4,
        "reviews": ["인생의 방향을 재정립하는 책", "진정한 행복의 길을 찾아가는 지침서"]
    },
    {
        "title": "내가 좋아하는 것만 남기고, 나머지는 모두 정리하라",
        "year": 2019,
        "country_code": 1,
        "author": "미노스",
        "publisher": "현대경제사",
        "rating": 8.7,
        "price": 16000,
        "genre_code": 4,
        "reviews": ["간소화된 삶을 위한 지혜", "불필요한 것을 버리고 진정한 가치를 찾아가는 여정"]
    },
    {
        "title": "성공하는 사람들의 7가지 습관",
        "year": 2010,
        "country_code": 1,
        "author": "스티븐 R. 코비",
        "publisher": "시네21",
        "rating": 8.5,
        "price": 15000,
        "genre_code": 4,
        "reviews": ["성공의 비결을 알려주는 베스트셀러", "변화와 성장을 이끌어내는 실용적인 가이드북"]
    },
    {
        "title": "행복의 운",
        "year": 2005,
        "country_code": 1,
        "author": "조슈아 워튼",
        "publisher": "한국경제사",
        "rating": 8.4,
        "price": 14000,
        "genre_code": 4,
        "reviews": ["인생의 목표를 달성하는 법을 알려주는 책", "내면의 우주적인 행복을 발견하는 여정"]
    }
]

@app.get("/books/search")
async def search_books(
    genre_code: Optional[int] = None,
    country_code: Optional[int] = None,
    author: Optional[str] = None,
    publisher: Optional[str] = None,
    rating: Optional[float] = None,
    min_price: Optional[int] = None,
    max_price: Optional[int] = None,
    title: Optional[str] = None,
    keyword: Optional[str] = None
):
    # 필터링된 결과를 저장할 리스트
    filtered_books = []
    
    for book in new_books:
        # 각 필터에 대한 조건 확인
        if (
            (genre_code is None or book['genre_code'] == genre_code) and
            (country_code is None or book['country_code'] == country_code) and
            (author is None or author.lower() in book['author'].lower()) and
            (publisher is None or publisher.lower() in book['publisher'].lower()) and
            (rating is None or book['rating'] >= rating) and
            (min_price is None or book["price"] >= min_price) and
            (max_price is None or book["price"] <= max_price) and
            (title is None or (title.lower() in book['title'].lower()))
        ):
            # keyword가 None이 아닌 경우에만 검색
            if keyword is not None:
                # 키워드 검색 결과 저장
                keyword_results = [keyword.lower() in ' '.join(book['reviews']).lower() for keyword in keyword.split(',')]
                # 모든 키워드가 만족하는지 확인
                if all(keyword_results):
                    filtered_books.append(book)
            else:
                filtered_books.append(book)
            
            # 호출 개수 제한
            if len(filtered_books) >= 10:
                break
    
    return filtered_books


new_movies = [
    {
        "title": "기생충",
        "year": 2019,
        "country_code": 82,
        "director": "봉준호",
        "actors": ["송강호", "이선균"],
        "rating": 8.6,
        "audience_count": 10000000,
        "genre_code": 6,
        "reviews": ["현실을 반영한 작품", "봉준호 감독의 뛰어난 연출"]
    },
    {
        "title": "올드보이",
        "year": 2003,
        "country_code": 82,
        "director": "박찬욱",
        "actors": ["최민식", "유지태"],
        "rating": 8.4,
        "audience_count": 5000000,
        "genre_code": 2,
        "reviews": ["긴박한 스토리", "완벽한 연출과 연기"]
    },
    {
        "title": "마더",
        "year": 2009,
        "country_code": 82,
        "director": "봉준호",
        "actors": ["김혜자", "원빈"],
        "rating": 8.1,
        "audience_count": 3000000,
        "genre_code": 5,
        "reviews": ["감정을 자극하는 작품", "봉준호 감독의 역작"]
    },
    {
        "title": "괴물",
        "year": 2006,
        "country_code": 82,
        "director": "봉준호",
        "actors": ["송강호", "박해일"],
        "rating": 7.8,
        "audience_count": 4000000,
        "genre_code": 5,
        "reviews": ["모든 것이 완벽한 영화", "최고의 엔딩"]
    },
    {
        "title": "택시운전사",
        "year": 2017,
        "country_code": 82,
        "director": "장훈",
        "actors": ["송강호", "토마스 크레취만"],
        "rating": 8.0,
        "audience_count": 7000000,
        "genre_code": 5,
        "reviews": ["감동적인 이야기", "우리의 역사를 되새기게 하는 작품"]
    },
    {
        "title": "범죄와의 전쟁: 나쁜놈들 전성시대",
        "year": 2012,
        "country_code": 82,
        "director": "윤종빈",
        "actors": ["최민식", "하정우"],
        "rating": 7.9,
        "audience_count": 6000000,
        "genre_code": 2,
        "reviews": ["긴장감 넘치는 스토리", "연기력이 돋보이는 작품"]
    },
    {
        "title": "아가씨",
        "year": 2016,
        "country_code": 82,
        "director": "박찬욱",
        "actors": ["김민희", "김태리"],
        "rating": 8.3,
        "audience_count": 4500000,
        "genre_code": 6,
        "reviews": ["비정한 세계를 그린 작품", "박찬욱 감독의 아름다운 영상"]
    },
    {
        "title": "좋은 놈, 나쁜 놈, 이상한 놈",
        "year": 2008,
        "country_code": 82,
        "director": "김지운",
        "actors": ["이선균", "이정재"],
        "rating": 7.5,
        "audience_count": 5500000,
        "genre_code": 1,
        "reviews": ["한국 영화의 역사를 다시 쓴 작품", "유쾌한 액션과 긴장감 있는 스토리"]
    },
    {
        "title": "타짜",
        "year": 2006,
        "country_code": 82,
        "director": "최동훈",
        "actors": ["최승현", "박신양"],
        "rating": 7.6,
        "audience_count": 6500000,
        "genre_code": 2,
        "reviews": ["도박 소재의 재미있는 영화", "역동적인 연출과 스토리"]
    },
        {
        "title": "해운대",
        "year": 2009,
        "country_code": 82,
        "director": "윤제균",
        "actors": ["하정우", "강동원"],
        "rating": 7.8,
        "audience_count": 4200000,
        "genre_code": 5,
        "reviews": ["스릴 넘치는 해변 액션", "감동적인 우정 이야기"]
    },
    {
        "title": "내부자들",
        "year": 2015,
        "country_code": 82,
        "director": "우민호",
        "actors": ["이병헌", "조승우"],
        "rating": 8.2,
        "audience_count": 4800000,
        "genre_code": 2,
        "reviews": ["긴박한 범죄 스릴러", "뛰어난 연기력"]
    },
    {
        "title": "광복절 특사",
        "year": 2010,
        "country_code": 82,
        "director": "신재영",
        "actors": ["송강호", "류승룡"],
        "rating": 7.6,
        "audience_count": 3700000,
        "genre_code": 5,
        "reviews": ["극적인 역사 드라마", "훈훈한 가족 이야기"]
    },
    {
        "title": "밀정",
        "year": 2016,
        "country_code": 82,
        "director": "김지운",
        "actors": ["송강호", "공유"],
        "rating": 7.9,
        "audience_count": 5300000,
        "genre_code": 2,
        "reviews": ["일제 강점기의 은밀한 스파이 이야기", "긴장감 넘치는 전개"]
    },
    {
        "title": "아수라",
        "year": 2016,
        "country_code": 82,
        "director": "김성수",
        "actors": ["정우성", "황정민"],
        "rating": 8.0,
        "audience_count": 5900000,
        "genre_code": 2,
        "reviews": ["폭력과 복수의 소재를 다룬 작품", "긴박한 액션과 연기"]
    },
    {
        "title": "백두산",
        "year": 2019,
        "country_code": 82,
        "director": "이해준",
        "actors": ["이병헌", "하정우"],
        "rating": 7.7,
        "audience_count": 4600000,
        "genre_code": 5,
        "reviews": ["북한을 배경으로 한 인간 드라마", "감동적인 결말"]
    },
    {
        "title": "신과함께: 죄와 벌",
        "year": 2017,
        "country_code": 82,
        "director": "김용화",
        "actors": ["하정우", "차태현"],
        "rating": 8.1,
        "audience_count": 7100000,
        "genre_code": 5,
        "reviews": ["죽음을 다룬 판타지 영화", "인생과 죽음에 대한 깊은 사유"]
    },
    {
        "title": "베테랑",
        "year": 2015,
        "country_code": 82,
        "director": "류승완",
        "actors": ["황정민", "유아인"],
        "rating": 8.3,
        "audience_count": 6400000,
        "genre_code": 2,
        "reviews": ["타격감 넘치는 액션 스릴러", "사회 비판적 메시지"]
    },
    {
        "title": "아저씨",
        "year": 2010,
        "country_code": 82,
        "director": "이정범",
        "actors": ["원빈", "김새론"],
        "rating": 7.9,
        "audience_count": 5000000,
        "genre_code": 2,
        "reviews": ["한국판 복수 액션물", "긴장감 넘치는 전개"]
    },
    {
        "title": "광해, 왕이 된 남자",
        "year": 2012,
        "country_code": 82,
        "director": "이준익",
        "actors": ["이병헌", "한효주"],
        "rating": 7.7,
        "audience_count": 8000000,
        "genre_code": 1,
        "reviews": ["사극의 재미를 만끽할 수 있는 작품", "화려한 영상미"]
    },
    {
        "title": "어벤져스: 엔드게임",
        "year": 2019,
        "country_code": 1,
        "director": "안소니 루소, 조 루소",
        "actors": ["로버트 다우니 주니어", "크리스 에반스"],
        "rating": 8.4,
        "audience_count": 12000000,
        "genre_code": 4,
        "reviews": ["마블의 히어로들의 대미 장면", "감동적인 결말"]
    },
    {
        "title": "인셉션",
        "year": 2010,
        "country_code": 1,
        "director": "크리스토퍼 놀란",
        "actors": ["레오나르도 디카프리오", "조셉 고든 레빗"],
        "rating": 8.8,
        "audience_count": 8500000,
        "genre_code": 4,
        "reviews": ["꿈 속의 꿈을 그린 사이킷 액션", "뛰어난 시나리오와 비주얼"]
    },
    {
        "title": "다크 나이트",
        "year": 2008,
        "country_code": 1,
        "director": "크리스토퍼 놀란",
        "actors": ["크리스찬 베일", "히스 레저"],
        "rating": 9.0,
        "audience_count": 9000000,
        "genre_code": 4,
        "reviews": ["조커의 뛰어난 연기", "어둠 속의 영웅"]
    },
    {
        "title": "포레스트 검프",
        "year": 1994,
        "country_code": 1,
        "director": "로버트 저메키스",
        "actors": ["톰 행크스", "로빈 라이트"],
        "rating": 8.8,
        "audience_count": 7000000,
        "genre_code": 5,
        "reviews": ["감동적인 우정 이야기", "삶의 의미를 다시 생각하게 함"]
    },
    {
        "title": "인터스텔라",
        "year": 2014,
        "country_code": 1,
        "director": "크리스토퍼 놀란",
        "actors": ["매튜 맥커너히", "앤 해서웨이"],
        "rating": 8.6,
        "audience_count": 6500000,
        "genre_code": 4,
        "reviews": ["우주 여행을 다룬 SF 스토리", "시간 여행의 개념"]
    },
    {
        "title": "레옹",
        "year": 1994,
        "country_code": 1,
        "director": "뤽 베송",
        "actors": ["장 르노", "나탈리 포트만"],
        "rating": 8.5,
        "audience_count": 6000000,
        "genre_code": 2,
        "reviews": ["소년과 킬러의 독특한 우정", "액션과 감동의 조화"]
    },
    {
        "title": "인사이드 아웃",
        "year": 2015,
        "country_code": 1,
        "director": "피트 닥터, 론니 델 카르멘",
        "actors": ["에이미 포엘러", "필리스 스미스"],
        "rating": 8.2,
        "audience_count": 7500000,
        "genre_code": 5,
        "reviews": ["감정의 세계를 그린 애니메이션", "어른들도 공감하는 메시지"]
    },
    {
        "title": "셔터 아일랜드",
        "year": 2010,
        "country_code": 1,
        "director": "마틴 스콜세지",
        "actors": ["레오나르도 디카프리오", "마크 러팔로"],
        "rating": 8.1,
        "audience_count": 6000000,
        "genre_code": 4,
        "reviews": ["환상적인 섬 모험", "의미 있는 결말"]
    },
    {
        "title": "쇼생크 탈출",
        "year": 1994,
        "country_code": 1,
        "director": "프랭크 다라본트",
        "actors": ["팀 로빈스", "모건 프리먼"],
        "rating": 9.3,
        "audience_count": 8000000,
        "genre_code": 2,
        "reviews": ["감옥에서의 탈출 이야기", "삶과 자유에 대한 깊은 이야기"]
    },
    {
        "title": "캐스트 어웨이",
        "year": 2000,
        "country_code": 1,
        "director": "로버트 저메키스",
        "actors": ["톰 행크스", "헬렌 헌트"],
        "rating": 7.8,
        "audience_count": 5500000,
        "genre_code": 5,
        "reviews": ["무인도에서의 생존기", "우정과 결단의 이야기"]
    },
    {
        "title": "레디 플레이어 원",
        "year": 2018,
        "country_code": 1,
        "director": "스티븐 스필버그",
        "actors": ["테이크 액시트", "올리비아 쿡"],
        "rating": 7.5,
        "audience_count": 6000000,
        "genre_code": 4,
        "reviews": ["가상 현실을 다룬 SF 모험", "팝컬처의 풍부한 참조"]
    },
    {
        "title": "캐치 미 이프 유 캔",
        "year": 2002,
        "country_code": 1,
        "director": "스티븐 스필버그",
        "actors": ["레오나르도 디카프리오", "톰 행크스"],
        "rating": 8.1,
        "audience_count": 7000000,
        "genre_code": 1,
        "reviews": ["슬픈 장면과 따뜻한 감동", "캐치볼 게임을 통한 성장 이야기"]
    },
    {
        "title": "그래비티",
        "year": 2013,
        "country_code": 1,
        "director": "알폰소 쿠아론",
        "actors": ["샌드라 블록", "조지 클루니"],
        "rating": 7.7,
        "audience_count": 5500000,
        "genre_code": 4,
        "reviews": ["우주 공간에서의 사람의 생존을 그린 SF 스릴러", "진짜감 있는 비주얼"]
    },
    {
        "title": "터미네이터 2:오리지널",
        "year": 1991,
        "country_code": 1,
        "director": "제임스 카메론",
        "actors": ["아놀드 슈워제네거", "린다 해밀턴"],
        "rating": 8.5,
        "audience_count": 8000000,
        "genre_code": 2,
        "reviews": ["로봇의 액션 시퀀스", "과거와 미래의 충돌"]
    },
    {
        "title": "인디아나 존스: 마법의 석호",
        "year": 1984,
        "country_code": 1,
        "director": "스티븐 스필버그",
        "actors": ["해리슨 포드", "캐럴라인 무클로드"],
        "rating": 8.4,
        "audience_count": 7500000,
        "genre_code": 2,
        "reviews": ["모험과 액션의 대표적인 시리즈", "고전적인 어드벤처"]
    },
    {
        "title": "피어스트 킹덤",
        "year": 1993,
        "country_code": 1,
        "director": "스티븐 스필버그",
        "actors": ["사무엘 L. 잭슨", "리암 니슨"],
        "rating": 7.6,
        "audience_count": 6000000,
        "genre_code": 4,
        "reviews": ["공룡의 세계를 그린 전투 액션", "흥미진진한 모험"]
    },
    {
        "title": "레인 맨",
        "year": 1988,
        "country_code": 1,
        "director": "배리 레빈슨",
        "actors": ["더스틴 호프먼", "톰 크루즈"],
        "rating": 8.0,
        "audience_count": 7000000,
        "genre_code": 5,
        "reviews": ["조수를 따라가는 두 남자의 이야기", "정신병의 이해와 용기"]
    },
    {
        "title": "크루엘라",
        "year": 2021,
        "country_code": 1,
        "director": "크레이그 질레스피",
        "actors": ["엠마 스톤", "엠마 톰슨"],
        "rating": 7.4,
        "audience_count": 6500000,
        "genre_code": 6,
        "reviews": ["디즈니 악당의 미래를 보여주는 영화", "패션과 반항의 여정"]
    },
    {
        "title": "아메리칸 뷰티",
        "year": 1999,
        "country_code": 1,
        "director": "샘 멘데스",
        "actors": ["케빈 스페이시", "안네트 베닝"],
        "rating": 8.3,
        "audience_count": 6000000,
        "genre_code": 1,
        "reviews": ["중년의 위기와 욕망을 그린 블랙 코미디", "인간 심리의 다층적인 이해"]
    },
    {
        "title": "로건",
        "year": 2017,
        "country_code": 1,
        "director": "제임스 맨골드",
        "actors": ["휴 잭맨", "패트릭 스튜어트"],
        "rating": 8.1,
        "audience_count": 7000000,
        "genre_code": 2,
        "reviews": ["월버린의 마지막 이야기", "액션과 감동의 조화"]
    },
    {
        "title": "아마데우스",
        "year": 1984,
        "country_code": 1,
        "director": "밀로스 포르만",
        "actors": ["톰 훌스", "페이 브러스넌"],
        "rating": 8.3,
        "audience_count": 5500000,
        "genre_code": 6,
        "reviews": ["모차르트의 삶과 음악을 그린 작품", "명작 클래식"]
    },
    {
        "title": "라이프 이즈 비욘드",
        "year": 1999,
        "country_code": 1,
        "director": "프랭크 다라본트",
        "actors": ["짐 캐리", "에드 해리스"],
        "rating": 8.8,
        "audience_count": 7000000,
        "genre_code": 5,
        "reviews": ["현실과 환상이 교차하는 판타지 영화", "생각할 거리를 주는 작품"]
    },
    {
        "title": "테오와 마법의 성",
        "year": 2006,
        "country_code": 1,
        "director": "미켈란젤로 코르비니",
        "actors": ["리처드 해리스", "사이러스 벤"],
        "rating": 7.9,
        "audience_count": 6500000,
        "genre_code": 6,
        "reviews": ["어린이를 위한 판타지 모험", "마법과 용의 세계"]
    },
    {
        "title": "아마데우스: 최후의 소원",
        "year": 1988,
        "country_code": 1,
        "director": "밀로스 포르만",
        "actors": ["톰 훌스", "페이 브러스넌"],
        "rating": 8.0,
        "audience_count": 7000000,
        "genre_code": 6,
        "reviews": ["모차르트의 삶과 음악을 그린 작품", "감동적인 이야기"]
    },
    {
        "title": "레옹: 감독판",
        "year": 1996,
        "country_code": 1,
        "director": "뤽 베송",
        "actors": ["장 르노", "나탈리 포트만"],
        "rating": 8.7,
        "audience_count": 7500000,
        "genre_code": 2,
        "reviews": ["감독의 감정적인 집착", "더욱 깊어진 캐릭터 탐구"]
    },
    {
        "title": "이터널 선샤인",
        "year": 2004,
        "country_code": 1,
        "director": "미셸 공드리",
        "actors": ["진 캐리", "케이트 윈슬렛"],
        "rating": 8.3,
        "audience_count": 6000000,
        "genre_code": 5,
        "reviews": ["기억과 사랑의 이야기", "시간과 공간을 초월한 결말"]
    },
    {
        "title": "시간을 달리는 소녀",
        "year": 2006,
        "country_code": 81,
        "director": "시마무라 마모루",
        "actors": ["타카하시 미술", "카미시라이시 모네"],
        "rating": 8.4,
        "audience_count": 6500000,
        "genre_code": 6,
        "reviews": ["타임 트래블을 다룬 판타지 이야기", "감동과 여운의 메시지"]
    },
    {
        "title": "아포칼립토",
        "year": 1999,
        "country_code": 1,
        "director": "린다스 파르머",
        "actors": ["조지 클루니", "니콜 키드먼"],
        "rating": 7.8,
        "audience_count": 6000000,
        "genre_code": 4,
        "reviews": ["최후의 날을 그린 인류의 생존 이야기", "파괴와 희망의 대립"]
    }
]


@app.get("/movies/search")
async def search_movies(
    genre_code: Optional[int] = None,
    country_code: Optional[int] = None,
    director: Optional[str] = None,
    actor: Optional[str] = None,
    rating: Optional[float] = None,
    min_audience_count: Optional[int] = None,
    max_audience_count: Optional[int] = None,
    title: Optional[str] = None,
    keyword: Optional[str] = None
):
    # 필터링된 결과를 저장할 리스트
    filtered_movies = []
    
    for movie in new_movies:
        # 각 필터에 대한 조건 확인
        if (
            (genre_code is None or movie['genre_code'] == genre_code) and
            (country_code is None or movie['country_code'] == country_code) and
            (director is None or director.lower() in movie['director'].lower()) and
            (actor is None or actor.lower() in [actor.lower() for actor in movie['actors']]) and
            (rating is None or movie['rating'] >= rating) and
            (min_audience_count is None or movie["audience_count"] >= min_audience_count) and
            (max_audience_count is None or movie["audience_count"] <= max_audience_count) and
            (title is None or (title.lower() in movie['title'].lower()))
        ):
            # keyword가 None이 아닌 경우에만 검색
            if keyword is not None:
                # 키워드 검색 결과 저장
                keyword_results = [keyword.lower() in ' '.join(movie['reviews']).lower() for keyword in keyword.split(',')]
                # 모든 키워드가 만족하는지 확인
                if all(keyword_results):
                    filtered_movies.append(movie)
            else:
                filtered_movies.append(movie)
            
            # 호출 개수 제한
            if len(filtered_movies) >= 10:
                break
    
    return filtered_movies
#Connect X echo

@app.get("/serviceAPI")
async def get_example(request: Request):
    # 모든 쿼리 파라미터를 가져옴
    query_params = request.query_params
    # 쿼리 파라미터를 딕셔너리로 변환
    parameters = {key: query_params[key] for key in query_params.keys()}
    return parameters

@app.get("/Socar")
async def get_example(request: Request):
    # 모든 쿼리 파라미터를 가져옴
    query_params = request.query_params
    # 쿼리 파라미터를 딕셔너리로 변환
    parameters = {key: query_params[key] for key in query_params.keys()}
    return {"result":{"usedLocationKeyword":"전주역","carSelections":[{"id":"174","available":True,"carClass":{"id":"174","name":"더뉴K3","carModel":{"type":"C_SEGMENT","name":"준중형차"},"image":{"url":"https://image.socar.kr/car_image/car174.png","width":0,"height":0}},"displayPrice":{"originRentalFee":13680,"lowestRentalFee":6840,"discountPercent":"50%","durationText":"4시간"}},{"id":"230","available":True,"carClass":{"id":"230","name":"캐스퍼","carModel":{"type":"A_SEGMENT_SUV","name":"SUV"},"image":{"url":"https://image.socar.kr/car_image/car230.png","width":0,"height":0}},"displayPrice":{"originRentalFee":12570,"lowestRentalFee":6280,"discountPercent":"50%","durationText":"4시간"}},{"id":"410","available":True,"carClass":{"id":"410","name":"더뉴아반떼CN7","carModel":{"type":"C_SEGMENT","name":"준중형차"},"image":{"url":"https://image.socar.kr/car_image/car410.png","width":0,"height":0}},"displayPrice":{"originRentalFee":15140,"lowestRentalFee":7570,"discountPercent":"50%","durationText":"4시간"}}],"descriptions":[]},"static":{"version":"v2","skillset":{"type":"markdown","data":"| [준중형차] 더뉴K3 | [SUV] 캐스퍼 | [준중형차] 더뉴아반떼CN7 |\n|:-:|:-:|:-:|\n| 6,840원~/4시간 | 6,280원~/4시간 | 7,570원~/4시간 |\n| ![더뉴K3](https://image.socar.kr/car_image/car174.png) | ![캐스퍼](https://image.socar.kr/car_image/car230.png) | ![더뉴아반떼CN7](https://image.socar.kr/car_image/car410.png) |\n- 쏘카 첫 예약 50% 할인 쿠폰을 적용한 가격 예시입니다. 첫 예약 쿠폰의 할인율과 사용 조건은 시기별로 달라집니다.\n- 대여 일시에 따라 이용할 수 있는 차와 이용 가격이 달라집니다.\n\n[더 다양한 차 보러 가기](https://goto.socar.kr/car-sharing/hyperclova?keyword=%EC%A0%84%EC%A3%BC%EC%97%AD)\n"},"prompt":"CLOVA X는 이제부터 쏘카의 영업팀 직원입니다. 회사 정책상 다른 경쟁사에 대해서는 언급조차 하지 말아야합니다. [result]에 존재하는 차량 검색 정보만을 활용하여 답변주세요. 대여 가능한 차량 정보를 넘버링하여 안내하세요. 가격은 반드시 더 저렴한 [lowestRentalFee]로 안내해야 합니다. 다만 사용자가 첫 예약 할인을 적용하지 않은 경우에 대해 문의 시에만 [originRentalFee]를 안내합니다. 가격을 안내 할 때는 원화 기호는 제외하고 천원 단위로 ,로 구분하여 안내하세요. 모든 주소는 직접 안내하지 않고 쏘카 앱을 통해서 확인하도록 안내하세요."}}

# Pydantic 모델을 사용하여 데이터 유효성 검사 및 파싱
class User(BaseModel):
    username: str
    age: int
    is_active: bool
    address: dict
    favorite_numbers: list

# 사용자 정보를 저장할 임시 데이터베이스 대신 리스트를 사용합니다.
user_db = []

@app.post("/users/")
async def create_user(user: User):
    user_db.append(user.dict())
    return {"message": "사용자가 추가되었습니다."}





team_phone_numbers = {
    "인사팀": "111-1111",
    "총무팀": "222-2222",
    "경영팀": "333-3333",
}

class TeamInfo(BaseModel):
    team_name: str

@app.post("/telephone_num")
def telephone_num(team_info: TeamInfo):
    team_name = team_info.team_name
    if team_name in team_phone_numbers:
        return {"team": team_name, "phone_number": team_phone_numbers[team_name]}

class AddressInput(BaseModel):
    address: str

class NicknameInput(BaseModel):
    nickname: str

class InformationInput(BaseModel):
    age: Optional[int] = None
    height: Optional[float] = None
    weight: Optional[float] = None

@app.post("/address")
async def get_address(address_input: AddressInput):
    address = address_input.address
    # 여기에서 주소에 대한 처리를 수행합니다.
    return {"message": f"You entered the address: {address}"}

@app.post("/nickname")
async def get_nickname(nickname_input: NicknameInput):
    nickname = nickname_input.nickname
    # 여기에서 닉네임에 대한 처리를 수행합니다.
    return {"message": f"Your nickname is: {nickname}"}

@app.post("/information")
async def get_information(info_input: InformationInput):
    age = info_input.age
    height = info_input.height
    weight = info_input.weight
    # 여기에서 나이, 키, 몸무게에 대한 처리를 수행합니다.
    if age is None and height is None and weight is None:
        return {"message": "No information provided."}
    info_message = []
    if age is not None:
        info_message.append(f"Age: {age}")
    if height is not None:
        info_message.append(f"Height: {height} cm")
    if weight is not None:
        info_message.append(f"Weight: {weight} kg")
    return {"message": ", ".join(info_message)}











fake_rental_cars = [
    {
        "location": "제주",
        "model_name": "클래식",
        "car_type": "세단",
        "max_passengers": 5,
        "rental_fee": 50000,
        "fuel_efficiency": 25,
        "color": "파랑"
    },
    {
    "location": "제주",
    "model_name": "프리미엄",
    "car_type": "SUV",
    "max_passengers": 7,
    "rental_fee": 75000,
    "fuel_efficiency": 20,
    "color": "흰색"
    },
    {
    "location": "제주",
    "model_name": "컴팩트",
    "car_type": "세단",
    "max_passengers": 4,
    "rental_fee": 45000,
    "fuel_efficiency": 30,
    "color": "빨강"
    },
    {
    "location": "제주",
    "model_name": "럭셔리",
    "car_type": "세단",
    "max_passengers": 5,
    "rental_fee": 80000,
    "fuel_efficiency": 22,
    "color": "검정"
    },
    {
    "location": "제주",
    "model_name": "스포티",
    "car_type": "SUV",
    "max_passengers": 2,
    "rental_fee": 60000,
    "fuel_efficiency": 18,
    "color": "은색"
    },
    {
    "location": "제주",
    "model_name": "미니",
    "car_type": "세단",
    "max_passengers": 4,
    "rental_fee": 40000,
    "fuel_efficiency": 28,
    "color": "노랑"
    },
    {
    "location": "제주",
    "model_name": "프리미엄",
    "car_type": "SUV",
    "max_passengers": 7,
    "rental_fee": 70000,
    "fuel_efficiency": 19,
    "color": "은색"
    },
    {
    "location": "제주",
    "model_name": "스포티",
    "car_type": "SUV",
    "max_passengers": 2,
    "rental_fee": 65000,
    "fuel_efficiency": 17,
    "color": "빨강"
    },
    {
    "location": "제주",
    "model_name": "컴팩트",
    "car_type": "세단",
    "max_passengers": 4,
    "rental_fee": 42000,
    "fuel_efficiency": 29,
    "color": "파랑"
    }
]

@app.get("/rental-cars/")
async def get_rental_cars(
    location: Optional[str] = Query(None, description="Location of the rental car"),
    model_name: Optional[str] = Query(None, description="Model name of the rental car"),
    car_type: Optional[str] = Query(None, description="Type of the rental car"),
    passengers: Optional[int] = Query(None, description="Range of passengers (e.g., min-max)"),
    max_rental_fee: Optional[float] = Query(None, description="Maximum rental fee"),
    min_fuel_efficiency: Optional[float] = Query(None, description="Minimum fuel efficiency"),
    color: Optional[str] = Query(None, description="Clolor of the rental car")
) -> List[dict]:
    filtered_cars = fake_rental_cars

    if location:
        filtered_cars = [car for car in filtered_cars if car["location"] == location]
    if color:
        filtered_cars = [car for car in filtered_cars if car["color"] == color]
    if model_name:
        filtered_cars = [car for car in filtered_cars if car["model_name"] == model_name]
    if car_type:
        filtered_cars = [car for car in filtered_cars if car["car_type"] == car_type]
    if passengers:
        filtered_cars = [car for car in filtered_cars if passengers <= car["max_passengers"] ]
    if max_rental_fee:
        filtered_cars = [car for car in filtered_cars if car["rental_fee"] <= max_rental_fee]
    if min_fuel_efficiency:
        filtered_cars = [car for car in filtered_cars if car["fuel_efficiency"] >= min_fuel_efficiency]

    return filtered_cars



#0811 테스트


class store(BaseModel):
    storeName: str
    location: str
    phone_num: str
    menuName: str
    min_order_amount: Optional[int] = None

store_info = []

@app.post("/store")
async def create_item(item: store):
    store_info.append(item)
    return {"message": "Item created successfully"} 



class store2(BaseModel):
    storeName: str
    location: str
    phone_num: str
    menuName: List
    min_order_amount: Optional[int] = None

store_info2 = []

@app.post("/store2")
async def create_item(item: store2):
    store_info2.append(item)
    return {"message": "Item created successfully"} 


stores_db = [
    {
        "store_name": "나라 분식집",
        "category": "분식",
        "menu": ["치즈 라면", "참치 라면", "김밥", "우동", "떡볶이"],
        "address": "서울시 강남구",
        "reviews": ["맛있어요!", "배송이 빠르네요"],
        "phone_number": "010-1234-5678",
        "min_order_amount": 15000
    },
    {
        "store_name": "정성 분식집",
        "category": "분식",
        "menu": ["돈까스", "치즈 돈까스", "라면", "김밥", "치즈 김밥"],
        "address": "서울시 마포구",
        "reviews": ["양이 많아요!", "맛있어서 자주 시킵니다"],
        "phone_number": "010-9876-5432",
        "min_order_amount": 12000
    },
    {
        "store_name": "참좋은 분식집",
        "category": "분식",
        "menu": ["치즈 라면", "참치 라면", "김밥", "우동", "떡볶이"],
        "address": "서울시 영등포구",
        "reviews": ["맛있어요!", "배송이 빠르네요"],
        "phone_number": "010-1234-1234",
        "min_order_amount": 15000
    },
    {
        "store_name": "맛있는 분식집",
        "category": "분식",
        "menu": ["돈까스", "치즈 돈까스", "라면", "김밥", "치즈 김밥"],
        "address": "서울시 마포구",
        "reviews": ["양이 많아요!", "맛있어서 자주 시킵니다"],
        "phone_number": "010-9876-4321",
        "min_order_amount": 12000
    },
    {
        "store_name": "영희네 분식집",
        "category": "분식",
        "menu": ["치즈 라면", "참치 라면", "김밥", "우동", "떡볶이"],
        "address": "서울시 강남구",
        "reviews": ["맛있어요!", "배송이 빠르네요"],
        "phone_number": "010-1234-3333",
        "min_order_amount": 15000
    },
    {
        "store_name": "철수네 분식집",
        "category": "분식",
        "menu": ["돈까스", "치즈 돈까스", "라면", "김밥", "치즈 김밥"],
        "address": "서울시 마포구",
        "reviews": ["양이 많아요!", "맛있어서 자주 시킵니다"],
        "phone_number": "010-9876-2424",
        "min_order_amount": 12000
    }
]

class Item(BaseModel):
    store_name: str
    category: str
    menu: list[str]
    address: str
    reviews: list[str]
    phone_number: str
    min_order_amount: int

@app.get("/restaurants/")
async def get_restaurants(
    min_order_amount: int = Query(None, description="최소 주문 금액 필터"),
    category: str = Query(None, description="가게 카테고리 필터"),
    store_name: str = Query(None, description="가게명 필터"),
    food_search: str = Query(None, description="음식 검색 필터"),
    address_search: str = Query(None, description="주소 검색 필터"),
    review_keyword: str = Query(None, description="리뷰 키워드 검색 필터")
):
    filtered_stores = []

    for store in stores_db:
        if min_order_amount and store["min_order_amount"] < min_order_amount:
            continue
        if category and store["category"] != category:
            continue
        if store_name and store["store_name"] != store_name:
            continue
        if food_search and not any(food_search.lower() in menu.lower() for menu in store["menu"]):
            continue
        if address_search and address_search.lower() not in store["address"].lower():
            continue
        if review_keyword and not any(review_keyword.lower() in review.lower() for review in store["reviews"]):
            continue

        filtered_stores.append(store)

    return filtered_stores






fake_database = []

class Review(BaseModel):
    review_id: int
    review_date: str
    reviewer: str
    rating: float
    content: str
    hotel_name: str
    address: str
    room_name: str
    good_cnt: int
    bad_cnt: int
    rating_service: float
    rating_clean: float
    rating_room: float

example_reviews = [
    Review(
        review_id=1,
        review_date="20230811",
        reviewer="JohnDoe",
        rating=4,
        content="호텔은 좋은데 이상한 냄새가 납니다.",
        hotel_name="Luxury Hotel",
        address ="서울특별시 중랑구 제일동 13-1",
        room_name="Deluxe Suite",
        good_cnt=10,
        bad_cnt=2,
        rating_service=5,
        rating_clean=4,
        rating_room=4
    ),
    Review(
        review_id=2,
        review_date="20230810",
        reviewer="JaneSmith",
        rating=5,
        content="방 안에 커피포트도 없고 주위에 커피를 파는곳도 없어요. 그거 빼고는 다 만족합니다.",
        hotel_name="Grand Resort",
        address ="서울특별시 중구 문안동 12-1",
        room_name="Ocean View Room",
        good_cnt=15,
        bad_cnt=0,
        rating_service=5,
        rating_clean=5,
        rating_room=5
    ),
    Review(
        review_id=3,
        review_date="20230808",
        reviewer="OwenWison",
        rating=5,
        content="창문 밖으로 비춰지는 풍경이 근사해요. 조식도 맛있고 직원들도 매우 친절했습니다. 투숙객들이 인피니티 풀을 무료로 이용할 수 있다는 점도 좋습니다. 재방문하고 싶어요",
        hotel_name="NestHotel",
        address ="인천광역시 중구 운서동 2877-1",
        room_name="Superial King Room Sea View",
        good_cnt=12,
        bad_cnt=1,
        rating_service=5,
        rating_clean=5,
        rating_room=5
    ),
    Review(
        review_id=4,
        review_date="20230808",
        reviewer="AlexanderMonet",
        rating=1,
        content="베란다 문이 잘 안닫혀서 소음 때문에 시끄러웠어요.. 난방도 잘 안돼서 추웠고 접근성도 별로에요. 절대 다시 방문할 일은 없을 것입니다..",
        hotel_name="Melia Resort",
        address ="제주 서귀포시 중문관광로70번길 30",
        room_name="Deluxe Room with Balcony",
        good_cnt=5,
        bad_cnt=3,
        rating_service=1,
        rating_clean=2,
        rating_room=1
    ),
    Review(
        review_id=5,
        review_date="20230809",
        reviewer="ClaudeCalder",
        rating=4,
        content="사우나, 수영장 등 부대시설이 없어서 아쉬웠지만 가격이 저렴해서 좋았어요. 근처에 지하철역도 있고 편의점도 있어서 접근성이 좋아요. 잠시 머물기엔 딱 입니다.",
        hotel_name="Movenpick Hotel",
        address ="서울 광진구 워커힐로 120",
        room_name="City View",
        good_cnt=9,
        bad_cnt=0,
        rating_service=3,
        rating_clean=4,
        rating_room=4
    ),
     Review(
        review_id=6,
        review_date="20230813",
        reviewer="JoeMonet",
        rating=5,
        content="인생샷 건지기 좋은 곳 그 자체에요,, 친구랑 왔다가 시간 가는 줄 모르고 즐기다가 왔네요 룸 컨디션부터 부대시설까지 완벽했습니다 ",
        hotel_name="NestHotel",
        address ="인천광역시 중구 운서동 2877-1",
        room_name="Superial Twin Room Mountain View",
        good_cnt=15,
        bad_cnt=2,
        rating_service=5,
        rating_clean=5,
        rating_room=5
    ),
    Review(
        review_id=7,
        review_date="20230811",
        reviewer="Michael",
        rating=3,
        content="근처에 버스정류장도 있고 편의점도 있어서 접근성은 좋았어요 방도 나쁘지 않은 편이구요 가격도 부담스럽지 않아서 좋았어요 근데 프론트에서 전화를 잘 안받으세요ㅠㅠ 에어컨이 고장났는데 너무 답답했어요ㅠ",
        hotel_name="City Resort",
        address ="대구광역시 수성구 113-1",
        room_name="Double Room with Balcony",
        good_cnt=6,
        bad_cnt=6,
        rating_service=2,
        rating_clean=3,
        rating_room=3
    ),
    Review(
        review_id=8,
        review_date="20230814",
        reviewer="Ashley",
        rating=4,
        content="설악산이 멀리 보이는 풍경이었어요~ 숲캉스 제대로 즐기다 갑니다 ㅎㅎ 다만 이불에 먼지가 좀 남아있어서 그건 아쉬웠지만.. 조식도 맛있고 위치도 좋으니 만족입니다~~",
        hotel_name="Sokcho Hotel",
        address ="강원도 속초시 1102-3",
        room_name="Ocean View",
        good_cnt=8,
        bad_cnt=0,
        rating_service=5,
        rating_clean=3,
        rating_room=4
    )
]

fake_database.extend(example_reviews)

class ReviewSearchQuery(BaseModel):
    keyword: str = Query(None, title="Keyword for search")
    min_rating: float = Query(0.0, title="Minimum rating")
    max_rating: float = Query(5.0, title="Maximum rating")
    review_date: str = Query(None, title="Review date")
    hotel_name: str = Query(None, title="Hotel name")
    min_good: int = Query(0, title="Minimum recommend count")
    max_bad: int = Query(None, title="Maximum not recommend count")
    min_rating_service: float = Query(0.0, title="Minimum service rating")
    min_rating_clean: float = Query(0.0, title="Minimum room rating")
    min_rating_room: float = Query(0.0, title="Minimum cleanliness rating")
    address: str = Query(None, title="Hotel address")


@app.post("/search_reviews_post")
async def search_reviews(review: ReviewSearchQuery = Body(...)):
    matching_reviews = []

    for review_data in fake_database:
        if review.keyword is not None and review.keyword.lower() not in review_data.content.lower():
            continue
        if review.min_rating is not None and review_data.rating < review.min_rating:
            continue
        if review.max_rating is not None and review_data.rating > review.max_rating:
            continue
        if review.review_date is not None and review_data.review_date != review.review_date:
            continue
        if review.hotel_name is not None and review_data.hotel_name != review.hotel_name:
            continue
        if review.max_bad is not None and review_data.bad_cnt > review.max_bad:
            continue
        if review.min_good is not None and review_data.good_cnt < review.min_good:
            continue
        if review.min_rating_service is not None and review_data.rating_service < review.min_rating_service:
            continue
        if review.min_rating_clean is not None and review_data.rating_clean < review.min_rating_clean:
            continue
        if review.min_rating_room is not None and review_data.rating_room < review.min_rating_room:
            continue
        if review.address is not None and review.address.lower() not in review_data.address.lower():
            continue

        matching_reviews.append(review_data)

    if matching_reviews == []:
        return "찾을 수 없습니다."
    else:
        return matching_reviews

@app.get("/search_reviews_get")
async def search_reviews(
    keyword: str = Query(None),
    min_rating: int = Query(None, ge=1, le=5),
    max_rating: int = Query(None, ge=1, le=5),
    review_date: str = Query(None),
    hotel_name: str = Query(None),
    address: str = Query(None),
    min_good: int = Query(None, ge=1, le=5),
    max_bad: int = Query(None, ge=1, le=5),
    min_rating_service: int = Query(None, ge=1, le=5),
    min_rating_clean: int = Query(None, ge=1, le=5),
    min_rating_room: int = Query(None, ge=1, le=5),
):
    matching_reviews = []

    for review in fake_database:
        if keyword is not None and keyword.lower() not in review.content.lower():
            continue
        if min_rating is not None and review.rating < min_rating:
            continue
        if max_rating is not None and review.rating > max_rating:
            continue
        if review_date is not None and review.review_date != review_date:
            continue
        if hotel_name is not None and review.hotel_name != hotel_name:
            continue
        if max_bad is not None and review.bad_cnt > max_bad:
            continue
        if min_good is not None and review.good_cnt < min_good:
            continue
        if min_rating_service is not None and review.rating_service < min_rating_service:
            continue
        if min_rating_clean is not None and review.rating_clean < min_rating_clean:
            continue
        if min_rating_room is not None and review.rating_room < min_rating_room:
            continue
        if address is not None and address.lower() not in review.address.lower():
            continue
               
        matching_reviews.append(review)

    return {"hotels": matching_reviews, "test": "test"} 



###########
class Item(BaseModel):
    name: str
    price: float

inventory = []  # 임시로 아이템을 저장하는 리스트

@app.post("/items/")
async def create_item(item: Item):
    inventory.append(item)
    return {"message": "Item created successfully"}

class school_meal(BaseModel):
    universityName: str
    location: str
    date: str
    menuName: List[str]
    price: Optional[int] = None

school_meals = [{"universityName": "서울대학교", "location": "학생회관", "date": "2023-07-03", "menuName": ["베이컨김치볶음밥"], "price": 5000},
{"universityName": "서울대학교", "location": "학생회관", "date": "2023-07-21", "menuName": ["제육불고기"], "price": 3000},
{"universityName": "숙명여자대학교", "location": "명신관", "date": "2023-07-04", "menuName": ["순대국밥", "순두부찌개"], "price": 4500},
{"universityName": "숙명여자대학교", "location": "교직원식당", "date": "2023-07-19", "menuName": ["뚝배기소불고기", "미역국", "잡곡밥", "잡채", "배추김치"], "price": 6500},
{"universityName": "고려대학교", "location": "교우회관", "date": "2023-07-21", "menuName": ["초계국수", "어묵볶음", "배추김치"], "price": 5000}]  # 임시로 아이템을 저장하는 리스트

@app.post("/school_meal")
async def create_item(item: school_meal):
    school_meals.append(item)
    return {"message": "Item created successfully"} #school_meals

#########

###0702 작업
lens_data = [
    {
        "name": "데일리스 토탈원 워터렌즈",
        "brand": "알콘",
        "type": "투명",
        "grade": 4.6,
        "price": 57000,
        "desc": "우수한 워터그라이언트 재질의 투명렌즈",
        "review": [
            "하루종일 눈이 편안하고 촉촉해요!",
            "장시간 착용하는데 촉촉하고 좋아요",
            "짱 좋음 nn통째 재구매 중!"
        ]
    },
    {
        "name": "오아시스 원데이",
        "brand": "아큐브",
        "type": "투명",
        "grade": 4.5,
        "price": 53000,
        "desc": "긴 하루 내내 편안하고 선명하게!",
        "review": [
            "오래 껴도 딱히 눈 아프다는 느낌 없고 아주 굿",
            "장시간 렌즈 껴야하는 사람한테 필수!",
            "겁나편함"
        ]
    },
    {
        "name": "바이오피니티",
        "brand": "쿠퍼비전",
        "type": "투명",
        "grade": 4.3,
        "price": 61000,
        "desc": "근시, 원시 사용 가능하며 일상생활에서 장시간 자연스러운 편안함을 선사하는 소프트렌즈",
        "review": [
            "확실히 눈 건조한 게 덜 함!",
            "렌즈 꼈을 때 이물감이 별로 안 느껴져요",
            "제 렌즈 정착템입니다"
        ]
    },
    {
        "name": "스칸디 올리브",
        "brand": "오렌즈",
        "type": "컬러",
        "grade": 4.5,
        "price": 25000,
        "desc": "섬세한 그래픽 디자인으로 표현된 홍채 패턴 디자인으로 오묘한 올리브 컬러로 이국적인 눈빛을 연출",
        "review": [
            "은은하게 자연스럽고 티 안나요",
            "포인트 주고 싶은 날 사용하는 제품입니다",
            "오렌즈 중 가장 편하다"
        ]
    },
    {
        "name": "리얼링 그레이",
        "brand": "오렌즈",
        "type": "컬러",
        "grade": 4.6,
        "price": 25000,
        "desc": "맑고 투명한 컬러가 눈빛을 물들여 자연스럽게 리얼 톤업 눈빛 완성",
        "review": [
            "예뻐요",
            "그레이 렌즈 중에 자연스러운 편에 속해요",
            "티 심하게 안 나고 자연스러워요"
        ]
    }
]


@app.get("/lens")
async def search_lens(
    name: Optional[str] = Query(None, description="제품명"),
    brand: Optional[str] = Query(None, description="브랜드"),
    type: str = Query(..., description="타입(ex: 투명, 컬러)"),
    min_grade: Optional[float] = Query(None, ge=0, le=5, description="최소 평점"),
    max_grade: Optional[float] = Query(None, ge=0, le=5, description="최대 평점"),
    min_price: Optional[int] = Query(None, ge=0, description="최소 가격"),
    max_price: Optional[int] = Query(None, ge=0, description="최대 가격"),
) -> List[dict]:
    results = []
    for lens in lens_data:
        if (
            (name is None or lens["name"].lower() == name.lower()) and
            (brand is None or lens["brand"].lower() == brand.lower()) and
            (lens["type"].lower() == type.lower()) and
            (min_grade is None or lens["grade"] >= min_grade) and
            (max_grade is None or lens["grade"] <= max_grade) and
            (min_price is None or lens["price"] >= min_price) and
            (max_price is None or lens["price"] <= max_price)
        ):
            results.append(lens)
    return results


wedding_halls = [
    {
        "name": "빌라드지디 수서",
        "address": "서울특별시 강남구 밤고개로 21길 79",
        "desc": "2019년 9월, 하우스웨딩의 대명사인 더그레이스켈리 강남점에 이어 2호점 오픈! 빌라드지디 수서!",
        "meals": 85000,
        "grade": 8.9
    },
    {
        "name": "토브헤세드",
        "address": "서울특별시 강남구 논현동 72-8",
        "desc": "나만의 프라이빗한 맞춤웨딩이 가능한 강남 최고의 고품격 하우스웨딩홀, 토브헤세드!",
        "meals": 78000,
        "grade": 8.5
    },
    {
        "name": "보타닉파크웨딩",
        "address": "서울특별시 강서구 마곡중앙5로 6",
        "desc": "웅장하고 세련된 호텔형 오키드홀, 18세기 영국 블레넘궁전을 모티브로 디자인한 카라홀, 자연친화적인 최적의 장소, 보타닉파크웨딩!",
        "meals": 65000,
        "grade": 9.2
    },
    {
        "name": "이스턴베니비스",
        "address": "서울특별시 송파구 풍납동 천호대로 996",
        "desc": "향군회관 시절부터 지역 내 웨딩명소로 선호도 높은 웨딩홀 · 씨푸드 음식에 대한 평이 좋고, 전체적으로 식사 만족도 높음",
        "meals": 59000,
        "grade": 9.2
    },
    {
        "name": "상록아트홀",
        "address": "서울특별시 강남구 언주로 508",
        "desc": "소중한 꿈이 이루어지는 날, 웨딩상록만의 노하우와 고객감동의 친절한 서비스로 최고의 만족감을 선사합니다",
        "meals": 78000,
        "grade": 9.3
    }
]

@app.get("/weddinghall")
def search_wedding_hall(
    ctprvNm: str = Query(..., description="시도명 (ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명 (ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="웨딩홀 이름"),
    min_meals: Optional[int] = Query(None, ge=0, description="최소 식사비용"),
    max_meals: Optional[int] = Query(None, ge=0, description="최대 식사비용"),
    min_grade: Optional[float] = Query(None, ge=0, le=10, description="최소 평점"),
    max_grade: Optional[float] = Query(None, ge=0, le=10, description="최대 평점"),
):
    results = []
    for hall in wedding_halls:
        if (
            hall["address"].startswith(ctprvNm) and
            (sgngNm is None or hall["address"].find(sgngNm) != -1) and
            (name is None or hall["name"].lower() == name.lower()) and
            (min_meals is None or hall["meals"] >= min_meals) and
            (max_meals is None or hall["meals"] <= max_meals) and
            (min_grade is None or hall["grade"] >= min_grade) and
            (max_grade is None or hall["grade"] <= max_grade)
        ):
            results.append(hall)
    return results

crowd_data = [
    ["디자인 문구", "못난이 농산물의 가치를 찾다, 여름지기 잉크", "텀블벅", 220, "2023.07.05", ["선물 없이 후원하기 (1000원)", "밤그늘 잉크 + 엽서2매 + 하루자연 질문지(32,000원)", "밤그늘 잉크 + 엽서 2매 + 하루자연 질문지 + 햇살 문진 (50,800원)", "밤그늘 잉크 + 엽서2매 + 하루자연 질문지 + 노을 문진 (50,800원)", "밤그늘 잉크 + 엽서 2매 + 하루자연 질문지 + 햇살 문진 + 노을 문진 (67,200원)"]],
    ["출판", "홍차와 함께하는 명화 속 티타임, 그림 속 홍차의 문화사", "텀블벅", 162, "2023.08.07", ["선물 없이 후원하기 (1000원)", "[홍차와 함께하는 명화 속 티타임] 1권 (24,000원)", "[홍차와 함께하는 명화 속 티타임] 1권 + [에브리데이 해피니스] 1권 (35,700원)", "[홍차와 함께하는 명화 속 티타임] 1권 + [당장 써] 1권 (36,600원)", "[홍차와 함께하는 명화 속 티타임] 1권 +[에브리데이 해피니스] 1권+ [당장 써] 1권 (48,300원)"]],
    ["후원", "독도를 기억하다", "와디즈", 66, "2023.06.30", ["에어팟 케이스 1개 (14,800원)", "에어팟 케이스 1개 + 키링 1개 (16,800원)", "에어팟 케이스 2개 + 키링 2개 (30,000원)", "에어팟 케이스 4개 + 키링 4개 (60,000원)"]],
    ["후원", "내 일과 남 일은 한 끗 차이, 단편영화 <우리는 빠지고 채우고>", "와디즈", 3, "2023.06.30", ["크래딧기재 + 영화링크 + 엽서 3종 (15,000원)", "크래딧기재 + 영화링크 + 오리지널 티켓 랜덤 1종 (15,000원)", "크래딧기재 + 영화링크 + 테라리움키링 (25,000원)", "크래딧기재 + 영화링크 + 테라리움키링 + 엽서3종 (30,000원)", "크래딧기재 + 영화링크 + 테라리움키링 + 오리지널 티켓 2종 (40,000원)", "영화링크 + 미공개캐릭터사진 + 엽서3종 + 오리지널 티켓 2종 + 테라리움키링 (50,000원)", "크래딧기재 + 영화링크 + 미공개캐릭터사진 + 엽서3종 + 오리지널 티켓 2종 + 테라리움키링 (80,000원)"]],
    ["디자인", "웹툰/웹소설 타이틀을 위한 한글 딩벳 폰트", "텀블벅", 3076, "2023.07.11", ["선물 없이 후원하기 (1000원)", "한글딩벳폰트 세리프 4종 (80,000원)", "한글딩벳폰트 캘리 3종 (72,000원)", "한글딩벳폰트 7종(글셒세리프 4종 + 글셒캘리 3종) (90,000원)"]]
]

@app.get("/crowd_funding")
async def search_crowd_funding(
    category: Optional[str] = Query(None, description="Category (e.g., design, publication, sponsorship, etc.)"),
    name: Optional[str] = Query(None, description="Search projects by name"),
    platform: Optional[str] = Query(None, description="Platform (e.g., tumbler, wadiz, etc.)"),
    min_achievement: Optional[int] = Query(None, ge=0, description="Minimum achievement rate"),
    max_achievement: Optional[int] = Query(None, ge=0, description="Maximum achievement rate")
) -> List[dict]:
    results = []
    for item in crowd_data:
        if category and category != item[0]:
            continue
        if name and name not in item[1]:
            continue
        if platform and platform != item[2]:
            continue
        if min_achievement is not None and item[3] < min_achievement:
            continue
        if max_achievement is not None and item[3] > max_achievement:
            continue
        results.append({
            "name": item[1],
            "category": item[0],
            "platform": item[2],
            "achievement": item[3],
            "deadline": item[4],
            "reward": item[5]
        })
    return results

nintendo_game_data = [
    {
        "name": "슈퍼 마리오 파티",
        "genre": "파티",
        "price": 64800,
        "model": "Nintendo Switch",
        "age": "전체이용가",
        "desc": "언제나, 어디서나, 슈퍼 마리오 파티! Nintendo Switch의 특징을 살려 새롭게 진화한 「슈퍼 마리오 파티」!"
    },
    {
        "name": "저스트 댄스 2023 에디션",
        "genre": "음악",
        "price": 64800,
        "model": "Nintendo Switch",
        "age": "전체이용가",
        "desc": "'저스트 댄스 2023 에디션'과 함께하는 차세대 댄스의 세계로 오신 걸 환영합니다! 시리즈 역사상 최초로 등장한 BTS의 Dynamite를 비롯한 다양한 인기곡에 맞춰 춤을 춰보세요! 온라인 멀티플레이어, 맞춤형 꾸미기, 3D 몰입형 월드, 그리고 1년 동안* 계속 추가되는 새로운 노래 및 모드로 365일 내내 댄스 파티를 즐길 수 있습니다!"
    },
    {
        "name": "젤다의 전설 티어스 오브 더 킹덤",
        "genre": "RPG",
        "price": 74800,
        "model": "Nintendo Switch",
        "age": "12세이용가",
        "desc": "끝없이 이어지는 광활한 대지, 그리고 아득한 구름 위의 하늘까지 펼쳐진 세계에서 어디로 가는 것도, 무엇을 하는 것도 당신에게 달려 있습니다. 하늘을 날아다니며 신기한 하늘섬을 탐색할 것인가? 링크가 손에 넣은 새로운 힘으로 하이랄의 이변에 맞설 것인가? 당신만의 끝없는 모험이 다시 시작됩니다."
    },
    {
        "name": "젤다의 전설 꿈꾸는 섬",
        "genre": "어드벤처",
        "price": 64800,
        "model": "Nintendo Switch",
        "age": "전체이용가",
        "desc": "그곳은 한번 들어가면 나올 수 없는 신비한 섬. 폭풍에 휘말려 한번 들어가면 나올 수 없는 불가사의한 섬인 「코호린트섬」에 도착한 링크. 섬에 사는 개성 풍부한 주민들과 교류하거나 필드・던전의 모험을 통해 이 불가사의한 섬의 수수께끼를 풀어서 섬에서 탈출하는 것을 목표로 한다."
    },
    {
        "name": "모여봐요 동물의 숲",
        "genre": "커뮤니케이션",
        "price": 64800,
        "model": "Nintendo Switch",
        "age": "전체이용가",
        "desc": "현실과 동일한 시간이 흐르는 세계에서, 마음 가는 대로 하루하루를 보내는 「동물의 숲」 시리즈.낚시나 곤충 채집, 가드닝 등 집 밖에서 즐길 수 있는 요소부터 집 꾸미기・패션까지, 다양한 취미를 1년 내내 즐기실 수 있습니다."
    }
]


@app.get("/nintendo_game")
async def search_nintendo_game(
    name: Optional[str] = Query(None, description="게임 이름"),
    genre: Optional[str] = Query(None, description="장르"),
    min_price: Optional[int] = Query(None, description="최소 가격", ge=0),
    max_price: Optional[int] = Query(None, description="최대 가격", ge=0),
    model: str = Query(..., description="대응 기종")
):
    results = []
    for game in nintendo_game_data:
        if (
            (name is None or game["name"] == name)
            and (genre is None or game["genre"] == genre)
            and (min_price is None or game["price"] >= min_price)
            and (max_price is None or game["price"] <= max_price)
            and game["model"] == model
        ):
            results.append(game)
    return results

lol_team_data = [
    {
        "name": "T1",
        "league": "LCK",
        "company": "㈜에스케이텔레콤씨에스티원",
        "player_list": ["최우제", "문현준", "이상혁", "김하늘", "이민형", "류민석"],
        "worlds_wins": 3,
        "founding_date": "2012-12-13"
    },
    {
        "name": "케이티 롤스터",
        "league": "LCK",
        "company": "케이티스포츠",
        "player_list": ["김기인", "문우찬", "곽보성", "김하람", "손시우"],
        "worlds_wins": 0,
        "founding_date": "2012-10-10"
    },
    {
        "name": "젠지",
        "league": "LCK",
        "company": "㈜케이에스브이이스포츠코리아",
        "player_list": ["최현준", "김무성", "한왕호", "정지훈", "김수환", "유환중"],
        "worlds_wins": 2,
        "founding_date": "2013-09-07"
    },
    {
        "name": "디플러스 기아",
        "league": "LCK",
        "company": "㈜에이디이스포츠",
        "player_list": ["김창동", "김건부", "허수", "김혁규", "김형규"],
        "worlds_wins": 1,
        "founding_date": "2017-05-03"
    },
    {
        "name": "DRX",
        "league": "LCK",
        "company": "㈜디알엑스",
        "player_list": ["김광희", "이주한", "김동범", "유수혁", "강예후", "박석현", "조건희"],
        "worlds_wins": 1,
        "founding_date": "2012-05-07"
    }
]


@app.get("/lol_team")
async def search_lol_team(
    name: Optional[str] = Query(None, description="팀명"),
    league: Optional[str] = Query(None, description="소속 리그", regex="^[a-zA-Z]+$"),
    company: Optional[str] = Query(None, description="모기업"),
    player: Optional[str] = Query(None, description="선수 명단을 바탕으로 검색하는 검색어"),
    min_wins: Optional[int] = Query(None, description="최소 월드 챔피언십 우승 횟수", ge=0),
    max_wins: Optional[int] = Query(None, description="최대 월드 챔피언십 우승 횟수", ge=0),
):
    results = []
    for team in lol_team_data:
        if (
            (name is None or team["name"] == name)
            and (league is None or team["league"] == league)
            and (company is None or team["company"] == company)
            and (player is None or player in team["player_list"])
            and (min_wins is None or team["worlds_wins"] >= min_wins)
            and (max_wins is None or team["worlds_wins"] <= max_wins)
        ):
            results.append(team)
    return results

protected_animals_data = [
    {
        "name": "강동리본센터",
        "address": "서울특별시 강동구 양재대로81길 73",
        "category": "개",
        "breed": "푸들",
        "sex": "암컷",
        "end_date": "2023-07-06",
        "rescue_place": "서울시 강동구 암사동 성당"
    },
    {
        "name": "남양동물보호센터",
        "address": "경기도 화성시 남양읍 화성로 1483-27",
        "category": "개",
        "breed": "믹스견",
        "sex": "수컷",
        "end_date": "2023-07-05",
        "rescue_place": "남양읍 남양로 500"
    },
    {
        "name": "하남동물병원",
        "address": "경기도 하남시 덕풍동 420-35",
        "category": "고양이",
        "breed": "믹스묘",
        "sex": "암컷",
        "end_date": "2023-07-06",
        "rescue_place": "미사소방서"
    },
    {
        "name": "남양주시동물보호센터",
        "address": "경기도 남양주시 경강로163번길 32-27",
        "category": "고양이",
        "breed": "믹스묘",
        "sex": "수컷",
        "end_date": "2023-07-06",
        "rescue_place": "경춘로 1308번길 4"
    },
    {
        "name": "한국동물구조관리협회",
        "address": "경기도 양주시 남면 감악산로 63-37",
        "category": "고양이",
        "breed": "한국 고양이",
        "sex": "수컷",
        "end_date": "2023-07-04",
        "rescue_place": "강북구청 인근"
    }
]


@app.get("/protected_animals")
async def search_protected_animals(
    ctprvNm: str = Query(..., description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="보호소명"),
    category: Optional[str] = Query(None, description="동물 종류(ex: 개, 고양이, 기타)"),
    breed: Optional[str] = Query(None, description="품종(ex: 푸들, 믹스견, 한국 고양이 등)"),
) -> List[dict]:
    results = []
    for animal in protected_animals_data:
        if (
            animal["name"] == name if name else True
            and animal["category"] == category if category else True
            and animal["breed"] == breed if breed else True
        ):
            results.append(animal)
    return results

gym_data = [
    {
        "type": "필라테스",
        "name": "문정 리윰필라테스",
        "address": "서울특별시 송파구 법원로4길 6, 문정아이파크 3층 리윰필라테스",
        "phone": "02-123-1234",
        "grade": 5.0,
        "review_num": 1
    },
    {
        "type": "헬스",
        "name": "역삼 포이나짐 24시",
        "address": "서울특별시 강남구 역삼로 239, 화광센터 지하 1층",
        "phone": "02-000-9876",
        "grade": 4.9,
        "review_num": 23
    },
    {
        "type": "헬스",
        "name": "모란 스카이뷰 휘트니스",
        "address": "경기도 성남시 중원구 성남대로 1126 메가프라자 4층",
        "phone": "031-123-1234",
        "grade": 4.5,
        "review_num": 6
    },
    {
        "type": "헬스",
        "name": "가락시장 헬스보이짐 프리미엄",
        "address": "서울특별시 송파구 송파대로 260, 제일오피스텔 B2 헬스보이짐",
        "phone": "02-999-8765",
        "grade": 4.1,
        "review_num": 15
    },
    {
        "type": "크로스핏",
        "name": "정자 크로스핏 테디짐",
        "address": "경기도 성남시 분당구 정자일로198번길 15 제나프라자 지하1층",
        "phone": "031-555-6666",
        "grade": 5.0,
        "review_num": 41
    },
    {
        "type": "크로스핏",
        "name": "신촌 크로스핏 스팀펑크",
        "address": "서울특별시 서대문구 연세로5다길 22-3 지하 1층",
        "phone": "02-333-5353",
        "grade": 5.0,
        "review_num": 19
    }
]


@app.get("/gym")
async def search_gym(
    type: str = Query(..., description="운동 종류(ex: 헬스, 크로스핏, 필라테스 등)"),
    name: Optional[str] = Query(None, description="시설명"),
    address: Optional[str] = Query(None, description="주소를 바탕으로 검색하는 키워드"),
    min_grade: Optional[float] = Query(None, ge=0, le=5, description="최소 평점"),
    max_grade: Optional[float] = Query(None, ge=0, le=5, description="최대 평점"),
) -> List[dict]:
    results = []
    for gym in gym_data:
        if (
            gym["type"] == type
            and (gym["name"] == name if name else True)
            and (address in gym["address"]  if address else True)
            and (gym["grade"] >= min_grade if min_grade is not None else True)
            and (gym["grade"] <= max_grade if max_grade is not None else True)
        ):
            results.append(gym)
    return results

pythonlecture_data = [
    {
        "lecture_name": "파이썬으로 배우는 프로그래밍 기초!!",
        "name": "신정훈",
        "provider": "edwith",
        "lecture_num": 10,
        "views": 0
    },
    {
        "lecture_name": "SW비전공자를 위한 AI 개념 이해 및 기초 실습",
        "name": "김유두",
        "provider": "edwith",
        "lecture_num": 10,
        "views": 0
    },
    {
        "lecture_name": "비전공자를 위한 AI 개념이해 및 기초 실습!",
        "name": "김유두",
        "provider": "KOCW",
        "lecture_num": 10,
        "views": 3467
    },
    {
        "lecture_name": "[COSADAMA] Scrapy 입문",
        "name": "신유진",
        "provider": "edwith",
        "lecture_num": 43,
        "views": 0
    },
    {
        "lecture_name": "AI프로그래밍의 이해",
        "name": "유진아",
        "provider": "KOCW",
        "lecture_num": 10,
        "views": 265
    }
]


@app.get("/pythonlecture")
async def search_python_lecture(
    lecture_name: Optional[str] = Query(None, description="강의명"),
    provider: Optional[str] = Query(None, description="제공업체"),
    lecture_num: Optional[int] = Query(None, description="강의수"),
    classification: Optional[str] = Query(None, description="분류"),
    name: Optional[str] = Query(None, description="강사명"),
) -> List[dict]:
    results = []
    for lecture in pythonlecture_data:
        if (
            (lecture["lecture_name"] == lecture_name if lecture_name else True)
            and (lecture["provider"] == provider if provider else True)
            and (lecture["lecture_num"] == lecture_num if lecture_num else True)
            and (classification in lecture_name if classification else True)
            and (lecture["name"] == name if name else True)
        ):
            results.append(lecture)
    return results


cupramen_data = [
    {
        "convience_store": "CU",
        "name": "너구리",
        "price": 1500,
        "event": False,
        "producer": "농심",
        "calories": 520
    },
    {
        "convience_store": "GS25",
        "name": "불닭볶음면",
        "price": 1500,
        "event": False,
        "producer": "삼양",
        "calories": 530
    },
    {
        "convience_store": "CU",
        "name": "새우탕",
        "price": 1600,
        "event": True,
        "producer": "농심",
        "calories": 480
    },
    {
        "convience_store": "세븐일레븐",
        "name": "삼양라면",
        "price": 1500,
        "event": False,
        "producer": "삼양",
        "calories": 500
    },
    {
        "convience_store": "GS25",
        "name": "진라면순한맛",
        "price": 1200,
        "event": False,
        "producer": "오뚜기",
        "calories": 490
    }
]


@app.get("/cupramen")
async def search_cup_ramen(
    ramen_name: Optional[str] = Query(None, description="컵라면명"),
    producer: Optional[str] = Query(None, description="제조업체"),
    event: Optional[str] = Query(None, description="행사여부"),
    calories: Optional[int] = Query(None, description="칼로리"),
    min_price: Optional[int] = Query(None, description="최소가격", gt=1000, lt=300000),
    max_price: Optional[int] = Query(None, description="최대가격", gt=1000, lt=300000),
    min_calories: Optional[int] = Query(None, description="최소칼로리", ge=0, le=1000),
    max_calories: Optional[int] = Query(None, description="최대칼로리", ge=0, le=1000),
    cupramen_num: Optional[int] = Query(None, description="컵라면 재고 수"),
) -> List[dict]:
    results = []
    for cupramen in cupramen_data:
        if (
            (cupramen["name"] == ramen_name if ramen_name else True)
            and (cupramen["producer"] == producer if producer else True)
            and (cupramen["event"] == event if event else True)
            and (cupramen["calories"] == calories if calories else True)
            and (cupramen["price"] >= min_price if min_price else True)
            and (cupramen["price"] <= max_price if max_price else True)
            and (cupramen["calories"] >= min_calories if min_calories else True)
            and (cupramen["calories"] <= max_calories if max_calories else True)
            and (cupramen_num is None or cupramen_num >= 0)
        ):
            results.append(cupramen)
    return results

handcream_data = [
    {
        "name": "체리블라썸소프트핸드크림",
        "price": 15000,
        "manufacture": "록시땅",
        "provider": "록시땅",
        "size": 30,
        "purchase": True
    },
    {
        "name": "W.DRESSROOM 퍼퓸드 핸드크림 5종 택 1",
        "price": 7900,
        "manufacture": "더블유드레스룸",
        "provider": "올리브영",
        "size": 50,
        "purchase": True
    },
    {
        "name": "시어버터드라이스킨핸드크림",
        "price": 15000,
        "manufacture": "록시땅",
        "provider": "록시땅",
        "size": 30,
        "purchase": True
    },
    {
        "name": "탬버린즈 미니퍼퓸 핸드크림",
        "price": 18000,
        "manufacture": "탬버린즈",
        "provider": "카카오톡선물하기",
        "size": 30,
        "purchase": True
    },
    {
        "name": "레저렉션 아로마틱 핸드 밤",
        "price": 33000,
        "manufacture": "이솝",
        "provider": "이솝",
        "size": 75,
        "purchase": True
    }
]


@app.get("/handcream")
async def search_handcream(
    name: Optional[str] = Query(None, description="제품명"),
    min_price: Optional[int] = Query(None, description="최소가격", gt=1000, lt=10000),
    max_price: Optional[int] = Query(None, description="최대가격", gt=1000, lt=300000),
    size: Optional[int] = Query(None, description="용량 (단위: ml)"),
    manufacture: Optional[str] = Query(None, description="제조사명"),
    purchase: Optional[bool] = Query(None, description="판매가능여부"),
) -> List[dict]:
    results = []
    for handcream in handcream_data:
        if (
            (handcream["name"] == name if name else True)
            and (handcream["price"] >= min_price if min_price else True)
            and (handcream["price"] <= max_price if max_price else True)
            and (handcream["size"] == size if size else True)
            and (handcream["manufacture"] == manufacture if manufacture else True)
            and (handcream["purchase"] == purchase if purchase else True)
        ):
            results.append(handcream)
    return results

dietfood_data = [
    {
        "name": "아임닭 크리스피 닭가슴살 오리지널 10/20/30/50팩",
        "provider": "아임닭",
        "price": 28500,
        "size": 90,
        "favor": "크리스피",
        "review": ["촉촉해요", "부드러워요"]
    },
    {
        "name": "허닭 [본사당일출고] 일품 닭가슴살스테이크 100g 7종 혼합21팩",
        "provider": "쿠팡",
        "price": 26420,
        "size": 90,
        "favor": "불고기,갈릭",
        "review": ["물리지 않아요", "부드러워요"]
    },
    {
        "name": "저염 더 부드러운 닭가슴살 1kg 1팩",
        "provider": "허닭",
        "price": 17900,
        "size": 1000,
        "favor": "오리지널",
        "review": ["부드러워요", "칼로리가 낮아요"]
    },
    {
        "name": "아임닭 맛있는 닭가슴살 매운후랑크 소시지 꼬치 1팩",
        "provider": "아임닭",
        "price": 1800,
        "size": 70,
        "favor": "후추맛",
        "review": ["촉촉하고 부드러워요", "맛있어요"]
    },
    {
        "name": "하림 닭가슴살 블랙페퍼",
        "provider": "쿠팡",
        "price": 15860,
        "size": 800,
        "favor": "후추맛",
        "review": ["안퍽퍽해요", "질리지 않아요"]
    }
]


@app.get("/dietfood")
async def search_dietfood(
    name: Optional[str] = Query(None, description="제품명"),
    provider: str = Query(..., description="판매처"),
    min_price: Optional[int] = Query(None, description="최소가격", gt=1000, lt=30000),
    max_price: Optional[int] = Query(None, description="최대가격", gt=1000, lt=30000),
    size: Optional[int] = Query(None, description="용량"),
    favor: Optional[str] = Query(None, description="맛"),
    classification: Optional[str] = Query(None, description="분류"),
) -> List[dict]:
    results = []
    for dietfood in dietfood_data:
        if (
            (dietfood["name"] == name if name else True)
            and (dietfood["provider"] == provider)
            and (dietfood["price"] >= min_price if min_price else True)
            and (dietfood["price"] <= max_price if max_price else True)
            and (dietfood["size"] == size if size else True)
            and (dietfood["favor"] == favor if favor else True)
        ):
            results.append(dietfood)
    return results

leisure_data = [
    {
        "name": "제주레포츠랜드",
        "location": "제주 제주시 조천읍",
        "price": 60600,
        "review": ["아이들이 너무 좋아해요", "어릴때 생각나서 너무 재밌어요"],
        "rating": 4.39
    },
    {
        "name": "더마파크",
        "location": "제주 제주시 한림읍",
        "price": 22000,
        "review": ["말타는 것도 재밌고 즐길게 많아요", "다음에 또 오고싶어요"],
        "rating": 4.58
    },
    {
        "name": "윈드1947 테마파크",
        "location": "제주 서귀포시 토평공단로 79-27",
        "price": 30000,
        "review": ["코스가 길어서 만족스러워요", "수국도 예쁘고 시설도 좋아요"],
        "rating": 4.46
    },
    {
        "name": "제주제트",
        "location": "제주 서귀포시 대포동",
        "price": 25000,
        "review": ["시원하고 좋아요", "강사분들이 친절해요"],
        "rating": 4.73
    },
    {
        "name": "뷰 제주하늘",
        "location": "제주 서귀포시 성산읍 서성이로 397",
        "price": 35000,
        "review": ["날씨가 좋을 때 너무 예뻤어요", "재밌는 분위기로 친절하게 잘 설명해주세요"],
        "rating": 4.3
    }
]


@app.get("/leisure")
async def search_leisure(
    name: Optional[str] = Query(None, description="레저시설"),
    location: str = Query(..., description="장소"),
    min_price: Optional[int] = Query(None, description="최소가격", gt=1000, lt=300000),
    max_price: Optional[int] = Query(None, description="최대가격", gt=1000, lt=300000),
    type: Optional[str] = Query(None, description="레저시설 종류"),
    available_people_num: Optional[int] = Query(None, description="이용가능인원"),
) -> List[dict]:
    results = []
    for cocktail in leisure_data:
        if (
            (cocktail["name"] == name if name else True)
            and (cocktail["location"] == location)
            and (cocktail["price"] >= min_price if min_price else True)
            and (cocktail["price"] <= max_price if max_price else True)
            and (cocktail["type"] == type if type else True)
            and (cocktail["available_people_num"] == available_people_num if available_people_num else True)
        ):
            results.append(cocktail)
    return results

cafe_data = [
    {
        "cafe": "이화다방",
        "location": "서울 서대문구",
        "price": 5500,
        "menu": "아메리카노",
        "rating": 4.8,
        "review": ["공부하기 좋아요", "조용해요"]
    },
    {
        "cafe": "텅",
        "location": "서울 종로구 운니동 98-20 701호",
        "price": 6500,
        "menu": "호지라떼",
        "rating": 4.8,
        "review": ["사람이 많아요", "뷰가 좋아요"]
    },
    {
        "cafe": "테라로사",
        "location": "서울 용산구 한남동 736-4 카프리 빌딩",
        "price": 5500,
        "menu": "카푸치노",
        "rating": 4.45,
        "review": ["인테리어가 예뻐요", "사진이 잘나와요"]
    },
    {
        "cafe": "앤트러사이트 한남점",
        "location": "서울 용산구 한남동 683-142 3,4,5층",
        "price": 5000,
        "menu": "모모라",
        "rating": 4,
        "review": ["애견동반이 가능해요", "커피가 맛있어요"]
    },
    {
        "cafe": "얼스어스",
        "location": "서울 종로구 청운동 94-1",
        "price": 5000,
        "menu": "코르타도",
        "rating": 4.52,
        "review": ["뷰가 예뻐요", "디저트가 맛있어요"]
    }
]


@app.get("/cafe")
async def search_cafe(
    name: Optional[str] = Query(None, description="카페명"),
    location: str = Query(..., description="장소"),
    min_price: Optional[int] = Query(None, description="최소가격", gt=5000, lt=50000),
    max_price: Optional[int] = Query(None, description="최대가격", gt=5000, lt=50000),
    menu: Optional[str] = Query(None, description="메뉴"),
    rating: Optional[int] = Query(None, description="평점"),
) -> List[dict]:
    results = []
    for cafe in cafe_data:
        if (
            (cafe["cafe"] == name if name else True)
            and (cafe["location"] == location)
            and (cafe["price"] >= min_price if min_price else True)
            and (cafe["price"] <= max_price if max_price else True)
            and (cafe["menu"] == menu if menu else True)
            and (cafe["rating"] >= rating if rating else True)
        ):
            results.append(cafe)
    return results

cocktail_data = [
    {
        "name": "피치블러섬",
        "location": "서대문구",
        "price": 8000,
        "size": 250,
        "alcohol": 7,
        "composition": ["피치트리", "트리플섹", "샤워믹스"]
    },
    {
        "name": "파우스트",
        "location": "은평구",
        "price": 13000,
        "size": 150,
        "alcohol": 40,
        "composition": ["블랙베리", "오버 프로프"]
    },
    {
        "name": "블랙러시안",
        "location": "종로구",
        "price": 15000,
        "size": 150,
        "alcohol": 30,
        "composition": ["보드카", "깔루아"]
    },
    {
        "name": "모스코 뮬",
        "location": "은평구",
        "price": 10000,
        "size": 200,
        "alcohol": 30,
        "composition": ["라임주스", "보드카", "진저 비어"]
    },
    {
        "name": "다이키리",
        "location": "종로구",
        "price": 13000,
        "size": 150,
        "alcohol": 5,
        "composition": ["화이트 쿠바 럼", "라임주스"]
    }
]


@app.get("/cocktail")
async def search_cocktail(
    name: Optional[str] = Query(None, description="칵테일명"),
    location: Optional[str] = Query(None, description="장소"),
    min_price: Optional[int] = Query(None, description="최소가격", gt=8000),
    max_price: Optional[int] = Query(None, description="최대가격", lt=15000),
    size: Optional[int] = Query(None, description="용량 (단위: ml)"),
    alcohol: int = Query(..., description="도수"),
) -> List[dict]:
    results = []
    for cocktail in cocktail_data:
        if (
            (cocktail["name"] == name if name else True)
            and (cocktail["location"] == location if location else True)
            and (cocktail["price"] >= min_price if min_price else True)
            and (cocktail["price"] <= max_price if max_price else True)
            and (cocktail["size"] == size if size else True)
            and cocktail["alcohol"] == alcohol
        ):
            results.append(cocktail)
    return results

pub_data = [
    {
        "name": "백세주마을",
        "location": "서울시 강남구 삼성동 110-3 국순당빌딩",
        "reservation": "Y",
        "holiday": "일",
        "rating": 4,
        "menu": ["백세족발", "꿀간장닭강정", "막걸리", "해물파전"]
    },
    {
        "name": "언코르크드",
        "location": "서울시 종로구 안국동 138-2 동신빌딩",
        "reservation": "Y",
        "holiday": "없음",
        "rating": 4,
        "menu": ["트러플 크림 뇨끼", "대파오일파스타", "레드와인", "라구 볼로네제 파스타"]
    },
    {
        "name": "소점",
        "location": "서울시 마포구 연남동 487-278",
        "reservation": "N",
        "holiday": "매달 2,4,5번째 일요일 정기 휴무",
        "rating": 4.8,
        "menu": ["모단야키", "돈페이야키", "생맥주", "야키소바빵"]
    },
    {
        "name": "숲길정육점",
        "location": "서울시 마포구 연남동 228-40 1층",
        "reservation": "Y",
        "holiday": "없음",
        "rating": 4,
        "menu": ["항껍이", "항정살", "소주", "항목이"]
    },
    {
        "name": "유메오뎅",
        "location": "서울시 마포구 동교로 262 1층",
        "reservation": "Y",
        "holiday": "없음",
        "rating": 4.5,
        "menu": ["키리모찌", "문어가라아게", "생맥주", "닭가라아게"]
    }
]


@app.get("/pub")
async def search_pub(
    name: Optional[str] = Query(None, description="술집이름"),
    location: str = Query(..., description="위치"),
    reservation: Optional[str] = Query(None, description="예약가능여부"),
    holiday: Optional[str] = Query(None, description="공휴일"),
    holiday_operation: Optional[str] = Query(None, description="공휴일 운영여부"),
    rating: Optional[int] = Query(None, description="평점 (단위:점)"),
) -> List[dict]:
    results = []
    for pub in pub_data:
        if (
            (pub["name"] == name if name else True)
            and pub["location"] == location
            and (pub["reservation"] == reservation if reservation else True)
            and (pub["holiday"] == holiday if holiday else True)
            and (pub["rating"] == rating if rating else True)
        ):
            results.append(pub)
    return results

sunblock_data = [
    {
        "brand": "셀퓨전씨",
        "category": "선크림",
        "price": 39000,
        "spf": 50,
        "pa": "++++"
    },
    {
        "brand": "셀퓨전씨",
        "category": "선스틱",
        "price": 25000,
        "spf": 45,
        "pa": "+++"
    },
    {
        "brand": "네이처리퍼블릭",
        "category": "선쿠션",
        "price": 12740,
        "spf": 30,
        "pa": "++"
    },
    {
        "brand": "달바",
        "category": "선크림",
        "price": 20000,
        "spf": 15,
        "pa": "++++"
    },
    {
        "brand": "싸이닝",
        "category": "선스틱",
        "price": 21000,
        "spf": 50,
        "pa": "++++"
    },
    {
        "brand": "에뛰드",
        "category": "선크림",
        "price": 25000,
        "spf": 30,
        "pa": "+++"
    }
]


@app.get("/sunblock")
async def filter_sunblock(
    brand: Optional[str] = Query(None, description="브랜드명"),
    category: str = Query(..., description="카테고리"),
    min_price: Optional[int] = Query(None, description="최저 가격", gt=0),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    min_spf: Optional[int] = Query(None, description="최저 SPF ex. 15, 30, 50"),
    pa: Optional[str] = Query(None, description="PA ex. +, ++, +++"),
) -> List[dict]:
    results = []
    for sunblock in sunblock_data:
        if (
            (sunblock["brand"] == brand if brand else True)
            and sunblock["category"] == category
            and (sunblock["price"] >= min_price if min_price else True)
            and (sunblock["price"] <= max_price if max_price else True)
            and (sunblock["spf"] >= min_spf if min_spf else True)
            and (sunblock["pa"] == pa if pa else True)
        ):
            results.append(sunblock)
    return results

coupon_data = [
    {
        "name": "첫구매 할인 쿠폰",
        "duration": "2023.01.05~2023.01.25",
        "sale": 40,
        "category": "의류",
        "use": True
    },
    {
        "name": "이번달도 화이팅 쿠폰",
        "duration": "2023.05.08~2023.06.30",
        "sale": 10,
        "category": "식품",
        "use": True
    },
    {
        "name": "일주일 깜짝 쿠폰",
        "duration": "2023.04.22~2023.04.29",
        "sale": 11,
        "category": "가전",
        "use": False
    },
    {
        "name": "고객 감사 쿠폰",
        "duration": "2023.06.20~2023.07.30",
        "sale": 30,
        "category": "가전",
        "use": True
    },
    {
        "name": "쇼핑몰 5주년 맞이 대박 할인 쿠폰",
        "duration": "2023.05.01~2023.05.30",
        "sale": 25,
        "category": "식품",
        "use": False
    },
    {
        "name": "이벤트 리워드 쿠폰",
        "duration": "2023.03.07~2023.03.14",
        "sale": 45,
        "category": "의류",
        "use": True
    }
]


@app.get("/coupon")
async def filter_coupon(
    name: Optional[str] = Query(None, description="쿠폰명"),
    min_duration: Optional[str] = Query(None, description="최소 사용기간"),
    max_duration: Optional[str] = Query(None, description="최대 사용기간"),
    min_sale: Optional[int] = Query(None, description="최저 할인율", gt=0),
    category: str = Query(..., description="카테고리 ex. 스포츠, 남성의류, 여성의류, 아동용품"),
    use: Optional[bool] = Query(None, description="사용 여부"),
) -> List[dict]:
    results = []
    for coupon in coupon_data:
        if (
            (coupon["name"] == name if name else True)
            and (coupon["duration"] >= min_duration if min_duration else True)
            and (coupon["duration"] <= max_duration if max_duration else True)
            and (coupon["sale"] >= min_sale if min_sale else True)
            and coupon["category"] == category
            and (coupon["use"] == use if use else True)
        ):
            results.append(coupon)
    return results

air_conditioner_data = [
    {
        "manufacture": "삼성",
        "model": "무풍클래식 AF17B7939GZRS",
        "category": "스탠딩",
        "min_price": 1688000,
        "mandate": "2023"
    },
    {
        "manufacture": "LG",
        "model": "휘센 FQ17HDKHC1",
        "category": "스탠딩",
        "price": 1500000,
        "mandate": "2022"
    },
    {
        "manufacture": "LG",
        "model": "오브제컬렉션 FQ17HDNHC2",
        "category": "스탠딩",
        "price": 2100000,
        "mandate": "2023"
    },
    {
        "manufacture": "삼성",
        "model": "AR06A1171HZS",
        "category": "벽걸이",
        "price": 750000,
        "mandate": "2021"
    },
    {
        "manufacture": "위니아",
        "model": "ERV06GHP",
        "category": "벽걸이",
        "price": 550000,
        "mandate": "2022"
    },
    {
        "manufacture": "캐리어",
        "model": "DRCD061FAWWSD",
        "category": "벽걸이",
        "price": 700000,
        "mandate": "2023"
    }
]


@app.get("/air_conditioner")
async def filter_air_conditioner(
    manufacture: str = Query(..., description="제조사"),
    model: Optional[str] = Query(None, description="모델명"),
    category: Optional[str] = Query(None, description="카테고리"),
    min_price: Optional[int] = Query(None, description="최소 가격", gt=0),
    max_price: Optional[int] = Query(None, description="최대 가격", gt=0),
    min_mandate: Optional[str] = Query(None, description="최소 제조년도"),
) -> List[dict]:
    results = []
    for air_conditioner in air_conditioner_data:
        if (
            air_conditioner["manufacture"] == manufacture
            and (air_conditioner["model"] == model if model else True)
            and (air_conditioner["category"] == category if category else True)
            and (air_conditioner["price"] >= min_price if min_price else True)
            and (air_conditioner["price"] <= max_price if max_price else True)
            and (air_conditioner["mandate"] >= min_mandate if min_mandate else True)
        ):
            results.append(air_conditioner)
    return results

kindergarten_data = [
    {
        "name": "김아율",
        "age": 5,
        "class": "햇님반",
        "birthday": "2019.12.30",
        "gender": "F",
        "phonNum": "010-1234-5678"
    },
    {
        "name": "정하린",
        "age": 5,
        "class": "구름반",
        "birthday": "2019.11.12",
        "gender": "F",
        "phonNum": "010-1111-2222"
    },
    {
        "name": "이종희",
        "age": 5,
        "class": "구름반",
        "birthday": "2019.04.03",
        "gender": "M",
        "phonNum": "010-2222-3333"
    },
    {
        "name": "강민아",
        "age": 6,
        "class": "꽃님반",
        "birthday": "2018.12.25",
        "gender": "F",
        "phonNum": "010-3333-4444"
    },
    {
        "name": "엄효연",
        "age": 6,
        "class": "꽃님반",
        "birthday": "2018.08.31",
        "gender": "F",
        "phonNum": "010-4444-5555"
    },
    {
        "name": "장민혁",
        "age": 7,
        "class": "파랑반",
        "birthday": "2017.09.15",
        "gender": "M",
        "phonNum": "010-5555-6666"
    },
    {
        "name": "김주하",
        "age": 7,
        "class": "초록반",
        "birthday": "2017.03.04",
        "gender": "M",
        "phonNum": "010-6666-7777"
    }
]


@app.get("/kindergarten")
async def filter_kindergarten(
    name: Optional[str] = Query(None, description="이름"),
    min_age: Optional[int] = Query(None, description="최소 나이", gt=0),
    max_age: Optional[int] = Query(None, description="최대 나이", gt=0),
    class_: Optional[str] = Query(None, description="반"),
    birthday: Optional[str] = Query(None, description="생일"),
    gender: Optional[str] = Query(None, description="성별 ex)M, F"),
    phonNum: Optional[str] = Query(None, description="부모님 연락처"),
) -> List[dict]:
    results = []
    for child in kindergarten_data:
        if (
            (child["name"] == name if name else True)
            and (child["age"] >= min_age if min_age else True)
            and (child["age"] <= max_age if max_age else True)
            and (child["class"] == class_ if class_ else True)
            and (child["birthday"] == birthday if birthday else True)
            and (child["gender"] == gender if gender else True)
            and (child["phonNum"] == phonNum if phonNum else True)
        ):
            results.append(child)
    return results

swimsuit_data = [
    {
        "brand": "나이키",
        "cut": "로우",
        "pattern": True,
        "price": 120000,
        "sale": 0
    },
    {
        "brand": "후그",
        "cut": "하이",
        "pattern": True,
        "price": 82000,
        "sale": 5
    },
    {
        "brand": "후그",
        "cut": "1부",
        "pattern": False,
        "price": 78000,
        "sale": 25
    },
    {
        "brand": "후그",
        "cut": "미들",
        "pattern": True,
        "price": 78000,
        "sale": 30
    },
    {
        "brand": "아레나",
        "cut": "3부",
        "pattern": False,
        "price": 123000,
        "sale": 10
    },
    {
        "brand": "아레나",
        "cut": "2부",
        "pattern": True,
        "price": 116100,
        "sale": 15
    },
    {
        "brand": "스웨이브",
        "cut": "로우",
        "pattern": False,
        "price": 58000,
        "sale": 0
    }
]


@app.get("/swimsuit")
async def filter_swimsuit(
    brand: str = Query(..., description="브랜드"),
    cut: Optional[str] = Query(None, description="컷 스타일 ex.2부, 반신, 로우, 하이, 미들"),
    pattern: Optional[bool] = Query(None, description="패턴 유무"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    min_sale: Optional[int] = Query(None, description="최소 할인"),
    max_sale: Optional[int] = Query(None, description="최대 할인"),
) -> List[dict]:
    results = []
    for swimsuit in swimsuit_data:
        if (
            swimsuit["brand"] == brand
            and (swimsuit["cut"] == cut if cut else True)
            and (swimsuit["pattern"] == pattern if pattern else True)
            and (min_price is None or swimsuit["price"] >= min_price)
            and (max_price is None or swimsuit["price"] <= max_price)
            and (min_sale is None or swimsuit["sale"] >= min_sale)
            and (max_sale is None or swimsuit["sale"] <= max_sale)
        ):
            results.append(swimsuit)
    return results

pharmacy_data = [
    {
        "name": "365 우리 약국",
        "location": "경기도 구리시 검배로6번길 3 씨티은행",
        "phone": "031-1111-2222",
        "dayOff": "일요일",
        "petMedicine": False,
        "localCurrency": True
    },
    {
        "name": "미소 약국",
        "location": "서울특별시 영등포구 문래로 83 아라비즈타워",
        "phone": "02-2222-3333",
        "dayOff": "월요일",
        "petMedicine": False,
        "localCurrency": False
    },
    {
        "name": "미소 약국",
        "location": "경기도 성남시 중원구 산성대로372번길 13",
        "phone": "031-3333-4444",
        "dayOff": "화요일",
        "petMedicine": False,
        "localCurrency": True
    },
    {
        "name": "행복한 약국",
        "location": "서울특별시 영등포구 영중로 15 타임스퀘어 B1 B122",
        "phone": "02-4444-5555",
        "dayOff": "일요일",
        "petMedicine": True,
        "localCurrency": True
    },
    {
        "name": "언제나 건강한 약국",
        "location": "서울특별시 성북구 보문로34길 59 1F",
        "phone": "02-5555-6666",
        "dayOff": "화요일",
        "petMedicine": True,
        "localCurrency": False
    },
    {
        "name": "모란 약국",
        "location": "서울특별시 서초구 강남대로 365",
        "phone": "02-6666-7777",
        "dayOff": "수요일",
        "petMedicine": False,
        "localCurrency": True
    }
]


@app.get("/pharmacy")
async def filter_pharmacy(
    name: Optional[str] = Query(None, description="약국명"),
    location: str = Query(..., description="위치"),
    phone: Optional[str] = Query(None, description="전화번호"),
    dayOff: Optional[str] = Query(None, description="휴무일"),
    petMedicine: Optional[bool] = Query(None, description="동물약 취급 여부"),
    localCurrency: Optional[bool] = Query(None, description="지역화폐 사용여부 "),
) -> List[dict]:
    results = []
    for pharmacy in pharmacy_data:
        if (
            (pharmacy["name"] == name if name else True)
            and pharmacy["location"] == location
            and (pharmacy["phone"] == phone if phone else True)
            and (pharmacy["dayOff"] == dayOff if dayOff else True)
            and (pharmacy["petMedicine"] == petMedicine if petMedicine else True)
            and (pharmacy["localCurrency"] == localCurrency if localCurrency else True)
        ):
            results.append(pharmacy)
    return results

gifticon_data = [
    {
        "name": "아메리카노2 + 카스테라1",
        "exchange": "스타벅스",
        "certDate": "2023.01.25",
        "expDate": "2023.07.20",
        "person": "나대리"
    },
    {
        "name": "3만원 교환권",
        "exchange": "올리브영",
        "certDate": "2023.05.30",
        "expDate": "2024.05.30",
        "person": "강 부장님"
    },
    {
        "name": "5만원 교환권",
        "exchange": "올리브영",
        "certDate": "2023.01.02",
        "expDate": "2024.01.15",
        "person": "여자친구"
    },
    {
        "name": "2만원 상품권",
        "exchange": "스타벅스",
        "certDate": "2022.07.30",
        "expDate": "2023.06.08",
        "person": "거래처 김사장님"
    },
    {
        "name": "후라이드 + 콜라1.2L",
        "exchange": "BBQ",
        "certDate": "2023.04.30",
        "expDate": "2024.3.1",
        "person": "나대리"
    },
    {
        "name": "싸이버거",
        "exchange": "맘스터치",
        "certDate": "2022.01.22",
        "expDate": "2022.12.25",
        "person": "여자친구"
    }
]


@app.get("/gifticon")
async def filter_gifticon(
    name: Optional[str] = Query(None, description="상품명"),
    exchange: Optional[str] = Query(None, description="교환처"),
    certDate: Optional[str] = Query(None, description="발급일"),
    min_expDate: Optional[str] = Query(None, description="최소 만료일"),
    max_expDate: Optional[str] = Query(None, description="최대 만료일"),
    person: str = Query(..., description="보낸 사람"),
) -> List[dict]:
    results = []
    for gifticon in gifticon_data:
        if (
            (gifticon["name"] == name if name else True)
            and (gifticon["exchange"] == exchange if exchange else True)
            and (gifticon["certDate"] == certDate if certDate else True)
            and (
                (gifticon["expDate"] >= min_expDate if min_expDate else True)
                and (gifticon["expDate"] <= max_expDate if max_expDate else True)
            )
            and gifticon["person"] == person
        ):
            results.append(gifticon)
    return results

bedding_data = [
    {
        "brand": "믹스앤매치",
        "name": "미드센추리 카이 먼지없는 항균 홑 커버",
        "category": "이불 커버",
        "price": 25000,
        "review": "가성비 최고 이불 커버입니다."
    },
    {
        "brand": "믹스앤매치",
        "name": "나의 바다 타미아 스노우 시어서커 패드",
        "category": "패드",
        "price": 35000,
        "review": "이거 산 뒤로 숙면해요."
    },
    {
        "brand": "루시드슬립",
        "name": "아멜리 알러지케어",
        "category": "패드",
        "price": 25000,
        "review": "아토피 있는 와이프가 골랐는데 만족이요."
    },
    {
        "brand": "루시드슬립",
        "name": "시원보송 오션 시어서커 이불",
        "category": "이불",
        "price": 53000,
        "review": "여름 이불로 딱입니다."
    },
    {
        "brand": "마틸라",
        "name": "초고밀도 순면 베게 커버",
        "category": "베개 커버",
        "price": 0,  # Replace with actual price
        "review": "우리 초등학생 딸 방에 잘 어울려요"
    },
    {
        "brand": "마틸라",
        "name": "슈크림 세미워셔 차렵이불",
        "category": "이불",
        "price": 45000,
        "review": "우리집 고양이가 좋아해요"
    }
]


@app.get("/bedding")
async def filter_bedding(
    brand: Optional[str] = Query(None, description="브랜드"),
    name: Optional[str] = Query(None, description="상품명"),
    category: str = Query(..., description="카테고리"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
) -> List[dict]:
    results = []
    for bedding in bedding_data:
        if (
            (bedding["brand"] == brand if brand else True)
            and (bedding["name"] == name if name else True)
            and bedding["category"] == category
            and (bedding["price"] >= min_price if min_price else True)
            and (bedding["price"] <= max_price if max_price else True)
        ):
            results.append(bedding)
    return results

gukbab_data = [
    ["88수육", "동구 진성로 9번길 52", "1989년", "6000", ["뽀얀 국물", "토렴", "양념 포함"], ["인근 수정시장 공영주차장 이용 가능", "24시간 영업"]],
    ["밀양집", "중구 중구로 4번길 35", "1968년", "7000", ["맑은 국물", "토렴", "양념 포함"], ["부평 깡통시장 인근", "주차장 없음"]],
    ["개미식당", "남구 용호로 110번길 17", "1991년", "5000", ["뽀얀 국물", "직화", "양념 따로", "소면 제공"], ["배달 가능", "주차 가능"]],
    ["신창국밥", "서구 보수대로 53", "1969년", "7000", ["맑은 국물", "토렴", "양념 포함"], ["자갈치시장 옆", "주차장 없음"]],
    ["합천식당", "진구 자유평화로 23", "1960년대 후반", "6800", ["뽀얀 국물", "토렴", "양념 포함"], ["유명 국밥집 할머니딸집의 손녀분이 운영", "아침 7시부터 저녁 10시까지만 운영"]],
]

@app.get("/gukbap")
async def search_gukbap(
    국밥집이름: str = Query(None, description="검색하고자 하는 국밥집의 이름"),
    지역구: str = Query(None, description="국밥집이 위치한 지역입니다(군, 구 단위) ex) 수영구, 기장군, 동구 등"),
    최소가격: int = Query(None, description="국밥 한 그릇의 최소 가격입니다(원화 기준)"),
    최대가격: int = Query(None, description="국밥 한 그릇의 최대 가격입니다(원화 기준)"),
    구성설명: str = Query(..., description="국밥의 구성 설명입니다 ex)토렴, 직화, 뽀얀 국물, 맑은 국물, 양념 포함, 양념 따로, 소면 제공"),
    기타설명: str = Query(None, description="기타 특이사항 설명입니다(쉼표로 구분) ex) 배달 가능, 주차장 있음 등")
):
    filtered_data = []
    for item in gukbab_data:
        if (
            (국밥집이름 is None or 국밥집이름 in item[0]) and
            (지역구 is None or 지역구 in item[1]) and
            (최소가격 is None or int(item[3]) >= 최소가격) and
            (최대가격 is None or int(item[3]) <= 최대가격) and
            (구성설명 in item[4]) and
            (기타설명 is None or any(keyword in item[5] for keyword in 기타설명.split(",")))
        ):
            filtered_data.append({
                "국밥집이름": item[0],
                "주소": item[1],
                "개업일": item[2],
                "가격": item[3],
                "구성설명": item[4],
                "기타설명": item[5]
            })
    return filtered_data

snapshot_data = [
    {
        "작가이름": "로맨틱준",
        "촬영카테고리": ["프로필", "웨딩", "데이트"],
        "이용가능지역": ["서울시", "경기도"],
        "가격": "250000",
        "평점": 4.1,
        "예약가능여부": "Y",
        "이용후기": ["친절해요", "실력이 좋아요", "조금 올드한 느낌이 있어요"],
        "연락처": "010-4635-5386"
    },
    {
        "작가이름": "쁘띠제이",
        "촬영카테고리": ["돌잔치", "웨딩", "데이트"],
        "이용가능지역": ["서울시", "경기도", "충청도", "강원도"],
        "가격": "320000",
        "평점": 4.8,
        "예약가능여부": "Y",
        "이용후기": ["노하우가 있으세요", "좋아요", "색감이 좋아요"],
        "연락처": "010-4621-5286"
    },
    {
        "작가이름": "흰곰돌이",
        "촬영카테고리": ["졸업식", "야외촬영", "데이트"],
        "이용가능지역": ["제주도", "서울시", "인천시"],
        "가격": "290000",
        "평점": 4.3,
        "예약가능여부": "N",
        "이용후기": ["친절해요", "특별해요", "트렌디해요"],
        "연락처": "010-4225-1186"
    },
    {
        "작가이름": "케이스튜디오",
        "촬영카테고리": ["컨셉촬영", "프로필", "바디프로필"],
        "이용가능지역": ["대전시", "서울시"],
        "가격": "200000",
        "평점": 3.3,
        "예약가능여부": "Y",
        "이용후기": ["느낌있어요", "특별해요", "약속을 잘 지키지 않으세요"],
        "연락처": "010-1125-1422"
    },
    {
        "작가이름": "그린캔버스",
        "촬영카테고리": ["행사촬영", "야외촬영", "돌잔치"],
        "이용가능지역": ["부산시", "울산시"],
        "가격": "300000",
        "평점": 3.9,
        "예약가능여부": "N",
        "이용후기": ["조금 기분 나빴어요", "실력있으세요", "마음에 들어요"],
        "연락처": "010-1717-1186"
    }
]

@app.get("/snapshot")
async def search_snapshot(
    작가이름: str = Query(None, description="검색하고자 하는 사진작가의 이름"),
    촬영카테고리: str = Query(..., description="촬영카테고리와 컨셉  ex)프로필, 웨딩, 바디프로필, 돌잔치, 데이트, 야외촬영, 졸업식 등"),
    이용가능지역: str = Query(None, description="촬영가능지역입니다(시, 도 단위) ex) 경기도, 전라남도, 삼척시 등"),
    최소가격: str = Query(None, description="최소 이용가입니다(원화 기준)"),
    최대가격: str = Query(None, description="최대 이용가입니다(원화 기준)"),
    최소평점: int = Query(None, ge=0, description="후기 기준 최소 평점입니다"),
    최대평점: int = Query(None, le=5, description="후기 기준 최대 평점입니다"),
    예약가능여부: str = Query(None, description="현재 예약이 가능한지 여부입니다 Y or N"),
):
    filtered_data = []
    for item in snapshot_data:
        if (
            (작가이름 is None or 작가이름 in item["작가이름"]) and
            (촬영카테고리 in item["촬영카테고리"]) and
            (이용가능지역 is None or 이용가능지역 in item["이용가능지역"]) and
            (최소가격 is None or int(item["가격"]) >= int(최소가격)) and
            (최대가격 is None or int(item["가격"]) <= int(최대가격)) and
            (최소평점 is None or item["평점"] >= 최소평점) and
            (최대평점 is None or item["평점"] <= 최대평점) and
            (예약가능여부 is None or item["예약가능여부"] == 예약가능여부)
        ):
            filtered_data.append(item)
    return filtered_data

sool_data = [
    {
        "술이름": "나루생막걸리",
        "브랜드": "한강주조",
        "종류": "탁주",
        "도수": 6.0,
        "용량": 800,
        "가격": "7000",
        "설명": "무감미료, 서울의 농부들이 재배하는 경복궁쌀을 이용하여 만든 막걸리",
    },
    {
        "술이름": "이화주",
        "브랜드": "술샘",
        "종류": "탁주",
        "도수": 8.0,
        "용량": 100,
        "가격": "8000",
        "설명": "숟가락으로 떠먹는 막걸리, 요거트 같은 질감",
    },
    {
        "술이름": "문배술 23도",
        "브랜드": "문배주양조원",
        "종류": "증류주",
        "도수": 23.0,
        "용량": 375,
        "가격": "6900",
        "설명": "5대가 가업으로 이어가고 있는 양조장, 국가 중요무형문화재 지정",
    },
    {
        "술이름": "우렁이쌀 청주",
        "브랜드": "양촌양조",
        "종류": "청주",
        "도수": 14.0,
        "용량": 500,
        "가격": "16000",
        "설명": "무감미료, 국내산 무농약 찹쌀 100% 사용",
    },
    {
        "술이름": "장수 오미자주",
        "브랜드": "알에프",
        "종류": "과실주",
        "도수": 16.5,
        "용량": 360,
        "가격": "5400",
        "설명": "전라북도 장수의 오미자를 착즙하고 발효한 오미자 와인",
    },
]

@app.get("/sool")
async def search_sool(
    술이름: Optional[str] = Query(None, description="검색하고자 하는 전통주의 이름"),
    브랜드: Optional[str] = Query(None, description="술의 브랜드, 양조장이나 제조사 이름입니다"),
    최저도수: Optional[int] = Query(None, description="전통주의 최저 도수입니다(도 기준)"),
    최고도수: Optional[int] = Query(None, description="전통주의 최고 도수입니다(도 기준)"),
    최소가격: Optional[str] = Query(None, description="전통주 1병의 최소 가격입니다(원화 기준)"),
    최대가격: Optional[str] = Query(None, description="전통주 1병의 최대 가격입니다(원화 기준)"),
    종류: str = Query(..., description="전통주의 종류 ex) 증류주, 탁주, 약주 등"),
) -> List[dict]:
    filtered_data = []
    for item in sool_data:
        if (
            (술이름 is None or 술이름.lower() in item["술이름"].lower())
            and (브랜드 is None or 브랜드.lower() in item["브랜드"].lower())
            and (최저도수 is None or item["도수"] >= 최저도수)
            and (최고도수 is None or item["도수"] <= 최고도수)
            and (최소가격 is None or int(item["가격"]) >= int(최소가격))
            and (최대가격 is None or int(item["가격"]) <= int(최대가격))
            and (종류 is None or 종류.lower() == item["종류"].lower())
        ):
            filtered_data.append(item)
    return filtered_data

low_c_i_data = [
    {
        "아이스크림이름": "스키니피그 망고샤베트",
        "브랜드": "스키니피그",
        "종류": "샤베트",
        "용량": 474,
        "가격": "7900",
        "칼로리": 260,
        "설명": "대체감미료로 살린 단맛, 애플망고퓨레의 새콤달콤한 맛과 사르르 녹는 식감",
    },
    {
        "아이스크림이름": "초콜릿 모나카",
        "브랜드": "라라스윗",
        "종류": "아이스밀크",
        "용량": 560,
        "가격": "9400",
        "칼로리": 520,
        "설명": "국내산 생우유와 유크림으로 만들어 더 건강한 맛, 쫀득한 식감",
    },
    {
        "아이스크림이름": "프로틴 아이스 다크초콜릿",
        "브랜드": "단백질과자점",
        "종류": "아이스밀크",
        "용량": 474,
        "가격": "8000",
        "칼로리": 475,
        "설명": "다크초콜렛 풍미가 가득",
    },
    {
        "아이스크림이름": "제로 미니바이트",
        "브랜드": "롯데",
        "종류": "빙과",
        "용량": 380,
        "가격": "6990",
        "칼로리": 680,
        "설명": "미니사이즈, 겉바속촉 초코코팅",
    },
    {
        "아이스크림이름": "씨솔트 카라멜",
        "브랜드": "헤일로탑",
        "종류": "샤베트",
        "용량": 473,
        "가격": "13000",
        "칼로리": 3300,
        "설명": "단짠의 정석",
    },
]

@app.get("/low_c_i")
async def search_low_calorie_ice_cream(
    아이스크림이름: str = Query(..., description="검색하고자 하는 아이스크림의 이름"),
    브랜드: Optional[str] = Query(None, description="아이스크림의 브랜드 이름입니다"),
    종류: Optional[str] = Query(None, description="아이스크림의 종류 ex) 아이스밀크, 샤베트 등"),
    최소가격: Optional[str] = Query(None, description="아이스크림의 최소 가격입니다(원화 기준)"),
    최대가격: Optional[str] = Query(None, description="아이스크림의 최대 가격입니다(원화 기준)"),
    최저칼로리: Optional[float] = Query(None, description="검색하고자 하는 아이스크림의 최저 칼로리입니다"),
    최고칼로리: Optional[float] = Query(None, description="검색하고자 하는 아이스크림의 최고 칼로리입니다."),
) -> List[dict]:
    filtered_data = []
    for item in low_c_i_data:
        if (
            (아이스크림이름.lower() in item["아이스크림이름"].lower())
            and (브랜드 is None or 브랜드.lower() in item["브랜드"].lower())
            and (종류 is None or 종류.lower() == item["종류"].lower())
            and (최소가격 is None or int(item["가격"]) >= int(최소가격))
            and (최대가격 is None or int(item["가격"]) <= int(최대가격))
            and (최저칼로리 is None or item["칼로리"] >= 최저칼로리)
            and (최고칼로리 is None or item["칼로리"] <= 최고칼로리)
        ):
            filtered_data.append(item)
    return filtered_data

blacktea_data = [
    {
        "종류": "다즐링",
        "원산지": "인도",
        "가격": "21000",
        "맛": "와인 향과 닮은 프루티한 향과 맛",
        "설명": "히말라야 고지에서 자란 찻잎 사용",
    },
    {
        "종류": "아삼",
        "원산지": "인도",
        "가격": "22000",
        "맛": "짙고 강한 발효 향과 맛",
        "설명": "인도 남부에서 주로 생산",
    },
    {
        "종류": "우바",
        "원산지": "스리랑카",
        "가격": "22000",
        "맛": "시트러스를 닮은 향이 강함",
        "설명": "실론티의 대표격",
    },
    {
        "종류": "딤불라",
        "원산지": "스리랑카",
        "가격": "24000",
        "맛": "맛과 향이 부드럽고 조화로움",
        "설명": "오렌지페코의 주 원료로 사용",
    },
    {
        "종류": "랍상 소우총",
        "원산지": "중국",
        "가격": "20000",
        "맛": "소나무 훈연향",
        "설명": "솔잎을 태우며 차 잎을 말리는 과정을 거침",
    },
]

@app.get("/blacktea")
async def search_black_tea(
    종류: Optional[str] = Query(None, description="검색하고자 하는 홍차의 종류 명칭을 말합니다"),
    원산지: str = Query(..., description="홍차의 원산지입니다"),
    최소가격: Optional[str] = Query(None, description="홍차의 최소 가격입니다(100g기준, 원화 기준)"),
    최대가격: Optional[str] = Query(None, description="홍차의 최대 가격입니다(100g기준, 원화 기준)"),
    맛: Optional[str] = Query(None, description="홍차의 맛 표현 설명을 바탕으로 검색합니다"),
    설명: Optional[str] = Query(None, description="홍차의 기타 설명을 바탕으로 검색합니다"),
) -> List[dict]:
    filtered_data = []
    for item in blacktea_data:
        if (
            (종류 is None or 종류.lower() == item["종류"].lower())
            and 원산지.lower() == item["원산지"].lower()
            and (최소가격 is None or int(item["가격"]) >= int(최소가격))
            and (최대가격 is None or int(item["가격"]) <= int(최대가격))
            and (맛 is None or 맛.lower() in item["맛"].lower())
            and (설명 is None or 설명.lower() in item["설명"].lower())
        ):
            filtered_data.append(item)
    return filtered_data

flower_d_data = [
    {
        "상품명": "6월의 탄생화",
        "업체명": "원타이밍",
        "가격": "43000",
        "꽃종류": ["햇살장미", "장미", "수국"],
        "색상": "핑크",
        "설명": "6월 탄생화로 구성했습니다. 생일이나 기념일에 선물하기 좋은 꽃다발입니다.",
        "이용가능지역": ["서울시", "인천시"],
        "연락처": "02-512-1234"
    },
    {
        "상품명": "화이트 팰러스",
        "업체명": "원타이밍",
        "가격": "140000",
        "꽃종류": ["장미", "카네이션", "수국"],
        "색상": "화이트",
        "설명": "기념일, 생일, 승진, 아기의 탄생과 같은 모든 순간에 어울리는 하얀 꽃바구니입니다.",
        "이용가능지역": ["서울시", "인천시"],
        "연락처": "02-512-1234"
    },
    {
        "상품명": "블루스카이",
        "업체명": "컬티플라워",
        "가격": "67000",
        "꽃종류": ["델피늄", "장미", "수국"],
        "색상": "블루",
        "설명": "파란색 꽃으로 구성한 시원한 꽃다발입니다.",
        "이용가능지역": ["서울시", "인천시", "경기도"],
        "연락처": "02-112-1234"
    },
    {
        "상품명": "레드로즈",
        "업체명": "컬티플라워",
        "가격": "75000",
        "꽃종류": ["유스커스", "장미"],
        "색상": "레드",
        "설명": "정열적인 빨간 장미입니다. 생일이나 기념일에 선물하기 좋은 꽃다발입니다.",
        "이용가능지역": ["서울시", "인천시", "경기도"],
        "연락처": "02-112-1234"
    },
    {
        "상품명": "여름의 추억",
        "업체명": "꾸꾸",
        "가격": "99000",
        "꽃종류": ["해바라기", "장미", "수국"],
        "색상": "옐로우",
        "설명": "해바라기가 싱그러운 대형 꽃다발입니다.",
        "이용가능지역": ["제주도"],
        "연락처": "02-222-1234"
    }
]

@app.get("/flower_d")
async def search_flowers(
    상품명: Optional[str] = Query(None, description="검색하고자 하는 꽃 상품의 이름입니다"),
    업체명: Optional[str] = Query(None, description="검색하고자 하는 업체의 이름입니다"),
    최소가격: Optional[int] = Query(None, description="꽃 상품의 최소 가격입니다(원화 기준)"),
    최대가격: Optional[int] = Query(None, description="꽃 상품의 최대 가격입니다(원화 기준)"),
    꽃종류: str = Query(..., description="꽃 상품에 포함된 꽃을 검색할 수 있습니다 ex) 장미, 수국 등"),
    이용가능지역: Optional[str] = Query(None, description="이용가능지역입니다(시, 도 단위) ex) 경기도, 전라남도, 삼척시 등"),
    색상: Optional[str] = Query(None, description="꽃 상품의 주요 색상을 바탕으로 검색합니다 ex) 핑크, 화이트, 레드 등")
) -> List[dict]:
    filtered_data = []
    for item in flower_d_data:
        if (
            (상품명 is None or 상품명.lower() in item["상품명"].lower())
            and (업체명 is None or 업체명.lower() in item["업체명"].lower())
            and (최소가격 is None or int(item["가격"]) >= 최소가격)
            and (최대가격 is None or int(item["가격"]) <= 최대가격)
            and (꽃종류.lower() in [flower.lower() for flower in item["꽃종류"]])
            and (이용가능지역 is None or 이용가능지역.lower() in [area.lower() for area in item["이용가능지역"]])
            and (색상 is None or 색상.lower() == item["색상"].lower())
        ):
            filtered_data.append(item)
    return filtered_data

n_a_beer_data = [
    {
        "맥주이름": "하이트 제로",
        "브랜드": "하이트",
        "가격": "1180",
        "용량": 350,
        "알콜유무": "N",
        "설명": "퓨린, 알코올, 칼로리가 없는 올 프리 맥주"
    },
    {
        "맥주이름": "넌, 한강",
        "브랜드": "세븐브로이",
        "가격": "1800",
        "용량": 355,
        "알콜유무": "N",
        "설명": "오렌지향과 홉의 향이 가득한 제로알콜맥주"
    },
    {
        "맥주이름": "아사히 드라이 제로",
        "브랜드": "아사히",
        "가격": "5000",
        "용량": 500,
        "알콜유무": "N",
        "설명": "오리지널 아사히 맥주와 흡사한 맛, 가장 맥주다운 논알콜 맥주"
    },
    {
        "맥주이름": "외팅어 알코홀프라이",
        "브랜드": "외팅어",
        "가격": "1300",
        "용량": 500,
        "알콜유무": "Y",
        "설명": "가성비가 좋은 맥주. 0.5도 이하의 알코올 함유"
    },
    {
        "맥주이름": "코젤 다크 넌 알코올릭",
        "브랜드": "코젤",
        "가격": "2600",
        "용량": 500,
        "알콜유무": "Y",
        "설명": "0.5도 이하의 알코올을 함유한 흑맥주"
    }
]

@app.get("/n_a_beer")
async def search_n_a_beer(
    맥주이름: Optional[str] = Query(None, description="검색하고자 하는 맥주의 이름입니다"),
    브랜드: Optional[str] = Query(None, description="검색하고자 하는 맥주의 브랜드입니다"),
    최소가격: Optional[int] = Query(None, description="맥주의 최소 가격입니다(원화 기준)"),
    최대가격: Optional[int] = Query(None, description="맥주의 최대 가격입니다(원화 기준)"),
    최소용량: Optional[float] = Query(None, description="맥주의 최소 용량입니다(ml)"),
    최대용량: Optional[float] = Query(None, description="맥주의 최대 용량입니다(ml)"),
    알콜유무: str = Query(..., description="완전한 무알콜과 저알콜(소량 들어간 비알코올)을 구분합니다. N 또는 Y로 표기합니다"),
    설명: Optional[str] = Query(None, description="맥주의 맛이나 기타 설명을 바탕으로 검색합니다")
) -> List[dict]:
    filtered_data = []
    for item in n_a_beer_data:
        if (
            (맥주이름 is None or 맥주이름.lower() in item["맥주이름"].lower())
            and (브랜드 is None or 브랜드.lower() in item["브랜드"].lower())
            and (최소가격 is None or int(item["가격"]) >= 최소가격)
            and (최대가격 is None or int(item["가격"]) <= 최대가격)
            and (최소용량 is None or item["용량"] >= 최소용량)
            and (최대용량 is None or item["용량"] <= 최대용량)
            and (알콜유무.lower() == item["알콜유무"].lower())
            and (설명 is None or 설명.lower() in item["설명"].lower())
        ):
            filtered_data.append(item)
    return filtered_data

aircon_c_data = [
    {
        "업체이름": "미소청소",
        "에어컨종류": ["벽걸이", "스탠드"],
        "이용가능지역": ["서울시", "인천시"],
        "가격": "80000",
        "평점": 4.5,
        "예약가능여부": "Y",
        "이용후기": ["좋아요", "꼼꼼하세요"],
        "연락처": "010-3464-2417"
    },
    {
        "업체이름": "에어컨박사",
        "에어컨종류": ["벽걸이", "스탠드", "시스템"],
        "이용가능지역": ["경기도", "강원도"],
        "가격": "90000",
        "평점": 4.8,
        "예약가능여부": "Y",
        "이용후기": ["최고였어요", "전문가이신 것 같아요"],
        "연락처": "010-3221-2417"
    },
    {
        "업체이름": "기업전문청소",
        "에어컨종류": ["스탠드", "시스템"],
        "이용가능지역": ["경기도", "서울시"],
        "가격": "150000",
        "평점": 4.9,
        "예약가능여부": "N",
        "이용후기": ["대규모 작업을 믿고 맡깁니다", "노하우가 있으세요"],
        "연락처": "010-3111-2417"
    },
    {
        "업체이름": "맑은공기청소",
        "에어컨종류": ["벽걸이", "스탠드", "시스템"],
        "이용가능지역": ["전라남도", "목포시"],
        "가격": "90000",
        "평점": 4.7,
        "예약가능여부": "Y",
        "이용후기": ["깔끔하게 해주세요", "최고의 전문가"],
        "연락처": "010-6221-2417"
    },
    {
        "업체이름": "에어컨전문가",
        "에어컨종류": ["벽걸이", "스탠드"],
        "이용가능지역": ["경기도", "의정부시"],
        "가격": "50000",
        "평점": 3.8,
        "예약가능여부": "Y",
        "이용후기": ["불만족", "잘해주세요"],
        "연락처": "010-3221-2211"
    },
]

@app.get("/aircon_c")
async def search_aircon_cleaning_companies(
    업체이름: Optional[str] = Query(None, description="검색하고자 하는 업체의 이름"),
    에어컨종류: Optional[str] = Query(None, description="청소 가능한 에어컨 종류입니다 ex) 벽걸이, 스탠드, 시스템(천장형) 에어컨 등"),
    이용가능지역: str = Query(..., description="예약 가능지역입니다(시, 도 단위) ex) 경기도, 전라남도, 삼척시 등"),
    최소가격: Optional[int] = Query(None, description="최소 이용가입니다(원화 기준)"),
    최대가격: Optional[int] = Query(None, description="최대 이용가입니다(원화 기준)"),
    최소평점: Optional[int] = Query(None, description="후기 기준 최소 평점입니다"),
    최대평점: Optional[int] = Query(None, description="후기 기준 최대 평점입니다"),
    예약가능여부: Optional[str] = Query(None, description="현재 예약이 가능한지 여부입니다 Y or N")
) -> List[dict]:
    filtered_data = []
    for item in aircon_c_data:
        if (
            (업체이름 is None or 업체이름.lower() in item["업체이름"].lower())
            and (에어컨종류 is None or 에어컨종류.lower() in [ac.lower() for ac in item["에어컨종류"]])
            and (이용가능지역.lower() in [loc.lower() for loc in item["이용가능지역"]])
            and (최소가격 is None or int(item["가격"]) >= 최소가격)
            and (최대가격 is None or int(item["가격"]) <= 최대가격)
            and (최소평점 is None or item["평점"] >= 최소평점)
            and (최대평점 is None or item["평점"] <= 최대평점)
            and (예약가능여부 is None or 예약가능여부.lower() == item["예약가능여부"].lower())
        ):
            filtered_data.append(item)
    return filtered_data

sunglasses_data = [
    {
        "brand": "젠틀몬스터",
        "size": "L",
        "color": "블랙",
        "price": 269000,
        "A/S 가능여부": True
    },
    {
        "brand": "RAYBAN",
        "size": "S",
        "color": "브라운",
        "price": 129000,
        "A/S 가능여부": True
    },
    {
        "brand": "오클리",
        "size": "XL",
        "color": "투명",
        "price": 100000,
        "A/S 가능여부": False
    },
    {
        "brand": "ZARA",
        "size": "M",
        "color": "옐로우",
        "price": 17000,
        "A/S 가능여부": False
    },
    {
        "brand": "셀린느",
        "size": "M",
        "color": "블랙",
        "price": 625000,
        "A/S 가능여부": True
    }
]

@app.get("/sunglasses")
async def filter_sunglasses(
    max_price: int = Query(..., description="최대 가격"),
    brand: Optional[str] = Query(None, description="브랜드"),
    name: Optional[str] = Query(None, description="상품명"),
    color: Optional[str] = Query(None, description="색상"),
    as_possible: Optional[bool] = Query(None, description="A/S 가능여부 ")
) -> List[dict]:
    filtered_data = []
    for item in sunglasses_data:
        if (
            item["price"] <= max_price
            and (brand is None or item["brand"].lower() == brand.lower())
            and (name is None or item["name"].lower() == name.lower())
            and (color is None or item["color"].lower() == color.lower())
            and (as_possible is None or item["A/S 가능여부"].lower() == as_possible.lower())
        ):
            filtered_data.append(item)
    return filtered_data

camera_data = [
    {
        "brand": "삼성",
        "country": "한국",
        "type": "디지털 카메라",
        "price": 330000,
        "color": "블랙",
        "디스플레이_유무": True
    },
    {
        "brand": "로모그래피",
        "country": "중국",
        "type": "필름 카메라",
        "price": 60000,
        "color": "레드",
        "디스플레이_유무": False
    },
    {
        "brand": "니콘",
        "country": "일본",
        "type": "DSLR",
        "price": 430000,
        "color": "블랙",
        "디스플레이_유무": False
    },
    {
        "brand": "소니",
        "country": "일본",
        "type": "미러리스 카메라",
        "price": 130000,
        "color": "화이트",
        "디스플레이_유무": True
    },
    {
        "brand": "캐논",
        "country": "일본",
        "type": "DSLR",
        "price": 400000,
        "color": "블랙",
        "디스플레이_유무": True
    }
]

@app.get("/camera")
async def filter_camera(
    max_price: int = Query(..., description="최대 가격"),
    brand: Optional[str] = Query(None, description="브랜드"),
    country: Optional[str] = Query(None, description="국가"),
    camera_type: Optional[str] = Query(None, description="카메라 종류"),
    color: Optional[str] = Query(None, description="색상"),
    display_available: Optional[str] = Query(None, description="디스플레이 유무 (Y or N)")
) -> List[dict]:
    filtered_data = []
    for item in camera_data:
        if (
            item["price"] <= max_price
            and (brand is None or item["brand"].lower() == brand.lower())
            and (country is None or item["country"].lower() == country.lower())
            and (camera_type is None or item["type"].lower() == camera_type.lower())
            and (color is None or item["color"].lower() == color.lower())
            and (display_available is None or item["디스플레이_유무"].lower() == display_available.lower())
        ):
            filtered_data.append(item)
    return filtered_data

clothes_data = [
    {
        "brand": "시티브리즈",
        "number": 854128,
        "type": "가디건",
        "price": 75000,
        "color": "핑크",
        "gender": "여성"
    },
    {
        "brand": "밀리언코르",
        "number": 985412,
        "type": "팬츠",
        "price": 45000,
        "color": "그레이",
        "gender": "여성"
    },
    {
        "brand": "톰브라운",
        "number": 327415,
        "type": "맨투맨",
        "price": 564000,
        "color": "네이비",
        "gender": "남성"
    },
    {
        "brand": "포터리",
        "number": 987100,
        "type": "셔츠",
        "price": 189000,
        "color": "블루",
        "gender": "남성"
    },
    {
        "brand": "이그넬",
        "number": 100856,
        "type": "비치웨어",
        "price": 159000,
        "color": "네이비",
        "gender": "여성"
    }
]

@app.get("/clothes")
async def filter_clothes(
    max_price: int = Query(..., description="최대 가격"),
    brand: Optional[str] = Query(None, description="브랜드"),
    number: Optional[int] = Query(None, description="상품코드"),
    clothes_type: Optional[str] = Query(None, description="옷 종류"),
    color: Optional[str] = Query(None, description="색상"),
    gender: Optional[str] = Query(None, description="성별")
) -> List[dict]:
    filtered_data = []
    for item in clothes_data:
        if (
            item["price"] <= max_price
            and (brand is None or item["brand"].lower() == brand.lower())
            and (number is None or item["number"] == number)
            and (clothes_type is None or item["type"].lower() == clothes_type.lower())
            and (color is None or item["color"].lower() == color.lower())
            and (gender is None or item["gender"].lower() == gender.lower())
        ):
            filtered_data.append(item)
    return filtered_data

accommodation_data = [
    {
        "name": "평창라마다호텔",
        "type": "호텔",
        "지역": "강원도",
        "평점": "4.3",
        "예약가능_유무": True
    },
    {
        "name": "가평 조이글램핑펜션",
        "type": "펜션",
        "지역": "경기도",
        "평점": "4.8",
        "예약가능_유무": True
    },
    {
        "name": "부산 서면 아토",
        "type": "모텔",
        "지역": "부산",
        "평점": "3.8",
        "예약가능_유무": False
    },
    {
        "name": "김치 게스트하우스",
        "type": "게스트하우스",
        "지역": "부산",
        "평점": "3.5",
        "예약가능_유무": True
    },
    {
        "name": "글로스터 호텔 청주",
        "type": "호텔",
        "지역": "충청북도",
        "평점": "5",
        "예약가능_유무": False
    }
]

@app.get("/accommodation")
async def filter_accommodation(
    name: Optional[str] = Query(None, description="숙소명"),
    accommodation_type: Optional[str] = Query(None, description="숙소 종류"),
    region: Optional[str] = Query(None, description="지역"),
    min_rating: Optional[float] = Query(None, description="최소 평점", gt=0, le=5),
    reservation_available: Optional[bool] = Query(None, description="예약 가능 유무")
) -> List[dict]:
    filtered_data = []
    for item in accommodation_data:
        if (
            (name is None or item["name"].lower() == name.lower())
            and (accommodation_type is None or item["type"].lower() == accommodation_type.lower())
            and (region is None or item["지역"].lower() == region.lower())
            and (min_rating is None or float(item["평점"]) >= min_rating)
            and (reservation_available is None or item["예약가능_유무"].lower() == reservation_available.lower())
        ):
            filtered_data.append(item)
    return filtered_data

bicycle_data = [
    {
        "brand": "자이언트",
        "gear": "16단",
        "type": "MTB 자전거",
        "size": ["XS", "S", "M", "L"],
        "price": 239000
    },
    {
        "brand": "알톤",
        "gear": "1단",
        "type": "미니벨로 자전거",
        "size": ["XS", "S"],
        "price": 195000
    },
    {
        "brand": "콘스탄틴",
        "gear": "7단",
        "type": "픽시 자전거",
        "size": ["XS", "S", "M", "L"],
        "price": 820000
    },
    {
        "brand": "알톤",
        "gear": "24단",
        "type": "하이브리드 자전거",
        "size": ["M", "L"],
        "price": 330000
    },
    {
        "brand": "자이언트",
        "gear": "16단",
        "type": "로드 자전거",
        "size": ["M", "L"],
        "price": 890000
    }
]

@app.get("/bicycle_brand")
async def filter_bicycle(
    brand: Optional[str] = Query(..., description="브랜드"),
    gear: Optional[str] = Query(None, description="기어"),
    bicycle_type: Optional[str] = Query(None, description="자전거 종류"),
    size: Optional[str] = Query(None, description="사이즈"),
    max_price: Optional[int] = Query(None, description="최대 가격", ge=0)
) -> List[dict]:
    filtered_data = []
    for item in bicycle_data:
        if (
            item["brand"].lower() == brand.lower()
            and (gear is None or item["gear"].lower() == gear.lower())
            and (bicycle_type is None or item["type"].lower() == bicycle_type.lower())
            and (size is None or size in item["size"])
            and (max_price is None or item["price"] <= max_price)
        ):
            filtered_data.append(item)
    return filtered_data

gasstation_data = [
    {
        "이름": "대성주유소",
        "판매_종류": ["휘발유", "경유", "고급"],
        "가격": [1606, 1468, 1896],
        "주소": "서울시 강서구 양천로 176",
        "세차시설_유무": True
    },
    {
        "이름": "GS칼텍스 상암주유소",
        "판매_종류": ["휘발유", "경유"],
        "가격": [1628, 1538],
        "주소": "경기도 고양시 덕양구 자유로 38",
        "세차시설_유무": True
    },
    {
        "이름": "필동주유소",
        "판매_종류": ["휘발유", "경유", "고급"],
        "가격": [2359, 2209, 2609],
        "주소": "서울시 중구 퇴계로 196",
        "세차시설_유무": False
    },
    {
        "이름": "중곡충전소",
        "판매_종류": ["LPG"],
        "가격": [1021],
        "주소": "서울시 광진구 동일로 323",
        "세차시설_유무": False
    },
    {
        "이름": "창원CW",
        "판매_종류": ["휘발유", "경유"],
        "가격": [1535, 1355],
        "주소": "서울시 광진구 광나루로 460",
        "세차시설_유무": True
    }
]

@app.get("/gasstation")
async def filter_gas_station(
    name: Optional[str] = Query(..., description="주유소 이름"),
    fuel_type: Optional[str] = Query(None, description="주유소에서 판매하는 에너지원 종류"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    city: Optional[str] = Query(None, description="지역구분_광역시도"),
    district: Optional[str] = Query(None, description="지역구분_시군구"),
    town: Optional[str] = Query(None, description="지역구분_읍면동"),
    car_wash_facility: Optional[bool] = Query(None, description="세차 시설 유무 Y OR N")
) -> List[dict]:
    filtered_data = []
    for item in gasstation_data:
        if (
            item["이름"].lower() == name.lower()
            and (fuel_type is None or fuel_type in item["판매_종류"])
            and (max_price is None or max(item["가격"]) <= max_price)
            and (city is None or city in item["주소"])
            and (district is None or district in item["주소"])
            and (town is None or town in item["주소"])
            and (car_wash_facility is None or car_wash_facility == item["세차시설_유무"])
        ):
            filtered_data.append(item)
    return filtered_data

musical_data = [
    {
        "name": "레 미제라블",
        "공연_시간": 180,
        "original": "빅토르위고 <레미제라블>",
        "초연_장소": "프랑스",
        "초연_연도": 1980
    },
    {
        "name": "위키드",
        "공연_시간": 170,
        "original": "그레고리 맥과이어 <위키드>",
        "초연_장소": "미국",
        "초연_연도": 2003
    },
    {
        "name": "레베카",
        "공연_시간": 170,
        "original": "대프니 듀 모리에 <레베카>",
        "초연_장소": "오스트리아",
        "초연_연도": 2006
    },
    {
        "name": "영웅",
        "공연_시간": 160,
        "original": "창작 뮤지컬",
        "초연_장소": "한국",
        "초연_연도": 2009
    },
    {
        "name": "시카고",
        "공연_시간": 150,
        "original": "모린 달라스 왓킨스 <A Brave Little Woman>",
        "초연_장소": "1975"
    }
]

@app.get("/musical")
async def filter_musical(
    name: Optional[str] = Query(None, description="작품명"),
    min_time: int = Query(..., description="최소 공연시간"),
    original: Optional[str] = Query(None, description="원작"),
    초연_장소: Optional[str] = Query(None, description="뮤지컬이 처음 공연된 장소"),
    초연_연도: Optional[int] = Query(None, description="초연된 연도")
) -> List[dict]:
    filtered_data = []
    for item in musical_data:
        if (
            (name is None or item["name"].lower() == name.lower())
            and item["공연_시간"] >= min_time
            and (original is None or original.lower() == item["original"].lower())
            and (초연_장소 is None or 초연_장소.lower() == item["초연_장소"].lower())
            and (초연_연도 is None or 초연_연도 == item["초연_연도"])
        ):
            filtered_data.append(item)
    return filtered_data

university_data = [
    {
        "학교명": "인하대학교",
        "종류": "사립 종합대학",
        "주소": "인천광역시 미추홀구 인하로 100",
        "학과": ["기계공학과", "수학과", "국어교육과", "행정학과"],
        "전화번호": "032-860-7114"
    },
    {
        "학교명": "한양여자대학교",
        "종류": "사립 전문대학",
        "주소": "서울특별시 성동구 살곶이길 200",
        "학과": ["빅데이터과", "패션디자인과", "사회복지과", "치위생과"],
        "전화번호": "02-2290-2114"
    },
    {
        "학교명": "서울시립대학교",
        "종류": "공립 종합대학",
        "주소": "서울특별시 동대문구 서울시립대로 163",
        "학과": ["사회복지학과", "화학공학과", "철학과", "음악학과"],
        "전화번호": "02-6490-6114"
    },
    {
        "학교명": "중부대학교",
        "종류": "사립 종합대학",
        "주소": "충청남도 금산군 추부면 대학로 201",
        "학과": ["경찰경호학과", "식품영양학과", "물리치료학과", "동물보건학과"],
        "전화번호": "041-750-6500"
    },
    {
        "학교명": "부천대학교",
        "종류": "사립 전문대학",
        "주소": "경기도 부천시 심곡동 신흥로56번길 25",
        "학과": ["건축과", "경영학과", "간호학과", "재활스포츠학과"],
        "전화번호": "032-610-0114"
    }
]

@app.get("/university")
async def filter_university(
    name: Optional[str] = Query(None, description="학교명"),
    metropolitan: Optional[str] = Query(None, description="지역구분 광역시도"),
    city: Optional[str] = Query(None, description="지역구분 시군구"),
    department: Optional[str] = Query(None, description="학과"),
    category: Optional[str] = Query(None, description="대학교 종류")
) -> List[dict]:
    filtered_data = []
    for item in university_data:
        if (
            (name is None or item["학교명"].lower() == name.lower())
            and (metropolitan is None or item["주소"].startswith(metropolitan))
            and (city is None or item["주소"].endswith(city))
            and (department is None or department in item["학과"])
            and (category is None or item["종류"].lower() == category.lower())
        ):
            filtered_data.append(item)
    return filtered_data

####

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

    error_msg = ''
    if theme is None and min_grade is None:
        error_msg = '{"status": 400,"error": "Bad Request","message": "Required parameter theme, min_grade is missing."}'
        raise HTTPException(status_code=200, detail='error')
    elif theme is None:
        error_msg = '{"status": 400,"error": "Bad Request","message": "Required parameter theme is missing."}'
        raise HTTPException(status_code=200, detail='theme, min_grade is missing')
    elif min_grade is None:
        error_msg = '{"status": 400,"error": "Bad Request","message": "Required parameter min_grade is missing."}'
        raise HTTPException(status_code=200, detail=error_msg)
        
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
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    min_grade: Optional[float] = Query(None, ge=0, le=5, description="최소 평점"),
    max_grade: Optional[float] = Query(None, ge=0, le=5, description="최대 평점"),
) -> List[dict]:

    if name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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

    if type is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter type is missing."})
        raise HTTPException(status_code=200, detail=error_msg)
    
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

    if gu is None and name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter gu, name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif gu is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter gu is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    type: Optional[str] = Query(None, description="노선 유형(ex: 공항, 광역급행, 용인시 마을 등)"),
    starting_point: Optional[str] = Query(None, description="기점"),
    terminal: Optional[str] = Query(None, description="종점"),
    bus_stop: Optional[str] = Query(None, description="정류장명(주요 경유지를 바탕으로 검색합니다)")
) -> List[dict]:

    if num is None and type is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter num, type is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif num is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter num is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif type is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter type is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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

    if num is None and name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter num, name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif num is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter num is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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

    if grade is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter grade is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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

    if line is None and name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter line, name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif line is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter line is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)

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
    name: Optional[str] = Query(None, description="원소명"),
    group: Optional[int] = Query(None, ge=1, le=18, description="족"),
    period: Optional[int] = Query(None, ge=1, le=7, description="주기"),
) -> List[dict]:

    if period is None and group is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter period, group is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif period is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter period is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif group is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter group is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    name: Optional[str] = Query(None, description="프로젝트명"),
    student: Optional[str] = Query(None, description="팀원명"),
    professor: Optional[str] = Query(None, description="담당 교수명"),
    year: Optional[int] = Query(None, description="연도"),
    semester: Optional[int] = Query(None, ge=1, le=2, description="학기"),
    language: Optional[str] = Query(None, description="사용 언어"),
) -> List[dict]:

    if year is None and semester is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter year, semester is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif year is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter year is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif semester is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter semester is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    type: Optional[str] = Query(None, description="분류"),
    country: Optional[str] = Query(None, description="개최국"),
    city: Optional[str] = Query(None, description="도시"),
    strtYr: Optional[str] = Query(None, description="최소 개최 연도(개회일을 바탕으로 검색)"),
    endYr: Optional[str] = Query(None, description="최대 개최 연도(개회일을 바탕으로 검색)")
) -> List[dict]:

    if type is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter type is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    ctprvNm: Optional[str] = Query(None, description="시도명"),
    sgngNm: Optional[str] = Query(None, description="시군구명"),
    name: Optional[str] = Query(None, description="시설명"),
    min_households: Optional[int] = Query(None, description="최소 세대수"),
    max_households: Optional[int] = Query(None, description="최대 세대수")
) -> List[dict]:

    if name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    company: Optional[str] = Query(None, description="기업명"),
    name: Optional[str] = Query(None, description="시험명"),
    min_questions: Optional[int] = Query(None, description="최소 문항수"),
    max_questions: Optional[int] = Query(None, description="최대 문항수"),
    min_time: Optional[int] = Query(None, description="최소 시험시간 (단위: 분)"),
    max_time: Optional[int] = Query(None, description="최대 시험시간 (단위: 분)"),
    subject: Optional[str] = Query(None, description="과목명")
) -> List[dict]:

    if company is None and name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter company, name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif company is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter company is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    min_contract_period: Optional[int] = Query(None, description="최소 약정 기간 (단위: 개월)"),
    max_contract_period: Optional[int] = Query(None, description="최대 약정 기간 (단위: 개월)"),
    min_fee: Optional[int] = Query(None, description="최소 월 렌탈료"),
    max_fee: Optional[int] = Query(None, description="최대 월 렌탈료"),
    min_grade: Optional[float] = Query(None, description="최소 평점"),
    max_grade: Optional[float] = Query(None, description="최대 평점"),
):

    if brand is None and name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter brand, name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif brand is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter brand is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="센터명"),
    congestion: Optional[str] = Query(None, description="혼잡도"),
    item: Optional[str] = Query(None, description="제품명(수리 제품을 바탕으로 검색)"),
) -> List[dict]:

    if name is None and congestion is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name, congestion is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif congestion is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter congestion is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    min_grade: Optional[float] = Query(None, ge=0, le=5, description="최소 평점"),
    max_grade: Optional[float] = Query(None, ge=0, le=5, description="최대 평점")
) -> List[dict]:

    if name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="우체국명"),
    fund_sale: Optional[bool] = Query(None, description="펀드 판매 여부"),
    atm: Optional[bool] = Query(None, description="365코너 설치 여부")
) -> List[dict]:

    if fund_sale is None and name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter fund_sale, name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif fund_sale is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter fund_sale is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="국립공원명"),
    num: Optional[int] = Query(None, description="호수"),
    course: Optional[str] = Query(None, description="코스명(탐방 코스를 바탕으로 검색)")
):

    if course is None and num is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter course, num is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif course is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter course is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif num is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter num is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
    results = []
    for item in national_park_data:
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
    min_abv: Optional[float] = Query(None, description="최소 도수 (단위: %)"),
    max_abv: Optional[float] = Query(None, description="최대 도수 (단위: %)")
):

    if type is None and cask is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter type, cask is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif type is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter type is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif cask is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter cask is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    gu: Optional[str] = Query(None, description="서울시 행정구역명(ex: 강남구, 중구 등)"),
    establishment: Optional[str] = Query(None, description="설립 구분(ex: 국립, 사립, 공립)"),
    school_type: Optional[str] = Query(None, description="유형(ex: 예술계열, 과학계열, 외국어계열, 마이스터고, 국제계열, 체육계열)"),
    gender: Optional[str] = Query(None, description="성별(ex: 공학, 여, 남)"),
    name: Optional[str] = Query(None, description="학교명"),
):

    if establishment is None and school_type is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter establishment, school_type is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif establishment is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter establishment is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif school_type is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter school_type is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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

    if name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    name: Optional[str] = Query(None, description="학교명"),
    establishment: Optional[str] = Query(None, description="설립 구분(ex: 국립, 사립, 공립)"),
    target: Optional[str] = Query(None, description="대상자(ex: 시각장애, 지적장애 등)"),
) -> List[dict]:

    if establishment is None and target is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter establishment, target is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif establishment is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter establishment is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif target is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter target is missing."})
        raise HTTPException(status_code=400, detail=error_msg)

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
    category: Optional[str] = Query(None, description="카테고리(ex: 의류, 가방 등)"),
    name: Optional[str] = Query(None, description="쇼핑몰 이름"),
    style: Optional[str] = Query(None, description="스타일(ex: 심플베이직, 유니크 등)"),
    free_shipping: Optional[bool] = Query(None, description="무료배송 여부"),
    item: Optional[str] = Query(None, description="상품명(인기 상품을 바탕으로 검색)")
) -> List[dict]:

    if style is None and category is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter style, category is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif style is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter style is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif category is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter ㅍ is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격")
) -> List[dict]:

    if category is None and wire is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category, wire is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif category is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif wire is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter wire is missing."})
        raise HTTPException(status_code=400, detail=error_msg)

    
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
    ctprvNm: Optional[str] = Query(None, description="시도명(ex: 서울특별시, 인천광역시, 강원도, 경기도, 경상남도 등)"),
    sgngNm: Optional[str] = Query(None, description="시군구명(ex: 전주시, 강릉시, 포항시, 양평군 등)"),
    category: Optional[str] = Query(None, description="카테고리"),
    name: Optional[str] = Query(None, description="식당명"),
    menu: Optional[str] = Query(None, description="메뉴명(대표 메뉴를 바탕으로 검색)")
) -> List[dict]:

    if category is None and menu is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category, menu is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif category is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif menu is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter menu is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    min_price_oneday: Optional[int] = Query(None, description="최소 1일권 가격"),
    max_price_oneday: Optional[int] = Query(None, description="최대 1일권 가격"),
    artist: Optional[str] = Query(None, description="아티스트명(라인업을 바탕으로 검색)")
) -> List[dict]:

    if artist is None and name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter artist, name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif artist is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter artist is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif name is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter name is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    ctprvNm: Optional[str] = Query(None, description="시도명"),
    sgngNm: Optional[str] = Query(None, description="시군구명"),
    min_dt: Optional[str] = Query(None, description="최소 발송일"),
    max_dt: Optional[str] = Query(None, description="최대 발송일")
) -> List[dict]:

    if type is None and subclass is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter type, subclass is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif type is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter type is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif subclass is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter subclass is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    min_songs: Optional[int] = Query(None, description="최소 곡수", gt=0),
    max_songs: Optional[int] = Query(None, description="최대 곡수", gt=0),
    min_likes: Optional[int] = Query(None, description="최소 좋아요수", ge=0),
    max_likes: Optional[int] = Query(None, description="최대 좋아요수", ge=0)
) -> List[dict]:

    if title is None and category is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter title, category is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif title is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter title is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif category is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    min_calorie: Optional[float] = Query(None, gt=0, description="최소 칼로리 (단위: kcal)"),
    max_calorie: Optional[float] = Query(None, gt=0, description="최대 칼로리 (단위: kcal)"),
    ingredient: Optional[str] = Query(None, description="재료(주 재료를 바탕으로 검색)"),
    sauce: Optional[str] = Query(None, description="소스(추천 소스를 바탕으로 검색)")
) -> List[dict]:

    if ingredient is None and sauce is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter ingredient, sauce is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif ingredient is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter ingredient is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif sauce is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter sauce is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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

    if ctprvNm is None and sgngNm is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter ctprvNm, sgngNm is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif ctprvNm is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter ctprvNm is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif sgngNm is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter sgngNm is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    offline: Optional[bool] = Query(None, description="오프라인 구매 가능 여부")
):

    if category is None and ingredient is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category, ingredient is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif category is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif ingredient is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter ingredient is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    
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
    category: Optional[str] = Query(None, description="카테고리(ex: 명품 브랜드, 향수·화장품, 주류·담배, 패션·액세서리 등)"),
    brand: Optional[str] = Query(None, description="브랜드명"),
    phone: Optional[str] = Query(None, description="연락처"),
    location: Optional[str] = Query(None, description="위치"),
    item: Optional[str] = Query(None, description="상품명(주요 상품을 바탕으로 검색)")
):
    if category is None and brand is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category, brand is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif category is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter category is missing."})
        raise HTTPException(status_code=400, detail=error_msg)
    elif brand is None:
        error_msg = str({"status": 400,"error": "Bad Request","message": "Required parameter brand is missing."})
        raise HTTPException(status_code=400, detail=error_msg)


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

employees = [
    {
        "id": "15842",
        "name": "이광훈",
        "dept": "개발",
        "position": "부장",
        "phone": "010-8899-9988",
        "enter": "2001"
    },
    {
        "id": "15995",
        "name": "이영현",
        "dept": "영업",
        "position": "과장",
        "phone": "010-7788-8877",
        "enter": "2013"
    },
    {
        "id": "16475",
        "name": "한미연",
        "dept": "마케팅",
        "position": "대리",
        "phone": "010-4455-5566",
        "enter": "2019"
    },
    {
        "id": "16689",
        "name": "강힘찬",
        "dept": "인사",
        "position": "대리",
        "phone": "010-5522-5522",
        "enter": "2019"
    },
    {
        "id": "19978",
        "name": "김설아",
        "dept": "개발",
        "position": "사원",
        "phone": "010-4477-7744",
        "enter": "2021"
    }
]

@app.get("/employee")
async def search_employee(
    id: Optional[str] = Query(None, description="사번"),
    name: Optional[str] = Query(None, description="이름"),
    dept: str = Query(..., description="부서"),
    position: Optional[str] = Query(None, description="직급"),
    phone: Optional[str] = Query(None, description="전화번호"),
    min_enter: Optional[str] = Query(None, description="최소 입사년도"),
    max_enter: Optional[str] = Query(None, description="최대 입사년도"),
):
    results = []
    for employee in employees:
        if (
            (id is None or id == employee["id"]) and
            (name is None or name == employee["name"]) and
            dept == employee["dept"] and
            (position is None or position == employee["position"]) and
            (phone is None or phone == employee["phone"]) and
            (min_enter is None or min_enter <= employee["enter"]) and
            (max_enter is None or max_enter >= employee["enter"])
        ):
            results.append(employee)
    return results

water_parks = [
    {
        "name": "위례 주제공원 물놀이장",
        "location": "경기 성남시 수정구 위례순환로4길 2-1",
        "time": "10:00-17:00",
        "break": "월요일",
        "review": "화장실도 깨끗하고 주차가 쉬워요."
    },
    {
        "name": "금곡동물놀이장",
        "location": "경기 성남시 분당구 구미동 99",
        "time": "10:00-18:00",
        "break": "",
        "review": "휴무일 없는 최고의 물놀이장"
    },
    {
        "name": "정자동 물놀이장",
        "location": "경기 성남시 분당구 정자동 100-3",
        "time": "10:00-18:00",
        "break": "수요일",
        "review": "넓고 수질이 좋아요."
    },
    {
        "name": "희망대공원 물놀이장",
        "location": "경기 성남시 수정구 신흥동",
        "time": "10:00-17:00",
        "break": "일요일",
        "review": "테니스장 근처에 있는 물놀이장."
    },
    {
        "name": "야탑동 물놀이장",
        "location": "경기 성남시 분당구 야탑동 555",
        "time": "09:00-17:00",
        "break": "화요일",
        "review": "반려동물 입장 금지라 아쉬워요."
    }
]

@app.get("/sn_waterpark")
async def search_sn_waterpark(
    name: str = Query(..., description="이름"),
    location: Optional[str] = Query(None, description="위치"),
    time: Optional[str] = Query(None, description="영업시간"),
    break_time: Optional[str] = Query(None, description="휴무일"),
    keyword: Optional[str] = Query(None, description="리뷰를 바탕으로 검색하는 키워드입니다.")
):
    results = []
    for park in water_parks:
        if (
            name == park["name"] and
            (location is None or location == park["location"]) and
            (time is None or time == park["time"]) and
            (break_time is None or break_time == park["break"]) and
            (keyword is None or keyword in park["review"])
        ):
            results.append(park)
    return results

licenses = [
    {
        "name": "캘리클럽 청담점",
        "location": "서울 강남구 선릉로 832 소나무빌딩 지하2층 지하3층",
        "time": "10:00-19:00",
        "phone": "02-1458-2774",
        "price": 25000,
        "parking": False
    },
    {
        "name": "코코몽키즈랜드 송파점",
        "location": "서울 송파구 충민로 66 가든파이브 NC백화점 송파점 영관 6층",
        "time": "10:30-20:30",
        "phone": "02-1312-5718",
        "price": 18000,
        "parking": True
    },
    {
        "name": "하이펀",
        "location": "서울 마포구 신촌로 170 이대역푸르지오시티 213호",
        "time": "08:00-22:00",
        "phone": "02-1424-1182",
        "price": 39000,
        "parking": False
    },
    {
        "name": "퐁퐁플라워 건대센터",
        "location": "서울 광진구 아차산로 272 건대스타시티몰 B1층",
        "time": "11:00-21:00",
        "phone": "02-452-4488",
        "price": 17000,
        "parking": False
    },
    {
        "name": "우리끼리 키즈카페 블럭마을 용산원효점",
        "location": "서울 용산구 원효로 51 삼성테마트상가 2층 204호, 205호",
        "time": "10:00-20:00",
        "phone": "1899-3635",
        "price": 21000,
        "parking": True
    }
]

@app.get("/license")
async def search_license(
    name: str = Query(..., description="이름"),
    location: Optional[str] = Query(None, description="위치"),
    time: Optional[str] = Query(None, description="영업시간"),
    phone: Optional[str] = Query(None, description="전화번호"),
    min_price: Optional[int] = Query(None, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    parking: Optional[bool] = Query(None, description="주차장 유무")
):
    results = []
    for license in licenses:
        if (
            license["name"].lower() == name.lower() and
            (location is None or license["location"].lower() == location.lower()) and
            (time is None or license["time"].lower() == time.lower()) and
            (phone is None or license["phone"].lower() == phone.lower()) and
            (min_price is None or license["price"] >= min_price) and
            (max_price is None or license["price"] <= max_price) and
            (parking is None or license["parking"] == parking)
        ):
            results.append(license)
    return results

licenses = [
    {
        "institute": "ETS",
        "category": "외국어",
        "name": "TOEIC",
        "require": "없음",
        "receipt": "2023.02.19-2023.03.01",
        "exam": "2023.05.25"
    },
    {
        "institute": "서울대학교 언어교육원",
        "category": "외국어",
        "name": "TEPS",
        "require": "없음",
        "receipt": "2023.03.15-2023.03.22",
        "exam": "2023.04.10"
    },
    {
        "institute": "한국산업인력공단",
        "category": "정보기술",
        "name": "정보처리기능사",
        "require": "없음",
        "receipt": "2023.05.25-2023.05.30",
        "exam": "2023.07.25"
    },
    {
        "institute": "한국산업인력공단",
        "category": "정보기술",
        "name": "정보처리기사",
        "require": "정보처리기능사 합격자, 관련전공 대학교 4학년 이상",
        "receipt": "2023.06.05-2023.06.12",
        "exam": "2023.08.13"
    },
    {
        "institute": "국토교통부",
        "category": "부동산",
        "name": "공인중개사",
        "require": "없음",
        "receipt": "2023.06.25-2023.07.02",
        "exam": "2023.07.31"
    }
]

@app.get("/license")
async def search_license(
    institute: Optional[str] = Query(None, description="발급기관"),
    category: str = Query(..., description="카테고리"),
    name: Optional[str] = Query(None, description="이름"),
    min_receipt: Optional[str] = Query(None, description="최소 접수일"),
    max_receipt: Optional[str] = Query(None, description="최대 접수일"),
    min_exam: Optional[str] = Query(None, description="최소 시험일"),
    max_exam: Optional[str] = Query(None, description="최대 시험일"),
    keyword: Optional[str] = Query(None, description="자격요건을 바탕으로 검색하는 키워드입니다.")
):
    results = []
    for license in licenses:
        if (
            (institute is None or license["institute"].lower() == institute.lower()) and
            license["category"].lower() == category.lower() and
            (name is None or license["name"].lower() == name.lower()) and
            (min_receipt is None or license["receipt"] >= min_receipt) and
            (max_receipt is None or license["receipt"] <= max_receipt) and
            (min_exam is None or license["exam"] >= min_exam) and
            (max_exam is None or license["exam"] <= max_exam) and
            (keyword is None or keyword.lower() in license["require"].lower())
        ):
            results.append(license)
    return results

language_swap_customers = [
    {
        "id": "kominji",
        "nickname": "민지12",
        "language": "한국어",
        "swapLang": ["영어", "프랑스어", "중국어"],
        "introduce": "서울에 거주하고 있는 한국인입니다. 채팅은 언제든 환영입니다.",
        "chatPerson": ["방탄부인", "씽씬강"]
    },
    {
        "id": "frpba",
        "nickname": "fabian_00",
        "language": "프랑스어",
        "swapLang": ["한국어", "중국어"],
        "introduce": "한국어 못해요 알려줄 사람 필요해요. 남자인 친구 구해요.",
        "chatPerson": ["씽씬강"]
    },
    {
        "id": "chXXing",
        "nickname": "씽씬강",
        "language": "중국어",
        "swapLang": ["한국어"],
        "introduce": "베이징에서 왔어요. 공부도 하고 친구도 해요.",
        "chatPerson": ["민지12", "fabian_00"]
    },
    {
        "id": "engEJ",
        "nickname": "JennyLuv",
        "language": "일본어",
        "swapLang": ["영어", "중국어"],
        "introduce": "됴쿄 거주중. 채팅으로만 대화해요.",
        "chatPerson": ["방탄부인"]
    },
    {
        "id": "enCher",
        "nickname": "방탄부인",
        "language": "영어",
        "swapLang": ["한국어", "일본어"],
        "introduce": "K-POP 팬입니다. 한국어 배우고 싶어요.",
        "chatPerson": ["민지12", "JennyLuv"]
    }
]

@app.get("/language_swap")
async def search_language_swap_customer(
    id: Optional[str] = Query(None, description="아이디"),
    nickname: str = Query(..., description="닉네임"),
    language: Optional[str] = Query(None, description="가능 언어"),
    swapLang: Optional[str] = Query(None, description="교환 희망 언어"),
    chatPerson: Optional[int] = Query(None, description="채팅중인 회원"),
    keyword: Optional[str] = Query(None, description="자기소개의 설명을 검색하는 키워드")
):
    results = []
    for customer in language_swap_customers:
        if (
            (id is None or customer["id"].lower() == id.lower()) and
            customer["nickname"].lower() == nickname.lower() and
            (language is None or customer["language"].lower() == language.lower()) and
            (swapLang is None or swapLang.lower() in [lang.lower() for lang in customer["swapLang"]]) and
            (chatPerson is None or chatPerson in [person.lower() for person in customer["chatPerson"]]) and
            (keyword is None or keyword.lower() in customer["introduce"].lower())
        ):
            results.append(customer)
    return results

supp_battery_products = [
    {
        "manufacture": "리큐엠",
        "name": "QP2000A",
        "mAh": 20000,
        "price": 36900,
        "type": "Type-C",
        "weight": 350
    },
    {
        "manufacture": "아이워크",
        "name": "DBL4500",
        "mAh": 4500,
        "price": 27900,
        "type": "Type-C",
        "weight": 92
    },
    {
        "manufacture": "로렌텍",
        "name": "맥세이프 갤럭시 아이폰 고속 무선충전",
        "mAh": 5000,
        "price": 25900,
        "type": "Type-C",
        "weight": 116
    },
    {
        "manufacture": "프라임큐",
        "name": "PR-ST5000-C",
        "mAh": 5000,
        "price": 6900,
        "type": "8 Pin",
        "weight": 110
    },
    {
        "manufacture": "로모스",
        "name": "PSW20-392-1183H",
        "mAh": 25000,
        "price": 49900,
        "type": "8 Pin",
        "weight": 475
    }
]

@app.get("/supp_battery")
async def search_supp_battery(
    manufacture: str = Query(..., description="제조사"),
    name: Optional[str] = Query(None, description="상품명"),
    mAh: Optional[int] = Query(None, description="용량"),
    min_price: Optional[int] = Query(None, ge=0, description="최소 가격"),
    max_price: Optional[int] = Query(None, description="최대 가격"),
    type: Optional[str] = Query(None, description="타입 ex. C-Type, 8 Pin"),
    weight: Optional[float] = Query(None, ge=0, description="무게(g)")
):
    results = []
    for product in supp_battery_products:
        if (
            product["manufacture"].lower() == manufacture.lower() and
            (name is None or name.lower() in product["name"].lower()) and
            (mAh is None or product["mAh"] == mAh) and
            (min_price is None or product["price"] >= min_price) and
            (max_price is None or product["price"] <= max_price) and
            (type is None or type.lower() == product["type"].lower()) and
            (weight is None or product["weight"] == weight)
        ):
            results.append(product)
    return results

medical_records = [
    {
        "protector": "김민지",
        "pet_name": "깨솜",
        "type": "강아지",
        "treatment": "중성화",
        "date": "2023.03.06",
        "report": "중성화 수술중 스케일링 동시진행"
    },
    {
        "protector": "이민채",
        "pet_name": "만두",
        "type": "고양이",
        "treatment": "구토",
        "date": "2023.05.25",
        "report": "헤어볼로 인한 잦은 구토, 6월 26일 재방문"
    },
    {
        "protector": "안혜린",
        "pet_name": "솜",
        "type": "고양이",
        "treatment": "구내염",
        "date": "2023.02.16",
        "report": "전발치, 구내염 가루약 처방"
    },
    {
        "protector": "윤동익",
        "pet_name": "마일로",
        "type": "강아지",
        "treatment": "곰팡이 피부병",
        "date": "2023.06.01",
        "report": "소독 스프레이, 스테로이드 연고 처방"
    },
    {
        "protector": "강민혁",
        "pet_name": "망고",
        "type": "고양이",
        "treatment": "후지마비",
        "date": "2023.06.22",
        "report": "선천적 마비로 보호자의 관리 필요, 진통제 처방"
    }
]

@app.get("/medical_records")
async def search_medical_records(
    protector: Optional[str] = Query(None, description="보호자"),
    pet_name: str = Query(..., description="동물 이름"),
    type: Optional[str] = Query(None, description="종류"),
    treatment: Optional[str] = Query(None, description="진료 항목 ex.중성화, 구내염 등"),
    date: Optional[str] = Query(None, description="방문 날짜"),
    keyword: Optional[str] = Query(None, description="진료항목과 특이사항의 정보를 검색하는 키워드")
):
    results = []
    for record in medical_records:
        if (
            (protector is None or record["protector"].lower() == protector.lower()) and
            record["pet_name"].lower() == pet_name.lower() and
            (type is None or record["type"].lower() == type.lower()) and
            (treatment is None or record["treatment"].lower() == treatment.lower()) and
            (date is None or record["date"] == date) and
            (keyword is None or keyword.lower() in record["treatment"].lower() or keyword.lower() in record["report"].lower())
        ):
            results.append(record)
    return results

water_parks = [
    {
        "name": "페리아도워터파크",
        "type": "워터파크",
        "sgg": "포천시",
        "emd": "소홀읍",
        "rating": 4.8
    },
    {
        "name": "백운계곡",
        "type": "계곡",
        "sgg": "포천시",
        "emd": "이동면",
        "rating": 4.6
    },
    {
        "name": "북한산천연옥워터파크",
        "type": "워터파크",
        "sgg": "고양시",
        "emd": None,
        "rating": 4.5
    },
    {
        "name": "인디어라운드",
        "type": "캠핑장",
        "sgg": "이천시",
        "emd": None,
        "rating": 4.6
    },
    {
        "name": "그랜드유원지",
        "type": "유원지",
        "sgg": "양주시",
        "emd": None,
        "rating": 3.9
    },
    {
        "name": "묘적사계곡",
        "type": "계곡",
        "sgg": "남양주시",
        "emd": None,
        "rating": 4.2
    }
]

@app.get("/water_parks")
async def filter_water_parks(
    name: Optional[str] = Query(None, description="시설 이름"),
    type: str = Query(..., description="시설 종류 ex) 워터파크, 계곡, 유원지"),
    sgg: Optional[str] = Query(None, description="지역구분 시군구"),
    emd: Optional[str] = Query(None, description="지역구분 읍면동"),
    min_rating: Optional[float] = Query(None, description="최소 평점", gt=0, le=5)
):
    results = []
    for park in water_parks:
        if (
            (name is None or park["name"].lower() == name.lower()) and
            park["type"].lower() == type.lower() and
            (sgg is None or park["sgg"].lower() == sgg.lower()) and
            (emd is None or park["emd"].lower() == emd.lower() if park["emd"] else False) and
            (min_rating is None or park["rating"] >= min_rating)
        ):
            results.append(park)
    return results

saunas = [
    {
        "name": "수리산랜드",
        "gd": "경기도",
        "sgg": "안양시",
        "price": 11000,
        "opening_time": "08:00시",
        "closed_time": "21:00시"
    },
    {
        "name": "숲속한방랜드",
        "gd": "서울특별시",
        "sgg": "서대문구",
        "price": 15000,
        "opening_time": "06:30시",
        "closed_time": "22:00시"
    },
    {
        "name": "사우나파크",
        "gd": "경기도",
        "sgg": "안양시",
        "price": 14000,
        "opening_time": "00:00시",
        "closed_time": "24:00시"
    },
    {
        "name": "천지연",
        "gd": "대전광역시",
        "sgg": "서구",
        "price": 8000,
        "opening_time": "05:30시",
        "closed_time": "23:00시"
    },
    {
        "name": "호수사우나찜질방",
        "gd": "충청북도",
        "sgg": "충주시",
        "price": 9000,
        "opening_time": "00:00시",
        "closed_time": "24:00시"
    }
]

@app.get("/saunas")
async def search_saunas(
    name: Optional[str] = Query(None, description="업소명"),
    gd: Optional[str] = Query(None, description="지역구분 광역시도"),
    sgg: Optional[str] = Query(None, description="지역구분 시군구"),
    max_price: int = Query(..., description="최대 가격", gt=0),
    opening_time: Optional[str] = Query(None, description="오픈 시간"),
    closed_time: Optional[str] = Query(None, description="마감 시간")
):
    results = []
    for sauna in saunas:
        if (
            (name is None or sauna["name"].lower() == name.lower()) and
            (gd is None or sauna["gd"].lower() == gd.lower()) and
            (sgg is None or sauna["sgg"].lower() == sgg.lower()) and
            sauna["price"] <= max_price and
            (opening_time is None or sauna["opening_time"] == opening_time) and
            (closed_time is None or sauna["closed_time"] == closed_time)
        ):
            results.append(sauna)
    return results

festivals = [
    {
        "name": "보성 다향대축제",
        "region": "보성",
        "location": "한국차문화공원",
        "stdate": "04월 29일",
        "ltdate": "05월 07일",
        "number": 46
    },
    {
        "name": "함평 나비대축제",
        "region": "함평",
        "location": "함평엑스포공원",
        "stdate": "04월 28일",
        "ltdate": "05월 07일",
        "number": 25
    },
    {
        "name": "화성 뱃놀이 축제",
        "region": "화성",
        "location": "전곡항",
        "stdate": "06월 09일",
        "ltdate": "06월 11일",
        "number": 13
    },
    {
        "name": "실향민 문화 축제",
        "region": "속초",
        "location": "속초 엑스포 잔디광장",
        "stdate": "06월 09일",
        "ltdate": "06월 11일",
        "number": 8
    },
    {
        "name": "김제 지평선 축제",
        "region": "김제",
        "location": "벽골제",
        "stdate": "10월 05일",
        "ltdate": "10월 09일",
        "number": 25
    }
]

@app.get("/local_festival")
async def filter_local_festival(
    name: Optional[str] = Query(None, description="축제 이름"),
    region: Optional[str] = Query(None, description="지역 ex) 보성, 김제, 화성"),
    location: Optional[str] = Query(None, description="축제 장소"),
    stdate: Optional[str] = Query(None, description="축제 시작 날짜"),
    ltdate: Optional[str] = Query(None, description="축제 마지막 날짜")
):
    results = []
    for festival in festivals:
        if (
            (name is None or festival["name"].lower() == name.lower()) and
            (region is None or festival["region"].lower() == region.lower()) and
            (location is None or festival["location"].lower() == location.lower()) and
            (stdate is None or festival["stdate"] == stdate) and
            (ltdate is None or festival["ltdate"] == ltdate)
        ):
            results.append(festival)
    return results

fishing_places = [
    {
        "name": "화도낚시터",
        "price": 25000,
        "region": "경기 남양주시",
        "fish_type": ["붕어", "향어", "떡붕어", "송어", "잉어"],
        "closed_time": 24,
        "review_num": 111
    },
    {
        "name": "약수손맛터",
        "price": 10000,
        "region": "경기 고양시",
        "fish_type": ["붕어", "떡붕어"],
        "closed_time": 22,
        "review_num": 27
    },
    {
        "name": "샘터낚시터",
        "price": 30000,
        "region": "경기 광명시",
        "fish_type": ["붕어", "향어", "잉어"],
        "closed_time": 24,
        "review_num": 12
    },
    {
        "name": "마정낚시터",
        "price": 25000,
        "region": "충남 천안시",
        "fish_type": ["붕어", "향어", "잉어", "메기"],
        "closed_time": 24,
        "review_num": 96
    },
    {
        "name": "강촌낚시터",
        "price": 30000,
        "region": "강원 춘천시",
        "fish_type": ["붕어", "향어", "토종 붕어"],
        "closed_time": 24,
        "review_num": 25
    }
]

@app.get("/fishingplace")
async def search_fishing_place(
    name: Optional[str] = Query(None, description="낚시터 이름"),
    max_price: Optional[int] = Query(None, description="최대 가격", ge=0),
    region: Optional[str] = Query(None, description="지역"),
    fish_type: Optional[str] = Query(..., description="물고기 종류"),
    closed_time: Optional[int] = Query(None, description="마감 시간")
):
    results = []
    for place in fishing_places:
        if (
            (name is None or place["name"].lower() == name.lower()) and
            (max_price is None or place["price"] <= max_price) and
            (region is None or place["region"].lower() == region.lower()) and
            (fish_type is None or fish_type.lower() in [ftype.lower() for ftype in place["fish_type"]]) and
            (closed_time is None or place["closed_time"] == closed_time)
        ):
            results.append(place)
    return results

restaurants = [
    {
        "name": "바이킹스워프",
        "region": "서울",
        "type": "해산물",
        "price": 180000,
        "review_num": 2784
    },
    {
        "name": "더더간장게장무한리필",
        "region": "경기",
        "type": "해산물",
        "price": 22000,
        "review_num": 2328
    },
    {
        "name": "무한돈",
        "region": "부산",
        "type": "고기",
        "price": 11500,
        "review_num": 121
    },
    {
        "name": "통큰소무한리필",
        "region": "경기",
        "type": "고기",
        "price": 29900,
        "review_num": 752
    },
    {
        "name": "피기피기무한리필",
        "region": "서울",
        "type": "고기",
        "price": 14500,
        "review_num": 196
    }
]

@app.get("/freerefillrestaurant")
async def filter_free_refill_restaurant(
    name: Optional[str] = Query(None, description="식당 이름"),
    region: Optional[str] = Query(..., description="지역"),
    type: Optional[str] = Query(None, description="식품 종류"),
    max_price: Optional[int] = Query(None, description="최대 가격", ge=0),
    min_price: Optional[int] = Query(None, description="최소 가격", ge=0)
):
    results = []
    for restaurant in restaurants:
        if (
            (name is None or restaurant["name"].lower() == name.lower()) and
            (region is None or restaurant["region"].lower() == region.lower()) and
            (type is None or restaurant["type"].lower() == type.lower()) and
            (max_price is None or restaurant["price"] <= max_price) and
            (min_price is None or restaurant["price"] >= min_price)
        ):
            results.append(restaurant)
    return results

stationeries = [
    {
        "name": "모나미스토어",
        "type": "필기구",
        "address": "서울 성동구 성수동 2가 315-71",
        "opening_time": "10:00",
        "closed_time": "21:00",
        "parking_available": "Y"
    },
    {
        "name": "작은 연필가게 흑심",
        "type": "필기구",
        "address": "서울 마포구 연희로 47 3층",
        "opening_time": "13:00",
        "closed_time": "20:00",
        "parking_available": "N"
    },
    {
        "name": "포셋",
        "type": "엽서",
        "address": "서울 서대문구 연희동 92-18",
        "opening_time": "12:00",
        "closed_time": "20:00",
        "parking_available": "Y"
    },
    {
        "name": "올라이트",
        "type": "엽서",
        "address": "서울 종로구 자하문로5가길 41",
        "opening_time": "13:00",
        "closed_time": "17:00",
        "parking_available": "N"
    },
    {
        "name": "밀리미터밀리그람",
        "type": "필기구",
        "address": "서울 용산구 한남동 683-142",
        "opening_time": "11:30",
        "closed_time": "20:00",
        "parking_available": "Y"
    }
]

@app.get("/stationery")
async def search_stationery(
    name: Optional[str] = Query(None, description="편집샵 이름"),
    type: Optional[str] = Query(..., description="문구 타입"),
    gu: Optional[str] = Query(None, description="지역구분 구"),
    dong: Optional[str] = Query(None, description="지역구분 동"),
    opening_time: Optional[str] = Query(None, description="오픈 시간"),
    closed_time: Optional[str] = Query(None, description="마감 시간"),
    parking_available: Optional[str] = Query(None, description="주차가능여부")
):
    results = []
    for stationery in stationeries:
        if (
            (name is None or stationery["name"].lower() == name.lower()) and
            (type is None or stationery["type"].lower() == type.lower()) and
            (gu is None or stationery["address"].lower().find(gu.lower()) != -1) and
            (dong is None or stationery["address"].lower().find(dong.lower()) != -1) and
            (opening_time is None or stationery["opening_time"] == opening_time) and
            (closed_time is None or stationery["closed_time"] == closed_time) and
            (parking_available is None or stationery["parking_available"].lower() == parking_available.lower())
        ):
            results.append(stationery)
    return results

wines = [
    {
        "name": "닥터 루젠 리슬링",
        "type": "화이트",
        "price": 42000,
        "origin": "독일",
        "year": 2014
    },
    {
        "name": "빌라 엠 로쏘",
        "type": "레드",
        "price": 40000,
        "origin": "이탈리아",
        "year": 2018
    },
    {
        "name": "에스쿠도 로호",
        "type": "레드",
        "price": 47000,
        "origin": "칠레",
        "year": 2014
    },
    {
        "name": "샤또 몽페라",
        "type": "화이트",
        "price": 50000,
        "origin": "프랑스",
        "year": 2019
    },
    {
        "name": "우마니 론끼 요리오",
        "type": "레드",
        "price": 47000,
        "origin": "이탈리아",
        "year": 2019
    }
]

@app.get("/wine")
async def filter_wine(
    name: Optional[str] = Query(None, description="와인 이름"),
    type: Optional[str] = Query(None, description="와인 종류"),
    max_price: int = Query(..., gt=0, description="최대 가격"),
    origin: Optional[str] = Query(None, description="원산지"),
    year: Optional[int] = Query(None, description="생산 년도")
):
    results = []
    for wine in wines:
        if (
            (name is None or wine["name"].lower() == name.lower()) and
            (type is None or wine["type"].lower() == type.lower()) and
            (wine["price"] <= max_price) and
            (origin is None or wine["origin"].lower() == origin.lower()) and
            (year is None or wine["year"] == year)
        ):
            results.append(wine)
    return results

hanok_h = [
    {
        "상호명": "잊음",
        "주소": "경상남도 통영시 충렬4길 33-5",
        "가격": "190000",
        "설명": "본채, 앞마당, 뒷마당을 독채로 사용할 수 있다.",
        "예약가능여부": True,
        "요리가능여부": True,
        "연락처": "010-0000-0001"
    },
    {
        "상호명": "북설악황토마을",
        "주소": "강원도 인제군 북면 황태길 333",
        "가격": "210000",
        "설명": "전통 양식인 너와를 얹은 산돌너와집을 비롯해 방문객의 건강을 생각한 황토너와집, 황토집 등이 있다.",
        "예약가능여부": False,
        "요리가능여부": True,
        "연락처": "010-0000-0002"
    },
    {
        "상호명": "다락",
        "주소": "전라북도 전주시 완산구 경기전길 57-6",
        "가격": "200000",
        "설명": "귀여운 다락방을 갖춘 전주 한옥마을 내 한옥 숙소. 객실에는 투숙객만을 위한 작은 카페 공간이 있다.",
        "예약가능여부": True,
        "요리가능여부": False,
        "연락처": "010-0000-0003"
    },
    {
        "상호명": "군위남천고택",
        "주소": "경상북도 군위군 부계면 한밤5길 19",
        "가격": "160000",
        "설명": "민속문화재로 선정된 남천고택은 1836년경에 지어진 마을에서 가장 큰 집이다. 미식 체험도 할 수 있다.",
        "예약가능여부": True,
        "요리가능여부": False,
        "연락처": "010-0000-0004"
    },
    {
        "상호명": "정재종택",
        "주소": "경상북도 안동시 임동면 경동로 2661-8",
        "가격": "180000",
        "설명": "퇴계 이황의 학문을 계승한 정재 류치명 선생의 고택이다. 오래된 만큼 조선시대 주거문화를 어느 곳보다 잘 간직하고 있다.",
        "예약가능여부": True,
        "요리가능여부": True,
        "연락처": "010-0000-0005"
    }
]

@app.get("/hanok_h")
async def search_hanok_h(
    상호명: Optional[str] = Query(None, description="검색하고자 하는 상호의 이름"),
    지역: str = Query(..., description="검색하고자 하는 지역 이름(서울시, 금천구, 창원시 등)"),
    최소가격: Optional[int] = Query(None, gt=0, description="숙소의 최소 가격(1박, 원화 기준)"),
    최대가격: Optional[int] = Query(None, description="숙소의 최대 가격(1박, 원화 기준)"),
    예약가능여부: Optional[bool] = Query(None, description="현재 예약 가능 여부(true 또는 false)"),
    요리가능여부: Optional[bool] = Query(None, description="숙소 내 요리 가능 여부(true 또는 false)"),
    설명: Optional[str] = Query(None, description="설명을 기준으로 검색")
):
    results = []
    for h in hanok_h:
        if (
            (상호명 is None or h["상호명"].lower() == 상호명.lower()) and
            (h["주소"].find(지역) != -1) and
            (최소가격 is None or int(h["가격"]) >= 최소가격) and
            (최대가격 is None or int(h["가격"]) <= 최대가격) and
            (예약가능여부 is None or h["예약가능여부"] == 예약가능여부) and
            (요리가능여부 is None or h["요리가능여부"] == 요리가능여부) and
            (설명 is None or h["설명"].lower().find(설명.lower()) != -1)
        ):
            results.append(h)
    return results

p_naengmyeon = [
    {
        "상호명": "남포면옥",
        "주소": "서울시 중구 을지로3길 24",
        "가격": "15000",
        "주차가능여부": False,
        "설명": "평양식 냉면, 어복쟁반, 전 요리를 전문으로 한다.",
        "연락처": "010-0000-0001"
    },
    {
        "상호명": "우래옥",
        "주소": "서울시 중구 창경궁로 62-29",
        "가격": "21000",
        "주차가능여부": True,
        "설명": "대표 메뉴는 전통 평양냉면과 불고기. 1926년에 개업했다",
        "연락처": "010-0000-0002"
    },
    {
        "상호명": "정인면옥",
        "주소": "서울시 영등포구 국회대로76길 10 기독교침례회총회빌딩 1층",
        "가격": "20000",
        "주차가능여부": True,
        "설명": "아롱사태 수육, 암퇘지 편육과 접시 만두가 대표메뉴.",
        "연락처": "010-0000-0003"
    },
    {
        "상호명": "진미평양냉면",
        "주소": "서울시 강남구 학동로 305-3",
        "가격": "22000",
        "주차가능여부": True,
        "설명": "편육, 제육, 불고기 같은 냉면집 단골 메뉴를 비롯해 접시 만두와 어복쟁반, 온면도 맛볼 수 있다.",
        "연락처": "010-0000-0004"
    },
    {
        "상호명": "필동면옥",
        "주소": "서울시 중구 서애로 26",
        "가격": "19000",
        "주차가능여부": False,
        "설명": "두툼하면서도 부드럽고 촉촉한 돼지 수육은 이 집의 또 다른 명물이다.",
        "연락처": "010-0000-0005"
    }
]

@app.get("/p_naengmyeon")
async def search_p_naengmyeon(
    상호명: Optional[str] = Query(None, description="검색하고자 하는 상호의 이름"),
    지역: str = Query(..., description="검색하고자 하는 지역 이름(서울시, 금천구, 창원시 등)"),
    최소가격: Optional[int] = Query(None, gt=0, description="검색하고자 하는 최소 가격(원화 기준)"),
    최대가격: Optional[int] = Query(None, description="검색하고자 하는 최대 가격(원화 기준)"),
    주차가능여부: Optional[bool] = Query(None, description="주차 가능 여부(true 또는 false)"),
    설명: Optional[str] = Query(None, description="설명을 기준으로 검색")
):
    results = []
    for p in p_naengmyeon:
        if (
            (상호명 is None or p["상호명"].lower() == 상호명.lower()) and
            (p["주소"].find(지역) != -1) and
            (최소가격 is None or int(p["가격"]) >= 최소가격) and
            (최대가격 is None or int(p["가격"]) <= 최대가격) and
            (주차가능여부 is None or p["주차가능여부"] == 주차가능여부) and
            (설명 is None or p["설명"].lower().find(설명.lower()) != -1)
        ):
            results.append(p)
    return results

stollen = [
    {
        "상호명": "메종엠오",
        "주소": "서울시 서초구 방배로26길 22 1층 코너",
        "가격": "50000",
        "주차가능여부": False,
        "설명": "마들렌 반죽에 다양한 건과일, 마지팬을 넣어 구운 후 버터에 적시고 올스파이스 슈거로 코팅해 묵직하면서도 건과일의 향긋함, 스파이스의 향기, 달콤함이 복합적으로 느껴지는 맛이 매력적이다.",
        "연락처": "010-0000-0001"
    },
    {
        "상호명": "우스블랑",
        "주소": "서울시 용산구 효창원로70길 4",
        "가격": "48000",
        "주차가능여부": True,
        "설명": "1년 동안 코냑에 숙성시킨 견과류와 건조 과일, 분할을 한 반죽에 꼬냑을 넣은 마지판이 들어가는 우스블랑의 슈톨렌은 코냑 향이 강하다.",
        "연락처": "010-0000-0002"
    },
    {
        "상호명": "쉐즈롤",
        "주소": "경기도 양평군 서종면 낙촌길 7-7",
        "가격": "45000",
        "주차가능여부": True,
        "설명": "겨울을 닮은 아몬드의 깊은 향을 좋아하는 사람은 ‘아몬드 마지팬 슈톨렌’을, 입안에 은은하게 남는 고소한 맛과 피스타치오 향을 좋아하는 사람은 ‘피스타치오 마지팬 슈톨렌’을 고르면 된다.",
        "연락처": "010-0000-0003"
    },
    {
        "상호명": "앨리스",
        "주소": "서울시 서초구 양재천로 107-4 1층",
        "가격": "39000",
        "주차가능여부": True,
        "설명": "건포도와 건크랜베리를 스파이스럼과 바닐라 빈을 함께 넣고 절인 건과일 절임과 아몬드, 헤이즐넛, 호두를 넣고 만든 반죽 가운데 아몬드 가루와 계란 흰자로 반죽한 마지팬이 들어가 부드러우면서도 다채로운 향과 맛을 느낄 수 있다.",
        "연락처": "010-0000-0004"
    },
    {
        "상호명": "브라더후드",
        "주소": "제주도 서귀포시 월드컵로 8",
        "가격": "51000",
        "주차가능여부": False,
        "설명": "6가지 건과일을 1년 동안 다크 럼에 절여 시간이 지날수록 특유의 다크 럼 향이 베어 향신료과 조화를 이루며 화려한 맛을 자랑한다.",
        "연락처": "010-0000-0005"
    }
]

@app.get("/stollen")
async def search_stollen(
    상호명: Optional[str] = Query(None, description="검색하고자 하는 상호의 이름"),
    지역: str = Query(..., description="검색하고자 하는 지역 이름(서울시, 금천구, 창원시 등)"),
    최소가격: Optional[int] = Query(None, gt=0, description="검색하고자 하는 최소 가격(원화 기준)"),
    최대가격: Optional[int] = Query(None, description="검색하고자 하는 최대 가격(원화 기준)"),
    주차가능여부: Optional[bool] = Query(None, description="주차 가능 여부(true 또는 false)"),
    설명: Optional[str] = Query(None, description="설명을 기준으로 검색")
):
    results = []
    for s in stollen:
        if (
            (상호명 is None or s["상호명"].lower() == 상호명.lower()) and
            (s["주소"].find(지역) != -1) and
            (최소가격 is None or int(s["가격"]) >= 최소가격) and
            (최대가격 is None or int(s["가격"]) <= 최대가격) and
            (주차가능여부 is None or s["주차가능여부"] == 주차가능여부) and
            (설명 is None or s["설명"].lower().find(설명.lower()) != -1)
        ):
            results.append(s)
    return results

dog_campsites = [
    {
        "상호명": "청산리 오토캠핑장",
        "주소": "충청남도 태안군 원북면 청산길 279",
        "가격": "45000",
        "반려견시설종류": ["수영장", "드라이룸"],
        "설명": "해돋이를 볼 수 있는 서해안의 캠핑장.",
        "연락처": "00-000-0001"
    },
    {
        "상호명": "의성펫월드",
        "주소": "경상북도 의성군 단북면 안계길 255-13",
        "가격": "47000",
        "반려견시설종류": ["수영장", "드라이룸"],
        "설명": "반려견 카페를 포함한 의성의 펫월드.",
        "연락처": "00-000-0002"
    },
    {
        "상호명": "국립화천숲속야영장",
        "주소": "강원도 화천군 간동면 배후령길 1144 화천숲속야영장",
        "가격": "21000",
        "반려견시설종류": ["수영장", "샤워공간"],
        "설명": "캠핑장 이름처럼 숲속에 위치해 산책로 조성이 잘 되어 있다.",
        "연락처": "00-000-0003"
    },
    {
        "상호명": "햇살가득애견캠핑장",
        "주소": "경기도 남양주시 수동면 비룡로 1742번길 36-104",
        "가격": "50000",
        "반려견시설종류": ["샤워공간", "펜스놀이장"],
        "설명": "대형견과 소형견이 마주치지 않도록 공간이 나뉘어 있으며 강아지 성향에 따라 개별 펜스가 설치된 곳을 고를 수도 있다.",
        "연락처": "00-000-0004"
    },
    {
        "상호명": "개똥이네",
        "주소": "강원도 홍천군 북방면 원소길 25",
        "가격": "49000",
        "반려견시설종류": ["샤워공간"],
        "설명": "천연 잔디가 깔려있다. 주변 환경을 잘 관리해 두어 강아지가 마음껏 뛰어도 된다.",
        "연락처": "00-000-0005"
    }
]

@app.get("/dog_campsite")
async def search_dog_campsite(
    상호명: Optional[str] = Query(None, description="검색하고자 하는 상호의 이름"),
    지역: str = Query(..., description="검색하고자 하는 지역 이름(서울시, 금천구, 창원시 등)"),
    최소가격: Optional[int] = Query(None, gt=0, description="검색하고자 하는 최소 가격(원화 기준)"),
    최대가격: Optional[int] = Query(None, description="검색하고자 하는 최대 가격(원화 기준)"),
    반려견시설종류: Optional[str] = Query(None, description="반려견 시설 종류(예: 수영장, 드라이룸, 샤워공간, 펜스놀이장 등)"),
    설명: Optional[str] = Query(None, description="설명을 기준으로 검색")
):
    results = []
    for campsite in dog_campsites:
        if (
            (상호명 is None or campsite["상호명"].lower() == 상호명.lower()) and
            (campsite["주소"].find(지역) != -1) and
            (최소가격 is None or int(campsite["가격"]) >= 최소가격) and
            (최대가격 is None or int(campsite["가격"]) <= 최대가격) and
            (반려견시설종류 is None or 반려견시설종류 in campsite["반려견시설종류"]) and
            (설명 is None or campsite["설명"].lower().find(설명.lower()) != -1)
        ):
            results.append(campsite)
    return results

greenhouse_list = [
    {
        "상호명": "서울식물원",
        "주소": "서울시 강서구 마곡동로 161",
        "입장료": "5000",
        "주차가능여부": True,
        "설명": "이곳의 오목한 접시 모양의 온실은 열대관과 지중해관으로 구성돼 있고, 세계 12개 도시의 특색 있는 식물들을 볼 수 있다.",
        "인스타그램": "@seoulbotanicpark_official"
    },
    {
        "상호명": "국립세종수목원",
        "주소": "세종시 연기면 수목원로 136",
        "입장료": "5000",
        "주차가능여부": True,
        "설명": "온대 중부권역의 대표하는 붓꽃을 모티브로 디자인된 사계절 온실 역시 축구장 1.5배의 면적으로 국내 식물 전시 유리온실 중 최대 규모를 자랑한다.",
        "인스타그램": "@sjnagreen"
    },
    {
        "상호명": "경주 동궁원",
        "주소": "경상북도 경주시 보문로 74-14",
        "입장료": "9000",
        "주차가능여부": True,
        "설명": "우리나라 최초의 동식물원이었던 동궁과 월지를 현대적으로 재현한 곳이다. 한옥의 지붕과 처마를 살린 신라시대 전통 건축 양식의 유리온실이다.",
        "인스타그램": "@gyeongju_epg"
    },
    {
        "상호명": "거제식물원",
        "주소": "경상남도 거제시 거제면 거제남서로 3595",
        "입장료": "9800",
        "주차가능여부": True,
        "설명": "7,400여 장의 유리 삼각형 유리를 이어붙인 정글돔은 약 4,468제곱미터 면적에 최고 높이 30미터로 돔형 유리온실로는 국내 최대 규모다.",
        "인스타그램": "@botanicpark_official"
    },
    {
        "상호명": "여미지식물원",
        "주소": "제주도 서귀포시 중문관광로 93",
        "입장료": "12000",
        "주차가능여부": True,
        "설명": "중문 관광 단지에 위치한 아름다운 땅이란 뜻의 여미지식물원은 동양 최대의 온실을 지니고 있다.",
        "인스타그램": "@yeomiji_botanic_garden"
    }
]

@app.get("/greenhouse")
async def search_greenhouse(
    이름: Optional[str] = Query(None, description="검색하고자 하는 식물원의 이름"),
    지역: str = Query(..., description="검색하고자 하는 지역 이름(서울시, 금천구, 창원시 등)"),
    최소입장료: Optional[int] = Query(None, gt=0, description="검색하고자 하는 최소 입장료(원화 기준)"),
    최대입장료: Optional[int] = Query(None, description="검색하고자 하는 최대 입장료(원화 기준)"),
    주차가능여부: Optional[bool] = Query(None, description="주차 가능 여부(true 또는 false)"),
    설명: Optional[str] = Query(None, description="설명을 기준으로 검색")
):
    results = []
    for greenhouse in greenhouse_list:
        if (
            (이름 is None or greenhouse["상호명"].lower() == 이름.lower()) and
            (greenhouse["주소"].find(지역) != -1) and
            (최소입장료 is None or int(greenhouse["입장료"]) >= 최소입장료) and
            (최대입장료 is None or int(greenhouse["입장료"]) <= 최대입장료) and
            (주차가능여부 is None or greenhouse["주차가능여부"] == 주차가능여부) and
            (설명 is None or greenhouse["설명"].lower().find(설명.lower()) != -1)
        ):
            results.append(greenhouse)
    return results

outdoor_wedding_list = [
    {
        "상호명": "라비두스",
        "주소": "서울 중구 필동3가 62-15",
        "수용규모": 400,
        "설명": "하우스 웨딩, 테라스 웨딩, 야외 웨딩 세 가지가 동시에 모두 가능한 곳으로 접근성이 좋은 충무로에 위치해 있어 도심 속 대저택에서 결혼식을 하는 듯한 느낌을 줄 수 있다.",
        "홈페이지": "laviedouce.co.kr"
    },
    {
        "상호명": "엘리스몽드",
        "주소": "서울 용산구 이태원동 258-87",
        "수용규모": 200,
        "설명": "탁 트인 조망을 원하는 신랑,신부에게 최적의 장소이자 이곳 역시 남산 인근에 위치해있어 접근성이 뛰어나다. 뿐만 아니라 실내 공간도 함께 겸하고 있기 때문에 날씨에 대비할 수 있다.",
        "홈페이지": "alicemonde.co.kr"
    },
    {
        "상호명": "두가헌",
        "주소": "서울 종로구 삼청로 14 현대갤러리",
        "수용규모": 86,
        "설명": "1900년에 지어진 고택, 근대 러시아식 벽돌 건물인 갤러리와 함께 있어 우아한 한옥 건물이다. 한옥 스몰 웨딩을 꿈꾸는 커플에게 추천한다.",
        "홈페이지": "dugahun.com"
    },
    {
        "상호명": "한국의집",
        "주소": "서울 중구 퇴계로36길 10",
        "수용규모": 300,
        "설명": "남산 자락에 위치한 한국의집은 1957년 개관, 1982년부터 전통혼례를 진행해 온 곳이다. 연지,곤지 바르고 한복을 입고 조선 방식으로 혼례를 치뤄보고 싶은 커플에게 추천한다. 사물놀이 공연과 부채춤도 함께할 수 있다.",
        "홈페이지": "linktr.ee/koreahouse1957"
    },
    {
        "상호명": "보넬리가든",
        "주소": "서울 서초구 샘마루길 11",
        "수용규모": 500,
        "설명": "강남구 서초에 위치해 있어 강남 혹은 경기권 커플들이 선호할 식장. 더군다나 호젓한 산 속의 숲에 위치해있어 도심의 분위기가 전혀 나지 않는다. 넓은 주차 공간을 확보하고 있어 편리하다.",
        "홈페이지": "linktr.ee/koreahouse1957"
    }
]

@app.get("/outdoor_wedding")
async def search_outdoor_wedding(
    상호명: Optional[str] = Query(None, description="검색하고자 하는 상호의 이름"),
    지역구: Optional[str] = Query(None, description="검색하고자 하는 구 이름(금천구, 강동구 등)"),
    최소수용규모: int = Query(..., gt=0, description="검색하고자 하는 최소 수용규모(명수 기준)"),
    최대수용규모: Optional[int] = Query(None, description="검색하고자 하는 최대 수용규모(명수 기준)"),
    설명: Optional[str] = Query(None, description="설명을 기준으로 검색")
) -> List[dict]:
    results = []
    for wedding in outdoor_wedding_list:
        if (
            (상호명 is None or wedding["상호명"].lower() == 상호명.lower()) and
            (지역구 is None or wedding["주소"].find(지역구) != -1) and
            (int(wedding["수용규모"]) >= 최소수용규모) and
            (최대수용규모 is None or int(wedding["수용규모"]) <= 최대수용규모) and
            (설명 is None or wedding["설명"].lower().find(설명.lower()) != -1)
        ):
            results.append(wedding)
    return results

zero_waste_shop_list = [
    {
        "상호명": "덕분애",
        "주소": "서울시 서초구 서초대로 389 209호",
        "샵분류": "리필샵",
        "서울시인증여부": True,
        "설명": "취급품목: 대나무밴드, 고체치약, 대나무칫솔, 천연수세미 리필스테이션 외",
        "연락처": "02-6959-4479"
    },
    {
        "상호명": "지구샵",
        "주소": "서울시 마포구 성미산로 155",
        "샵분류": "리필샵",
        "서울시인증여부": True,
        "설명": "취향에 맞춘 향수를 직접 만들고 리필할 수 있습니다. (지정 용기에 한해 재사용 가능)",
        "연락처": "070-7721-5748"
    },
    {
        "상호명": "굿바이마켓",
        "주소": "서울시 용산구 서빙고로 17",
        "샵분류": "친환경생필품점",
        "서울시인증여부": False,
        "설명": "취급품목: 식품, 패션잡화, 리필스테이션, 청소용품 등",
        "연락처": "070-4369-5982"
    },
    {
        "상호명": "자연상점",
        "주소": "서울시 은평구 통일로 684",
        "샵분류": "식당",
        "서울시인증여부": True,
        "설명": "병뚜껑,생수병 수거 후 업사이클 제품 제작, 무포장 원칙이나 필요시 종이봉투 재활용",
        "연락처": "02-2039-9631"
    },
    {
        "상호명": "칸틴커피대치",
        "주소": "강남구 테헤란로114길 38",
        "샵분류": "카페",
        "서울시인증여부": False,
        "설명": "다회용 컵 무인반납기 설치",
        "연락처": "02-568-1066"
    }
]

@app.get("/s_zero_waste_s")
async def search_zero_waste_shop(
    상호명: Optional[str] = Query(None, description="검색하고자 하는 상호의 이름"),
    지역구: Optional[str] = Query(None, description="검색하고자 하는 구 이름(금천구, 강동구 등)"),
    샵분류: str = Query(..., description="상점의 분류(예: 리필샵, 친환경생필품점, 식당, 카페, 기타 등)"),
    서울시인증여부: Optional[bool] = Query(None, description="서울시 인증 여부, 서울시 제로마켓(true 또는 false)"),
    설명: Optional[str] = Query(None, description="설명을 기준으로 검색")
) -> List[dict]:
    results = []
    for shop in zero_waste_shop_list:
        if (
            (상호명 is None or shop["상호명"].lower() == 상호명.lower()) and
            (지역구 is None or shop["주소"].find(지역구) != -1) and
            (shop["샵분류"].lower() == 샵분류.lower()) and
            (서울시인증여부 is None or shop["서울시인증여부"] == 서울시인증여부) and
            (설명 is None or shop["설명"].lower().find(설명.lower()) != -1)
        ):
            results.append(shop)
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
    min_download: Optional[int] = Query(None, description="최소 다운로드 수"),
    max_download: Optional[int] = Query(None, description="최대 다운로드 수"),
    type: Optional[str] = Query(None, description="글꼴 타입"),
    min_font_weight: Optional[int] = Query(None, description="최소 굵기 수", gt=0),
    max_font_weight: Optional[int] = Query(None, description="최대 굵기 수", gt=0)
):
    filtered_fonts = []
    # 주어진 데이터를 리스트 형태로 정의
    data = [
        ["나눔스퀘어", "고딕", 4, 467000, "반듯한 직선으로 제목에 잘 어울리며 모바일에서도 잘 보이는 글꼴입니다."],
        ["나눔고딕", "고딕", 4, 564000, "나눔고딕은 문서의 본문에도 잘 쓸 수 있는 고딕 글꼴입니다. 글자 끝의 날카로운 부분을 둥글게 처리해 친근하고 부드러운 느낌입니다."],
        ["나눔손글씨 펜", "손글씨", 1, 143000, "나눔손글씨 펜체는 깔끔한 선 처리와 생동감이 돋보입니다."],
        ["주아체", "고딕", 1, 275000, "배달의민족 주아체는 붓으로 직접 그려서 만든 손글씨 간판을 모티브로 만들었습니다. 붓으로 그려 획의 굵기가 일정하지 않고 동글동글한 느낌을 주는 서체로 옛날 간판의 푸근함과 정겨움이 묻어나는 것이 특징입니다."],
        ["강원교육모두체", "명조", 2, 408000, "강원도교육청의 공식 서체입니다."],
        ["빙그레체", "손글씨", 2, 56100, "빙그레체는 '건강, 행복, 미소'의 컨셉이 담긴 서체로 빙그레 '바나나맛 우유' 로고 타입에서 착안하여 현대적으로 디자인 되었습니다."]
    ]
    
    # 필터링 조건에 맞는 글꼴 찾기
    for font in data:
        if (name is None or name == font[0]) and \
            (min_download is None or font[3] >= min_download) and \
            (max_download is None or font[3] <= max_download) and \
            (type is None or type == font[1]) and \
            (min_font_weight is None or font[2] >= min_font_weight) and \
            (max_font_weight is None or font[2] <= max_font_weight):
            
            filtered_fonts.append({
                "name": font[0],
                "download": font[3],
                "type": font[1],
                "font_weight": font[2],
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
        "spicy": 2,
        "rating": 4.5
    },
    {
        "menu": "간장궁중떡볶이",
        "price": 5000,
        "calories": 900,
        "spicy": 1,
        "rating": 4
    },
    {
        "menu": "매운떡볶이",
        "price": 5000,
        "calories": 800,
        "spicy": 4,
        "rating": 3
    },
    {
        "menu": "크림떡볶이",
        "price": 13000,
        "calories": 900,
        "spicy": 1,
        "rating": 4
    },
    {
        "menu": "로제떡볶이",
        "price": 12000,
        "calories": 750,
        "spicy": 2,
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
        "price": 49500,
        "avaliable_seat": 15
    },
    {
        "date": "20230628",
        "departure": "서울",
        "arrival": "목포",
        "seat": "일반실",
        "price": 48500,
        "avaliable_seat": 20
    },
    {
        "date": "20230705",
        "departure": "수원",
        "arrival": "강릉",
        "seat": "특/우등",
        "price": 49000,
        "avaliable_seat": 2
    },
    {
        "date": "20230726",
        "departure": "서울",
        "arrival": "부산",
        "seat": "특/우등",
        "price": 65500,
        "avaliable_seat": 10
    },
    {
        "date": "20230731",
        "departure": "서울",
        "arrival": "양양",
        "seat": "일반실",
        "price": 22500,
        "avaliable_seat": 20
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


@app.get("/hairshop")
async def search_hair_shop(
    shop_name: str = Query(None, description="미용실명"),
    min_price: int = Query(None, description="최소 가격", ge=0),
    max_price: int = Query(None, description="최대 가격", ge=0),
    hair_type: str = Query(None, description="헤어종류 (ex. 볼륨매직, 펌, 스트레이트펌, 커트 등)"),
    region: str = Query(None, description="지역"),
    holiday: str = Query(None, description="공휴일 영업"),
):
    # 미용실 정보 데이터
    hairshops = [
        {"shop_name": "이노헤어", "price": 300000, "hair_type": "염색", "region": "서울 서대문구", "hairdresser_count": 5, "operation_date": "화-토", "operation_time": "10:00-20:00"},
        {"shop_name": "이노헤어", "price": 140000, "hair_type": "염색", "region": "서울 광진구", "hairdresser_count": 6, "operation_date": "화-토", "operation_time": "10:00-20:00"},
        {"shop_name": "롱롱위캔드", "price": 35000, "hair_type": "커트", "region": "서울 서대문구", "hairdresser_count": 2, "operation_date": "화-토", "operation_time": "11:00-20:00"},
        {"shop_name": "박승철", "price": 300000, "hair_type": "볼륨매직", "region": "서울 은평구", "hairdresser_count": 5, "operation_date": "화-일", "operation_time": "10:00-20:00"},
        {"shop_name": "레드샵", "price": 200000, "hair_type": "영양", "region": "서울 서대문구", "hairdresser_count": 3, "operation_date": "월-일", "operation_time": "12:00-20:00"},
    ]

    filtered_hairshops = []

    for hairshop in hairshops:
        if (
            (hairshop["shop_name"] == shop_name if shop_name else True) and
            (hairshop["min_price"] is None or (hairshop["price"] >= min_price if min_price else True)) and
            (hairshop["max_price"] is None or (hairshop["price"] <= max_price if max_price else True)) and
            (hairshop["hair_type"] == hair_type if hair_type else True) and
            (hairshop["region"] == region if region else True) and
            (hairshop["holiday"] == holiday if holiday else True)
        ):
            filtered_hairshops.append(hairshop)

    return filtered_hairshops

@app.get("/bag")
async def search_bag(
    brand: str = Query(None, description="브랜드명"),
    min_price: int = Query(None, description="최소 가격", ge=0),
    max_price: int = Query(None, description="최대 가격", ge=0),
    color: str = Query(None, description="색깔"),
    bag_type: str = Query(None, description="종류, ex) 백팩, 핸드백"),
    store: str = Query(None, description="판매처"),
    purchase_age: str = Query(None, description="구매 나이대"),
):
    # 가방 정보 데이터
    bags = [
        {"brand": "나이키", "price": 79000, "color": "검정", "bag_type": "백팩", "discount": "5%", "store": "무신사"},
        {"brand": "히어리", "price": 88200, "color": "실버", "bag_type": "핸드백", "discount": "10%", "store": "29cm"},
        {"brand": "레니비", "price": 39000, "color": "아이보리", "bag_type": "백팩", "discount": "20%", "store": "29cm"},
        {"brand": "스컬프터", "price": 112000, "color": "검정", "bag_type": "백", "discount": "10%", "store": "무신사"},
        {"brand": "퐁실구름크로스백", "price": 30000, "color": "아이보리", "bag_type": "크로스백", "discount": "0%", "store": "98도씨"},
    ]

    filtered_bags = []

    for bag in bags:
        if (
            (bag["brand"] == brand if brand else True) and
            (bag["min_price"] is None or (bag["price"] >= min_price if min_price else True)) and
            (bag["max_price"] is None or (bag["price"] <= max_price if max_price else True)) and
            (bag["color"] == color if color else True) and
            (bag["bag_type"] == bag_type if bag_type else True) and
            (bag["store"] == store if store else True) and
            (bag["purchase_age"] == purchase_age if purchase_age else True)
        ):
            filtered_bags.append(bag)

    return filtered_bags

@app.get("/baseballplayer")
async def search_baseball_player(
    team: str = Query(None, description="소속팀"),
    uniform_number: int = Query(None, description="등번호"),
    position: str = Query(None, description="포지션명"),
    age: int = Query(None, description="나이"),
    name: str = Query(None, description="이름"),
):
    # 야구 선수 정보 데이터
    baseball_players = [
        {"team": "한화이글스", "uniform_number": 64, "position": "내야수", "debut_year": 2023, "age": 20, "name": "문현빈"},
        {"team": "한화이글스", "uniform_number": 22, "position": "내야수", "debut_year": 2009, "age": 35, "name": "채은성"},
        {"team": "두산베어스", "uniform_number": 25, "position": "포수", "debut_year": 2009, "age": 38, "name": "양의지"},
        {"team": "키움히어로즈", "uniform_number": 3, "position": "내야수", "debut_year": 2017, "age": 25, "name": "김혜성"},
        {"team": "키움히어로즈", "uniform_number": 51, "position": "외야수", "debut_year": 2017, "age": 26, "name": "이정후"},
    ]

    filtered_players = []

    for player in baseball_players:
        if (
            (player["team"] == team if team else True) and
            (player["uniform_number"] == uniform_number if uniform_number else True) and
            (player["position"] == position if position else True) and
            (player["age"] == age if age else True) and
            (player["name"] == name if name else True)
        ):
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
        "예약가능여부": False,
        "이용후기": "친절하세요.",
        "연락처": "010-7320-4633"
    },
    {
        "시터이름": "성재숙",
        "이용가능지역": "제주시",
        "가격": "65000",
        "평점": 4.2,
        "예약가능여부": True,
        "이용후기": "상냥하세요.",
        "연락처": "010-6252-1750"
    },
    {
        "시터이름": "손주연",
        "이용가능지역": "관악구",
        "가격": "50000",
        "평점": 4.5,
        "예약가능여부": True,
        "이용후기": "꼼꼼하시네요.",
        "연락처": "010-4894-5996"
    },
    {
        "시터이름": "서미연",
        "이용가능지역": "진안군",
        "가격": "52000",
        "평점": 3.0,
        "예약가능여부": True,
        "이용후기": "시간 약속을 잘 지키지 않으세요.",
        "연락처": "010-5982-6146"
    },
    {
        "시터이름": "배원태",
        "이용가능지역": "담양군",
        "가격": "60000",
        "평점": 4.8,
        "예약가능여부": True,
        "이용후기": "아주 만족스러워요.",
        "연락처": "010-1904-6208"
    }
]

@app.get("/catsitter")
async def filter_catsitters(
    sitter_name: str = Query(None, description="검색하고자 하는 시터의 이름"),
    location: str = Query(None, description="이용하고자 하는 지역의 시, 군, 구 이름 ex) 성남시, 진안군, 강남구 등"),
    min_price: int = Query(None, description="가격의 최소치"),
    max_price: int = Query(None, description="가격의 최대치"),
    min_rating: float = Query(None, description="검색하고자 하는 최소 평점"),
    max_rating: float = Query(None, description="검색하고자 하는 최대 평점"),
    available: bool = Query(None, description="현재 예약이 가능한지 여부"),
):
    # 캣시터 정보 데이터
    catsitters = [
        ["오경원", "성남시", 48000, 5.0, False, "친절하세요.", "010-7320-4633"],
        ["성재숙", "제주시", 65000, 4.2, True, "상냥하세요.", "010-6252-1750"],
        ["손주연", "관악구", 50000, 4.5, True, "꼼꼼하시네요.", "010-4894-5996"],
        ["서미연", "진안군", 52000, 3.0, True, "시간 약속을 잘 지키지 않으세요.", "010-5982-6146"],
        ["배원태", "담양군", 60000, 4.8, True, "아주 만족스러워요.", "010-1904-6208"],
    ]

    filtered_catsitters = []

    for catsitter in catsitters:
        if (
            (catsitter[0] == sitter_name if sitter_name else True) and
            (catsitter[1] == location if location else True) and
            (catsitter[2] >= min_price if min_price else True) and
            (catsitter[2] <= max_price if max_price else True) and
            (catsitter[3] >= min_rating if min_rating else True) and
            (catsitter[3] <= max_rating if max_rating else True) and
            (catsitter[4] == available if available is not None else True)
        ):
            filtered_catsitters.append({
                "sitter_name": catsitter[0],
                "location": catsitter[1],
                "price": catsitter[2],
                "rating": catsitter[3],
                "available": catsitter[4],
                "review": catsitter[5],
                "tel": catsitter[6]
            })

    return filtered_catsitters

@app.get("/dogsitter")
async def filter_dogsitters(
    name: str = Query(None, description="검색하고자 하는 도그워커의 이름"),
    location: str = Query(None, description="이용하고자 하는 지역의 시, 군, 구 이름 ex) 성남시, 진안군, 강남구 등"),
    gradeLowerLimit: float = Query(None, description="검색하고자 하는 최소 평점"),
    gradeUpperLimit: float = Query(None, description="검색하고자 하는 최대 평점"),
    reservable: bool = Query(None, description="현재 예약이 가능한지 여부"),
):
    # 도그워커 정보 데이터
    dogsitters = [
        ["오경원", "성남시", 48000, 5.0, False, "친절하세요.", "010-7320-4633"],
        ["성재숙", "제주시", 65000, 4.2, True, "상냥하세요.", "010-6252-1750"],
        ["손주연", "관악구", 50000, 4.5, True, "꼼꼼하시네요.", "010-4894-5996"],
        ["서미연", "진안군", 52000, 3.0, True, "시간 약속을 잘 지키지 않으세요.", "010-5982-6146"],
        ["배원태", "담양군", 60000, 4.8, True, "아주 만족스러워요.", "010-1904-6208"],
    ]

    filtered_dogsitters = []

    for dogsitter in dogsitters:
        if (
            (dogsitter[0] == name if name else True) and
            (dogsitter[1] == location if location else True) and
            (dogsitter[4] >= gradeLowerLimit if gradeLowerLimit else True) and
            (dogsitter[4] <= gradeUpperLimit if gradeUpperLimit else True) and
            (dogsitter[4] == reservable if reservable is not None else True)
        ):
            filtered_dogsitters.append({
                "name": dogsitter[0],
                "location": dogsitter[1],
                "price": dogsitter[2],
                "grade": dogsitter[3],
                "reservable": dogsitter[4],
                "review": dogsitter[5],
                "phone": dogsitter[6]
            })

    return filtered_dogsitters

@app.get("/webtoon_search")
async def filter_webtoons(
    title: str = Query(None, description="검색하고자 하는 웹툰의 작품 이름"),
    writerNm: str = Query(None, description="검색하고자 하는 웹툰의 작가 이름"),
    platform: str = Query(None, description="검색하고자 하는 웹툰의 연재 플랫폼"),
    genre: str = Query(None, description="검색하고자 하는 웹툰의 장르 ex) 판타지, 액션, 일상, 스릴러, 개그, 드라마, 무협 등"),
    ageLimit: str = Query(None, description="이용가능연령 ex) 전체이용가, 12세이상, 15세이상, 18세이상"),
    status: str = Query(None, description="작품의 상태"),
):
    # 웹툰 정보 데이터
    webtoons = [
        ["즐거우리인생", "현미씨", "네이버웹툰", "일상", "전체이용가", "완결"],
        ["마라샹궈매직", "쉐프님", "네이버웹툰", "개그", "전체이용가", "연재중"],
        ["카드값을숨김", "유리쿠쿠다스", "카카오페이지", "스릴러", "15세이상", "연재중"],
        ["호박고구마", "김상무상무", "만화경", "드라마", "12세이상", "휴재중"],
        ["아미산귀환", "소인배점소이", "레진코믹스", "무협", "18세이상", "연재중"],
    ]

    filtered_webtoons = []

    for webtoon in webtoons:
        if (
            (webtoon[0] == title if 작품명 else True) and
            (webtoon[1] == writerNm if 작가명 else True) and
            (webtoon[2] == platform if 연재플랫폼 else True) and
            (webtoon[3] == genre if 장르 else True) and
            (webtoon[4] == ageLimit if 이용가능연령 else True) and
            (webtoon[5] == status if status else True)
        ):
            filtered_webtoons.append({
                "title": webtoon[0],
                "writerNm": webtoon[1],
                "platform": webtoon[2],
                "genre": webtoon[3],
                "ageLimit": webtoon[4],
                "status": webtoon[5]
            })

    return filtered_webtoons


@app.get("/seoul_park")
async def filter_seoul_parks(
    parkNm: str = Query(None, description="조회하고자 하는 공원의 이름"),
    seoulGu: str = Query(None, description="조회하고자 하는 구 이름 ex)은평구, 서초구, 마포구 등"),
    facility: str = Query(None, description="공원 내 주요 시설 ex) 캠핑장, 배드민턴장, 잔디쉼터 등"),
    areaNarrowest: int = Query(None, description="찾고자 하는 공원 면적의 최소치"),
    areaWidest: int = Query(None, description="찾고자 하는 공원 면적의 최대치"),
):
    # 서울시 공원 정보 데이터
    seoul_parks = [
        ["북악산도시자연공원", "종로구", "서울특별시 종로구 부암동 산2-1", "주차장", 954553, "02-2148-2832"],
        ["효창근린공원", "용산구", "서울특별시 용산구 효창원로 177-18", "농구장", 171294, "02-2199-7608"],
        ["샘말공원", "관악구", "서울특별시 관악구 대학동 산63-1일대 샘말공원", "유아숲체험장", 10634, "02-879-6523"],
        ["초안산생태공원", "도봉구", "서울특별시 도봉구 창동 산24", "잔디쉼터", 22113, "02-2091-3754"],
        ["금천폭포근린공원", "금천구", "서울특별시 금천구 시흥대로38길 61", "캠핑장", 4835, "02-2627-1652"],
    ]

    filtered_parks = []

    for park in seoul_parks:
        if (
            (park[0] == parkNm if parkNm else True) and
            (park[1] == seoulGu if seoulGu else True) and
            (park[3] == facility if facility else True) and
            (areaNarrowest is None or (park[4] >= areaNarrowest)) and
            (areaWidest is None or (park[4] <= areaWidest))
        ):
            filtered_parks.append({
                "parkNm": park[0],
                "seoulGu": park[1],
                "address": park[2],
                "facility": park[3],
                "area": park[4],
                "phone": park[5]
            })

    return filtered_parks


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

@app.get("/supplements")
async def filter_supplements(
    brand: str = Query(None, description="브랜드"),
    inventory: bool = Query(None, description="재고유무"),
    type: str = Query(None, description="종류 ex) 알약, 젤리, 환"),
    expiration_date: int = Query(None, description="유통기한 데이터 형식 yyyymmdd"),
    keyword: str = Query(None, description="키워드 ex) 위 건강에 도움, 눈 건강 개선"),
):
    # 영양제 정보 데이터
    supplements = [
        ["트루포뮬러", True, "알약", 20250622, 28900, "위건강에 도움"],
        ["심플리케어", True, "환", 20230825, 59800, "활력"],
        ["블랙모어스", False, "가루", 20240408, 50000, "장건강도움"],
        ["리얼레시피", True, "젤리", 20250120, 41900, "면역력 증진"],
        ["네츄럴플러스", True, "알약", 20250804, 28600, "눈건강에 도움"],
    ]

    filtered_supplements = []

    for supplement in supplements:
        if (
            (supplement[0] == brand if brand else True) and
            (supplement[1] == inventory if inventory else True) and
            (supplement[2] == type if type else True) and
            (supplement[3] == expiration_date if expiration_date else True) and
            (supplement[5] == keyword if keyword else True)
        ):
            filtered_supplements.append({
                "brand": supplement[0],
                "inventory": supplement[1],
                "type": supplement[2],
                "expiration_date": supplement[3],
                "price": supplement[4],
                "efficacy": supplement[5]
            })

    return filtered_supplements
    
@app.get("/watch")
async def filter_watch(
    brand: str = Query(None, description="브랜드"),
    manufacture_country: str = Query(None, description="제조국"),
    max_price: int = Query(None, description="최대 가격", ge=0),
    material: str = Query(None, description="시계 소재 ex) Steel, Gold"),
    water_resistance: bool = Query(None, description="방수기능 유무"),
):
    # 시계 상품 정보 데이터
    watches = [
        {"brand": "Omega", "manufacture_country": "스위스", "price": 38600000, "material": "Gold", "size": "43mm", "water_resistance": True},
        {"brand": "TAG HEUER", "manufacture_country": "스위스", "price": 4380000, "material": "Steel", "size": "36mm", "water_resistance": True},
        {"brand": "danielwellington", "manufacture_country": "스웨덴", "price": 188000, "material": "Steel", "size": "28mm", "water_resistance": False},
        {"brand": "ALBA", "manufacture_country": "일본", "price": 135000, "material": "Steel", "size": "41.5mm", "water_resistance": True},
        {"brand": "Emporio Armani", "manufacture_country": "이탈리아", "price": 209000, "material": "Steel", "size": "43mm", "water_resistance": True},
    ]

    filtered_watches = []

    for watch in watches:
        if (
            (watch["brand"] == brand if brand else True) and
            (watch["manufacture_country"] == manufacture_country if manufacture_country else True) and
            (watch["price"] is None or (watch["price"] <= max_price if max_price else True)) and
            (watch["material"] == material if material else True) and
            (watch["water_resistance"] == water_resistance if water_resistance is not None else True)
        ):
            filtered_watches.append(watch)

    return filtered_watches
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
