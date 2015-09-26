from sys import argv

script, filename, line = argv

def case1_write(file,line):
    file.write(line)
    file.write(" wrote\nNow printing:")
    
def case2_print(file, line):
    print >>file, line

file = open(filename, 'a')
case1_write(file,line)
case2_print(file, line)
file.close()