import os 
    
# path
path = 'docs' 
try: 
    os.mkdir(path) 
except OSError as error: 
    print(error)

# path 2
path2 = 'output'
try:
    os.mkdir(path2) 
except OSError as error: 
    print(error)