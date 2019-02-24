shopping_list = []
   #add items,see items. you want ot enter "DONE" - Show .Ask for help
def add_to_list(item):
    shopping_list.append(new_item)
    print("Added ! List has {} item".format(len(shopping_list)))

def show_help():
    print("What should be picked up at the store ?")
    print(''' 
    Enter 'DONE' to stop adding items
    Enter 'HELP' for help
    Enter 'SHOW' to see your current list
    ''')

def show_list():
    print("Here is your list:")
    for item in shopping_list:
        print(item)

show_help()

while True:
    new_item = input("> ")
    if new_item == 'DONE':
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == 'SHOW':
        show_list()
        continue
    add_to_list(new_item)

show_list()

# if __name__ == "__main__":
#     main()