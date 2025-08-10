"""
CP1404 Week 10 wikipedia page program
"""


import wikipedia

def main():
    """Search for a wikipedia page"""

    print("Wikipedia page search tool")
    title = input("Enter a page title or search phrase: ")
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)
            print("Page title:", page.title)
            print("Page content:", page.content)
            print("Page url:", page.url)
            print("Page summary:", page.summary)

        except wikipedia.exceptions.PageError:
            print("Page not found")
        except wikipedia.exceptions.DisambiguationError:
            print("Page not found")
        except wikipedia.exceptions.RedirectError:
            print("Page not found")

        title = input("Enter a page title or search phrase: ")

    print("Goodbye")

if __name__ == "__main__":
    main()


main()