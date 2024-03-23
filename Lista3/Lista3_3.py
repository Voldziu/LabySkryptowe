import time,sys,os,argparse

"""
command line for that: 
cat plik.txt | python Lista3_3.py

python Lista3_3.py plik.txt --lines=10 --follow
"""

def tail_printer_input(input,num_lines):
    lines = input.readlines()
    if len(lines) <= 10:
        print("".join(lines), end='')
    else:
        print("".join(lines[-num_lines:]), end='')

def tail_printer(filename, num_lines):


    if not os.path.exists(filename):
        print("Plik nie istnieje")
        return
    with open(filename,'r',encoding='utf-8') as file:
        tail_printer_input(file,num_lines)





def tail():
    parser = argparse.ArgumentParser(description='ULUMULU')
    parser.add_argument('file',nargs='?',help='Sciezka do pliku')
    parser.add_argument('--lines',type=int,default=10,help='Liczba linij do printowania')
    parser.add_argument('--follow',action='store_true',help='ciagle sledzenie')

    if_pipe=  not sys.stdin.isatty()
    args = parser.parse_args()


    if not if_pipe:
        input=args.file
        tail_printer(input,args.lines)
    else:
        input=sys.stdin
        print(input)
        tail_printer_input(input,args.lines)

    if args.follow:
        try:
            with open(args.file,'r') as file:
                file.seek(0,os.SEEK_END)
                while True:
                    current_position=file.tell()
                    line = file.readline()
                    if not line:
                        time.sleep(0.2)
                        current_size=os.stat(args.file).st_size
                        if current_position>current_size:
                            file.seek(0)
                    else:
                        sys.stdout.write(line)
                        sys.stdout.flush()

        except KeyboardInterrupt:
            print("\n Zakonczenie sledzenia pliku")


if __name__=="__main__":
    tail()


