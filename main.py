# bin/venv python3
import os

def get_file(data):
    pass
def change_filename(input_filename, output_filename):
    with open(input_filename, mode='r') as file:  
        next(file)
        for line in file:
            line = line.replace('\n', '')
            line = line.split(",")
            line=line[0]+","+'"'+  '-'.join(line[1:]).replace('"','') +'"'



            #line = '"' + line[0] + '"' + ',' + '"' + '-'.join(line[1:]) + '"'
            with open(output_filename, mode='a') as new_file:
                new_file.write(line)
                new_file.write("\n")
   
    with open(output_filename, mode='rb+') as new_file:
        new_file.seek(-1, os.SEEK_END)
        new_file.truncate()
    
if __name__ == "__main__":

    if not os.path.exists(os.path.join(os.getcwd(), "result")):
        os.makedirs(os.path.join(os.getcwd(),"result"))
    for x in os.listdir(os.getcwd()):
        if x.find(".csv")!=-1:
            path_file=os.path.join(os.getcwd(),"result")
            print (path_file)
            change_filename(x,os.path.join(path_file,x))
