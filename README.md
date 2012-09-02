Welcome to the WikiKrawl project. 
  
  The simile timeline is a powerful and engaging timeline that has been created under the MIT opensource license, 
  using the simplemediawiki api, nltk toolkit and Beautiful soup it's possible to build timelines that source
  eventData from wikipedia. 
  
  
  To Summarize the development process, we'll iterate by developing the following functions of the program:
    Phase 1: collect the simplist of data using simplemediawikiapi
        Collect(dates and the sentences they belong to(dateSentences))
            -from articles
        Store(dates and the sentences they belong to(dateSentences))
            -in a dict dict structure with dateYear as the primary key(TBD)
        Feed(dates and the sentences they belong to)
            -to simile timeline structure
            
    Phase 2: collect advanced semanticData that will allow us to parse 
        Collect(dates, dateSentences, articleSubjs, articleCategories, articleInnerWikiLinks)(semanticEventData)
            -from articles 
            -from timeline_articles
            -from metadata
        Store(dates, dateSentences, articleSubjs, articleCategories, articleInnerWikiLinks)(semanticEventData)
            -in some advanced data format
        Feed(dates, dateSentences, articleSubjs)
            -to simile timeline
            
    Phase 3: build an explore/crawl function that will use collected semanticEventData to find relative articles. 
        Explore(collectedArticleInnerWikiLinks, articleCategories) 
            -to Collect semanticEventData from other articles
        Collect(EventData(dates paired with dateSentences), semanticEventData(now defined as articleSubjs, articleCategories, articleInnerWikiLinks))
            -from articles
            -from timeline_articles
            -from metadata
        Store(EventData(dates paired with dateSentences), semanticEventData)
            -in an advancedData format oriented towards checking the semanticEventData
        Feed(advancedData)
            -to similetimeline that is logical
            
    Phase 4: clean, improve speed, limit redundancy, play with parameters to optimize
  
    Phase 5: provide a host, install on the host, provide a web interface to give users the ability to play with parameters
    
    Phase 6: Let the users decide what phase 6 will be. 
          
          
Currently on Phase 1:
  This project will have many iterations, begining with a build that accesses(parses and collects) eventData from a
  single article. This data will be stored on a locally in a TBD data structure that will be fed to a simileTimeline input. 
  
  
  