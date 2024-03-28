def create_an_empty_list():
    return []

def create_a_list():
    return [1,2,3,4]

def add_element_to_end_of_list(l, element):
    list = [create_a_list()]
    return [list, element]

def add_element_to_start_of_list(l, element):
    l.insert(0, element)  # Insert 'element' at the start of the list 'l'
    return l  # Return the modified list

def remove_element_from_end_of_list(l):
    l.pop()  # Remove the last element from the list 'l'
    return l  # Return the modified list 'l'

def remove_element_from_start_of_list(l):
    l.pop(0)  # Remove the last element from the list 'l'
    return l  # Return the modified list 'l'

def retrieve_first_element_from_list(l):
    return l[0]

def retrieve_element_from_index(l, index):
    return l[index]

def retrieve_last_element_from_list(l):
    return l[-1]
