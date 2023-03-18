import pymysql
import os
from git import Repo
import time

# Establish connection to the database
cnx = pymysql.connect(user='ak', host='localhost', database='dbmslab')




# Create a cursor object
cursor = cnx.cursor()

start = time.time()
cursor.execute("create view faculty as select ID ,name,dept_name from instructor;")
cursor.execute("select * from faculty;")
myresult = cursor.fetchall()
end = time.time()

# Print the results
for x in myresult:
    print(x)
print("time taken:",end - start)

# Close the cursor and connection
cursor.close()
cnx.close()

# Initialize a new Git repository or open an existing one
repo_path = os.getcwd()
repo = Repo.init(repo_path)

# Add the database.py file to the repository
repo.index.add(['database_lab_7.py'])

# Commit the changes
repo.index.commit('Add database.py')

# Push the changes to GitHub
origin = repo.remote(name='origin')
origin.push()
