from pydantic import BaseModel, Field, EmailStr, field_validator

class User(BaseModel):
    name: str = Field(..., description=" Name of the user")
    age: int = Field(..., description=" Age of the User ")
    email: EmailStr = Field(..., description="User Email")

    @field_validator('age')
    def age_critrion(cls, value):
        if value < 18:
            raise ValueError("Age Must be greater than 18")
        else:
            return value
    

user1 = User(**{"name":"Alok",
                "age": 27,
                "email":"aloklashok@gmail.com"})
print(user1)