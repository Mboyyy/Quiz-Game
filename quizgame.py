from multiprocessing.connection import answer_challenge

print("Selamat datang di quiz komputer!!")

playing = input("Kamu ingin bermain? ")

text = "Mboy ganteng"
if playing.lower() != "mau":
    quit()

print("Okayy!! ayo kita bermain :)")
score = 0

answer = input("Apa yang itu CPU? ")
if answer == "central processing unit":
    print('Benar!!')
    score += 1
else:
    print("Salah!")

answer = input("Apa itu GPU? ")
if answer == "graphic processing unit":
    print('Benar!')
    score += 1
else:
    print("Salah!")

answer = input("Apa itu RAM? ")
if answer == "random access memory":
    print('Benar!')
    score += 1
else:
    print("Salah!")

answer = input("Apa itu PSU? ")
if answer == "Power Supply":
    print('Benar!')
    score += 1
else:
    print("Salah!")

answer = input("Apa itu MB? ")
if answer == "motherboard":
    print('Benar!')
    score += 1
else:
    print("Salah!")

print("GG GAMING!!")
print("Kamu dapat score " + str(score) + " pertanyaan yang benar")
print("Kamu dapat " + str((score / 4) + 100) + "%.")