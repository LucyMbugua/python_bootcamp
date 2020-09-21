#dictionary
my_details ={"first_name": "lucy",
              "last_name": "Wanjiku",
              True: "it is true",
              10:"Ten",
              "interests": ["cooking", "fishing"],
              "isHappy": False,
              "parents": {
                  "mother": {
                      "fname":"Jane",
                      "lname": "Doe",
                      "age":10
                    }, 
                    "father": {
                      "fname":"Peter",
                      "lname": "Doe",
                      "age":15
                    },
                }
            }
#print(my_details["interests"])
print(my_details["parents"]["father"]["fname"])
my_details["parents"]["father"]["fname"] = "Kimani"

#copy method
original = {1:"Jan", 2:"feb"}
new = original.copy()
print ("Original:", original)
print("New:",  new)

#pop method
# random fruits dictionary
fruits = { "apple": 2, "orange": 3, "grapes": 4 }

element = fruits.pop("apple")
print("The popped element is:", element)
print("The dictionary is:", fruits)

#clear method
moy = {1: "Jan", 2: "Feb"}

moy.clear()
print("moy =", moy)

#input method


