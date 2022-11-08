import os
for top, dirs, files in os.walk('/home/samsky/Documents/'):
    for nm in files:       
        print os.path.join(top, nm)
