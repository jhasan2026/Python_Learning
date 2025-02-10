
import re

text_to_search = '''abcdefghijklmnopqurtuvwxyz
    ABCDEFGHIJKLMNOPQRSTUVWXYZ
    1234567890
    
    Ha HaHa
    
    MetaCharacters (Need to be escaped):
    . ^ $ * + ? { } [ ] \ | ( )
    
    coreyms.com
    
    321-555-4321
    123.555.1234
    123*555*1234
    800-555-1234
    900-555-1234
    
    cat 
    mat
    pat
    bat
    
    Mr. Schafer
    Mr Smith
    Ms Davis
    Mrs. Robinson
    Mr. T
    
    '''

sentence = 'Start a sentence and then bring it to an end'

# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'.')    #Any Character Except New Line
# pattern = re.compile(r'\d')   #Digit (0-9)
# pattern = re.compile(r'\D')   #Not a Digit (0-9)
# pattern = re.compile(r'\w')   #Word Character (a-z, A-Z, 0-9, _)
# pattern = re.compile(r'\W')   #Not a Word Character
# pattern = re.compile(r'\s')  #Whitespace (space, tab, newline)
# pattern = re.compile(r'\S')   #Not Whitespace (space, tab, newline)
# pattern = re.compile(r'\bHa')  #Word Boundary
# pattern = re.compile(r'\BHa')  #Not a Word Boundary
# pattern = re.compile(r'^Start')   #Beginning of a String
# pattern = re.compile(r'^Start')   #Beginning of a String("start")
# pattern = re.compile(r'^a')   #Beginning of a String("a")
# pattern = re.compile(r'end$')   #End of a String("end")
# pattern = re.compile(r'a$')   #End of a String("a")



# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')   #contain ddd()ddd()dddd  ()->any char except new line
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d')   #contain ddd()ddd()dddd  ()->[- or .]
# pattern = re.compile(r'[8,9]00[-.]\d\d\d[-.]\d\d\d\d')   #contain ddd()ddd()dddd  ()->[8 or 9]00
# pattern = re.compile(r'[1-5]')   #contain 1 to 5
# pattern = re.compile(r'[a-zA-Z]')   #contain a to z or A to Z   {[]      - Matches Characters in brackets}
# pattern = re.compile(r'[^a-zA-Z]')   #contains Not a to z or A to Z  {[^ ]    - Matches Characters NOT in brackets}
# pattern = re.compile(r'[^b]at')   #contain (not b) and (a + t)
# pattern = re.compile(r'\d{3}.\d{3}.\d{4}')   #contain digit*3  digit*3   digit*4   [ {3}     - Exact Number]
# pattern = re.compile(r'Mr\.?\s[A-Z]\w+')   #contain Mr. or Mr   [ ?   - 0 or One] + OneChar + (oneOrMorw+)
# pattern = re.compile(r'Mr\.?\s[A-Z]\w*')   #contain Mr. or Mr   [ ?   - 0 or One] + + OneChar + (zeroOrMorw*)
pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')   #contain M(). or M()   [ ?   - 0 or One] + + OneChar + (zeroOrMorw*)   ()->[( )     - Group]


# -----------------------------------------------
# matches = pattern.finditer(text_to_search)
#
#
# with open('data.txt','r',encoding='utf-8') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)



# -----------------------------------------------
matches = pattern.finditer(text_to_search)

for match in matches:
    print(match)


# # ----------------------------------------------------
#
# matches = pattern.finditer(sentence)
#
# for match in matches:
#     print(match)