#!/usr/bin/python3.7
# coding: utf8

import random #import random for computer choice

# choices list for the game
choices = ["PIERRE", "FEUILLE", "CISEAUX"]

def playerName():
    """function for ask player name"""
    name = input("votre nom ")
    while controlName(name) is False:
        print("votre nom doit contenir au minimum 2 caractere et maxi 15")
        name = input("votre nom")
    return name

def controlName(name):
    """function control name"""
    try:
        assert len(name) > 1 and len(name) < 15
    except AssertionError as a:
        return False


