from jose import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext

SECRET_KEY = "autosentinel_secret"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

fake_admin = {
    "username": "admin",
    "password": pwd_context.hash("admin123")
}

def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)

def authenticate(username, password):
    if username == fake_admin["username"] and verify_password(password, fake_admin["password"]):
        return True
    return False

def create_token(data):
    expire = datetime.utcnow() + timedelta(hours=10)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)