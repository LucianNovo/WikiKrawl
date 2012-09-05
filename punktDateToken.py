import urllib2
from simplemediawiki import MediaWiki
from bs4 import BeautifulSoup
import nltk
import nltk.data
import os.path
#from nltk.tokenize import word_tokenize, workpunct_tokenize, sent_tokenize

class dispParameters: 
	def __init__(self, band, frame):
		self.isBand = band #if there should be a band for the event(0/1)
		self.frame  = frame #early(0), late(1), the(era, decade, etc)(2) 
		
class referenceMetadata:
	def __init__(self, inpReferenceFromSentence):
		self.referenceFromSentence = inpReferenceFromSentence #the reference to an internal article that is within the sentence.#Might become a list!
		
class dateSentence:
	def __init__(self, inpDateSentence, inpDate):
		self.dateSentence = inpDateSentence
		self.date		  = inpDate

class eventEntry:
	def __init__(self, inpDateSentence, inpDate, inpBand, inpFrame, inpReferenceFromSentence):
		self.dateSentenceEntry = dateSentence(inpDateSentence, inpDate) 
		self.dispParameters    = dispParameters(inpBand, inpFrame)
		self.referenceMetadata = referenceMetadata(inpReferenceFromSentence)

from nltk.tokenize.punkt import PunktWordTokenizer

def command_control(article_title):
	dateSentenceDate = {}
	articleInWikitext, htmlArticle	= fetch_article_in_wikitext(article_title)
	dateSentenceDate = DateGather(htmlArticle, dateSentenceDate)
	rewriteTheJS(article_title, dateSentenceDate)

def fetch_article_in_wikitext(articleTitle): #fetches the article data using the simplemediawiki lib.
	import codecs
	wiki = MediaWiki('http://en.wikipedia.org/w/api.php')
	wikiTextPage = wiki.call({'action':'parse', 'page': articleTitle, 'prop': 'wikitext'});
	wikiTextPage = wikiTextPage['parse']['wikitext']['*']
	codecs.open("FetchFunctionPulls/fetchWikiTextPage",'w', encoding='utf-8').write(wikiTextPage)
	htmlArticle = wiki.call({ 'action':'parse','page':articleTitle, 'prop': 'text'});
	htmlArticle = htmlArticle['parse']['text']['*']
	codecs.open("FetchFunctionPulls/fetchHTMLPage",'w', encoding='utf-8').write(htmlArticle)
	#print type(htmlArticle)
	return wikiTextPage, htmlArticle

def DateGather(htmlText,datesentencedateDataStruct): #returns the sentences and dates in a list (sentences, dates)
	import codecs
	htmlText = TOCKiller(htmlText)
	htmlTextSoupObj = BeautifulSoup(htmlText)
	text = htmlTextSoupObj.get_text()
	text = text.replace("\'","\\\'")
	text = text.replace("\n", "")
	text = referenceBracketRemover(text)
	text = cutOffSection(text, "See also")
	codecs.open("TextFromArticleFile",'w',encoding='utf-8').write(text)#save the article text to a local location. 
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	sentenceList = sent_detector.tokenize(text.strip())
	lastWord = -1
	for sentence in sentenceList:
		subList = PunktWordTokenizer().tokenize(sentence)#lists all words in the sentence
		for w in subList: #for each word
			if w.startswith('19'):
				sentence = sentence.replace("\n","")
				datesentencedateDataStruct = insertIntoDict(datesentencedateDataStruct, w, sentence, lastWord)
				lastWord = w
	return datesentencedateDataStruct

def insertIntoDict(dictDataName, inpWord, inpSentence, inpLastWord):#inserts the semanticSentenceData into an appropriate dictionary
	inpReferenceFromSentence = 0 
	if(inpWord.endswith('s')):
		era = 1
	else:
		era = 0
	if(dictDataName.has_key(inpWord[:4])):
		dictDataName[inpWord[:4]][inpSentence] = eventEntry(inpSentence, inpWord[:4], era, inpLastWord, inpReferenceFromSentence) #must match the following call: 
	else:
		dictDataName[inpWord[:4]] = {}#create a key for that date, then a dictionary for the semanticEventEntries. 
		dictDataName[inpWord[:4]][inpSentence] = eventEntry(inpSentence, inpWord[:4], era, inpLastWord, inpReferenceFromSentence) #must match the following call: (self, inpDateSentence, inpDate, inpBand, inpFrame, inpReferenceFromSentence):
	return dictDataName
	
def TOCKiller(inpArticle):#removes a certain content block while there it is still formatted in wikitext writup #use the wikitext formatting to remove the contents bar. #this function will serve as an intermediary between grabing and cleaning.
	startTOC   = inpArticle.find('<table id="toc" class="toc">')
	endTOC     = inpArticle[startTOC:].find('</table>')
	retArticle = inpArticle[:startTOC] + inpArticle[(endTOC+startTOC):]
	return retArticle 
	
def referenceBracketRemover(inpText):
	import re
	inpText = re.sub(r'\[\d{,3}\]',"",inpText)
	inpText = re.sub(r'\[(.*?)\]',"",inpText)
	return inpText

def rewriteTheJS(mainArticleTitle,dateEventDictDict):
	import codecs
	simileTimelineJSFilePath = "timeline_local_example_1.0/local_example/local_data.js"
	import os.path
	import re
	if (os.path.isfile(simileTimelineJSFilePath)):
		JSfile = codecs.open(simileTimelineJSFilePath, 'w', encoding='utf-8')
		appendFile = """var timeline_data = {  // save as a global variable
						'dateTimeFormat': 'iso8601',
						'wikiURL': "http://simile.mit.edu/shelf/",
						'wikiSection': '"""
		appendFile += (mainArticleTitle)
		appendFile += ("""', 'events' : [ \n""")
		for dateDict in dateEventDictDict.values():
			for event in dateDict.values():			
				timelineEvent = ""
				timelineEvent += (""" {\'start\': '""")
				timelineEvent += event.dateSentenceEntry.date
				timelineEvent += ("""' , 'end': '""")
				timelineEvent += event.dateSentenceEntry.date
				timelineEvent += ("""' , 'title' : '""")
				timelineEvent += event.dateSentenceEntry.dateSentence
				timelineEvent += ("""' , 'description' : '""") 
				timelineEvent += event.dateSentenceEntry.dateSentence
				timelineEvent += ("""', 'icon' : 'dull-blue-circle.png'""")
				timelineEvent += ("""}, \n""")
				appendFile += (timelineEvent)
		appendFile = cutOffSection(appendFile, ',')
		appendFile += (""" ] }""")
		JSfile.write(appendFile)

def cutOffSection(inpText, stopPoint):
	return inpText[:inpText.rfind(stopPoint)]

command_control('Great Depression')
		
		


				