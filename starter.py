import shutil
import sys
starter_pokemon_offsets = [0x169BB5, 0x169DB8, 0x169D82]

starters = [1, 4, 7]

try:
    with open("./starters.txt") as starters_file:
        lines = starters_file.readlines()
        number_of_lines = len(lines)
        if number_of_lines == 0 or number_of_lines > 3:
            sys.exit("Expecting 1-3 lines with pokedex id in each line in starters.txt file.")
        for i, line in enumerate(lines):
            try:
                pokedex_id = int(line)
            except ValueError:
                sys.exit(f'Non number found on line {i+1} - {line}')
                
            starters[i] = int(line)
except FileNotFoundError:
    print("starters.txt file not found. Expecting 1-3 lines with pokedex id in each line.")

changed_rom_filename = "Pokemon Radical Red Chose Starters.gba"
shutil.copy("Pokemon Radical Red.gba", changed_rom_filename)
with open(changed_rom_filename, "rb+") as rom:
    for i, starter_offset in enumerate(starter_pokemon_offsets):
        starter = starters[i].to_bytes(2, byteorder='little')
        rom.seek(starter_offset)
        rom.write(starter)
    print(f'Changed starters to {starters}')
