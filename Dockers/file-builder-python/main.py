file1 = open("./../output_mount/myfile.txt","w") 
L = ["This is Delhi \n","This is Paris \n","This is London \n"]  
  
# \n is placed to indicate EOL (End of Line) 
file1.write("Hello \n") 
file1.writelines(L) 
file1.close() #to change file access modes 
  
print("Execution done")