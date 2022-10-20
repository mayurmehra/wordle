import random

def check(guess:str, answer:str) -> bool:
    actual = list(answer.upper())
    response = list(guess.upper())
    
    for i in range(len(actual)):
        if response[i] != actual[i]:
            if response[i] in actual:
                response[i] = response[i].lower()
            else:
                response[i] = '_'
    return response


def main(answer):
    counter = 6
    while True:
        guess = input('Enter your guess:')

        if guess.isalpha() and len(guess)==5 and guess in words:
            if guess != answer:
                response = check(guess,answer)
                print(' '.join(response))

                counter -= 1
                if counter == 0:
                    print("You have run out of guesses. The word was:" , answer)
                    break
                print(f'You have {counter} guesses left')
                
            else:
                print('You Won!')
                break

        else:
            print('Invalid guess')
            continue

words = []
with open('wordlist.txt', 'r') as file:
    words = file.readlines()
for i in range(len(words)):
    words[i] = words[i][:5]

answer = random.choice(words)
words = set(words)

main(answer)