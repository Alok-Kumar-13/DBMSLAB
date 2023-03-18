#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pymysql
import os
from git import Repo
import time

# Establish connection to the database
cnx = pymysql.connect(user='ak', host='localhost', database='dbmslab')
# Create a cursor object
cursor = cnx.cursor()


# In[4]:


# 1. Create a view of instructors without their salary called faculty
start = time.time()
cursor.execute("create view faculty as select ID ,name,dept_name from instructor;")
cursor.execute("select * from faculty;")
myresult = cursor.fetchall()
end = time.time()

# Print the results
for x in myresult:
    print(x)
print("time taken for query 1:",end - start)


# In[6]:



## 2. Create a view of department salary totals
start = time.time()
cursor.execute("create view dept_total_salary as select dept_name ,sum(salary) as 'Total' from instructor group by dept_name ;")
cursor.execute("select * from dept_total_salary;")
myresult = cursor.fetchall()
end = time.time()
for x in myresult:
    print(x)
print("time taken for query 2:",end - start)


# In[8]:


#3. Create a role of student
start = time.time()
cursor.execute("create role students ;")
end = time.time()
print("time taken for query 3:",end - start)


# In[9]:


#4. Give select privileges on the view faculty to the role student.
start = time.time()
cursor.execute("grant select on faculty to student")
end = time.time()
print("time taken for query 4:",end - start)


# In[14]:


# 5. Create a new user and assign her the role of student.

start = time.time()
cursor.execute("CREATE USER 'new_user'@'localhost' IDENTIFIED BY '12345'")
cursor.execute("GRANT student TO 'new_user'@'localhost' ")
end = time.time()
print("time taken for query 5:",end - start)


# In[15]:


# 6. Revoke privileges of the new user

start = time.time()
cursor.execute("REVOKE ALL PRIVILEGES, GRANT OPTION FROM 'new_user'@'localhost'")
end = time.time()
print("time taken for query 6:",end - start)


# In[17]:


# 7. Remove the role of student.
start = time.time()
cursor.execute("drop role students ")
end = time.time()
print("time taken for query 7:",end - start)


# In[20]:


# 8. Give select privileges on the view faculty to the new user.

start = time.time()
query = "grant select on faculty to new_user@localhost"
cursor.execute(query)
end = time.time()
print("time taken for query 8:",end - start)


# In[42]:


# 9. Create table teaches3 with same columns as teaches but 
# with additional constraint that that semester is one of fall, winter, spring or summer.
start = time.time()
query = "CREATE TABLE teaches3 (ID INT NOT NULL,Course_id VARCHAR(10) NOT NULL,sec_id VARCHAR(10) NOT NULL,semester ENUM('fall', 'winter', 'spring', 'summer') NOT NULL,year INT NOT NULL, PRIMARY KEY (ID))"

cursor.execute(query)
end = time.time()
print("time taken for query 9:",end - start)


# In[30]:


# 10. Create index ID column of teaches.
# Compare the difference in time to obtain query results with or without index.

start = time.time()
query = "SELECT * FROM teaches WHERE ID = 83821"
cursor.execute(query)
end = time.time()
myresult = cursor.fetchall()
for x in myresult:
    print(x)
print("time taken for query 10 without index:",end - start)

cursor.execute("create index on teaches (ID)")

start = time.time()
query = "SELECT * FROM teaches WHERE ID = 83821"
cursor.execute(query)
end = time.time()
myresult = cursor.fetchall()
for x in myresult:
    print(x)
print("time taken for query 10 with index:",end - start)


# In[34]:


# 11. Drop the index to free up the space.

start = time.time()
query = "ALTER TABLE teaches DROP INDEX idx_teaches_Course_id"
cursor.execute(query)
end = time.time()

print("time taken for query 11 with index:",end - start)


# In[ ]:



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

