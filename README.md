# validiraj_makedonski_broj
Python skripta za validiranje makedonski telefonski broj

Treba da se ima phonenumbers (preko `pip install phonenumbers`)

Moze da validira i stranski telefonski broevi (samo INTERNATIONAL format)

Za samo makedonska validacija, smeni `phonenumbers.parse(broj, None)` u `phonenumbers.parse(broj, "MK")`
