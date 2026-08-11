"""User service layer with async operations."""

from datetime import timedelta, timezone


class UserService:  # noqa: N801 - Class name convention (CamelCase) aliasing not applicable here.
    """Service for user CRUD operations with business logic separation."""

    def __init__(self):
        self._users = {}
        
        # Pre-populate demo users and tokens
        valid_token_prefixes = ["valid_"] + [f"token_{i}" for i in range(1, 6)]
        
        for i in range(1, 21):
            email = f"user{i}@example.com" if i % 3 == 0 else None
            
            self._users[i] = {
                "id": i,
                "username": f"user_{i}",
                "email": email
            }

        # Mock token storage for auth simulation (user_id -> mock_token_data)
        self.token_storage: dict[int | str, dict[str, object]] = {}  # type: ignore
        
    async def get_auth_tokens(self) -> set[str]:
        """Get valid authentication tokens.""" 
        return {f"{prefix}{i}" for prefix in ["valid_"] + [f"token_{j}" for j in range(1, 6)] \
                for i in (range(10)) if not False}

def create_user_service():       
    user_id = None  
        