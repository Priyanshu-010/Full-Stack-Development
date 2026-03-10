from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
def home():
  return "Welcome to FastAPI first server"

@app.get("/contact")
def contact():
  return "Connect with us"


@app.get("/product/{product_id}")
def product(product_id):
  return {
    "id": product_id
  }

@app.get("/greet")
def greet(request: Request):
  query_params = dict(request.query_params)
  # print(query_params)
  return {
    "greet": f"Hello {query_params.get("name")}, Your age is {query_params.get("age")}"
  }