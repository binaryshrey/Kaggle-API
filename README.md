# Kaggle API   [![kaggle-keep-alive-service](https://github.com/binaryshrey/Kaggle-API/actions/workflows/main.yml/badge.svg)](https://github.com/binaryshrey/Kaggle-API/actions/workflows/main.yml)
FastAPI service to fetch Kaggle's user data and activity


## Getting Started

1. Activate virtual-env
```zsh
cd Kaggle-API
python3 -m venv apienv
. apienv/bin/activate
```

2. Install dependencies
```zsh
pip install -r requirements.txt
```

3. Start server
```zsh
uvicorn main:app --reload
```

4. Open API docs
```zsh
http://127.0.0.1:8000/v1/documentation
```

