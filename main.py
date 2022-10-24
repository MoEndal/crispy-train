            print(f"a) {questions[question_number][1]}")
            print(f"b) {questions[question_number][2]}")
            print(f"c) {questions[question_number][3]}")
            print(f"d) {questions[question_number][4]}")
            print("")
            answer = input("Valitse vastauksesi (a-d):")
            if answer == questions[question_number][5]:
                correct_answers += 1
                question_number += 1
                print("Oikein!")
                print("")
            else:
                print(questions[question_number][6])
                print("Yritä uudestaan.")
                print("")
               
        print(f"Oikeiden vastausten määrä: {correct_answers}")
