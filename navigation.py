import json

def read_json(path):
    """reads json file 
    and returns dict or list"""
    try:
        with open(path, 'r', encoding='utf-8') as j:
            info=json.load(j)
    except:
        print("This is not a json file. Please try again.")
        raise SystemExit()
    return info

def list_navig(lst):
    """navigation in list"""
    length=len(lst)
    print(f"This element is a list. It contains {length} elements.")
    print("You can enter number of element (starting from 0), and we will follow it,\
or enter 'show' to show its elements.")
    counter=0
    j=1
    while j!=0:
        written=input("Your choise: ")
        if written=='show':
            if length<=5 or length-counter<=5:
                for i in range(counter, length):
                    print(f"{i}: {lst[i]}")
                counter+=i
                print("Choose number of element or 'exit' to exit this programm")
            else:
                for i in range(5):
                    print(f"{counter+i}: {lst[counter+i]}")
                if counter==0:
                    print("...\nThese are first 5 elements. Enter the number, or 'show' to show 5 more, or 'exit' to exit.")
                else:
                    print("...\nThese are next 5 elements. Enter the number, or 'show' to show 5 more, or 'exit' to exit.")
                counter+=5
        elif written=='exit':
            raise SystemExit()
        else:
            try:
                element=lst[int(written)]
                j=0
            except:
                print("Something is not correct.\nPlase try again. You can enter 'exit' to exit programm.")
    main_navig(element)

def dict_navig(dct):
    """navigation through dict"""
    length=len(dct)
    print(f"This is a dictionary. It contain {length} items.")
    print("You can enter the key, and we will follow it,\
or enter 'show' to show the elements.")
    j=0
    while j==0:
        written=input("Your choise: ")
        if written=='show':
            print(dct)
            print("Choose the key or 'exit' to exit this programm")
            # else:
            #     for i in range(5):
            #         print(dct[i])
                # if counter==0:
                #     print("...\nThese are first 5 elements. Enter the key, or 'show' to show 5 more, or 'exit' to exit.")
                # else:
                #     print("...\nThese are next 5 elements. Enter the key, or 'show' to show 5 more, or 'exit' to exit.")
                # counter+=5
        elif written=='exit':
            exit()
        elif written in dct.keys():
            main_navig(dct[written])
            j=1        
        else:
            print("Something is not correct.\nPlase try again. You can enter 'exit' to exit programm.")

def main_navig(object):
    """the main navigation"""
    if type(object)==list:
        list_navig(object)
    elif type(object)==dict:
        dict_navig(object)
    else:
        print(f"The final element is '{object}', type = {type(object)}")
    

if __name__=="__main__":
    file_path=input("Please input the json file path: ")
    dict_file=read_json(file_path)
    main_navig(dict_file)