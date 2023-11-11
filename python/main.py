import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    version='0.1.0',
    title='Training API',
    description='API for training',
    docs_url='/',
)


class Product(BaseModel):
    id: str
    name: str
    price: float


products = [
        {'id': '1', 'name': 'Product 1', 'price': 9.99},
        {'id': '2', 'name': 'Product 2', 'price': 19.99},        
    ]

@app.get("/api/v1/products")
def get_all():
    return products

# Init package
if __name__ == '__main__':
    uvicorn.run('main:app', host="localhost", port=7000, reload=True)