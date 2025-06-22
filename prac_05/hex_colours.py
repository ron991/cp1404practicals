"""
Hex Colours
Colour codes in a dictionary:
"""


COLOUR_NAME_TO_HEXADECIMAL_CODE = {
    "absolutezero" : 	"#0048ba",
    "acidgreen":    "#b0bf1a",
    "aliceblue" : "#f0f8ff",
    "alizarincrimson": "#e32636",
    "amaranth" : "#e52b50",
    "amber" : "#ffbf00",
    "amethyst" : "#9966cc",
    "antiquewhite" : "#faebd7",
    "antiquewhite1" : "#ffefdb",
    "apricot" : "#fbceb1"


}
# From previous prac to display all available colours
# for name, code in COLOUR_NAME_TO_HEXADECIMAL_CODE.items():
#     print(f"{name:3} is {code}")

def main():
    """Run a hexadecimal colour lookup program"""
    colour_name = input("Enter colour name: ").replace(" ", "").lower()
    while colour_name != "":

        try:
            print(f"{colour_name} is {COLOUR_NAME_TO_HEXADECIMAL_CODE[colour_name]}")
        except KeyError:
            print(f"{colour_name} is not a hexadecimal colour")
        colour_name = input("Enter colour name: ").replace(" ", "").lower()



main()