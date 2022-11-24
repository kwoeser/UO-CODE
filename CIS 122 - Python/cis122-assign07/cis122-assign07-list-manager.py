# CIS 122 Fall 2021 assignment 7
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: list manager assignment

command_lst = ['Add', 'Delete', 'List', 'Clear']
command_descrips = ['Add to list', 'Delete Information', 'List Information', 'Clear list']
lst = []

def cmd_help():
    '''Purpose: To help the user understand the commands

    Returns: The command_lst and command_descrips 
    '''
    print("*** Available commands ***")
    for item in range(get_max_list_item_size(t)):
        # Prints the command and the description will using the pad_right function to create
        # a space between them
        print(pad_right(command_lst[item], 10), command_descrips[item])
    print("Empty to exit")


def cmd_add(t):
    '''Purpose: To add items to the list(lst)

    Arg: t: which is going to be the list(lst)
    
    Returns: Adds whatever item is inputted to the list(lst)
    '''
    while True:
            add = input("Enter Infomation (empty to stop): ")
            
            if len(add) == 0:
                break
            # Adds the add input to the list
            lst.append(add)
            print("Added, item count =", len(lst))


def cmd_delete(t):
    '''Purpose: To delete items to the list(lst)

    Arg: t: which is going to be the list(lst)
    
    Returns: deletes whatever item is inputted to the list(lst)
    '''
    while True:
            if len(lst) == 0:
                print("There is nothing in the list to delete")
                break
            
            for items in lst:
                print(pad_right(lst.index(items), 2), items)

            delete = input('Enter number to delete (empty to stop): ')
            if len(delete) == 0:
                break

            # If delete is greater than or equal to the length of the list it's not a possible input
            elif int(delete) >= len(lst):
                print("Enter a number in the index")
                pass

            
            else:
                # lst[int(delete)].isdigit()
                # Deletes the index that is equalivent to the delete input
                del lst[int(delete)]

                if len(lst) == 0:
                    print("All items deleted")
                    break
                
                
                
def cmd_list(t):
    '''Purpose:  Prints the items in the list(lst) and the length of the list

    Arg: t: which is going to be the list(lst)
    
    Returns: The list and the length of it
    '''
    if len(lst) == 0:
            print("List contains", len(lst), 'item(s)')

    # Prints how many items are in the list and the names of each item on different lines
    elif len(lst) > 0:
            print("List contains", len(lst), 'item(s)')
            for items in lst:
                print(items)


def cmd_clear(t):
    '''Purpose:  Clears the list

    Arg: t: which is going to be the list(lst)
    
    Returns: How many items were cleared
    '''
    print(len(lst) ,"item(s) removed, list empty")
    # Clears the list
    lst.clear() 


def get_max_list_item_size(t):
    '''Purpose:  Prints the items in the list(lst) and the length of the list

    Arg: t: which is going to be the list(lst)
    
    Returns: The list and the length of it
    '''
    return len(command_lst)




# Previous assignment
def pad_string(data, size, dir = 'L', character = ' '):
   data = str(data)
   if len(data) > size:
      return data
   elif dir.upper() == 'L':
      return character * (size - len(data)) + data
   else:
      return data + character * (size - len(data))

def pad_left(data, size, character = ' '):
   return pad_string(data, size, 'L', character)


def pad_right(data, size, character = ' '):
   return pad_string(data, size, 'R', character)



while True:
    t = input("Enter a command (? for help): ")
    t = t.strip()

    if len(t) == 0:
        print("Goodbye!")
        break

    # Whatever command is entered that function will be called
    elif 'list' in t:
        cmd_list(lst)


    elif 'add' in t:
        cmd_add(lst)

            
    elif 'clear' in t:
        cmd_clear(lst)


    elif 'del' in t:  
        cmd_delete(lst)

                
    elif '?' in t:
        cmd_help()



    

