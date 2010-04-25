# -*- coding: utf-8 -*-

from random import choice

def showHangman ( count ):

	head = ' '
	larm = ' '
	chest = ' '
	rarm = ' '
	torso = ' '
	lleg = ' '
	rleg = ' '

	if count > 0:
		head = 'O'
	if count > 1:
		chest = '|'
	if count > 2:
		larm = '\\'
	if count > 3:
		rarm = '/'
	if count > 4:
		torso = '|'
	if count > 5:
		lleg = '/'
	if count > 6:
		rleg = '\\'

	print "      .-----."
	print "      |     %s" % head
	print "      |    %s%s%s" % ( larm, chest, rarm )
	print "      |     %s" % torso
	print "      |    %s %s" % ( lleg, rleg )
	print "  ____|____"

def showState ( missed, guessed, stub ):
	print "=" * 40
	showHangman( len( missed ) )
	print
	print "  Guessed :", " ".join( guessed )
	print "   Missed :", " ".join( missed )
	print
	print "      Word:", "".join( stub )
	print

def main ():

	f = open( 'words.txt', 'r' )
	words = []
	for word in f:
		words.append( word.replace( "\n", '' ) )
	f.close()

	word = choice( words ).upper()
	found = 0
	stub = []
	for i in range( 0, len( word ) ):
		stub.append( "_" )

	guessed = []
	missed = []

	print "  Welcome To Hangman!"
	print

	while len( missed ) < 7 and len( word ) > found:
		showState( missed, guessed, stub )
		while True:
			guess = raw_input( "  Guess A Letter: " ).upper()
			print
			if len( guess ) != 1:
				print "  Oops! You can only guess one letter at a time. Try again!"
				print
			elif guess in guessed:
				print "  Oops! You already guessed that letter! Try again!"
				print
			else:
				if guess in word:
					for i in range( 0, len( word ) ):
						if guess == word[i]:
							stub[i] = guess
							found = found + 1
					print "  You guessed correct!"
				else:
					missed.append( guess )
					print "  You guessed wrong!"
				guessed.append( guess )
				break
		print

	showState( missed, guessed, stub )

	if len( missed ) >= 7:
		print "  You lost!"
		print
		print "  The word was", word
	else:
		print "  You won!"
		print "  Great job!"
	print

if __name__ == "__main__":
	main()
