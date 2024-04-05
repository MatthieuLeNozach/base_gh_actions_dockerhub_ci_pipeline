from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def healthcheck() -> dict:
    return {'status': 'ok'}

@app.get('/items/{item_id}')
def read_item(item_id: int, q: str = None) -> dict:
    return  {'item_id': item_id, 'q': q}