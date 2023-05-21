import os
from string import ascii_lowercase

SNES_ROM_PATH = '/home/m/Downloads/Games/'
TARGET_PATH = '/home/m/sorted_games'


def create_alphabet_dirs():
    if not os.path.exists(TARGET_PATH):
        os.makedirs(TARGET_PATH)
    for char in '0' + ascii_lowercase:
        full_dir = os.path.join(TARGET_PATH, char)
        if not os.path.exists(full_dir):
            os.makedirs(full_dir)


def move_snes_games():
    all_games = os.listdir(SNES_ROM_PATH)
    all_games.sort()
    for game in all_games:
        old_game_path = os.path.join(SNES_ROM_PATH, game)
        starts_with = game[0].lower()
        target = '0'
        if starts_with in ascii_lowercase:
            target = starts_with
        new_game_path = os.path.join(TARGET_PATH, target, game)
        os.rename(old_game_path, new_game_path)

if __name__ == '__main__':
    create_alphabet_dirs()
    move_snes_games()
