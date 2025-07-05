"""
CP1404 Languages
Estimated Time to complete: 1hr
Actual Time to complete:
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """List and print programming languages."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ruby, visual_basic, python]
    print(languages)
    print(python)
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
