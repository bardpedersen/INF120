#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:53:51 2021

@author: Bard
"""
import random

class Deck(object):    
    def __init__(self):
        ranks = ["A", "2", "3", "4", "5", "6", "7",
                 "8", "9", "10", "J", "Q", "K"]
        suits = ["C", "D", "H", "S"]
        self.deck = [s+r for s in suits for r in ranks]
        random.shuffle(self.deck)
        
    def hand(self, n=1):
        """Deal n cards. Return hand as list."""
        hand = [self.deck[i] for i in range(n)] # pick cards
        del self.deck[:n] # remove cards
        return hand

    def deal(self, cards_per_hand, no_of_players):
        """Deal no_of_players hands. Return list of lists."""
        return [self.hand(cards_per_hand) for i in range(no_of_players)]
    
    def putback(self, card):
        """Put back a card under the rest."""
        self.deck.append(card)
    
    def __str__(self):
        return str(self.deck)
    
    
def same_rank(hand, n_of_a_kind):
    ranks = [card[1:] for card in hand]
    counter = 0
    already_counted = []
    for rank in ranks:
        if rank not in already_counted and ranks.count(rank) == n_of_a_kind:
            counter += 1
            already_counted.append(rank)
    return counter


def same_suit(hand):
    suits = [card[0] for card in hand]
    counter = {}   # counter[suit] = how many cards of suit
    for suit in suits:
        count = suits.count(suit)
        if count > 1:
            counter[suit] = count
    return counter


#%%
# two pairs among five cards
N = 10000
M = 0
for i in range(N):
    h = Deck().hand(5)
    M += same_rank(h, 2) == 2
p = M / N
print(f"The probability of receiving exactly two pairs among five cards is approximately {100*p}%")

#%%
# >= 4 cards of same suit among 5 cards
N = 10000
M = 0
for i in range(N):
    h = Deck().hand(5)
    M += list(same_suit(h).values())[0] >= 4
p = M / N
print(f"The probability of receiving four or five cards of the same suit among five cards is approximately {100*p}%")

#%%
N = 10000
M = 0
for i in range(N):
    h = Deck().hand(5)
    M += same_rank(h, 4)
p = M / N
print(f"The probability of receiving four-of-a-kind among five cards is approximately {100*p}%")


