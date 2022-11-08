dir = ['run01', 'run18', 'run14', 'run13', 'run12', 'run11', 'run08']
for file in sorted(dir, key=lambda x:int(x.replace('run', ''))):
    print(file)
