from fastapi import FastAPI, Request
from mockdata import product
app = FastAPI() 

@app.get("/") # http route
def home():
    return "Welcome to the FastAPI application!"

@app.get("/contact")
def contact():
    return "Contact us at"


@app.get("/product")
def get_product():
    return product


#path param and query param - do revise

#path param
@app.get("/product/{id}")
def get_one_product(id:int ):
    # return {
    #     "id": id
    # }

    #now adding the logi - if product is available then return product else return not found
    for p in product:
        if p["id"] == id:
            return p
    return {
        "message": "Product not found"
    }


#query param- used when we dont know the number of params we will get from the user
# @app.get("/greet")
# def greet(name:str, age:int):
#     return {
#         "message": f"Hello {name}, you are {age} years old"
#     }
#now we will see the use of request 

# path param - designate specific resource in a url while quey param - filter or sort those resources.


@app.get("/greet")
def greet(request:Request):
    query_param = request.query_params
    print(query_param)
    name = query_param.get("name")
    age = query_param.get("age")
    return {
        "message": f"Hello {name}, you are {age} years old"
    }


# diff type of http methods - get, post, put, delete

@app.post("/create_product")
def create_product():
    return {
        "message": "Product created successfully"
    }
# we will use postman to test the http methods 


#now when we pass the data - we pass it in 3 ways body, header and query param
#when we use post method we use body to pass the data 


#now when we pass data in body we use pydantic model to validate the data 
# we use it because 