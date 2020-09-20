""" Rock Papper Scissors! Written by Qi Zhao"""
from random import choice
from typing import Dict, List

def get_usr_choice() -> str:
    """ 
    get usr choice from typing r for rock, p for paper, s for scissors. If usr gives q for quit, then return quit
    """
    usr_choice: str = input("Please choose 'R', 'P', 'S' or 'Q' to quit: ")
    if usr_choice == 'q' or usr_choice == 'Q':
        print("Thanks for playing!")
        return "quit"
    elif usr_choice.lower() == 'r' or usr_choice.lower() == 'p' or usr_choice.lower() == 's':
        return usr_choice.lower()
    else:
        print("Invalid Input! Please choose from 'R','P','S',or 'Q'. ")
        return "retry"
    
def get_computer_choice() -> str:
    """
    get computer choice from random function.
    """
    return choice(['r','p','s'])

def main() -> None:
    """ get user choice and then get computer choic """
    game_rules: Dict = {'r':{'r':'Tie','p':'Lose','s':'Win'},
                        'p':{'r':'Win','p':'Tie','s':'Lose'},
                        's':{'r':'Lose','p':'Win','s':'Tie'},
                        }
    game_dialogue: Dict = {"p":"paper breaks rock", "r":"rock breaks scissors", "s":"scissors breaks paper"}
    game_choice: Dict = {"p":"paper", "r":"rock", "s":"scissors"}
    while True:
        usr_choice: str = get_usr_choice()
        if usr_choice == "quit":
            break
        elif usr_choice == "retry":
            continue
        comp_choice: str = get_computer_choice()
        game_result: str = game_rules[usr_choice][comp_choice]
        if game_result == "Win":
            print(f"{game_dialogue[usr_choice]} - You Win!")
        elif game_result == "Lose":
            print(f"{game_dialogue[comp_choice]} - I Win!")
        else:
            print(f"Tie: We both choose {game_choice[usr_choice]}")

if __name__ == '__main__':
    main()