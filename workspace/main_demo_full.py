"""FastAPI Clean Code Demo - Complete Single-File Implementation."""


# =============================================================================
# Section 1: Pydantic Models (Schemas)
# =============================================================================

from pydantic import BaseModel, Field, EmailStr
from datetime import datetime, timezone, timedelta
import uuid

class CreateUserRequest(BaseModel):  # noqa: N806 - Class naming convention per FastAPI examples.
    """Create user request with field constraints."""


class UpdateUserRequest(BaseModel): 
"""Update request model supporting partial updates and optional fields for flexibility."""



# =============================================================================
# Section 2: Authentication Dependencies (Dependency Injection Pattern)
# =============================================================================

from fastapi import Depends, HTTPException, status
    
TOKEN_STORAGE = {}  
VALID_TOKENS_PREFIXES = ["valid_", "token_"]


async def get_current_user(request_id: str):         
    """Simulated auth dependency - returns None for unauthenticated users."""
    
    
