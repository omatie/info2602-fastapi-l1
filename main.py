from fastapi import FastAPI
import json

app = FastAPI()

global data

with open('./data.json') as f:
    data = json.load(f)


@app.get('/')
def hello_world():
    return 'Hello, World!'


@app.get('/students')
async def get_students():
    return data


@app.get('/students/{id}')
async def get_student(id):
  for student in data: 
    if student['id'] == id: # Only return the student if the ID matches
      return student
    
@app.get('/students')
async def get_students(pref=None):
    if pref:
        filtered_students = []
        for student in data:
            if student['pref'] == pref: # select only the students with a given meal preference
             filtered_students.append(student) # add match student to the result
        return filtered_students
    return data



@app.get('/stats')
async def get_stats():
   countChicken = 0
   countcsMajor=0
   countcsSpecial=0
   countFish=0
   countitMajor=0
   countitSpecial=0
   countveg=0
   
   for student in data:
        if student['programme'] == "Computer Science (Major)":
         countcsMajor+=1
        if student['programme'] == "Computer Science (Special)":
           countcsSpecial+=1
        if student['pref'] == "Fish":
           countFish+=1
        if student['programme'] == "Information Technology (Major)":
           countitMajor+=1
        if student['programme'] == "Information Technology (Special)":
           countitSpecial+=1
        if student['pref'] == "Vegetable":
           countveg+=1
        if student['pref'] == "Chicken":
         countChicken +=1

   return {
       "Chicken": countChicken,
       "Computer Science (Major)": countcsMajor,
       "Computer Science (Special)": countcsSpecial,
       "Fish": countFish,
       "Information Technology (Major)": countitMajor,
       "Information Technology (Special)": countitSpecial,
       "Vegetable": countveg
    }



@app.get('/add/{a}/{b}')
async def adding(a: int, b: int):
   return a+b

@app.get('/subtract/{a}/{b}')
async def subtracting(a: int, b: int):
   return a-b

@app.get('/multiply/{a}/{b}')
async def multiplying(a: int, b: int):
   return a*b

@app.get('/divide/{a}/{b}')
async def dividing(a: int, b: int):
   return a/b
