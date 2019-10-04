# bin/venv python3
import os

def get_file(data):
    pass

if __name__ == "__main__":

    with open('csv_old_file.csv', mode='r') as file:  
        next(file)
        for line in file:
            line = line.replace('"','').replace('\n', '')
            line = line.split(",")
            line = '"' + line[0] + '"' + ',' + '"' + '-'.join(line[1:]) + '"'
            with open('csv_new_file.csv', mode='a') as new_file:
                new_file.write(line)
                new_file.write("\n")
   
    with open('csv_new_file.csv', mode='rb+') as new_file:
        new_file.seek(-1, os.SEEK_END)
        new_file.truncate()
    