import pathlib
import os

origcwd = pathlib.Path().resolve()

current_folder = origcwd.joinpath("CodingNomads/Python_201/course_resources/07_apis")

os.chdir(current_folder)

import tmt_mysql_101 as sql

# 1) get info about film & category tables

# 2) 
    # TODO:
    # all actors with name of my choice
    # all actors & films they've been in
    # all actors who appeared in a comedy category of your choice
    # all comedy films ordered by rental rate
    # add a group by to either above
    # add a order by to either above
# 3)
    # TODO:
    # update all films in film table --> rental_duration = 10 IF movie length > 150
# 4)
    # TODO:
    # app to interface w new DB
    #   # create 3+ tables
    #   # insert + update + delete data in tables
    #   # join tables

# 5)
    # TODO:
    # get users data from the API from earlier
    # store in local DB
    # add check for record existence before inserting in DB
