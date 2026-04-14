import random
sec=random.randint(1,50)
attempt=0
while True:
 guess=int(input("guess the number btw 1 to 50:   "))
 if (guess>sec):
    print("tooo high get low number brother ")
 elif(guess<sec):
    print("hmm small number think for big")
 elif(guess==sec):
    print("ohh man you guess it correct you won")
    break
    