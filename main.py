import logging, json, requests
from fastapi import FastAPI
from utils.schemas import UserProfile
from utils.configs import PROFILE_URL, PROFILE_ACTIVITY_URL,headers


app = FastAPI()


# SETUP LOGGER
logger = logging.getLogger(__file__)


# DNA
app = FastAPI(
    title='Kaggle API',
    description='Kaggle API',
    version='0.0.1',
    docs_url='/v1/documentation',
    redoc_url='/v1/redoc',
    openapi_url='/v1/openapi.json'
)


@app.get("/")
async def root():
    return {"message": "Hello Kaggle!"}


@app.post("/user-profile")
async def get_user_profile(user_profile : UserProfile):

    try:
        payload = {
            "relativeUrl": f"/{user_profile.user_profile_name}"
        }

        response = requests.post(PROFILE_URL, json=payload, headers=headers)

        if response.status_code == 200:
            logger.info(f"PROFILE : {user_profile.user_profile_name} : success!")
            json_response = json.loads(response.text).get("userProfile")
            del json_response["usersFollowingMe"]
            return json_response
        else:
            logger.error(f"PROFILE : {user_profile.user_profile_name} : failed with {response.status_code} : {response.content} !")
            return {}

    except requests.exceptions.RequestException as e:
        logger.error(f"PROFILE : {user_profile.user_profile_name} : failed with {e}")
        return {}






@app.post("/user-profile-activity")
async def get_user_profile_activity(user_profile : UserProfile):

    try:
        payload = {
            "userName": f"{user_profile.user_profile_name}"
        }

        response = requests.post(PROFILE_ACTIVITY_URL, json=payload, headers=headers)

        if response.status_code == 200:
            logger.info(f"PROFILE ACTIVITY : {user_profile.user_profile_name} : success!")
            return json.loads(response.text)
        else:
            logger.error(f"PROFILE ACTIVITY: {user_profile.user_profile_name} : failed with {response.status_code} : {response.content} !")
            return {}

    except requests.exceptions.RequestException as e:
        logger.error(f"PROFILE ACTIVITY: {user_profile.user_profile_name} : failed with {e}")
        return {}
