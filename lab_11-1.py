#author CJP 2/8/2022

alma = open("alma_mater.txt", "r")
while True:
     file = alma.readline()
     if len(file) == 0:
           break
     print (file, end="\n")
alma.close()
