print ('User tips: Every line has a character and each slash indicates the start of a new word. ')
message = input('What is your message? \n')

for x in range (len(message)):
	if message[x] == 'A' or  message[x] == 'a':
		print('.-')
	elif message[x] == 'B' or  message[x] == 'b':
		print('-...')
	elif message[x] == 'C' or  message[x] == 'c':
		print('-.-.')
	elif message[x] == 'D' or  message[x] == 'd':
		print('-..')
	elif message[x] == 'E' or  message[x] == 'e':
		print('.')
	elif message[x] == 'F' or  message[x] == 'f':
		print('..-.')
	elif message[x] == 'G' or  message[x] == 'g':
		print('--.')
	elif message[x] == 'H' or  message[x] == 'h':
		print('....')
	elif message[x] == 'I' or  message[x] == 'i':
		print('..')
	elif message[x] == 'J' or  message[x] == 'j':
		print('.---')
	elif message[x] == 'K' or  message[x] == 'k':
		print('-.-')
	elif message[x] == 'L' or  message[x] == 'l':
		print('.-..')
	elif message[x] == 'M' or  message[x] == 'm':
		print('--')
	elif message[x] == 'N' or  message[x] == 'n':
		print('-.')
	elif message[x] == 'O' or  message[x] == 'o':
		print('---')
	elif message[x] == 'P' or  message[x] == 'p':
		print('.--.')
	elif message[x] == 'Q' or  message[x] == 'q':
		print('--.-')
	elif message[x] == 'R' or  message[x] == 'r':
		print('.-.')
	elif message[x] == 'S' or  message[x] == 's':
		print('...')
	elif message[x] == 'T' or  message[x] == 't':
		print('-')
	elif message[x] == 'U' or  message[x] == 'u':
		print('..-')
	elif message[x] == 'V' or  message[x] == 'v':
		print('...-')
	elif message[x] == 'W' or  message[x] == 'w':
		print('.--')
	elif message[x] == 'X' or  message[x] == 'x':
		print('-..-')
	elif message[x] == 'Y' or  message[x] == 'y':
		print('-.--')
	elif message[x] == 'Z' or  message[x] == 'z':
		print('--..')
	elif message[x] == '0':
		print('-----')
	elif message[x] == '1':
		print('.----')
	elif message[x] == '2':
		print('..---')
	elif message[x] == '3':
		print('...--')
	elif message[x] == '4':
		print('....-')
	elif message[x] == '5':
		print('.....')
	elif message[x] == '6':
		print('-....')
	elif message[x] == '7':
		print('--...')
	elif message[x] == '8':
		print('---..')
	elif message[x] == '9':
		print('----.')
	elif message[x] == ' ':
		print('/')
	else:
		print('Character at position ' + message[x] + 'cannot be identified')

x+1