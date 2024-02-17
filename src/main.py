from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home_page():
    # for API services
    # JSON-ready dict -> json.dumps({'hello': 'world'})
    return {"Hello": "World"}