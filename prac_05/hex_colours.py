HEX_COLOURS = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
               "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc",
               "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}

hex_code = input("Enter the hex colour code: ")
while hex_code != "":
    try:
        print(hex_code, "is", HEX_COLOURS[hex_code])
    except KeyError:
        print(hex_code, "is not a valid hex colour code")
    hex_code = input("Enter the hex colour code: ")

# TODO have hex_accept input without spacing and lowercase.
