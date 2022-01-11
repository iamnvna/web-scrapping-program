### Project One - 100DaysofCode
# Web Scrapping Program
This is a simple program that collects usernames from GitHub and returns a *url* to the Profile Picture of the user.

## Background
This project is part of my #100DaysOfCode learning streak. I intend to write a simple python program each day. Each project would:
* be heavily commented for learning purposes;
* include a README file similar to this one;
* include an algorithm to solve it without code.

## Algorithm
1. Start.
2. Install required libraries.
3. Create a variable to collect the username of the github account.
4. Concatenate the username to the github domain to create a complete url and store in a variable. 
5. Send a request to the url using the appropriate library. Example of a request libray is *requests* in python.
6. Collect the content of the request and store in a variable using an appropriate library. Example *bs4* from Python
7. Use specific tags and parameters to identify the *src* url that includes the link to the user's profile picture and store in a variable.
8. Print the variable.
9. Stop.

For more understanding, watch the full tutorial **[here](https://youtu.be/SqvVm3QiQVk?t=39)** from freeCodeCamp.org
