# -*- coding: utf-8 -*-
"""
Created on Sun May 15 18:54:27 2016

@author: 4bet20x

"2c": 1,
"2d": 2,
"2h": 3,
"2s": 4,
"3c": 5,
"3d": 6,
...
"kh": 47,
"ks": 48,
"ac": 49,
"ad": 50,
"ah": 51,
"as": 52
"""

import array
import numpy as np
from Deck import *

handsDB = open('/home/mrpotatohead/Documents/HandRanks.dat','rb')
ranks = array.array('i')
ranks.fromfile(handsDB, 32487834)


def LookupHand(hand):
    p = 53
    for card in hand:
        if type(card) != int:
            p = ranks[p + dic_deck[card]]
        else:
            p = ranks[p + card]
    return p
    
def GetHandCategory(Hand):
    return Hand >> 12
    
def GetRank(Hand):
    return (Hand & 0x00000FFF)

def EquityVsRandom(hand,iterations=1000):   
    ndeck = list(range(1,53))
    
    ndeck.remove(hand[0])
    ndeck.remove(hand[1])
    
    win = 0
    for i in range(iterations):
        _deck = list(ndeck)
        np.random.shuffle(_deck)
        villain = []
        villain.append(_deck.pop())
        villain.append(_deck.pop())
        
        board = _deck[:5]
        
        win += showdown(hand,villain,board)
            
    return (win / float(iterations))
            

def showdown(hero,vill,board):
    herohand = LookupHand(hero + board)
    villhand = LookupHand(vill + board)
    heroCat = GetHandCategory(herohand)
    villCat = GetHandCategory(villhand)
    if heroCat != villCat: return heroCat > villCat
    return GetRank(herohand) > GetRank(villhand)
    
def to_string(hero,vill,board):
    shero, svill, sboard = [], [], []
    for c in hero: shero.append(r_deck[c])
    for c in vill: svill.append(r_deck[c])
    for c in board: sboard.append(r_deck[c])
    return shero, svill, sboard
        
    
if __name__ == "__main__":   
    hero = [dic_deck['Ac'],dic_deck['As']]
    print(EquityVsRandom(hero, 10000))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
