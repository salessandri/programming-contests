#!/usr/bin/env python3

########################################################################
#   Solves problem 54 from projectEuler.net.
#   Determines the number of poker hands won by player 1.
#   Copyright (C) 2010  Santiago Alessandri
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#    
#   You can contact me at san.lt.ss@gmail.com or salessandri@nasel.com
#   Visit my wiki at http://san-ss.wikidot.com
########################################################################

class PokerHand:
    
    def __init__(self, cards):
        self.cards = cards
        
    @classmethod
    def create_hand(cls, cards):
        new_cards = []
        numbers = {}
        for n, c in cards:
            if n == 'T':
                n = 10
            elif n == 'J':
                n = 11
            elif n == 'Q':
                n = 12
            elif n == 'K':
                n = 13
            elif n == 'A':
                n = 14
            else:
                n = int(n)
            new_cards.append((n,c))
            
            numbers[n] = numbers.get(n, 0) + 1
        
        is_flush = len(set([c for n,c in new_cards])) == 1
        is_straight = len(numbers) == 5 and (max(numbers) - min(numbers) == 4 or set([2, 3, 4, 5, 14]) == set(numbers.keys()))
        
        if is_flush and is_straight:
            if set([2, 3, 4, 5, 14]) == set(numbers.keys()):
                numbers[1] = 1
                del numbers[14]
            return StraightFlush(numbers)
        
        if is_flush:
            return Flush(numbers)
        
        if is_straight:
            if set([2, 3, 4, 5, 14]) == set(numbers.keys()):
                numbers[1] = 1
                del numbers[14]
            return Straight(numbers)
        
        card_counts = sorted(numbers.values())
        
        if card_counts == [1,4]:
            return Poker(numbers)
        
        if card_counts == [2,3]:
            return FullHouse(numbers)
        
        if card_counts == [1,1,3]:
            return ThreeOfAKind(numbers)
        
        if card_counts == [1,2,2]:
            return DoublePair(numbers)
        
        if card_counts == [1,1,1,2]:
            return Pair(numbers)
        
        return HighCard(numbers)

class StraigthFlush(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsStraightFlush(self)
    
    def beatsStraightFlush(self, poker_hand):
        return max(self.cards) > max(poker_hand.cards)
    
    def beatsPoker(self, poker_hand):
        return True
    
    beatsFullHouse = beatsFlush = beatsStraight = beatsThreeOfAKind = beatsDoublePair = beatsPair = beatsHighCard = beatsPoker

class Poker(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsPoker(self)
    
    def beatsStraightFlush(self, poker_hand):
        return False
    
    def beatsPoker(self, poker_hand):
        poker_card_me = next(filter(lambda k: self.cards[k] == 4, self.cards))
        poker_card_other = next(filter(lambda k: poker_hand.cards[k] == 4, poker_hand.cards))
        if poker_card_me > poker_card_other:
            return True
        else:
            return False
    
    def beatsFullHouse(self, poker_hand):
        return True
    
    beatsFlush = beatsStraight = beatsThreeOfAKind = beatsDoublePair = beatsPair = beatsHighCard = beatsFullHouse

class FullHouse(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsFullHouse(self)
    
    def beatsStraightFlush(self, poker_hand):
        return False
    
    beatsPoker = beatsStraightFlush
    
    def beatsFullHouse(self, poker_hand):
        full_card_me = next(filter(lambda k: self.cards[k] == 3, self.cards))
        full_card_other = next(filter(lambda k: poker_hand.cards[k] == 3, poker_hand.cards))
        return full_card_me > full_card_other

    def beatsFlush(self, poker_hand):
        return True
    
    beatsStraight = beatsThreeOfAKind = beatsDoublePair = beatsPair = beatsHighCard = beatsFlush

class Flush(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsFlush(self)
    
    def beatsStraightFlush(self, poker_hand):
        return False
    
    beatsFullHouse = beatsPoker = beatsStraightFlush
    
    def beatsFlush(self, poker_hand):
        my_cards = sorted(self.cards, key=lambda x: -x)
        other_cards = sorted(poker_hand.cards, key=lambda x: -x)
        return my_cards > other_cards

    def beatsStraight(self, poker_hand):
        return True
    
    beatsThreeOfAKind = beatsDoublePair = beatsPair = beatsHighCard = beatsStraight
    

class Straight(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsStraight(self)
    
    def beatsStraightFlush(self, poker_hand):
        return False
    
    beatsFlush = beatsFullHouse = beatsPoker = beatsStraightFlush
    
    def beatsStraight(self, poker_hand):
        return max(self.cards) > max(poker_hand.cards)

    def beatsThreeOfAKind(self, poker_hand):
        return True
    
    beatsDoublePair = beatsPair = beatsHighCard = beatsThreeOfAKind

class ThreeOfAKind(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsThreeOfAKind(self)
    
    def beatsStraightFlush(self, poker_hand):
        return False
    
    beatsStraight = beatsFlush = beatsFullHouse = beatsPoker = beatsStraightFlush
    
    def beatsThreeOfAKind(self, poker_hand):
        three_card_me = next(filter(lambda k: self.cards[k] == 3, self.cards))
        three_card_other = next(filter(lambda k: poker_hand.cards[k] == 3, poker_hand.cards))
        return three_card_me > three_card_other

    def beatsDoublePair(self, poker_hand):
        return True
    
    beatsPair = beatsHighCard = beatsDoublePair
    
class DoublePair(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsDoublePair(self)
    
    def beatsStraightFlush(self, poker_hand):
        return False
    
    beatsThreeOfAKind = beatsStraight = beatsFlush = beatsFullHouse = beatsPoker = beatsStraightFlush
    
    def beatsDoublePair(self, poker_hand):
        two_cards_me = sorted(filter(lambda k: self.cards[k] == 2, self.cards), key=lambda x: -x)
        two_cards_other = sorted(filter(lambda k: poker_hand.cards[k] == 2, poker_hand.cards), key=lambda x: -x)
        if two_cards_me > two_cards_other:
            return True
        elif two_cards_me < two_cards_other:
            return False
        else:
            one_card_me = next(filter(lambda k: self.cards[k] == 1, self.cards))
            one_card_other = next(filter(lambda k: poker_hand.cards[k] == 1, poker_hand.cards))
            return one_card_me > one_card_other

    def beatsPair(self, poker_hand):
        return True
    
    beatsHighCard = beatsPair

class Pair(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsPair(self)
    
    def beatsStraightFlush(self, poker_hand):
        return False
    
    beatsDoublePair = beatsThreeOfAKind = beatsStraight = beatsFlush = beatsFullHouse = beatsPoker = beatsStraightFlush
    
    def beatsPair(self, poker_hand):
        two_card_me = next(filter(lambda k: self.cards[k] == 2, self.cards))
        two_card_other = next(filter(lambda k: poker_hand.cards[k] == 2, poker_hand.cards))
        if two_card_me > two_card_other:
            return True
        elif two_card_me < two_card_other:
            return False
        else:
            one_cards_me = sorted(filter(lambda k: self.cards[k] == 1, self.cards), key=lambda x: -x)
            one_cards_other = sorted(filter(lambda k: poker_hand.cards[k] == 1, poker_hand.cards), key=lambda x: -x)
            return one_cards_me > one_cards_other

    def beatsHighCard(self, poker_hand):
        return True

class HighCard(PokerHand):
    
    def beats(self, poker_hand):
        return not poker_hand.beatsHighCard(self)
    
    def beatsStraightFlush(self, poker_hand):
        return False
    
    beatsPair = beatsDoublePair = beatsThreeOfAKind = beatsStraight = beatsFlush = beatsFullHouse = beatsPoker = beatsStraightFlush

    def beatsHighCard(self, poker_hand):
        return sorted(self.cards, key=lambda x: -x) > sorted(poker_hand.cards, key=lambda x: -x)

if __name__ == '__main__':
    result = sum(1 for line in open('poker.txt') if
                 PokerHand.create_hand(line.strip().split(' ')[:5]).beats(PokerHand.create_hand(line.strip().split(' ')[5:])))
    print("The result is:", result)
