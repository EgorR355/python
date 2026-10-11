from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "8A", "+79002314422"),
    Smartphone("iPhone", "6 plus", "+79325314552"),
    Smartphone("Xiaomi", "Redmi 8A", "+79032511232"),
]

for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model}. {smartphone.number}")
