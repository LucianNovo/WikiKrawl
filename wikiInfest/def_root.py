import urllib2
#from urllib import encode 
import mwapi

#class hist_event:
#		def init(date, event_title, sentence)


def descend_get_ref(page):
	start_ref=page.find('[[')
	if start_ref == -1:
		return None, 0 
	end_ref=page.find(']]')
	article_title = page[(start_ref+2):end_ref+1]
	return article_title, end_ref+2 

def acquisition_refs(page): # collects all the references in a index, and stores them as the title
	article_refs=[]
	while True:
		ref, endpos = descend_get_ref(page) 
		if ref:
			article_refs.append(ref) 
			page = page[endpos:]
		else:
			break
	return article_refs
	
def smart_acquisition(scanned_ind,index,depth,page):#is the control function for reference parsing. Stores parsed/explored references in the index, stores unparse/discovered reference in another [] in scanned_ind
	size = len(index)#used to determine how many acquisitions should be preformed, and from which ref_index within the index	
	if depth == 1:#if the depth is one, only reap and return the things from the first index, also, store the title in the actual index.   
		index = acquisition_refs(page)#should return a [ [] ] index since this is the begining index,
		scanned_ind = scanned_ind + index #eventually will replace the references with the actual urls, and will prevent the smart_acq from circular references. 
		return index,scanned_ind 
	else:#reap the references 
		size = len(index)
		reapIndex = index[size-1]
		saveIndex = []
		tempIndex = []
		ret_index = index
		for a_ref in reapIndex:
			tempIndex = acquisition_refs(a_ref)#should return a [] so that it can be added to the specific index within the saveIndex in the next line
			saveIndex = saveIndex + tempIndex #in this statement
		for ref_index in ret_index:#filter all duplicate references from the saveIndex, before it is added to the saveIndex
			for ref in ref_index:
				if(saveIndex.index(ref)):
					index = saveIndex.index(ref)
					del saveIndex[index]
		ret_index.apppend(saveIndex)
		return ret_index, scanned_ind

def page_formater(page):# returns the article without the reference SECTION.
	page = str(page)
	end_article = page.find('==References==')
	article = page[:end_article]
	return article
		
def is_scanned(ref):
	for a_ref in scanned_index:
		if a_ref == ref:
			return True
		else:
			return False

def add_to_scanned(scanned_ref_index,ref):
	scanned_ref_index=scanned_ref_index + ref
	
def fetch_article_in_wikitext(article_title): #returns the wikitext page
	api = mwapi.MWApi('http://en.wikipedia.org')
	page = api.get({'action':'parse', 'page': article_title, 'prop': 'wikitext'})
	page = page['parse']['wikitext']
	return page

#def request_stringer(title, want_links):
#	if(want_links):
#		#format a request with links
#	else:
#		#format a request without links
	
def command_control(title):
	page = fetch_article_in_wikitext(title)#pulls the article from wikipedia using the title.
	page = page_formater(page)#returns the page without the references. 
	print "This is the article that we are scanning"
	print "--article omitted for space's sake--"
	scanned_refs_index, ref_index, index=[], [], []
	print "---------------------------------------------------------------"
	print "This is the the article reference index:"
	ref_index,scanned_refs_index= smart_acquisition(scanned_refs_index,index,1,page)#returns the 
	print ref_index
	print "---------------------------------------------------------------"
	print "This is the scanned index:"
	print scanned_refs_index
	
command_control('Great Depression')

#now I need to pull the other references, and save them to another 
#request w/ categories:/w/api.php?action=parse&format=json&page=Great%20Depression&prop=categories%7Clinks
# request /w/api.php?action=parse&format=json&page=Great%20Depression&prop=wikitext
# Now that I know the difference between these two, I can format a urlStringer, and an automatic requester- these should be used from the very first request.

class Article#object that contains the dateSentences, articleName, parentArticle
{
	def __init__(self, slugName, parentArt):
		self.artName = slugName
		self.parentArt = parentArt #the article that referenced this
		self.sentences = sentenceParser(slugName) #rips the sentences from the article, stores them in a DateSentence library of libraries
}

def sentenceParser(artTitle):#this takes the article title and returns a dictionary of DataSentence dictionaries.
{
	DictDict = {}
	SentDict = {}
	sentenceDate, remPage, date = getSentence_and_page(artTitle)
	#check if the date is in the DictDict
		#if yes add the SentenceDate to the sentDict
		#if no add the date to DictDic and the SentenceDate to the sentDict
	#
		
		
	#make the sentence as a DateSentence.
	#DateSentence("People died in 1923", "Great Depression", "1923")
	#Place the DateSentence in the dictionary 
	#
	#dictionary:
	# {"1923" : 1923_Dict}
	#		1923_Dict:
	#			{ "Article_name" : DateSentence }
	#
	# return the dictionary of DateSentence dictionaries. 
	#return DSDD
}

def getSentence_and_page(page): #returns the dateSentence, and the rest of the page
{
	frstPer, endPer = 0,0#bool value: whether the first or last period is found
	start_ref = page.find('19') #date
	if start_ref == -1:
		return None, 0 
	retDate = page[start_ref:start_ref+2] 
	#find the index of the first period before the date. 
	if(start_ref<10):
		frstPer = 1
		BegSent = 0
	while (frstPer != 1):
		preSent = page[(start_ref-10):start_ref]
		if (preSent.find('.')):
			BegSent = preSent.find('.')
			frstPer = 1 
		else:
			pre = 2
			preSent = page[(start_ref-(pre *10)):start_ref]
			pre = pre + 1
	  while (endPer != 1):
		postSent = page[(start_ref):(start_ref+10)]
		if (postSent.find('.')):
			EndSent = postSent.find('.')
			endPer = 1
		else:
			post = 2 
			postSent = page[start_ref:(start_ref + (post * 10)]
			post = post + 1
	dateSentence = page[BegSent:EndSent]
	remainPage = page[EndSent:]
	
	return dateSentence, remainPage, retDate
}





class DateSentence
{
	def __init__(self,inpSentence,inpParArtSlug, inpDate):
		self.sentence = inpSentence #
		self.parentArticle = inpParArtSlug
		self.date = inpDate
}