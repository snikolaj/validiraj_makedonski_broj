import phonenumbers

def validiraj(broj):
    # prvo trgni sve sto ne e broj
    broj_samo_cifre = ''.join(c for c in broj if c.isdigit())

    # posle vidi dali e 9 cifre
    # ako da, ne treba nisto drugo, samo formatiraj u E164
    if len(broj_samo_cifre) == 9:
        return "+389" + broj_samo_cifre[1:]

    # ako ne, idi preko phonenumbers
    try:
        validiran_broj = phonenumbers.parse(broj, None)
    except:
        return None
    
    if phonenumbers.is_valid_number(validiran_broj):
        #print(phonenumbers.format_number(validiran_broj, phonenumbers.PhoneNumberFormat.E164))
        return phonenumbers.format_number(validiran_broj, phonenumbers.PhoneNumberFormat.E164)
    else:
        return None

validan = "+38975223305"

assert validiraj("075223305") == validan
assert validiraj("+38975223305") == validan
assert validiraj("1234243") == None
assert validiraj("+ 389 75 223 305") == validan
assert validiraj("075 223 305") == validan
assert validiraj("Broj:+38975223305") == validan
assert validiraj("075223305 moj broj") == validan
