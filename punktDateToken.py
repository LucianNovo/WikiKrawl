import urllib2
from simplemediawiki import MediaWiki
from bs4 import BeautifulSoup
import nltk
import nltk.data
import os.path
#from nltk.tokenize import word_tokenize, workpunct_tokenize, sent_tokenize

from nltk.tokenize.punkt import PunktWordTokenizer

def command_control(article_title):
	dateSentenceDate = []
	articleInWikitext, htmlArticle	= fetch_article_in_wikitext(article_title)
	dateSentenceDate = DateGather(htmlArticle, dateSentenceDate)
	rewriteTheJS(article_title, dateSentenceDate)
	#print dateSentenceDate
	#preform a parse of all innerWiki links, or use the media wikiApi to shoo

def fetch_article_in_wikitext(articleTitle): #fetches the article data using the simplemediawiki lib.
	wiki = MediaWiki('http://en.wikipedia.org/w/api.php')
	wikiTextPage = wiki.call({'action':'parse', 'page': articleTitle, 'prop': 'wikitext'});
	htmlArticle = wiki.call({ 'action':'parse','page':articleTitle, 'prop': 'text'});#
	#print "The WikiText Article: "
	#print wikiTextPage
	#print "The Article in clean English: "
	#print article
	return wikiTextPage, htmlArticle

def DateGather(htmlText,datesentencedateDataStruct): #returns the sentences and dates in a list (sentences, dates)
	htmlText = str(htmlText)
	htmlTextSoupObj = BeautifulSoup(htmlText)
	text = htmlTextSoupObj.get_text()
	text = text.replace("\n","")
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	sentenceList = sent_detector.tokenize(text.strip())
	tempRedundancyCheck = 0#stores sentences to make sure that one sentence isn't reused multiple times. 
	for sentence in sentenceList:
		subList = PunktWordTokenizer().tokenize(sentence)
		saveLocForArtText = "../wikitext.doc" 
		for w in subList:
			if w.startswith('19'):
				datesentencedateDataStruct.append([ w[:4], sentence])
				print w[:4]
				print sentence
	return datesentencedateDataStruct

def rewriteTheJS(mainArticleTitle,dateEventIndex):
	import codecs
	simileTimelineJSFilePath = "../timeline_local_example_1.0/local_example/local_data.js"
	import os.path
	if (os.path.isfile(simileTimelineJSFilePath)):
		JSfile = codecs.open(simileTimelineJSFilePath, 'w', encoding='utf-8')
		appendFile = """var timeline_data = {  // save as a global variable
						'dateTimeFormat': 'iso8601',
						'wikiURL': "http://simile.mit.edu/shelf/",
						'wikiSection': """
		appendFile += (mainArticleTitle)
		appendFile += ("""', 'events' : [ """)
		for event in dateEventIndex:
			timelineEvent = ""
			timelineEvent += (""" {\'start\': '""")
			timelineEvent += (event[0])
			timelineEvent += ("""' , 'end': '""")
			timelineEvent += (event[0])
			timelineEvent += ("""' , 'title' : '""")
			timelineEvent += (event[1])
			timelineEvent += ("""' , 'description' : '""") 
			timelineEvent += (event[1])
			timelineEvent += ("""' }""")
			appendFile += (timelineEvent)
		appendFile += (""" ] }""")
		JSfile.write(appendFile)

command_control('Great Depression')
		
		
		


				