import os
import random

def clear():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

intro = '''
                     Tb.          Tb.
                     :$$b.        $$$b.
                     :$$$$b.      :$$$$b.
                     :$$$$$$b     :$$$$$$b
                      $$$$$$$b     $$$$$$$b
                      $$$$$$$$b    :$$$$$$$b
                      :$$$$$$$$b---^$$$$$$$$b
                      :$$$$$$$$$b        ""^Tb
                       $$$$$$$$$$b    __...__`.
                       $$$$$$$$$$$b.g$$$$$$$$$pb
                       $$$$$$$$$$$$$$$$$$$$$$$$$b
                       $$$$$$$$$$$$$$$$$$$$$$$$$$b
                       :$$$$$$$$$$$$$$$$$$$$$$$$$$;
                       :$$$$$$$$$$$$$^T$$$$$$$$$$P;
                       :$$$$$$$$$$$$$b  "^T$$$$P' :
                       :$$$$$$$$$$$$$$b._.g$$$$$p.db
                       :$$$$$$$$$$$$$$$$$$$$$$$$$$$$;
                       :$$$$$$$$"""^^T$$$$$$$$$$$$P^;
                       :$$$$$$$$       ""^^T$$$P^'  ;
                       :$$$$$$$$    .'       `"     ;
                       $$$$$$$$;   /                :
                       $$$$$$$$;           .----,   :
                       $$$$$$$$;         ,"          ;
                       $$$$$$$$$p.                   |
                      :$$$$$$$$$$$$p.                :
                      :$$$$$$$$$$$$$$$p.            .'
                      :$$$$$$$$$$$$$$$$$$p...___..-"
                      $$$$$$$$$$$$$$$$$$$$$$$$$;
   .db.               $$$$$$$$$$$$$$$$$$$$$$$$$$
  d$$$$bp.            $$$$$$$$$$$$$$$$$$$$$$$$$$;
 d$$$$$$$$$$pp..__..gg$$$$$$$$$$$$$$$$$$$$$$$$$$$
d$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p._            .gp.
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$p._.ggp._.d$$$$b
                         _   _               _           _      
 ___  ____ _   _____ 	| |_| |__   ___     | |__   __ _| |_ _ __ ___   __ _ _ __
/ __|/ _  \ \ / / _ \	| __| '_ \ / _ \    | '_ \ / _` | __| '_ ` _ \ / _` | '_ '
\__ \ (_| |\ V /  __/	| |_| | | |  __/    | |_) | (_| | |_| | | | | | (_| | | | |
|___/\__,_| \_/ \___|	\__ |_| |_|\___|    |_.__/ \__,_|\__|_| |_| |_|\__,_|_| |_|
'''

won = '''
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::-'    `-::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::-'          `::::::::::::::::
:::::::::::::::::::::::::::::::::::::::-  '   /(_M_)\  `:::::::::::::::
:::::::::::::::::::::::::::::::::::-'        |       |  :::::::::::::::
::::::::::::::::::::::::::::::::-         .   \/~V~\/  ,:::::::::::::::
::::::::::::::::::::::::::::-'             .          ,::::::::::::::::
:::::::::::::::::::::::::-'                 `-.    .-::::::::::::::::::
:::::::::::::::::::::-'                  _,,-::::::::::::::::::::::::::
::::::::::::::::::-'                _,--:::::::::::::::::::::::::::::::
::::::::::::::-'               _.--::::::::::::::::::::::#####:::::::::
:::::::::::-'             _.--:::::::::::::::::::::::::::#####:::::####
::::::::'    ##     ###.-::::::###:::::::::::::::::::::::#####:::::####
::::-'       ###_.::######:::::###::::::::::::::#####:##########:::####
:'         .:###::########:::::###::::::::::::::#####:##########:::####
     ...--:::###::########:::::###:::::######:::#####:##########:::####
 _.--:::##:::###:#########:::::###:::::######:::#####:#################
'#########:::###:#########::#########::######:::#####:#################
:#########:::#############::#########::######:::#######################
##########:::########################::################################
##########:::##########################################################
##########:::##########################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
'''

lost = '''
⠄⠄⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠄⠄⠄⠄⠠⠠⣤⣤⣤⠠⣤⣬⣬⣤⣬
⠄⠠⠠⠄⠠⠄⠄⠄⠠⠄⠄⠄⠄⠄⠠⠠⠠⠄⠠⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⣤⣤⠠⣤⣤⠠⣤⣬⣬⣬
⠄⠠⠄⠠⠄⠠⠄⠄⠄⠠⠄⠠⣤⣬⣬⣬⣤⠠⠠⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠠⠠⠠⠄⠄⠄⠠⠄⠠⠠⠠⠠⠠⠠⠄⠠⣤⠠⠠⣬⣬
⠠⠠⠠⠄⠠⠄⠠⠄⠄⠄⠠⣬⠟⣽⣽⣽⣽⣬⣤⠠⠠⠄⠄⠄⠠⠄⠄⠄⠄⠄⠠⠠⠄⠄⠠⠄⠠⠠⠠⠠⣤⣤⠠⠠⠠⠠⣤⠠⠠⠟
⠄⠠⠠⠠⠄⠠⠄⠄⠠⣬⣬⠟⣽⣽⣽⣽⣽⣽⣽⣽⠟⣤⠠⠄⠠⠄⠄⠄⠄⠠⠠⠠⠠⠠⠠⠠⠄⠄⠄⠄⠄⠠⠠⣤⠠⠠⠠⣤⠠⣬
⠠⠄⠠⠄⠠⠄⠄⠄⣬⠟⣤⠟⣽⠟⠟⠟⠟⣽⣽⣽⣿⣽⣽⠟⣤⣬⣤⠠⣬⣤⣬⣬⠟⠟⣽⠟⣬⠄⠄⠠⠄⠄⠠⠠⣬⠄⣤⠠⠠⣤
⠄⠠⠠⠠⠄⠠⠄⣤⠟⣤⣬⠟⣬⠟⣬⠟⣽⣽⣽⣽⣽⣽⣽⣿⣿⣿⣽⣽⣿⣽⣽⣽⣽⣿⣿⣿⣿⣽⠄⠠⣤⠠⠠⠠⣬⣬⠄⠠⠠⣬
⠠⠄⠠⠠⠠⠄⠠⣤⣬⣤⣬⣬⠟⠟⣽⠟⠟⠟⣽⣽⣿⣽⣿⣿⣿⣿⣿⠟⣽⣽⣿⣿⣽⣽⣿⣿⣿⣿⣤⠠⣽⣬⠠⠠⣤⣤⠄⠠⣤⣤
⠄⠠⠄⠠⠄⠠⣤⣬⣤⣤⣬⠟⠟⠟⠟⣽⣽⣿⣿⣽⠟⠟⠟⠟⠟⣽⣽⣿⣽⣽⣽⣽⣽⣽⣽⠟⠟⣽⣬⠠⠟⠟⠠⠠⣤⠄⠄⠠⠠⣤
⠠⠄⠠⠠⠄⠠⣤⠟⣬⣤⠟⠟⠟⣬⣬⣬⠟⠟⣽⣽⣽⣽⣽⠟⠟⠟⠟⠟⠟⠟⣽⣽⣿⣽⣽⣽⠟⣽⣬⣬⣤⠟⠄⠄⣬⠠⠄⠄⠄⠄
⠄⠠⠠⠠⠄⠠⣤⣬⣬⣤⣬⣬⣬⠟⠟⠟⠟⠟⣬⠟⣬⠟⠟⣽⣽⣽⣽⣽⣽⣽⠟⣽⠟⣽⠟⣽⠟⠟⠟⣬⣿⣤⠄⣤⠠⣬⠠⠄⠄⠠
⠠⠄⠄⠄⠄⠄⣬⣬⣬⣤⣤⠠⣤⣬⣤⣬⣿⣿⣬⣬⣬⠟⣬⣬⠟⠟⠟⣽⣽⠟⠟⠟⠟⠟⠟⣽⣽⣽⣽⠟⣽⣤⠄⣬⠠⠄⣬⣤⠄⠠
⠄⠠⠄⠠⠄⠄⣬⣽⣬⣬⣬⠠⠄⠠⠄⠠⣬⠟⠟⣿⣿⣿⣽⣽⣿⣿⣽⣿⠟⣬⣽⣽⣿⣿⣿⣿⣿⣤⠠⠟⠟⠠⣤⣤⣤⠄⠠⣤⣬⠠
⠠⠄⠄⠠⠠⠄⣤⠟⣽⠟⣤⠄⠄⠄⠄⠄⠠⠄⠠⣤⣽⣽⣽⣿⣿⠟⣿⣿⣿⣿⣿⣿⣿⠟⣬⠠⠄⠄⠄⠄⣤⣤⣽⣬⣤⣤⠄⠄⣤⣬
⠄⠄⠄⠠⣤⠠⣬⣬⠟⣽⠠⠄⠄⠠⠄⠄⠄⠄⠄⠄⠄⠠⣽⣿⣬⠟⣿⣿⣽⣿⣿⠟⠠⠄⠄⠄⠠⣤⠠⠄⠄⠠⠟⣤⠄⣬⣤⠄⠄⣤
⠠⠄⠄⠠⣬⣤⠟⠟⣬⣤⠄⠄⠄⠄⠠⠄⠄⠄⠠⠄⠄⠄⠠⣤⠟⣿⣽⣽⠟⣤⣤⠄⠄⠄⠄⠄⠠⣤⣤⠄⠠⠟⣤⠠⠄⠄⣤⣤⠠⣤
⠄⠠⠄⠠⣤⣤⣬⣤⠟⣬⠄⠄⠄⠄⠠⠠⠄⠟⣿⣿⠟⠠⠄⠄⠟⣽⣽⠟⠟⠠⠄⠄⠄⠠⠟⣽⣤⠄⠄⠄⠠⣿⣽⠄⣤⠠⠄⠠⠠⣤
⠠⠄⠄⠄⣤⠠⣬⣤⣬⣤⠠⠠⠄⠄⠄⠄⠠⠠⠠⠠⠄⠄⠠⠄⠠⣽⣿⣿⣤⠄⠄⠄⠄⠠⠟⣬⠠⠄⠄⠄⣬⣿⣬⠄⣤⣬⣤⠄⠄⣤
⠠⠠⠄⠄⠠⠠⣤⣬⠟⣤⣤⣤⠠⠠⠠⠄⠄⠄⠄⠄⠄⣤⠠⣤⣬⣿⣿⣿⣽⠟⣤⠄⠄⠄⠄⠄⠄⠠⠠⣤⣽⣽⠄⠠⠄⣤⣬⣤⣤⣤
⠠⠄⠄⠄⠄⠄⣬⣤⣽⣬⣬⣿⠟⣬⣿⣤⠟⣬⣽⣽⠟⠟⠟⣽⣽⣽⣿⣿⣽⣿⣿⣿⣽⣬⣤⠄⠄⣤⣿⣿⣿⠟⠄⠄⠠⠠⣬⣤⣤⠠
⠄⠠⠄⠠⠄⠄⣤⠠⣤⣤⠟⣿⠟⣽⣿⣿⣿⣿⣿⣽⠠⣬⣽⣬⠟⣿⣿⣿⣽⣿⣽⣿⣿⣿⣿⣿⠟⣽⣽⣿⣿⣽⠄⠄⠠⣬⠠⠠⠠⣬
⠠⠄⠠⠄⠄⠄⣤⠠⠠⠄⣽⣿⣽⣽⣿⣿⣿⠟⠟⣤⣽⠟⣤⣬⣽⣿⣿⣿⣿⣽⠟⣽⣿⣿⣿⣿⣿⣿⣽⣿⣽⣤⠄⠠⣤⠠⠠⠠⣤⣬
⠄⠠⠄⠠⠄⠄⣤⣬⠄⠄⣤⣽⣿⣽⣿⣽⣬⣤⣤⣬⣿⣿⣽⣽⣿⣿⣿⣿⣿⣿⣿⠟⣤⣤⣽⣿⣿⣿⣽⣿⠟⠠⠄⣤⠠⠠⠠⠠⣤⣤
⠠⠄⠠⠠⠠⠄⠠⣬⣤⠄⠄⣬⣽⣽⣬⣤⣤⣬⠟⣤⠄⠄⠠⣬⣽⣿⣿⣽⠟⣽⣽⣽⣿⠟⣤⣬⣿⣽⣬⣬⠟⠄⠠⠠⠠⠄⠠⠠⣤⣤
⠄⠄⠄⠠⠄⠄⠄⣤⣬⣤⠄⠄⣤⣤⣽⣿⣽⣤⣽⣽⠟⠟⣬⠟⠟⠟⠟⠟⣽⣿⣿⣿⣿⣽⣿⣤⠄⣬⣬⣽⠄⠄⣤⠠⠠⠠⠠⣤⣤⣤
⠄⠄⠠⠄⠠⠄⠄⠄⣤⠟⣬⠄⠄⠠⠟⣤⠠⠄⣤⣬⠟⣽⣽⣿⣿⣽⠟⣿⣿⣿⣿⠟⠠⠄⣤⠠⠄⣬⣿⠠⠄⠄⠠⣤⠠⠄⠠⣤⠄⠠
⠄⠠⠄⠠⠄⠄⠄⠄⠄⣤⣬⣬⠄⠄⣤⠠⠄⠠⠄⠄⠄⠄⠄⠄⠠⠠⠠⠠⠄⠄⠄⠄⠄⠄⠄⣤⣽⣽⠄⠄⠄⠄⠄⠠⠠⠠⣤⠠⠄⠠
⠄⠄⠠⠄⠄⠄⠠⠄⠠⠄⠄⣤⣬⠠⠠⣤⠠⠄⠠⠠⣤⠠⣤⣤⣤⣤⠠⠄⠠⠄⠠⣤⣤⠄⠟⣽⣤⠄⠄⠄⠄⠄⠠⠠⠠⠠⠠⠠⣤⣤
⠄⠠⠄⠠⠄⠠⠄⠠⠄⠄⠄⠄⣤⣬⣤⣬⠟⠠⠠⣤⣤⣤⠠⠠⠄⠄⠄⠠⣤⣬⠟⣽⠟⣽⠟⠄⠄⠄⠠⠠⠄⠄⠄⠠⠠⣤⠠⠠⠠⣤
⠠⠄⠄⠄⠄⠄⠠⠄⠄⠄⠄⠄⠠⠠⣤⣤⠟⠟⣤⣬⣤⠠⣤⣤⣤⣬⣬⣬⣽⣿⣿⣿⣽⠠⠄⠄⠄⠄⠠⠠⠄⠄⠄⠄⠄⠠⠠⠠⠠⠠
⠄⠄⠄⠠⠄⠠⠄⠠⠄⠄⠄⠠⠄⠠⠄⠠⠠⣬⠟⠟⣽⠟⠟⣽⣽⣿⣿⣿⣿⣿⣿⠟⠄⠄⠄⠄⠄⠄⠄⣤⠠⠄⠄⠠⠠⠠⠄⠠⠠⠠
⠄⠄⠠⠄⠄⠄⠠⠄⠄⠄⠠⠄⠄⠄⠄⠄⠄⠠⣬⠟⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣬⠄⠠⠄⠄⠄⠠⠄⠠⠠⠠⠄⠠⠠⠠⠠⠠⠠⠠⠠
⠄⠠⠄⠄⠄⠠⠄⠄⠄⠄⠄⠠⠄⠠⠄⠄⠄⠠⠄⠠⣬⣿⣿⣿⣿⣿⣿⣿⣽⠠⠄⠠⠠⠄⠄⠄⠄⠠⠠⣤⠠⠠⠄⠠⠠⠠⠠⠠⠠⠠
⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠄⠄⠠⠄⠠⠄⠄⠄⠠⠠⣤⣤⣤⣤⣤⠄⠄⠄⠠⠠⠠⠄⠄⠄⠠⠠⠠⠠⣤⠠⠄⠠⠠⠠⠠⠄⠠⠠
⠄⠠⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠄⠄⠠⠄⠠⠄⠄⠄⠄⠄⠄⠄⠄⠄⠠⠄⠠⠠⠄⠄⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠⠠
'''

batman = ['''
             .  .
             |\_|'
             | a_a'
             | | "]
         ____| '-\___
        /.----.___.-''
       //        _    '
      //   .-. (~v~) /|
     |'|  /\:  .--  / '
    // |-/  \_/____/\/~|
   |/  \ |  []_|_|_] \ |
   | \  | \ |___   _\ ]_}
   | |  '-' /   '.'  |
   | |     /    /|:  |
   | |     |   / |:  /"
   | |     /  /  |  /  "
   | |    |  /  /  |    "
   \ |    |/\/  |/|/\    "
    \|\ |\|  |  | / /\/\__"
     \ \| | /   | |__
          / |   |____)
          |_/

Good Start!
''',
'''
             .  .
             |\_|'
             | a_a'
             | | "]
         ____| '-\___
        /.----.___.-''
       //        _    '
      //   .-. (~v~) /|
     |'|  /\:  .--  / "
    // |-/  \_/____/\/~"
   |/  \ |  []_|_|_] ''"
   | \  | \ |___   _\ "..
   | |  ' ' /   ' '  |   ""
   | |     /    /|:  |
   | |     |   / |:  /"
   | |     /  /  |  /  "
   | |    |  /  /  |    "
   \ |    |/\/  |/|/\    "
    \|\ |\|  |  | / /\/\__'
     ' \| | /   | |__
          / |   |____)
          |_/

Joker cut off Batman's Right Hand!
''',
'''
             .  .
             |\_|'
             | a_a'
             | | "]
         ____| '-\___
        /.----.___.-''
       //        _    '
      //   .-. (~v~) /|
     |'|  /\:  .--  / /
    // |-/  \_/____/\/
   |/  \ |  []_|_|_] 
   | \  | \ |___   _\ 
   | |  '-' /   '.'  |  
   | |     /    /|:  |
   | |     |   / |:  /
   | |     /  /  |  / 
   | |    |  /  /  |   
   \ |    |/\/  ''  "
    \|\ |\|  |   ""
     \ \| | /       "
          / |   
          |_/

Joker cut off Batman's Right Leg!
''',
'''
             .  .
             |\_|'
             | a_a'
             | | "]
         ____| '-\___
        /.----.___.-''
       //        _    '
      //   .-. (~v~) /|
     |'|  /\:  .--  / /
    // |-/  \_/____/\/
   |/   "   []_|_|_] 
   | \  \.  |___   _\ 
   | |   '| /   '.'  |  
   | |     /    /|:  |
   | |     |   / |:  /
   | |     /  /  |_ / 
   | |    |  /    
   \ |    |/\/  
    \|\ |\|  |   
     \ \| | /     
          / |   
          |_/

Joker cut off Batman's Left Hand!
''',
'''
             .  .
             |\_|'
             | a_a'
             | | "]
         ____| '-\___
        /.----.___.-''
       //        _    '
      //   .-. (~v~) /|
     |'|  /\:  .--  / /
    // |_/  \_/____/\/
   |/       []_|_|_] 
   | \      |___   _\ 
   | |      /   '.'  |  
   | |     /    /|:  |
   | |     |   / |:  /
   | |     /  /  |_ / 
   | |    |  ""    
   \ |    |"  
    \|\ |\| "".    
     \ \|    / /

Joker cut off Batman's Left Leg!

Now this is your last chance to save Batman!
''']

def toArray(str):
    word = []
    for s in str:
        word += s
    return word

def makeStatus(str):
    status = []
    for s in str:
        if s == " ":
            status += " "
        else:
            status += "_"
    return status

def saved():
    for s in status:
        if(s == "_"):
            return 0
    return 1

def printStatus():
    for s in status:
        print(s, end = " ")
    print()

def getInput():
    a = input("Guess an alphabet of the name in small letters: ")
    if not a:
        print("Guess something fast...")
        a = getInput()
    a = a[0]
    return a

def updateStatus(index):
    word[index], status[index] = status[index], word[index]

def check(inp):
    flag = 0
    for index in range(0, len(word)):
        if( word[index] == inp ):
            updateStatus(index)
            flag = 1
    if (flag == 0):
        print("Wrong Choice!")
        return 1
    else:
        print("Right Choice! Let's Go.")
        return 0

def already(inp):
    for index in range(0, len(status)):
        if( status[index] == inp ):
            return 1
    return 0

def printBatman(index):
    if index < 5:
        print(batman[index])

dataset = ["SCARLET WITCH", "VISION", "WOLVERINE", "DEADPOOL", "SHANG CHI", "ABOMINATION", "NICK FURY", "MANTIS",  
            "CAPTAIN AMERICA", "IRONMAN", "THANOS", "HAWKEYE", "BLACK PANTHER", "BLACK WIDOW", "THOR", "LOKI", "HULK",
            "SPIDERMAN", "WINTER SOLDIER", "ULTRON", "ODIN", "MANDARIN", "HELA", "DOCTOR STRANGE", "WONG",
            "CAPTAIN MARVEL", "ANTMAN", "WASP", "STARLORD", "GAMORA", "NEBULA", "GROOT", "ROCKET", "BLADE", "EGO",
            "RED SKULL", "MYSTERIO", "VENOM", "DOCTOR OCTOPUS", "GREEN GOBLIN", "SCORPION", "VULTURE", "SANDMAN",
            "ELECTRO", "MORBIUS", "RIOT", "CARNAGE", "WAR MACHINE", "VALKYRIE", "LIZARD"]

killIndex = 0
marvel = random.choice(dataset)
word = toArray(marvel.lower())
status = makeStatus(word)

clear()
print(intro)
print("Batman is in danger!\nGuess who has come to save him from the MARVEL Universe.")
print("You have 5 lives. Each time you make a wrong choice, Batman looses a limb.")
print("After your first choice you will see the blanks at the top of the screen depicting the alphabets in the saviour's name.\n")

while ( killIndex < 5  and not saved() ):
    inp = getInput()
    clear()
    if (already(inp)):
        print("Already used. Try something else.")
    elif (check(inp)):
        killIndex += 1
    printStatus()
    printBatman(killIndex)

if(saved() ):
    clear()
    print(won)
    print("You Won! Batman is saved.")
else:
    clear()
    print(lost)
    print(f"{marvel} came for rescue.\nBut Alas! Batman is dead.")
