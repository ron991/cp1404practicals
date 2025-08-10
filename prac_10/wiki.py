"""
CP1404 Week 10 wikipedia page program
"""


import wikipedia

def main():
    """Search for a wikipedia page"""

    while True:
        title = wikipedia.search("Wikipedia")
        if title:
            page = wikipedia.page(title)
            content = page.content
            print(content)


main()