 print ('A slash indicates the start of a new word. ')
message = input('What is your message? \n')

for x in range (len(message)):
	if message[x] == 'A' or  message[x] == 'a':
		print('.-', end=' ')
	elif message[x] == 'B' or  message[x] == 'b':
		print('-...', end=' ')
	elif message[x] == 'C' or  message[x] == 'c':
		print('-.-.', end=' ')
	elif message[x] == 'D' or  message[x] == 'd':
		print('-..', end=' ')
	elif message[x] == 'E' or  message[x] == 'e':
		print('.', end=' ')
	elif message[x] == 'F' or  message[x] == 'f':
		print('..-.', end=' ')
	elif message[x] == 'G' or  message[x] == 'g':
		print('--.', end=' ')
	elif message[x] == 'H' or  message[x] == 'h':
		print('....', end=' ')
	elif message[x] == 'I' or  message[x] == 'i':
		print('..', end=' ')
	elif message[x] == 'J' or  message[x] == 'j':
		print('.---', end=' ')
	elif message[x] == 'K' or  message[x] == 'k':
		print('-.-', end=' ')
	elif message[x] == 'L' or  message[x] == 'l':
		print('.-..', end=' ')
	elif message[x] == 'M' or  message[x] == 'm':
		print('--', end=' ')
	elif message[x] == 'N' or  message[x] == 'n':
		print('-.', end=' ')
	elif message[x] == 'O' or  message[x] == 'o':
		print('---', end=' ')
	elif message[x] == 'P' or  message[x] == 'p':
		print('.--.', end=' ')
	elif message[x] == 'Q' or  message[x] == 'q':
		print('--.-', end=' ')
	elif message[x] == 'R' or  message[x] == 'r':
		print('.-.', end=' ')
	elif message[x] == 'S' or  message[x] == 's':
		print('...', end=' ')
	elif message[x] == 'T' or  message[x] == 't':
		print('-', end=' ')
	elif message[x] == 'U' or  message[x] == 'u':
		print('..-', end=' ')
	elif message[x] == 'V' or  message[x] == 'v':
		print('...-', end=' ')
	elif message[x] == 'W' or  message[x] == 'w':
		print('.--', end=' ')
	elif message[x] == 'X' or  message[x] == 'x':
		print('-..-', end=' ')
	elif message[x] == 'Y' or  message[x] == 'y':
		print('-.--', end=' ')
	elif message[x] == 'Z' or  message[x] == 'z':
		print('--..', end=' ')
	elif message[x] == '0':
		print('-----', end=' ')
	elif message[x] == '1':
		print('.----', end=' ')
	elif message[x] == '2':
		print('..---', end=' ')
	elif message[x] == '3':
		print('...--', end=' ')
	elif message[x] == '4':
		print('....-', end=' ')
	elif message[x] == '5':
		print('.....', end=' ')
	elif message[x] == '6':
		print('-....', end=' ')
	elif message[x] == '7':
		print('--...', end=' ')
	elif message[x] == '8':
		print('---..', end=' ')
	elif message[x] == '9':
		print('----.', end=' ')
	elif message[x] == ' ':
		print('/')
	else:
		print('Character at position ' + message[x] + 'cannot be identified')

x+1
print('')
