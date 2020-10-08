def get_kebab_case(string):
    lower_cased_string = string.lower()
    splitted_as_list = lower_cased_string.split(" ")
    kebab_cased = "-".join(splitted_as_list)
    return kebab_cased