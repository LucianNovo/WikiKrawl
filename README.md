#Welcome to the WikiKrawl project. 
  
  The simile timeline is a powerful and engaging timeline that has been created under the MIT opensource license, 
  using the simplemediawiki api, nltk toolkit and Beautiful soup it's possible to **scrape articles** from wikipedia
  and assemble timelines.
  
  Here's a summary of the development process. 
  
##Phase 1:
####Collect a very simple data set using simplemediawikiapi(the python wrapper) 
* Collect(dates and the sentences they belong to(dateSentences)) from articles
* Store(dates and the sentences they belong to(dateSentences)) in a dict dict structure with dateYear as the primary key(TBD)
* Feed(dates and the sentences they belong to) to simile timeline structure(by simply creating a json file)
            
####Phase 2: Collect more semantic data  
* Collect(dates, dateSentences, articleSubjs, articleCategories, articleInnerWikiLinks)(semanticEventData)
from articles, from timeline_articles, from metadata
* Store(dates, dateSentences, articleSubjs, articleCategories, articleInnerWikiLinks)(semanticEventData) in some advanced data format
* Feed(dates, dateSentences, articleSubjs) to simile timeline
            
####Phase 3: Apply the semanitic data for collecting relative articles
* Explore(collectedArticleInnerWikiLinks, articleCategories) to Collect semanticEventData from other articles
* Collect(EventData(dates paired with dateSentences), semanticEventData(now defined as articleSubjs, articleCategories, articleInnerWikiLinks)) from articles, from timeline_articles, from metadata
* Store(EventData(dates paired with dateSentences), semanticEventData) in an advancedData format oriented towards checking the semanticEventData
* Feed(advancedData) to similetimeline that is logical


#### Phase 4: build a product for users.
I've spent time away from the code to install mediawiki on my server and configure this [prototype](http://www.luciannovosel.com/MediaWiki/mediawiki-1.19.2/index.php?title=Great_depression, 'prototype')

##Current phase
#####Finnished Phase 1:
  This project will have many iterations, begining with a build that accesses(parses and collects) eventData from a
  single article. This data will be stored on a locally in a TBD data structure that will be fed to a simileTimeline. 

#####Currently on Phase 2:
  With the timeline up and running, it is time to begin to format events for the timeline, and build metadata for each of
  the eventDate entries. Gather Dates will now have a larger role in gathering references, and building more descriptive events.  
  
#####Fastforwared to Phase 4 to 'get something out there':
  Now that there is a working mediawiki site it will be easier to work towards the product.
