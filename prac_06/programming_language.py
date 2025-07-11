"""
CP1404 Programming Language
Estimated Time to complete: 1hr
Actual Time to complete: 2 1/2 hours
"""


class ProgrammingLanguage:
    """Information about programming language."""

    def __init__(self, name, typing, reflection, year ):
        """Create a ProgrammingLanguage object."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        """Return a string representation of the object."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"

    def is_dynamic(self):
        """Return True if the programming language is dynamic."""
        return self.typing == "Dynamic"


def run_tests():
    """Run all tests on the programming language class."""
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    python = ProgrammingLanguage("Python", "Dynamic", True, 1995)
    languages = [ruby, visual_basic, python]
    print(languages)
    print(python)

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    run_tests()

