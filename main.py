from fastapi import FastAPI, Query
from typing import List

app = FastAPI()

# 가상의 인터넷 소설 데이터
novels = [
    {"title": "The Legendary Guardian", "author": "Shi Luo Ye", "downloads": 100000, "genre": "Fantasy", "release_year": 2015, "platform": "Webnovel"},
    {"title": "Rebirth of the Thief Who Roamed the World", "author": "Mad Snail", "downloads": 80000, "genre": "Game", "release_year": 2010, "platform": "Webnovel"},
    {"title": "Lord of the Mysteries", "author": "Cuttlefish That Loves Diving", "downloads": 90000, "genre": "Mystery", "release_year": 2017, "platform": "Qidian"},
    {"title": "The King's Avatar", "author": "Butterfly Blue", "downloads": 120000, "genre": "Game", "release_year": 2011, "platform": "Webnovel"},
    {"title": "The Great Ruler", "author": "Tian Can Tu Dou", "downloads": 70000, "genre": "Fantasy", "release_year": 2012, "platform": "Qidian"},
    {"title": "Release That Witch", "author": "Er Mu", "downloads": 95000, "genre": "Fantasy", "release_year": 2014, "platform": "Webnovel"},
    {"title": "The Legendary Mechanic", "author": "Chocolion", "downloads": 85000, "genre": "Game", "release_year": 2016, "platform": "Qidian"},
    {"title": "Martial God Asura", "author": "Kindhearted Bee", "downloads": 110000, "genre": "Fantasy", "release_year": 2013, "platform": "Webnovel"},
    {"title": "I Shall Seal the Heavens", "author": "Er Gen", "downloads": 75000, "genre": "Fantasy", "release_year": 2014, "platform": "Qidian"},
    {"title": "The Great Thief", "author": "Boating Lyrics", "downloads": 85000, "genre": "Game", "release_year": 2015, "platform": "Webnovel"}
]

@app.get("/novels")
async def get_novels(
    title: str = Query(default=None),
    author: str = Query(default=None),
    platform: str = Query(default=None),
    genre: str = Query(default=None),
    min_downloads: int = Query(default=None, ge=0)
):
    filtered_novels = novels

    if title is not None:
        # 제목 필터링
        filtered_novels = [novel for novel in filtered_novels if title.lower() in novel['title'].lower()]

    if author is not None:
        # 작가 필터링
        filtered_novels = [novel for novel in filtered_novels if author.lower() in novel['author'].lower()]

    if platform is not None:
        # 플랫폼 필터링
        filtered_novels = [novel for novel in filtered_novels if platform.lower() == novel['platform'].lower()]

    if genre is not None:
        # 장르 필터링
        filtered_novels = [novel for novel in filtered_novels if genre.lower() == novel['genre'].lower()]

    if min_downloads is not None:
        # 최소 다운로드 필터링
        filtered_novels = [novel for novel in filtered_novels if novel['downloads'] >= min_downloads]

    return filtered_novels
