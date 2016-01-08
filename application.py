"SEARCH ENGINE"

import os
import sys
import urllib2
import re

class SearchEngine(object):
    """docstring for ClassName"""
    def __init__(self):
        pass

    def clear(self):
        """THIS CLEANS THE SCREEN"""
        if os.name == "posix":
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"):
            os.system("cls")

    #Test 1
    def is_space(self, word):
        """THIS VERIFIES IF THE WORD IS EMPTY"""
        if word.isspace() == True or word == "":
            return True
        else:
            return False

    def insert_word(self):
        """THIS SAVES THE WORD GIVEN BY THE USER"""
        self.clear()
        white = True
        while white == True:
            word = raw_input("\nInsert the word:  ")
            self.clear()
            white = self.is_space(word)
            if white == True:
                print "\n--Insert at least a letter to search"
            else:
                return word
        return word

    def first_url(self):
        """THIS SAVES THE FIRST URL"""
        url1 = raw_input("\nInsert the first URL:  ")
        return url1

    def second_url(self):
        """THIS SAVES THE SECOND URL"""
        url2 = raw_input("\nInsert the second URL:  ")
        return url2

    #Test 2
    def valid_url(self, url):
        """THIS VERIFIES IF THE URLS IS VALID"""
        try:
            page = urllib2.urlopen(url)
            html = page.read()
            return html
        except:
            self.clear()
            return False

    #Test 3
    def count_page(self, word, url):
        """THIS COUNTS THE TIMES THAT APPEAR THE WORD"""
        count_url = len(re.findall(word, url))
        return count_url

    def information(self, count_url1, count_url2, url1, url2):
        """THIS SHOW THE PAGE THAT HAS THE MORE TIMES THE WORD"""
        if count_url1 > count_url2:
            self.clear()
            print "\nTHIS URL CONTAINS MORE THE WORD: %s APPEARS  %s  TIMES" % (url1, count_url1)
        elif count_url2 > count_url1:
            self.clear()
            print "\nTHIS URL CONTAINS MORE THE WORD: %s APPEARS  %s  TIMES" % (url2, count_url2)
        elif count_url1 == count_url2 and count_url1 != 0 and count_url2 != 0:
            self.clear()
            print "\nTHE WORD IS REPEATED THE SAME QUATITY OF TIMES IN BOTH PAGES"
        elif count_url1 == 0 and count_url2 == 0:
            self.clear()
            print "\nTHE WORD YOU ARE SEARCHING IS NOT IN ANY PAGE"

    def search(self):
        """THIS VERIFIES IF THE URLs ENTERED ARE VALIDS"""
        word = self.insert_word()
        while True:
            url1 = self.first_url()
            page1 = self.valid_url(url1)
            if page1 == False:
                print "\nThe First URL is incorrect"
            else:
                while True:
                    url2 = self.second_url()
                    page2 = self.valid_url(url2)
                    if page2 == False:
                        print "\nThe Second URL is incorrect"
                    else:
                        count_url1 = self.count_page(word, page1)
                        count_url2 = self.count_page(word, page2)
                        self.information(count_url1, count_url2, url1, url2)
                        self.again()

    #Test 4
    def minuscule(self, option):
        """THIS CONVERTS THE ELECTION IN MINUSCULE"""
        option = option.lower()
        return option

    def again(self):
        """THIS ASK TO THE USER IF WANT TO INSERT ANOTHER WORD"""
        while True:
            option = raw_input("\nDo you want to search another word?: y/n ")
            option = self.minuscule(option)
            if option == "y":
                self.search()
            elif option == "n":
                self.clear()
                self.menu()
            else:
                self.clear()
                print "Only can write y/n"

    def menu(self):
        """THIS SHOWS THE MENU"""
        self.clear()
        print "--1. Search engine"
        print "--2. Exit"
        while True:
            option = raw_input("\nEnter the number of the desired option: -- ")
            if option == "1":
                self.search()
                raw_input("Press Enter")
                self.clear()
                self.menu()
            elif option == "2":
                self.clear()
                sys.exit()
            else:
                self.clear()
                print "Invalid Option "
                self.menu()

MAIN = SearchEngine()

if __name__ == '__main__':
    MAIN.menu()
