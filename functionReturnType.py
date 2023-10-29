# print("this is alexs back")


def format_name(f_name, l_name):
    """This take a first name and last name to format the name """
    if f_name == "" or l_name == "":
        return "You didn't provide valid input."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name(input("What id your first name ?"), input("what is your last name ?"))

print(formated_string)
