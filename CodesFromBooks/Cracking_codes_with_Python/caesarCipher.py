import sys
message = ' '.join(sys.argv[3:])
key = int(sys.argv[2])
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890 !?.'

translated = ''
for symbol in message:
    if symbol in SYMBOLS:
        symbolIndex = SYMBOLS.find(symbol)
        if sys.argv[1] == 'd':
            translatedIndex = symbolIndex - key
        elif sys.argv[1] == 'e':
            translatedIndex = symbolIndex + key
        if translatedIndex >= len(SYMBOLS):
            translatedIndex = translatedIndex - len(SYMBOLS)
        elif translatedIndex < 0:
            translatedIndex = translatedIndex + len(SYMBOLS)

        translated = translated + SYMBOLS[translatedIndex]
    else:
        translated = translated + symbol
print(translated)
