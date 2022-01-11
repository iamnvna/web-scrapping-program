## to begin, two python libraries were installed.

"""
The requests library was installed via "pip install requests" from the ide terminal.
Requests allows us to get the content and everything else hosted in a single url.
"""

"""
bs4 was installed next via the terminal as "pip install bs4"
I am yet to find out exactly the whole scope of the library but today's code was about using Beautiful Soup.
BeautifulSoup allows us to find a specific tag in an html file while passing descriptive arguments to narrow down the search.
"""

## Both Libraries are imported to be used in the code.
import requests
from bs4 import BeautifulSoup as bs

## A variable is created to hold the username of the Github user.
gituser = input("Input Github username: ")

## A variable is created, and the github username is concatenated with the domain to provide access to the user profile.
url = "https://github.com/"+gituser

## The requests library is used to send a request to the url
r = requests.get(url)

## The Beautiful Soup library is used to collect the feedback from the request stored in r. This data is parsed as an html since it's expected to be an html documet.
soup = bs(r.content, "html.parser")

## With the help of the html tags and parameters, the exact data which in our case is the src file, is extrated and stored in the userimage variable.
userimage = soup.find('img', {'alt' : 'Avatar'})['src']

## The link is printed out to the screen.
print(userimage)

