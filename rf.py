import os
import pdb
def my_file(filename):
    file_h = open(filename, 'r')
    con=file_h.read()



path = 'C:\\Users\\Rajat kushwaha\\Downloads\\enron1\\ham'

files = []
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        filename = "{}\{}".format(path, file)
        #pdb.set_trace()
        #file_h =open(filename, 'r')
        my_file(filename)



