from random import randint
import re

STARTTAG = "<start>"
ENDTAG = "<end>"
class MarkovChainBot:
	''' A Markov Chain text generator 
	data is a list of strings that it is trained on, ie a list of books.
	'''
	def __init__(self, exclusion_list):
		''' '''
		self.data = []
		self.probs = {STARTTAG: [ENDTAG]}
		self.trained = True
		self.exclusions = [re.compile(x) for x in exclusion_list]

	def Train(self):
		assert type(self.data) == list
		for obj in self.data:
			assert type(obj) == str
		if len(self.data) == 0:
			return

		self.probs = {}
		def addWordToProbsDict(dic, index, target):
			if index in dic.keys():
			   	dic[index].append(target)
			else:
				dic[index] = [target]

		for text in self.data:
			words = list(map(lambda x: x.lower(), text.split()))
			if not words:
				continue 
			addWordToProbsDict(self.probs, STARTTAG, words[0])
			for i in range(len(words)-1):
				addWordToProbsDict(self.probs, words[i], words[i+1])
			addWordToProbsDict(self.probs, words[len(words)-1], ENDTAG)

	def GenerateText(self):
		ret = ''
		curWord = STARTTAG
		while(curWord != ENDTAG):
			nextIn = randint(0, len(self.probs[curWord])-1)
			curWord = self.probs[curWord][nextIn]
			if(curWord == ENDTAG or curWord == STARTTAG):
				continue
			
			render = True
			for pat in self.exclusions:
				if(pat.match(curWord)):
					render = False
			if render:
				ret += curWord

			if(curWord != ENDTAG):
				ret += ' '
		return ret
			
		
