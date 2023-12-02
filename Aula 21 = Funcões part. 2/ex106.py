from time import sleep


def python_help():

    while True:
        system_intro = "PYTHON'S HELP SYSTEM"
        intro_size = len(system_intro) + 4

        print("~" * intro_size)
        print(f"  {system_intro}")
        print("~" * intro_size)

        user_input = str(input("Function or Library > "))

        if user_input.upper() in 'FIM':
            break

        sleep(0.5)

        system_resp = f"ACCESSING THE MANUAL OF THE COMMAND '{user_input}'"
        resp_size = len(system_resp) + 4

        print("~" * resp_size)
        print(f"  {system_resp}")
        print("~" * resp_size)

        sleep(0.5)

        print(help(user_input))

        sleep(2)


python_help()
