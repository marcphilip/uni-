# author marc 
# version 1.0

strophe = '''
Sie 
Sie haben
Sie haben uns
'''

refrain = '''
Sie haben uns
Sie haben uns gefragt
Sie haben uns gefragt
Sie haben uns gefragt und wir haben nichts gesagt
'''

for zeile in range(10):
    if(zeile == 5 or zeile == 9):
        print(refrain)
    else:
        print(strophe)
