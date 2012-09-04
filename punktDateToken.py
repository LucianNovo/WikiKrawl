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
	import codecs
	wiki = MediaWiki('http://en.wikipedia.org/w/api.php')
	wikiTextPage = wiki.call({'action':'parse', 'page': articleTitle, 'prop': 'wikitext'});
	wikiTextPage = wikiTextPage['parse']['wikitext']['*']
	codecs.open("FetchFunctionPulls/fetchWikiTextPage",'w', encoding='utf-8').write(wikiTextPage)
	htmlArticle = wiki.call({ 'action':'parse','page':articleTitle, 'prop': 'text'});
	htmlArticle = htmlArticle['parse']['text']['*']
	codecs.open("FetchFunctionPulls/fetchHTMLPage",'w', encoding='utf-8').write(htmlArticle)
	print type(htmlArticle)
	return wikiTextPage, htmlArticle

def DateGather(htmlText,datesentencedateDataStruct): #returns the sentences and dates in a list (sentences, dates)
	import codecs
	htmlText = TOCKiller(htmlText)
	htmlTextSoupObj = BeautifulSoup(htmlText)
	text = htmlTextSoupObj.get_text()
	text = text.replace("\'","\\\'")
	text = text.replace("\\n", "")
	text = referenceBracketRemover(text)
	text = cutOffSection(text, "See also")
	codecs.open("TextFromArticleFile",'w',encoding='utf-8').write(text)#save the article text to a local location. 
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	sentenceList = sent_detector.tokenize(text.strip())
	tempRedundancyCheck = 0 #stores sentences to make sure that one sentence isn't reused multiple times. Not implemented yet bc redundancy is currently desired.
	for sentence in sentenceList:
		subList = PunktWordTokenizer().tokenize(sentence)
		for w in subList:
			if w.startswith('19'):
				sentence = sentence.replace("\n","")
				datesentencedateDataStruct.append([ w[:4], sentence])
				print w[:4]
				print sentence
	return datesentencedateDataStruct

def cutOffSection(inpText, stopPoint):
	return inpText[:inpText.rfind(stopPoint)]
	
#use the wikitext formatting to remove the contents bar.
#this function will serve as an intermediary between grabing and cleaning.
def TOCKiller(inpArticle):#removes a certain content block while there it is still formatted in wikitext writup
	startTOC   = inpArticle.find('<table id="toc" class="toc">')
	endTOC     = inpArticle[startTOC:].find('</table>')
	retArticle = inpArticle[:startTOC] + inpArticle[(endTOC+startTOC):]
	return retArticle 
	
def referenceBracketRemover(inpText):
	import re
	inpText = re.sub(r'\[\d{,3}\]',"",inpText)
	inpText = re.sub(r'\[(.*?)\]',"",inpText)
	return inpText

def rewriteTheJS(mainArticleTitle,dateEventIndex):
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
			timelineEvent += ("""' }, \n""")
			appendFile += (timelineEvent)
		appendFile += (""" ] }""")
		JSfile.write(appendFile)

command_control('Great Depression')
		
		
		


				