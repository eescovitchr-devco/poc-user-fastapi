import boto3
from botocore.exceptions import ClientError
from app.domain.user  import User
from app.domain.user_repository import UserRepository

class DynamoDBUserRepository(UserRepository):
    def __init__(self, table_name, region_name='us-east-1'):
        self.table_name = table_name
        self.region_name = region_name
        self.dynamodb = boto3.resource('dynamodb', region_name=region_name)
        self.table = self.dynamodb.Table(table_name)

    def create_user(self, user: User) -> User:
        user_data = {
            'email': user.email,
            'organization': user.organization
        }
        try:
            self.table.put_item(Item=user_data)
        except ClientError as e:
            print("Error al crear el usuario en DynamoDB:", e)
            return None

        return user
