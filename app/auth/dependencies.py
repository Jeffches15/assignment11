# app/auth/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from app.models.user import User
from app.schemas.user import UserResponse

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Depends: Declare a FastAPI dependency.
    # It takes a single "dependable" callable (like a function).
    # Don't call it directly, FastAPI will call it for you.
def get_current_user(
    db,
    token: str = Depends(oauth2_scheme)
) -> UserResponse:
    """Dependency to get current user from JWT token."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    user_id = User.verify_token(token)
    if user_id is None:
        raise credentials_exception
    
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise credentials_exception
        
    # Converts the ORM User object into a UserResponse (Pydantic model) using Pydantic's model_validate().
    return UserResponse.model_validate(user)  # Updated from from_orm

def get_current_active_user(
    current_user: UserResponse = Depends(get_current_user)
) -> UserResponse:
    """Dependency to get current active user."""
    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )
    return current_user
