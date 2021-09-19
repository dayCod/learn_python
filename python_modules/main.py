# OWN MODULE
# 1 => import module with alliases 
# import module as md 
# 2 => import all function in the module
from module import *
# 3 => import specific function of the module
# from module import biodata

# BUILT IN MODULE
# So much more built in or not build in modules in python, You can explore it 
import datetime as dt

# get_info = md.biodata("Wirandra Alaya Rahman", "07 Feb 2003", "18", "08123456789")
# print(get_info)

now = dt.datetime.now()
get_info = biodata("Wirandra Alaya Rahman", "07 Feb 2003", "18", "08123456789")
print(get_info)
print(f"- Today : {now}") 


