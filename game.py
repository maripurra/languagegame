def age_prompt():
    age = None
    try:
        age = int(input("Kuinka vanha olet?"))
        return age
    except:
        print("Not a number")
        return age_prompt()


print("KEILIR GAME")
what = input("Mitä kuuluu?")

if what == "hyvää":
    print("kiva juttu")
elif what == "hyvaa":
    print("Tarkoititko hyvää?")
else:
    print("no höh")

your_name = input("Mikä on nimesi?")
print("Moi, {}!".format(your_name))

if your_name == "Vignir":
    print("Olet islantilainen!")
elif your_name == "Ile" or your_name == "Ilmari":
    print("Olet siis suomalainen!")
else:
    print("Onhan se nimi sekin :-)")
# age = age_prompt()

age = None

while True:
    try:
        age = int(input("Kuinka vanha olet?"))
        break
    except:
        print("Not a number!")
        continue

print("Your age is: {}".format(age))

if age > 34:
    print("You are so old")
elif age == 33:
    print("WOW")
else:
    print("You are still young")

print("Mukavaa päivänjatkoa!")
