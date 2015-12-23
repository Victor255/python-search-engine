"SEARCH ENGINE"

import os
import sys
import urllib2
import re

class SearchEngine(object):
    """docstring for ClassName"""
    def __init__(self):
        pass

    def menu(self):
        """THIS KEEP THE MENU"""
        while True:
            self.clean_screen()
            self.shows_menu()
            two_menu = self.two_menu()
            self.true_menu(two_menu)
            self.menu_decision(two_menu)

    def shows_menu(self):
        """THIS SHOWS THE MENU"""
        print "--1.SEARCH WORD"
        print "--2.EXIT"

    def two_menu(self):
        """THIS ASKS THE USER TO ENTER THE NUMBER OF THE DESIRED OPTION"""
        val_menu = raw_input("\nEnter the number of the desired option: -- ")
        val_menu = self.minuscule(val_menu)
        return val_menu

    #Test 1
    def true_menu(self, val_menu):
        """"THIS VERIFIES IF THE OPTION IS CORRECT"""
        if val_menu == "1" or val_menu == "2":
            return "Valid option"
        else:
            return "Invalid option"

    #Test 2
    def minuscule(self, val_menu):
        """THIS CONVERTS THE ELECTION IN MINUSCULE"""
        val_menu = val_menu.lower()
        return val_menu

    def menu_decision(self, two_menu):
        """THIS PROMPTS THE USER TO ENTER A NUMBER"""
        if two_menu == "1":
            self.search()
        elif two_menu == "2":
            self.exit()
        else:
            press = raw_input("\nInvalid option")

    def search(self):
        """THIS INTERACTS WITH THE USER"""
        self.clean_screen()
        valid_url = "Incorrect urls"
        while valid_url == "Incorrect urls":
            word, url1, url2 = self.ask_url()
            page_html1 = self.url_one(url1)
            page_html2 = self.url_two(url2)
            valid_url = self.valid_url(page_html1, page_html2)
        page_one = self.page_one(word, page_html1)
        page_two = self.page_two(word, page_html2)
        verifie_word = self.verifie_word(word, page_one, page_two, url1, url2)

    def ask_url(self):
        """IT PROMPTS THE USER TO ENTER A WORD AND URL"""
        word = raw_input("Enter the word you want to search: ")
        self.clean_screen()
        url1 = raw_input("\nEnter the first URL: ")
        url2 = raw_input("\nEnter the second URL: ")
        return word, url1, url2

    def url_one(self, url1):
        """THIS SAVES THE FIRST URL"""
        try:
            page1 = urllib2.urlopen(url1)
            page_html1 = page1.read()
            return page_html1
        except:
            try:
                url1 = "http://%s" % url1
                page_html1 = self.url_one(url1)
                return page_html1
            except:
                press = raw_input("The first URL is incorrect")
                return "Incorrect url"

    def url_two(self, url2):
        """THIS SAVES THE SECOND URL"""
        try:
            page2 = urllib2.urlopen(url2)
            page_html2 = page2.read()
            return page_html2
        except:
            try:
                url2 = "http://%s" % url2
                page_html2 = self.url_two(url2)
                return page_html2
            except:
                press = raw_input("The Second URL is incorrect")
                return "Incorrect url"

    def valid_url(self, page_html1, page_html2):
        """THIS VERIFIES IF THE URLS ENTERED ARE CORRECT"""
        if page_html1 == "Incorrect url" or page_html2 == "Incorrect url":
            valid_url = "Incorrect urls"
            press = raw_input("\nPlease enter a valid url!!!")
            self.clean_screen()
            return valid_url
        else:
            return "Correct urls"

    #Test 3
    def page_one(self, word, page_html1):
        """THIS RETURNS US TO THE URL THAT CONTAINS THE WORD ENTERED"""
        page_one = page_html1.count(word)
        return page_one

    #Test 4
    def page_two(self, word, page_html2):
        """THIS RETURNS US TO THE URL THAT CONTAINS THE WORD ENTERED"""
        page_two = page_html2.count(word)
        return page_two

    def verifie_word(self, word, page_one, page_two, url1, url2):
        """THIS SHOW THE PAGE THAT HAS MORE TIMES THE WORD"""
        if page_one > page_two:
            print "\nTHIS URL CONTAINS MORE THE WORD: %s APPEARS  %s  TIMES" % (url1, page_one)
        elif page_two > page_one:
            print "\nTHIS URL CONTAINS MORE THE WORD: %s APPEARS  %s  TIMES" % (url2, page_two)
        elif page_one == page_two and page_one != 0 and page_two != 0:
            print "\nTHE WORD IS REPEATED THE SAME QUATITY OF TIMES IN BOTH PAGES"
        elif page_one == 0 and page_two == 0:
            print "\nTHE WORD YOU ARE SEARCHING IS NOT IN ANY PAGE"
        press = raw_input("\nPRESS ENTER")

    def clean_screen(self):
        """THIS CLEANS THE SCREEN"""
        os.system('reset')

    def exit(self):
        self.clean_screen()
        sys.exit()

def application():
    my_program = SearchEngine()
    my_program.menu()

if __name__ == '__main__':
    application()
