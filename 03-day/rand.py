from random import randint


def game():
    counter = 0
    rand = randint(1, 100)
    while True:
        try:
            user_tipp = int(
                input('Gondoltam egy számra 1 és 100 között, add meg a tipped:'))
            counter += 1
            if user_tipp > rand:
                print('Kisebb számra gondoltam')
            elif user_tipp < rand:
                print('Nagyobb számra gondoltam')
            else:
                print(f'Eltaláltad {counter} próbálkozásból')
            break
        except:
            print('Ez nem egy 1 és 100 közötti szám')
        finally:
            print(f'AZ eddigi próbálkozások száma: {counter}')


game()
