import pymysql
import os
from git import Repo
import time

# Establish connection to the database
cnx = pymysql.connect(user='ak', host='localhost', database='dbmslab')
# Create a cursor object
cursor = cnx.cursor()

print("---------------Enter a Instructor Details--------------------")
Id = input('Instructor Id :')
name = input('Instructor Name :')
dept_name = input('Department Name :')
salary = float(input('Salary :'))
query = """INSERT INTO instructor (id, name, dept_name, salary) 
                                VALUES (%s, %s, %s, %s) """
record = (Id,name,dept_name,salary)
cursor.execute(query , record)

cnx.commit()
print("Record inserted successfully into instructor table")


# Close the cursor and connection
cursor.close()
cnx.close()

# Initialize a new Git repository or open an existing one
repo_path = os.getcwd()
repo = Repo.init(repo_path)

# Add the database.py file to the repository
repo.index.add(['SmallProject.py'])

# Commit the changes
repo.index.commit('Add SmallProject.py')

# Push the changes to GitHub
origin = repo.remote(name='origin')
origin.push()