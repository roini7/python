from mystuff.texas_holdem import deck
card_count = 52
NULL = 0
ONE = 1
hand = []
rank_choice = index = suit_choice = 0
print("Welcome to the _Texas HoldEm_ simulator! ")

for i in range(2):
    while (1 > rank_choice or rank_choice > index + 1) or (1 > suit_choice or suit_choice > 4):  # stay in loop until
        print("Please choose your {} card rank from the deck: ".format(i + 1))               # 2 valid cards are chosen
        for index, rank in enumerate(deck):
            print("{}: {}".format(index + 1, rank[0]))  # print rank choice
        rank_choice = int(input())
        if 1 <= rank_choice <= index + 1:
            print("""Please choose your cards suit:
                     \n1.clubs\n2.diamonds\n3.hearts\n4.spades""")  # print suit choice
            suit_choice = int(input())
            if 1 <= suit_choice <= 4:  # double 'if' to verify valid choices within loop
                if deck[rank_choice - 1][1][1][suit_choice - 1] == NULL:  # check if chosen card in deck
                    print("Card not in deck")
                    rank_choice = 0
                    continue
                deck[rank_choice - 1][1][1][suit_choice - 1] = NULL  # if not in deck update deck values
                print("Your {} card is : {} , {}"
                      .format(i + 1, deck[rank_choice - 1][0], deck[rank_choice - 1][1][0][suit_choice - 1]))
                hand.append(deck[rank_choice - 1][0])
                hand.append(deck[rank_choice - 1][1][0][suit_choice - 1])
                card_count = card_count - 1
    rank_choice = 0

print("=" * 40)
print("""Your hand is :
1. {} , {}
2. {} , {}
There are {} cards in the deck.""".format(hand[0], hand[1], hand[2], hand[3], card_count))  # print hand and card count

menu = 0

while menu != 4:
    print("""Select from the menu what you would like to do next:
    1.Discard a card
    2.Calculate the chance of drawing a card
    3.View deck
    4.Exit""")
    menu = int(input())

    if menu == 1:
        print("Please select a card rank from the deck: ")
        for index, rank in enumerate(deck):
            print("{}: {}".format(index + 1, rank[0]))
        rank_choice = int(input())
        if 1 <= rank_choice <= index + 1:
            print("""Please choose your cards suit:
                     \n1.clubs\n2.diamonds\n3.hearts\n4.spades""")
            suit_choice = int(input())
            if 1 <= suit_choice <= 4:
                if deck[rank_choice - 1][1][1][suit_choice - 1] == NULL:
                    print("Card not in deck")
                    continue
                else:
                    deck[rank_choice - 1][1][1][suit_choice - 1] = NULL
                    card_count = card_count - 1
                    print("The card you chose is : {} , {}\nthere are {} in the deck"
                          .format(deck[rank_choice - 1][0], deck[rank_choice - 1][1][0][suit_choice - 1], card_count))
                print("=" * 40)
    elif menu == 2:  # calculate chance of drawing a card from deck based on card count
        print("Please select a card rank from the deck: ")
        for index, rank in enumerate(deck):
            print("{}: {}".format(index + 1, rank[0]))
        rank_choice = int(input())
        if 1 <= rank_choice <= index + 1:
            print("""Please choose your cards suit:
                     \n1.clubs\n2.diamonds\n3.hearts\n4.spades""")
            suit_choice = int(input())
            if deck[rank_choice - 1][1][1][suit_choice - 1] != NULL:
                print("The chance of drawing {} , {}"
                      .format(deck[rank_choice - 1][0], deck[rank_choice - 1][1][0][suit_choice - 1]))
                print("is : {0:.0%}".format(1./card_count))  # how do i show decimal values in %
            else:
                print("This card has already been drawn")
    elif menu == 3:  # print table of deck module , how to aline table in python
        print("\t\t\t", end="")
        for rank in deck:
            print("{}\t|\t".format(rank[0]), end="")
        print("")
        print("clubs:   ", end="")
        for rank in deck:
            print("\t{}\t".format(rank[1][1][0]), end="")
        print("")
        print("diamonds:", end="")
        for rank in deck:
            print("\t{}\t".format(rank[1][1][1]), end="")
        print("")
        print("hearts:   ", end="")
        for rank in deck:
            print("\t{}\t".format(rank[1][1][2]), end="")
        print("")
        print("spades:   ", end="")
        for rank in deck:
            print("\t{}\t".format(rank[1][1][3]), end="")
        print("")
        print("=" * 150)

    elif menu == 4:
        print("Thanks for playing!")
        break
