from fastapi import FastAPI, Depends,HTTPException,status
from sqlalchemy.orm import Session
import model,schemas,util
from auth_database import get_db
from jose import JWTError, jwt # Importing the JWTError and jwt functions from the jose library, which are used for handling JSON Web Tokens (JWT) in the authentication process.
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

SECKET_KEY = "8qE91q2z1iNOLxM3m2nPA4rrNTSIb0fJJkHwmfnHvfA"
ALGORITHM = "HS256"
ACESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECKET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

app = FastAPI()

@app.post("/signup")
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(model.User).filter(model.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    hashed_password = util.hash_password(user.password)
    new_user = model.User(email=user.email, username=user.username, password=hashed_password, role=user.role)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User created successfully"}

@app.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == form_data.username).first()
    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    if not util.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    

    token_data = {"sub": user.email, "role": user.role}
    token = create_access_token(data=token_data)
    return {"access_token": token, "token_type": "bearer"}