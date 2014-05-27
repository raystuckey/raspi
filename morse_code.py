from piglow import PiGlow
from time import sleep
from re import match

piglow = PiGlow()
piglow.all(0)
speed = .12


morse = {' ':'     ','a':'.-','b':'-...','c':'-.-.','d':'-..','e':'.','f':'..-.','g':'--.','h':'....','i':'..','j':'.---','k':'-.-','l':'.-..','m':'--','n':'-.','o':'---','p':'.--.','q':'--.-','r':'.-.','s':'...','t':'-','u':'..-','v':'...-','w':'.--','x':'-..-','y':'-.--','z':'--..','1':'.----','2':'..---','3':'...--','4':'....-','5':'.....','6':'-....','7':'--...','8':'---..','9':'----.','0':'-----','.':'.-.-.-',',':'--..--', '?':'..--..', "'":'.----.', '!':'-.-.--','/':'-..-.','(':'-.--.',')':'-.--.-','&':'.-...',':':'---...',';':'-.-.-.','=':'-...-','+':'.-.-.','-':'-...-','"':'.-..-.','error':'........' }
def dot(brightness=20):
    piglow.colour(1,brightness)
    sleep(speed)
    piglow.colour(1,0)
    sleep(speed)

def dash(brightness=20):
    piglow.colour(1,brightness)
    sleep(3*speed)
    piglow.colour(1,0)
    sleep(speed)

def space():
    sleep(2*speed)

def end_letter():
    sleep(2*speed)

def end_word():
    sleep(6*speed)


def code(sentance):
    if match('''^[a-zA-Z0-9.,?'!/()&:;=+" -]+$''',sentance):
        sen = sentance.lower()
        encoded = ''
        for letter in sen:
            encoded = encoded + morse[letter] + ' '

    else:
        encoded = morse['error']
        sentance = 'ERROR'
    print sentance.upper()
    print encoded    
    return encoded

def play_code(sentance):
    encoded = code(sentance)
    for char in encoded:
        if char == '.':
            dot()
        if char == '-':
            dash()
        if char == '|':
            end_letter()
        if char == ' ':
            space()

#play_code('I like fatties.')

