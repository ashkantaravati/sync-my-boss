from jdatetime import datetime, date


def get_kebab_case(string):
    lower_cased_string = string.lower()
    splitted_as_list = lower_cased_string.split(" ")
    kebab_cased = "-".join(splitted_as_list)
    return kebab_cased


def get_formatted_jdatetime(datetime_object, object_type="datetime", show_seconds=True):
    year = datetime_object.year
    month = datetime_object.month
    day = datetime_object.day
    if object_type.lower() == "datetime":
        jobject = datetime(
            year,
            month,
            day,
            datetime_object.hour,
            datetime_object.minute,
            datetime_object.second,
            locale="fa_IR",
        )
        format_rule = "%a, %d %b %Y %H:%M:%S" if show_seconds else "%a, %d %b %Y %H:%M"
        return jobject.strftime(format_rule)
    elif object_type.lower() == "date":
        jobject = date(year, month, day, locale="fa_IR")
        return jobject.strftime("%a, %d %b %Y")
    else:
        raise ValueError("Unexpected argument was passed")


def get_today_formatted_jdatetime():
    return get_formatted_jdatetime(date.today(), object_type="Date")


def get_choices_as_json_serializable(CHOICES, value_key, display_key):
    serializable_choices = [
            {f"{value_key}": choice[0], f"{display_key}": choice[1]}
            for choice in CHOICES
        ]
    return serializable_choices