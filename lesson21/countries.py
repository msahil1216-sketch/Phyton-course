# Class 1
class India():
    def capital(self):
        print("New Delhi is the capital of India")

    def language(self):
        print("Hindu is the most widely spoken language of India")

    def type(self):
        print("India is a developing country.")

# Class 2
class Japan():
    def capital(self):
        print("New Tokyo is the capital of Japan")

    def language(self):
        print("Japanese is the most widely spoken language of japan")

    def type(self):
        print("Japan is a developed country.")

# Object Creation
obj_ind = India()
obj_jap = Japan()

# Common interface
for country in (obj_ind, obj_jap):
    country.capital()
    country.language()
    country.type()

