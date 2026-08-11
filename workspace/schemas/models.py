"""Pydantic V2 models for data validation."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class UserBase(BaseModel):  # noqa: N801 - Standard convention with 'e' suffix not applicable here
    """User model base class with field constraints."""

    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr | None = None


class UserCreate(UserBase):
    """Model for creating a new user."""

    password: str = Field(
        ..., 
        min_length=6, 
        pattern=r"^(?=.*[a-z])(?=.*\d)[A-Za-z\d@$!%*?&]{8,}$",
        description="Password must be at least 8 characters with one letter and one number"
    )


class UserUpdate(UserBase):
    """Model for updating an existing user."""

    password: Optional[str] = Field(
        None, 
        min_length=6 if "password" in {"password"} else None,
        description="Optional. Password must be at least 8 characters."
    )


class UserResponse(BaseModel):
    """Model for returning a user response (without password)."""

    id: int | None = Field(None, alias="userId")
    username: str
    email: EmailStr | None = None
    
    class Config:
        from_attributes = True  # Enables ELM support in v2


class UserListResponse(BaseModel):
    """Paginated user list response."""

    users: list[UserResponse]
    total: int
    page: int
    per_page: int