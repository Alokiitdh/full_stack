from pydantic import BaseModel, Field, computed_field

class Orders(BaseModel):
    id : int
    quantity: int
    price_per_quantity: float

    @computed_field
    @property
    def total_amount(self)-> float:
        return self.quantity * self.price_per_quantity
    

order1 = Orders(**{'id': 123, 'quantity': 3, 'price_per_quantity': 99})
print(order1)