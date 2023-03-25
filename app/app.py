from fastapi import FastAPI
app = FastAPI()

#minimal app get request
@app.get("/",tags=['ROOT'])
async def root() -> dict:
    return{"Ping":"Pong" } 

#Get -> Read todo

@app.get("/todo", tags=['todos'])
async def get_todo() -> dict:
    return {"data":todos} 


#Post ->Create todo
@app.post("/todo", tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data" : "A todo has been added"
    }

#Put -> Update todo 

@app.put("/todo/{id}", tags=['todos'])
async def update_todo(id:int, body:dict) -> dict:
    for todo in todos:
        if int(todo['id'])==id:
            todo['Activity'] = body['Activity']
            return { 
                "data" : f"A todo has {id} been added"
            }
       
    return { 
            "data" : f"A todo has {id} been not been added"
    }
             
    

#Delete - Delete todo
@app.delete("/todo/{id}", tags=['todos'])
async def delete_todo(id:int) -> dict:
    for todo in todos:
        if int(todo['id'])==id:
            todos.remove(todo)
            return { 
                "data" : f"A todo has {id} been deletes"
            }
       
    return { 
            "data" : f"A todo has {id} been not been deletes"
    }
          



todos = [
  {
     "id" :"1",
    "Activity" : "Jogging for some hours"

  },
   {
     "id" : "2",
    "Activity" : "coding for an hour"

  }
]