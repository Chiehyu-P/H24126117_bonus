import random

def create_deck():  #洗牌
    deck=[]
    ranks=['ACE','2','3','4','5','6','7','8','9','10','JACK','QUEEN','KING']
    suits=['SPADE','HEART','DIAMOND','CLUB']
    for r in ranks:
        for s in suits:
            deck.append((r,s))
    random.shuffle(deck)
    return deck

def deal_cards(deck):  #抽牌
    player_hand=[deck.pop(),deck.pop()]
    dealer_hand=[deck.pop(),deck.pop()]
    return player_hand,dealer_hand


def compute_total_value(hand):  #計算手中牌的點數
    total_value=0
    num_aces=0
    for card in hand:
        if card[0] in ['JACK','QUEEN','KING']:  #J,Q,K 加十點
            total_value+=10
        elif card[0]=='ACE':
            num_aces+=1
            total_value+=11
        else:
            total_value+=int(card[0])

    while total_value>21 and num_aces>0:  #當手中點數超過21點,ACE算1點
        total_value-=10
        num_aces-=1
    return total_value

def display_hand(hand,total_value):
    print('Your current value is ',total_value)
    print('With the hand: ',', '.join([f'{card[0]}-{card[1]}' for card in hand]))


def dealers_hand(hand,total_value):
    print('Dealer\'s current value is ',total_value)
    print('With the hand: ',', '.join([f'{card[0]}-{card[1]}' for card in hand]))


def playgame():
    play=input('Want to play again? (y/n): ')
    if play=='y':
        return True
    else:
        return False



while True:
    deck=create_deck()
    player_hand,dealer_hand=deal_cards(deck)

    player_total=compute_total_value(player_hand)
    dealer_total=compute_total_value(dealer_hand)
    display_hand(player_hand,player_total)

    while True:
        player_action=input('Hit or stay? (Hit=1,Stay=0): ')
        if player_action=='1':
            player_hand.append(deck.pop())
            player_total=compute_total_value(player_hand)
            if player_total>21:
                print('Your current value is Bust!(>21)')
                display_hand(player_hand,player_total)
                if playgame()==False:
                    exit()
                elif playgame()==True:
                    tmpt=1
                    break
            display_hand(player_hand,player_total)


        elif player_action=='0':
            break

    while True:
        if tmpt==1:
            break

        dealer_action=input('Hit or stay? (Hit=1,Stay=0): ')

        dealers_hand(dealer_hand,dealer_total)
        dealer_hand.append(deck.pop())
        dealer_total=compute_total_value(dealer_hand)