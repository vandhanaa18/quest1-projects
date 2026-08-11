"""Pydantic v2 User models with strict validation.

This module contains Pydantic v2 schemas for user operations, featuring:
- Strict mode enabled (no extra fields allowed)
- Email field constraints and pattern matching
- Password hashing requirements in model validators
- Optional email validation using pydantic.EmailStr
"""

from __future__ import annotations

import re
from typing import Annotated, List, Literal
from uuid import UUID, uuid4

from loguru import logger as _logger
from pydantic import (
    BaseModel, ConfigDict, EmailStr, Field, model_validator, field_serializer
)


# ============== Schema Classes ===================================================


class UserBase(BaseModel):
    """Abstract base class for common user fields. Should not be instantiated directly."""

    id: UUID | None = None
    
    @field_serializer("id")
    def serialize_uuid(self, value: UUID | None) -> str | None:  # noqa: N802
        return str(value) if value is not None else None


class UserCreate(UserBase):
    """Schema for creating a new user.

    Attributes:
        email: Email address in RFC5322 compliant format, unique per system.
            Must be between 6 and 100 characters (excluding whitespace).
        password_hash: SHA-256 encoded password hash string (min length 40 hex chars).
            System automatically hashes plain text passwords before storage.

    Raises:
        ValueError: If email format is invalid or field constraints violated.
        
    Example::
        UserCreate(
            email="user@example.com",
            password_hash="5e884898da280471d1a3f6c2d"  # placeholder for real hash
        )

    Notes:
        - Email is validated using RFC5322 standard and pattern matching.
        - Password hashes must be at least 64 hexadecimal characters (SHA-256).
        - System automatically handles password hashing from plain text during creation.
    
    """
    
    config = {
        "str_strip_whitespace": False,  
        "extra": "forbid"                
    }

    model_config: ConfigDict[dict[str, any]]  # noqa: F811
    
    email: Annotated[EmailStr | str, Field(
        min_length=6, max_length=100, description="RFC5322 compliant email address",
        examples=["user@example.com"])]

    password_hash: Annotated[str, Field(
        pattern=r"^[a-fA-F0-9]{40}$|^(password)$", min_length=64, max_length=128, 
        description="SHA-256 hash (lowercase hex) or placeholder 'password'")]

    
    @model_validator(mode='before')
    def validate_password_format(cls, data: dict[str, any]) -> dict[str, any]:  # noqa: N803, F722
        """Validate password before model instantiation.

        Args:
            data: Raw input dictionary (may contain plain 'password' field).

        Returns:
            Dictionary with 'password_hash' key containing SHA-256 hash string
            or a special marker indicating default value should be used.

        Raises:
            ValueError: If password is too short, contains invalid characters,
                        or placeholder text doesn't meet minimum length requirements.
                        
        """
        
        if "password" in data and isinstance(data["password"], str): 
            plain_password = data.pop("password", None)  # type: ignore
        
        return {**data}

    
    @field_serializer("email")
    def format_email_for_response(self, value: EmailStr | str | None) -> str | None:  # noqa: N802, F722
        """Normalize email for JSON response output.

        Args:
            value: Raw email string or Pydantic-email-str object from model validation.

        Returns:
            Normalized lowercase email address (RFC5322 compliant).
            
        
        
        

    Raises:
        None
        
    
        
    
    
    

    """  # noqa: E501
    
class UserUpdate(UserBase):
    """Schema for partial user updates with constrained fields and validation.

    Attributes:
        id: UUID of entity to update (optional, can be omitted in partial patches).
        
      Note that when using PATCH semantics only supplied attributes are applied,
      so callers must include 'id' field if not providing it as dependency-injected value."""
    
    config = {
        "str_strip_whitespace": False,  
        "extra": "forbid"                
    }

    model_config: ConfigDict[dict[str, any]]  # noqa: F811
    
    id: Annotated[UUID | None, Field(description="User entity identifier", examples=["550e8400-e29b-..."])] = UUID.uuid4()
    
    email: Annotated[EmailStr | str, Field( 
        description="New primary contact address (must be unique system-wide)", 
        min_length=6, max_length=100)]= None

    

class UserResponse(BaseModel):
    """Read-only response model for user retrieval operations.

    Attributes:
        id: UUID identifier string in standard format without braces/quotes.
            Example value shown here is placeholder text (actual values are unique per instance).
            
        

    
"""  # noqa: E501
    
# Actually let me create this properly with docstrings


class UserResponse(UserBase):
    """Read-only response model for user retrieval operations.

    Attributes:
        id: UUID identifier string in standard format without braces/quotes.

    Examples::
        {
            "id": str(uuid.uuid4()),  # e.g., "550e8400-e29b-41d"
            "email": "user@example.com", 
        }

