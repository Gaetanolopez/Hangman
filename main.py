import random

list1 = ['abruptly',
         'absurd',
         'abyss',
         'affix',
         'askew',
         'avenue',
         'awkward',
         'axiom',
         'azure',
         'bagpipes',
         'bandwagon',
         'banjo',
         'bayou',
         'beekeeper',
         'bikini',
         'blitz',
         'blizzard',
         'boggle',
         'bookworm',
         'boxcar',
         'boxful',
         'buckaroo',
         'buffalo',
         'buffoon',
         'buxom',
         'buzzard',
         'buzzing',
         'buzzwords',
         'caliph',
         'cobweb',
         'cockiness',
         'croquet',
         'crypt',
         'curacao',
         'cycle',
         'daiquiri',
         'dirndl',
         'disavow',
         'dizzying',
         'duplex',
         'dwarves',
         'embezzle',
         'equip',
         'espionage',
         'euouae',
         'exodus',
         'faking',
         'fishhook',
         'fixable',
         'fjord',
         'flapjack',
         'flopping',
         'fluffiness',
         'flyby',
         'foxglove',
         'frazzled',
         'frizzled',
         'fuchsia',
         'funny',
         'gabby',
         'galaxy',
         'galvanize',
         'gazebo',
         'giaour',
         'gizmo',
         'glowworm',
         'glyph',
         'gnarly',
         'gnostic',
         'gossip',
         'grogginess',
         'haiku',
         'haphazard',
         'hyphen',
         'iatrogenic',
         'icebox',
         'injury',
         'ivory',
         'ivy',
         'jackpot',
         'jaundice',
         'jawbreaker',
         'jaywalk',
         'jazziest',
         'jazzy',
         'jelly',
         'jigsaw',
         'jinx',
         'jiujitsu',
         'jockey',
         'jogging',
         'joking',
         'jovial',
         'joyful',
         'juicy',
         'jukebox',
         'jumbo',
         'kayak',
         'kazoo',
         'keyhole',
         'khaki',
         'kilobyte',
         'kiosk',
         'kitsch',
         'kiwifruit',
         'klutz',
         'knapsack',
         'larynx',
         'lengths',
         'lucky',
         'luxury',
         'lymph',
         'marquis',
         'matrix',
         'megahertz',
         'microwave',
         'mnemonic',
         'mystify',
         'naphtha',
         'nightclub',
         'nowadays',
         'numbskull',
         'nymph',
         'onyx',
         'ovary',
         'oxidize',
         'oxygen',
         'pajama',
         'peekaboo',
         'phlegm',
         'pixel',
         'pizazz',
         'pneumonia',
         'polka',
         'pshaw',
         'psyche',
         'puppy',
         'puzzling',
         'quartz',
         'queue',
         'quips',
         'quixotic',
         'quiz',
         'quizzes',
         'quorum',
         'razzmatazz',
         'rhubarb',
         'rhythm',
         'rickshaw',
         'schnapps',
         'scratch',
         'shiv',
         'snazzy',
         'sphinx',
         'spritz',
         'squawk',
         'staff',
         'strength',
         'strengths',
         'stretch',
         'stronghold',
         'stymied',
         'subway',
         'swivel',
         'syndrome',
         'thriftless',
         'thumbscrew',
         'topaz',
         'transcript',
         'transgress',
         'transplant',
         'triphthong',
         'twelfth',
         'twelfths',
         'unknown',
         'unworthy',
         'unzip',
         'uptown',
         'vaporize',
         'vixen',
         'vodka',
         'voodoo',
         'vortex',
         'voyeurism',
         'walkway',
         'waltz',
         'wave',
         'wavy',
         'waxy',
         'wellspring',
         'wheezy',
         'whiskey',
         'whizzing',
         'whomever',
         'wimpy',
         'witchcraft',
         'wizard',
         'woozy',
         'wristwatch',
         'wyvern',
         'xylophone',
         'yachtsman',
         'yippee',
         'yoked',
         'youthful',
         'yummy',
         'zephyr',
         'zigzag',
         'zigzagging',
         'zilch',
         'zipper',
         'zodiac',
         'zombie', ]

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

logo = '''
 _                                            
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

secret_word = random.randint(0, len(list1) - 1)
secret_word = list1[secret_word]
list2 = list()
n = 0
life = 6
for x in secret_word:
    list2.append(" ")
print(logo)
print(stages[6], list2)

while " " in list2:
    guess = input(f"guess the word (you have {life} life)\n")
    if not guess in secret_word:
        life = life - 1
        print(life)
        if life == 0:
            print(stages[0], secret_word, "Game Over")
            break
    if guess in secret_word:
        for x in range(0, len(secret_word)):
            if secret_word[x] == guess:
                list2[x] = guess
                n = n + 1
                if " " not in list2:
                    print("You win")

    if life == 6:
        print(stages[6], list2)
    elif life == 5:
        print(stages[5], list2)
    elif life == 4:
        print(stages[4], list2)
    elif life == 3:
        print(stages[3], list2)
    elif life == 2:
        print(stages[2], list2)
    elif life == 1:
        print(stages[1], list2)
    elif life == 0:
        print(stages[0], list2, "Game Over")