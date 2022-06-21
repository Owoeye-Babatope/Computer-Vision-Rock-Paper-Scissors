from random import randint

guess_option = ['rock', 'paper', 'sccissors']

def get_computer_choice():
    '''
    
    This function randomly picks from the guess options declared in the file
    and presents it as the computer chosen file.
    
    '''
    guess = randint(0, 2)
    computer_guess = guess_option[guess]
    # print(f"Computer guess: {computer_guess}")
    return computer_guess



def get_user_choice():
    '''
    This function request a number representing eitther

    rock (1)
    paper (2)
    scissors (3)

    accordingly and sets it as the user option and hence returned.

    '''
    
    
    user_input = input('Please choose 1 for rock, 2 for paper, or 3 for sccissors \n')
    user_guess = guess_option[int(user_input)-1]
    # print(f"User guess: {user_guess}")
    return user_guess


def collect():
    user = get_user_choice()
    computer = get_computer_choice()
    
    print(f"user: {user} \ncomputer: {computer}")
    
    
    
    
    


if __name__ == '__main__':
    collect()