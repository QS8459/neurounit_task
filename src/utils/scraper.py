from src.settings import settings
from asyncio import run
import asyncpg
from lxml import html
from datetime import datetime


class ParserService:
    def xpath_or_none(self, element: html.HtmlElement, xpath_expr):
        value = element.xpath(xpath_expr)
        if isinstance(value, html.HtmlElement):
            return value
        if isinstance(value, str) and value == '':
            return None
        if isinstance(value, str) and value != '':
            return value
        if isinstance(value, float) and not value.is_integer():
            return None
        if isinstance(value, float) and value.is_integer():
            return float(value)
        return value

    def parse_xml(self, elements, records: html.HtmlElement):
        flat_list: list = []
        for i in range(0, len(records)):
            for key, value in elements.items():
                if key != "date":
                    flat_list.append(self.xpath_or_none(records[i], value))
                else:
                    flat_list.append(value)
        return {
            'long_arr_value': flat_list,
            'len_value': len(elements.keys())
        }

    def generate_placeholder(self, num_records: int = 0, num_fields_per_record: int = 0):
        placeholder: str = ''
        for i in range(num_records):
            placeholder += '('
            for j in range(1, num_fields_per_record + 1):
                placeholder += f"${i * num_fields_per_record + j}" + (', ' if j < num_fields_per_record else '')
            placeholder += ')' + (', ' if i + 1 < num_records else '')

        return placeholder


async def connect_to_db():
    conn = await asyncpg.connect(f'postgresql://{settings.PG_USER}:{settings.PG_PASSWD}@{settings.PG_HOST}:{settings.PG_PORT}/{settings.PG_DB}')
    return conn


async def many_insert(values: list, placeholder: str = ""):
    try:
        conn = await connect_to_db()
        query = f"INSERT INTO public.units(sales_date, xml_id, name, quantity, price, category) VALUES {placeholder};"
        async with conn.transaction():
            result = await conn.execute(query, *values)
            print(result)
    except Exception as e:
        print(e)
        raise


def parse_file(file_name: str):
    service = ParserService()
    with open(file_name, 'r') as file:
        page = html.fromstring(file.read())
        products_xml: html.HtmlElement = service.xpath_or_none(page, '//products/product')
        data = datetime.strptime(
            service.xpath_or_none(page, "string(//products/@date)") + " 00:00:00.000000",
            '%Y-%m-%d %H:%M:%S.%f')
        elements = {
            'date': data,
            'id': 'number(id[position()=1]/text())',
            'name': 'string(name[position()=1]/text())',
            'quantity': 'number(quantity[position()=1]/text())',
            'price': 'number(price[position()=1]/text())',
            'category': 'string(category[position()=1]/text())'
        }
    values = service.parse_xml(elements, records=products_xml)
    num_records: int = len(products_xml)
    num_fields_per_record: int = values.get("len_value")
    placeholder = service.generate_placeholder(num_records, num_fields_per_record)
    run(many_insert(placeholder=placeholder, values=values.get('long_arr_value')))


if __name__ == "__main__":
    parse_file('gen_xml.xml')