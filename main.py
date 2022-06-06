# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
import random
from time import sleep

import operator
import pandas as pd
import openpyxl
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# /html/body/game-app//game-theme-manager/div/game-keyboard
keyboard_dict = {}
dictionary = [line.split(',') for line in open("dictionary.txt")]
browser = webdriver.Chrome(executable_path=r"./chromedriver.exe")


def start_world():
    browser.get("https://www.powerlanguage.co.uk/wordle/")
    sleep(5)
    modal = browser.execute_script("return document.querySelector('game-app').shadowRoot.querySelector("
                                   "'game-modal').shadowRoot.querySelector('game-icon');")
    modal.click()

    keyboard = browser.execute_script("return document.querySelector('game-app').shadowRoot.querySelector("
                                      "'game-keyboard').shadowRoot.querySelector('#keyboard');")

    buttons = browser.execute_script("return arguments[0].querySelectorAll('[data-key]');", keyboard)
    for button in buttons:
        keyboard_dict[button.get_attribute('innerHTML')] = button

    choose_first = choose_random_word(dictionary[0])
    sleep(10)
    print('Random word is : ', choose_first)
    press_word(choose_first)
    sleep(5)
    absent, present, correct = check_keyboard(keyboard, choose_first)
    copy = filter_dict(dictionary[0], absent, present, correct)
    finish = ""
    count = 0
    while count < 5:
        print(copy)
        choose_word = choose_random_word(copy)
        if choose_word == finish:
            break
        press_word(choose_word)
        sleep(5)
        absent, present, correct = check_keyboard(keyboard, choose_first)
        copy = filter_dict(dictionary[0], absent, present, correct)
        count += 1
        finish = choose_word


def check_keyboard(keyboard, word):
    key_absent = browser.execute_script('return arguments[0].querySelectorAll("[data-state]");',
                                        keyboard)
    absent_list = []
    present_list = []
    for w in key_absent:
        if w.get_attribute("data-state") == "absent":
            absent_list.append(w.get_attribute('innerHTML'))
        elif w.get_attribute("data-state") == "present":
            present_list.append(w.get_attribute('innerHTML'))

    correct_list = check_board(key_absent)
    return absent_list, present_list, correct_list


def check_board(absent):
    correct = []
    for w in absent:
        if w.get_attribute("data-state") != "correct":
            continue
        else:
            correct.append(w.get_attribute('innerHTML'))
            break
    if not correct:
        return []
    board = browser.execute_script("return document.querySelector('game-app').shadowRoot.querySelector("
                                   "'#board').querySelectorAll('game-row');")
    correct = ["-", "-", "-", "-", "-"]
    for b in board:
        if b.get_attribute('letters') != "":
            check_tile = browser.execute_script("return arguments[0].shadowRoot.querySelectorAll('game-tile')", b)
            for i in range(len(check_tile)):
                if check_tile[i].get_attribute('evaluation') == "correct":
                    correct[i] = check_tile[i].get_attribute('letter')
    return correct


def filter_dict(dictionary, absent, present, correct):
    copy_dict = dictionary

    # absent filtering
    if absent:
        for w in absent:
            copy_dict = [k for k in copy_dict if w not in k]

    if not present:
        print("No present list")
    else:
        for a in present:
            copy_dict = [k for k in copy_dict if a in k]

    if correct:
        for i in copy_dict:
            if len(copy_dict) > 1:
                counter = 0
                for j in range(len(correct)):
                    if i[j] == correct[j]:
                        counter += 1
                    elif correct[j] == "-":
                        continue
                    else:
                        counter = 0
                        break
                if counter > 0:
                    copy_dict = [k for k in copy_dict if i == k]
            else:
                break
    print(copy_dict)
    return copy_dict


def press_word(word):
    for w in word:
        keyboard_dict[w].click()
    keyboard_dict['enter'].click()


def filter_out(diction):
    for i in range(len(diction)):
        diction[i] = diction[i].replace("\n", "")
    return diction


def choose_random_word(diction):
    return random.choice(diction)







start_world()
