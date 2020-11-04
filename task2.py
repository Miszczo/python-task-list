
answer_1 = ["1", "1."]
answer_2 = ["2", "2."]
answer_3 = ["3", "3."]
answer_4 = ["4", "4."]


required = ("\nUse only 1, 2, 3, or 4\n")

taskList = r"TaskList\list.csv"

def task_add():
    with open(taskList, 'a') as f:
        f.write("\n#" + " ")
        f.write(input(">> "))


def task_show():
            f = open(taskList)
            print(f.read())
            f.close()
def task_delete():
    open(taskList, 'w').close()

def main():

    print("---Welcome in your personal task list---\n"
          "what you wanna do?\n")
    print("chose number:\n"
          "1. Add task\n"
          "2. Edit task\n"
          "3. Show list\n"
          "4. Delete")
    choice = input(">>> ")

    if choice in answer_1:
        task_add()
    #     doesn't work
    # elif choice in answer_2:
    #     print("something")
    elif choice in answer_3:
        task_show()
    elif choice in answer_4:
        task_delete()
    else:
        print(required)

if __name__ == "__main__":
    main()


