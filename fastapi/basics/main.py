from fastapi import FastAPI, Request
from dtos import ProductDTO

app = FastAPI()

products = []

@app.get("/")
def home():
  return "Welcome to FastAPI first server"

@app.get("/contact")
def contact():
  return "Connect with us"
@app.get("/product")
def contact():
  return products


@app.get("/product/{product_id}")
def product(product_id: int):
  for oneProduct in products:
    if oneProduct.get("id") == product_id:
      return oneProduct

@app.get("/greet")
def greet(request: Request):
  query_params = dict(request.query_params)
  # print(query_params)
  return {
    "greet": f"Hello {query_params.get("name")}, Your age is {query_params.get("age")}"
  }

# How to send data: 
# body, headers - request headers, query_params
@app.post("/create")
def create(data: ProductDTO):
  data = data.model_dump()
  # print(data)
  products.append(data)
  print(product)
  return {"status": "product created successfully", "data": data}

