with open("./Input/Names/invited_names.txt")as names:
    peopleNames=names.readlines()

with open("./Input/Letters/starting_letter.txt") as firstLetter:
    letter=firstLetter.read()
    for name in peopleNames:
        endLetter=letter.replace("[name]",name.strip())
        with open(f"./output/letters/sendLetter {name}.txt","w")as send:
            send.write(endLetter)
