
answer_1 = ["1", "1."]
answer_2 = ["2", "2."]
answer_3 = ["3", "3."]



required = ("\nUse only 1, 2,or 3\n")

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
        "2. Show tasks\n"
        "3. Delete")
    choice = input(">>> ")

    if choice in answer_1:
        task_add()
    elif choice in answer_2:
        task_show()
    elif choice in answer_3:
        task_delete()
    else:
        print(required)

if __name__ == "__main__":
    main()


