from typing import Generator, Dict
from backend.db.client import supabase
from backend.services.newsapi_scrapper.news_api_fetcher import get_previous_day

def fetch_last_days_posts() -> Generator[Dict, None, None]:

    start = get_previous_day(1)
    response = (
        supabase
        .table("recent_posts_view")
        .select("*")
        .gte("created_at", start)
        .order("created_at", desc=False)
        .execute()
    )

    for row in response.data:
        yield row
