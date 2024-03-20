import sys
from os import environ

def print_env_variables(*args):
    filtered_variables={}

    if args:
        print("dupa")
        for env in environ:
            for arg in args:

                if env.lower() in arg.lower():
                    filtered_variables[env]=environ[env]
                    break
    else:
        filtered_variables=environ

    sorted_vars=sorted(filtered_variables.items(),key=lambda x:x[0])

    for k,v in sorted_vars:
        print(f"{k}={v}")





if __name__=="__main__":
    list_of_filtering_names = sys.argv[1:]
    print_env_variables(*list_of_filtering_names)
