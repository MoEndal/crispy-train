
elif play_the_game == "y":

    while True:
        continuing = input("Jatkatko matkaa? (y/n)")
        print("")
        if continuing == "n":
            break
        if continuing == "y":
            print(questions[question_number][0])
