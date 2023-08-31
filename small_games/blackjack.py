# import required packages
import random as rd

def main():
    '''Main function where Blackjack is played'''

    # initial variables like playing card values and players in the game defined
    sam, dealer, full_deck = generate_initial_hands()


    # check if either player has won the game
    if sum(sam) == 21 and sum(dealer) == 21:
        print("You both have Blackjack! The game is a tie. Sam: {}, Dealer: {}".format(sum(sam), sum(dealer)))
        exit()
    elif sum(sam) == 21:
        print("Sam has Blackjack and the dealer does not. Sam wins! Sam: {}, Dealer: {}".format(sum(sam), sum(dealer)))
        exit()
    elif sum(dealer) == 21:
        print("The dealer has Blackjack and Sam does not. The dealer wins! Sam: {}, Dealer: {}".format(sum(sam),
            sum(dealer)))
        exit()

    # game proceeds if neither player has won
    print("Neither player has Blackjack. The game will proceed...")

    # Sam draws until he has 17 or more points, the dealer draws until he has more points than Sam, or 21
    sam = draw_until_17_or_more(sam, full_deck)
    dealer = draw_until_more_than_sam_or_lose(dealer, sam, full_deck)

    # conclusion of game
    if sum(sam) < 21 and sum(dealer) >= 21:
        print("Sam wins by the dealer going bust! Sam: {}, Dealer: {}".format(sum(sam), sum(dealer)))
    elif sum(sam) == 21 and sum(dealer) > 21:
        print("Sam wins by Blackjack and the dealer going bust! Sam: {}, Dealer: {}".format(sum(sam), sum(dealer)))
    elif sum(sam) > 21:
        print("Sam loses by going bust! Sam: {}, Dealer: {}".format(sum(sam), sum(dealer)))
    elif sum(sam) < 21 and sum(dealer) > sum(sam) and sum(dealer) < 21:
        print("Sam loses because the dealer outscored him. Sam: {}, Dealer: {}".format(sum(sam), sum(dealer)))
    elif sum(sam) < 21 and sum(dealer) == 21:
        print("Sam loses because the dealer wins by Blackjack! Sam: {}, Dealer: {}".format(sum(sam), sum(dealer)))
    elif sum(sam) == 21 and sum(dealer) == 21:
        print("Both Sam and the dealer got Blackjack! It's a tie! Sam: {}, Dealer: {}".format(sum(sam), sum(dealer)))
    elif sum(sam) == sum(dealer):
        print("Both Sam and the dealer got the same amount of points. It's a tie! Sam: {}, Dealer: {}"
              .format(sum(sam), sum(dealer)))


def draw_until_17_or_more(drawee, full_deck):
    '''This function draws cards until the drawee's total is 17 or more'''
    while sum(drawee) < 17:
        random_element = rd.choice(full_deck)
        drawee.append(random_element)
        full_deck.remove(random_element)
    return drawee

def draw_until_more_than_sam_or_lose(drawee, sam, full_deck):
    '''This function draws cards until the drawee's total is higher than Sam's total or equal to 21'''
    while sum(drawee) < sum(sam):
        random_element = rd.choice(full_deck)
        drawee.append(random_element)
        full_deck.remove(random_element)
        if sum(drawee) == 21:
            return drawee
    return drawee

def generate_initial_hands():
    full_deck = [2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10,
                 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 11, 11, 11, 11]
    sam = []
    dealer = []
    while len(sam) < 2:
        random_element = rd.choice(full_deck)
        sam.append(random_element)
        full_deck.remove(random_element)
    while len(dealer) < 2:
        random_element = rd.choice(full_deck)
        dealer.append(random_element)
        full_deck.remove(random_element)
    return sam, dealer, full_deck

main()





