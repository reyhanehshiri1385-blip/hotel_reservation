ch = input("yyyy_mm_dd")
from datetime import datetime
ch = datetime.strptime(ch,"%Y_%m_%d")
print(ch)