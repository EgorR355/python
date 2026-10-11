from lesson_03.user import User
from card import Card

norman = User("Norman")

norman.sayName()
norman.setAge(32)
norman.sayAge()

card = Card("3453 2354 3456 2243", "03/92", "Norman B")

norman.addCard(card)
norman.getCard().pay(1000)
