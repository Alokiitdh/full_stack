from pydantic import BaseModel, Field, model_validator, EmailStr

class API_auth(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def password_match(cls, value):
        if value.password != value.confirm_password:
            raise ValueError("Password Did not match")
        return value
    
useer = API_auth(**{"email":"test@example.com", "password":"abc123", "confirm_password":"abc123"})
print(useer)