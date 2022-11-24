# CIS 122 Fall 2021 assignment 8
# Author: Karma Woeser
# Partner: Your Partner
# References: 
# Description: group manager assignment


# Dictionaries
groups = {}

# Lists
command_lst = ['?','C','G','A','L','X']
command_descrips = ['list Commands','Create A new group','List groups',
'Add data to a group','List data for a group','Exit']


def create_group(d):
    '''Purpose: Creates a group and the it's field inputs.

    Arguments: d: which is the dictionary (groups)

    Returns: Will create a group an add items into a field_lst
    '''
    while True:
        group_name = input("Enter group name (empty to quit): ")
        group_name.strip()
        
        if len(group_name)== 0:
            break

        elif group_name in groups :
            print("Group already exists")
            
        else:
            # Creates an list that will be added to the dictionary 
            key_lst = []
            while True:
                key_name = input('Enter field name (Empty to stop): ')

                if len(key_name) == 0:
                    break
            
                else:
                    key_lst.append(key_name)

            # Adds key_lst to the dictionary
            groups[group_name] = {'_keys_': key_lst, '_data_':[]}
            

    
def list_groups(d):
    '''Purpose: Lists the groups 

    Arguments: d: which is the dictionary (groups)

    Returns: Prints the group name, total number of keys, and the keys
    '''
    
    print("**List of groups**")
    for group in groups:
        print(group + ":", len(d[group]['_keys_']), 'properties', d[group]['_keys_'])



def add_group_data(d):
    '''Purpose: Adds data to the keys in the dictionary

    Arguments: d: which is the dictionary (groups)

    Returns: Adds data to the keys
    '''
    print("** Add group data **")
    list_groups(groups)
    print()
    
    while True:
        group_name = input('Enter group name (empty to cancel): ')

        if len(group_name)== 0:
            break

        elif group_name not in groups:
            print("This group does not yet exist. You have create one.")
            pass
        
        else:
            # Creates an list that will be added to the dictionary 
            added_data = []

            # Loops through the keys in the groups dictionary
            for group in groups[group_name]['_keys_']:
                data_item = input("Enter " + group + ':')


                added_data_lst.append(data_name)
                

        # Adds the data to the dictionary (groups) and keeps the keys the same
        groups[group_name] = {'_keys_': [] , '_data_': added_data_lst}
        print(added_data_list)
        print(groups[group_name])
            
                

# Unforuntaly, got stuck on this one and didn't have time to come to office hours
def list_group_data(d):
    pass
            

        
print(">> Welcome to Group Manager <<")
print("This program creates groups with dynamic properties")
while True:
    print()
    cmd = input('Command (Empty or X to quit, ? for help): ')
    cmd.strip()

    if len(cmd) == 0 or cmd.upper() == 'X':
        break

    # Whatever command is entered that function will be called (similar to the list mangaer)
    elif cmd == '?':
        for item in range(len(command_lst)):
            print(command_lst[item] + ': ' + command_descrips[item])

    elif cmd == 'c':
        create_group(groups)

    elif cmd == 'g':
        list_groups(groups)

    elif cmd == 'a':
        add_group_data(groups)

    elif cmd == 'l':
        list_group_data(groups)

    else:
        print("Not a real command")
        pass



