import xml.etree.ElementTree as ET

def create_xml():
    data = ET.Element("store")
    item1 = ET.SubElement(data, "item")
    item1.set("category", "electronics")
    ET.SubElement(item1, "name").text = "Laptop"
    ET.SubElement(item1, "price").text = "1000"

    item2 = ET.SubElement(data, "item")
    item2.set("category", "books")
    ET.SubElement(item2, "name").text = "Python Programming"
    ET.SubElement(item2, "price").text = "40"

    tree = ET.ElementTree(data)
    tree.write("products.xml")

create_xml()
import xml.etree.ElementTree as ET

def read_and_process_xml(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    
    items = []
    for item in root.findall("item"):
        name = item.find("name").text
        price = float(item.find("price").text)
        category = item.get("category")
        items.append({"name": name, "price": price, "category": category})
    
    items.sort(key=lambda x: x["price"])
    total_price = sum(item["price"] for item in items)
    
    print("Товары по возрастанию цены:")
    for item in items:
        print(f"{item['name']} ({item['category']}): {item['price']}")
    
    print(f"\nОбщая стоимость товаров: {total_price}")

read_and_process_xml("products.xml")
