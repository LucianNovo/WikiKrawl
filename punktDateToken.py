import urllib2
from simplemediawiki import MediaWiki
from bs4 import BeautifulSoup
import nltk
import nltk.data
#from nltk.tokenize import word_tokenize, workpunct_tokenize, sent_tokenize

from nltk.tokenize.punkt import PunktWordTokenizer

def command_control(article_title):
	dateSentenceDate = []
	articleInWikitext, htmlArticle	= fetch_article_in_wikitext(article_title)
	dateSentenceDate = DateGather(htmlArticle, dateSentenceDate)
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
	
	print text
	sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
	sentenceList = sent_detector.tokenize(text.strip())
	for sentence in sentenceList:
		subList = PunktWordTokenizer().tokenize(sentence)
		for w in subList:
			if w.startswith('19'):
				datesentencedateDataStruct.append([ w[:4], sentence])
				print w[:4]
				print sentence
	return datesentencedateDataStruct

command_control('Great Depression')

				