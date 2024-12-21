from boxdb import *
from boxdb.support import get_elements


database = "rocketdb"
# create_database(database)

# create_table(database , {'name':"demo"})
# create_column(database,"demo","id" ,data_type="int", primary_key=True)
# create_column(database,"demo","task" , data_type="str",not_null=True)
# create_column(database,"demo","status" , data_type="bool",not_null=True)

# add_row(database,"demo",(1,"try adding some components",False))
# add_row(database,"tasks",(2,"under the class component system",False))
# add_row(database,"tasks",(6,"task2",False))\
# remove_row(database ,"tasks","5")
# task =  get_elements("rocketdb", "tasks","task") 
# status =  get_elements("rocketdb", "tasks","status")

update_row(database, "tasks","1","status","True")


print(get_table(database,"demo"))