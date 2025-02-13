from faker import Faker
import xml.etree.ElementTree as gfg
from datetime import datetime
faker = Faker()


def generate_products(**kwargs):

    for key, value in kwargs.items():
        if key in ['id', 'quantity', 'price']:
            temp = gfg.SubElement(value, key)
            temp.text = str(faker.random_int(min=1, max=100))
        if key in ['name', 'category']:
            temp = gfg.SubElement(value, key)
            temp.text = faker.word()


if __name__ == "__main__":
    try:
        root = gfg.Element('products', attrib={'date': datetime.utcnow().strftime('%Y-%m-%d')})

        for _ in range(10):
            product = gfg.Element('product')
            data = {
                'id': product,
                'name': product,
                'price': product,
                'quantity': product,
                'category': product
            }
            root.append(product)
            generate_products(**data)

        tree = gfg.ElementTree(root)
        with open('/app/gen_xml.xml', 'wb') as f:
            tree.write(f)
    except Exception as e:
        raise ValueError('We have a problem in xml generator')