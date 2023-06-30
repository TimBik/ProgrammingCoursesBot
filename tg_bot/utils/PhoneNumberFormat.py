import phonenumbers

def number_format(text):
    x = phonenumbers.parse(text, "RU")
    phoneNumber = phonenumbers.format_number(x,phonenumbers.PhoneNumberFormat.E164)
    return phoneNumber
