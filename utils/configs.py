import os
from dotenv import load_dotenv



load_dotenv()


def env_get(env_var: str) -> str:
    val = os.environ.get(env_var)
    if not val:
        raise KeyError(f"Env variable '{env_var}' is not set!")
    return val


PROFILE_URL = env_get("PROFILE_URL")
COOKIE = env_get("COOKIE")
X_Kaggle_Build_Version = env_get("X_Kaggle_Build_Version")
X_Xsrf_Token = env_get("X_Xsrf_Token")


headers = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, zstd",
    "Accept-Language": "en-GB,en;q=0.5",
    "Content-Length": "23",
    "Content-Type": "application/json",
    "Cookie": COOKIE,
    "Origin": "https://www.kaggle.com",
    "Priority": "u=1, i",
    "Referer": "https://www.kaggle.com",
    "Sec-Ch-Ua": "\"Brave\";v=\"125\", \"Chromium\";v=\"125\", \"Not.A/Brand\";v=\"24\"",
    "Sec-Ch-Ua-Mobile": "?1",
    "Sec-Ch-Ua-Platform": "Android",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Gpc": "1",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Mobile Safari/537.36",
    "X-Kaggle-Build-Version": X_Kaggle_Build_Version,
    "X-Xsrf-Token": X_Xsrf_Token
}