from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    user_profile_name: str = Field(min_length=1, max_length=100, title='user profile name')

    # Default config override
    class Config:
        schema_extra = {
            'example': {
                'user_profile_name': 'abhishek',
            }
        }
