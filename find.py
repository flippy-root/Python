import os
from glob import glob
result = [y for x in os.walk(PATH) for y in glob(os.path.join(x[0], '*.txt'))]

