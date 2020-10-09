from jdatetime import datetime


def get_kebab_case(string):
    lower_cased_string = string.lower()
    splitted_as_list = lower_cased_string.split(" ")
    kebab_cased = "-".join(splitted_as_list)
    return kebab_cased


def get_formatted_jdatetime(datetime_object):
    jobject = datetime(
        datetime_object.year,
        datetime_object.month,
        datetime_object.day,
        datetime_object.hour,
        datetime_object.minute,
        datetime_object.second,
        locale='fa_IR'
    )
    return jobject.strftime("%a, %d %b %Y %H:%M:%S")
