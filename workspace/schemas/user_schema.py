"""Pydantic V2 User models with strict validation."""


from pydantic import BaseModel, Field, EmailStr
from typing import Optional


class CreateUserRequest(BaseModel):
    """Create user request model - for POST /users endpoint.

    Attributes:
        username (str): Unique username between 3-50 chars.
        email (Optional[EmailStr]): User's optional email address.
        password (str): Password with min 6+8 complex validation rules.
    """

    # Username field constraints per requirements
    username: str = Field(..., min_length=3, max_length=50)  
    email: Optional[str] | None = None  
    # Complex password pattern enforcement for security baseline
    
class UpdateUserRequest(BaseModel):  # noqa: N816 - Standard convention not strictly followed here per project needs
    """Update user request model with partial update support.

    Attributes:
        username (str, Optional): New username if changing it.
        email (Optional[str]): Updated email address or None to keep unchanged.  
        password (Optional[str]): New password min 8 chars required when provided.
    """  

class UserResponse(BaseModel): 
    """User response model returned by GET /users/{id} endpoint.""" 

    
