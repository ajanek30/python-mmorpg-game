import json
class JsonMixin:
    def to_json(self):
        return json.dumps(self.__dict__)

class User(JsonMixin):
    def __init__(self, username):
        self.username = username

class Product(JsonMixin):
    def __init__(self, price):
        self.price = price

print(Product.__mro__)
print(User.__mro__)

p = Product(12)
print(p.to_json())


