from fastapi import FastAPI, HTTPException, status
from app.domain.user import User
from app.application.user_service import UserService
from app.presentation.dynamodb_user_repository import DynamoDBUserRepository

app = FastAPI()

dynamodb_repository = DynamoDBUserRepository(table_name='nita_users')
user_service = UserService(user_repository=dynamodb_repository)

@app.post("/users/", status_code=status.HTTP_201_CREATED)
def create_user(user: User):
    user_created = user_service.create_user(user)
    if user_created:
        return {"message": "User created successfully", "organization": user_created}
    else:
        raise HTTPException(status_code=500, detail="Could not create user")
