import os
import subprocess
import json
import argparse

# PATH_TO_JAR_FILE ="C:\\Users\\Mikolaj\\Downloads\\jar_files\\json-20240303.jar"  # SYSTEM DEPENDENT
PATH_TO_JAR_FILE = "/Users/mikolajmachalski/Downloads/json-20240303.jar"
def process_files(directory):
    current_directory = os.getcwd()
    print(current_directory)
    print('dir')
    print(directory)
    absolute_path = os.path.join(current_directory,directory)
    list_of_dict=[]
    dict_with_filename ={}
    for textfile in os.listdir(absolute_path):
        textfile_path = os.path.join(directory,textfile)
        print(textfile_path)
        if os.path.isfile(textfile_path):
            """
            System dependent, 
            console line:
            type TextFiles/Text1.txt | java -cp "C:\\Users\Mikolaj\Downloads\jar_files\json-20240303.jar" JavaReader/src/Main.java
            Must be in "Lista3" directory to launch that
            
            """
            command1 = f'cat {textfile_path}'
            command2 = f'java -cp {PATH_TO_JAR_FILE} JavaReader/src/Main.java'

            process1 = subprocess.Popen(command1, stdout=subprocess.PIPE, shell=True)
            process2 = subprocess.Popen(command2, stdin=process1.stdout, stdout=subprocess.PIPE, shell=True)

            output, _ = process2.communicate()
            dict_from_json = json.loads(output)
            dict_with_filename[textfile]=dict_from_json
            list_of_dict.append(dict_with_filename)
    print(dict_with_filename)








def main():
    parser = argparse.ArgumentParser(description='ULUMULU')
    parser.add_argument('file', nargs='?', help='Sciezka do pliku')
    args = parser.parse_args()
    directory = args.file
    process_files(directory)









if __name__ =="__main__":
    main()
