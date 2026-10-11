from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "8A", "+79002314422"),
    Smartphone("iPhone", "6 plus", "+79325314552"),
    Smartphone("Xiaomi", "Redmi 8A", "+79032511232"),
    Smartphone("Google", "Pixel 8", "+79004567890"),
    Smartphone("Huawei", "P60 Pro", "+79005678901")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")
