from src.settings import settings
from asyncio import run
import asyncpg
from asyncpg.exceptions import *
from datetime import datetime

async def connect(url):
    try:
        conn = await asyncpg.connect(url)
        return conn
    except ConnectionError as e:
        raise e
    except ConnectionRejectionError as e:
        raise e


async def exc(con: str, query: str, fetchall: bool = False):
    try:
        con = await connect(con)
        if fetchall:
            result = await con.fetch(query)
            return result
        results = await con.fetchrow(query)
        return results
    except Exception as e:
        raise e


if __name__ == "__main__":
    con_url =(f"postgresql://{settings.PG_USER}" +
        f":{settings.PG_PASSWD}" + "@" +
        f"{settings.PG_HOST}:{settings.PG_PORT}" +
        f"/{settings.PG_DB}"
              )
    total_revenue = run(exc(con_url,'SELECT SUM(price) AS total_revenue FROM units'))
    print(total_revenue.get('total_revenue'))

    top_three = run(exc(con_url, "SELECT name, COUNT(name) AS counted FROM units GROUP BY name ORDER BY counted DESC", fetchall=True))
    print([i.get('name') for i in top_three[:3]])
    date = datetime.now().strftime('%Y/%m/%d')

    prompt: str = (f"Проанализируй данные о продажах за {date}:\n"
                   f"Общая выручка: {total_revenue.get('total_revenue')})\n"
                   f"Топ-3 товара по продажам: {top_three[0].get('name'), top_three[1].get('name'), top_three[2].get('name')}\n"
                   # f"Распределение по категориям: {categories}"
                   "Составь краткий аналитический отчет с выводами и рекомендациями.")
    print(prompt)
