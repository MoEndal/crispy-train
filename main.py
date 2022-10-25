
correct_answers = 0
question_number = 0

#Kysymyksiä - lista?
questions = [("Missä kaupungissa ystäväsi asuu?", "Helsinki", "Tampere", "AWS city", "Pori", "c", "Etkö edes tiedä missä ystäväsi asuu?"),("Kuinka monta olutta juot junamatkalla?", "0", "3", "6", "12", "d", "Etkö osaa juoda tarpeeksi? Häpeä.")]


play_the_game = input("Lähdetkö ystävän luokse junan kyydillä? (n/y)")

if play_the_game == "n":
    print("Jää sitten kotiin! ")


elif play_the_game == "y":

    while True:
        continuing = input("Jatkatko matkaa? (y/n)")
        print("")
        if continuing == "n":
            break
        if continuing == "y":
            print(questions[question_number][0])

