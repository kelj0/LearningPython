win_condition=(['TL','TM','TR'],['ML','MM','MR'],['LL','LM','LR'],
               ['TL','ML','LL'],['TM','MM','LM'],['TR','MR','LR'],
               ['TL','MM','LR'],['LL','MM','TR'])

theBoard={'TL': ' ', 'TM': ' ', 'TR': ' ',
          'ML': ' ', 'MM': ' ', 'MR': ' ',
          'LL': ' ', 'LM': ' ', 'LR': ' '}

def printBroad(board):
    print(board['TL'] + '|' + board['TM'] + '|'+board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|'+board['MR'])
    print('-+-+-')
    print(board['LL'] + '|' + board['LM'] + '|'+board['LR'])


turn='X'
for i in range(9):
    printBroad(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move=input()
    
    theBoard[move]=turn
    if turn=='X':
        turn='Y'
    else:
        turn='X'


