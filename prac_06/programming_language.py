"""
CP1404 Programming Language
Estimated Time to complete: 1hr
Actual Time to complete:
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