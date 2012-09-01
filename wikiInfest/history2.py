Lucian-Novosels-MacBook-Pro:wikiCrawler lucstencildude$ easy_install python-mwapi
Searching for python-mwapi
Reading http://pypi.python.org/simple/python-mwapi/
Reading http://github.com/yuvipanda/python-mwapi
Best match: python-mwapi 0.1.1
Downloading http://pypi.python.org/packages/source/p/python-mwapi/python-mwapi-0.1.1.tar.gz#md5=11ae02e3b9adbaaf74624e663dee1397
Processing python-mwapi-0.1.1.tar.gz
Running python-mwapi-0.1.1/setup.py -q bdist_egg --dist-dir /var/folders/7F/7F32LJMME2i26IcDJ0x87E+++TI/-Tmp-/easy_install-8gRuF8/python-mwapi-0.1.1/egg-dist-tmp-BAOFrq
zip_safe flag not set; analyzing archive contents...
Adding python-mwapi 0.1.1 to easy-install.pth file

Installed /Library/Python/2.6/site-packages/python_mwapi-0.1.1-py2.6.egg
Processing dependencies for python-mwapi
Searching for requests
Reading http://pypi.python.org/simple/requests/
Reading http://python-requests.org
Reading https://github.com/kennethreitz/requests
Best match: requests 0.13.3
Downloading http://pypi.python.org/packages/source/r/requests/requests-0.13.3.tar.gz#md5=54387d7df6c69580b906dcb5a2bd0724
Processing requests-0.13.3.tar.gz
Running requests-0.13.3/setup.py -q bdist_egg --dist-dir /var/folders/7F/7F32LJMME2i26IcDJ0x87E+++TI/-Tmp-/easy_install-IYy5y1/requests-0.13.3/egg-dist-tmp-DLVbQb
warning: no files found matching 'tests/*.'
SyntaxError: ('invalid syntax', ('build/bdist.macosx-10.6-universal/egg/requests/packages/chardet2/test.py', 8, 27, "    print(f.ljust(60), end=' ')\n"))

zip_safe flag not set; analyzing archive contents...
requests._oauth: module references __file__
requests.certs: module references __file__
SyntaxError: ('invalid syntax', ('/Library/Python/2.6/site-packages/requests-0.13.3-py2.6.egg/requests/packages/chardet2/test.py', 8, 27, "    print(f.ljust(60), end=' ')\n"))

Adding requests 0.13.3 to easy-install.pth file

Installed /Library/Python/2.6/site-packages/requests-0.13.3-py2.6.egg
Finished processing dependencies for python-mwapi
Lucian-Novosels-MacBook-Pro:wikiCrawler lucstencildude$ python
Python 2.7.3 (v2.7.3:70274d53c1dd, Apr  9 2012, 20:52:43) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mwapi
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ImportError: No module named mwapi
>>> 
KeyboardInterrupt
>>> exit()
Lucian-Novosels-MacBook-Pro:wikiCrawler lucstencildude$ which python
/Library/Frameworks/Python.framework/Versions/2.7/bin/python
Lucian-Novosels-MacBook-Pro:wikiCrawler lucstencildude$ python
python            python2           python2.5         python2.6-config  python2.7-config  pythonw2          pythonw2.6        
python-32         python2-32        python2.5-config  python2.7         pythonw           pythonw2-32       pythonw2.7        
python-config     python2-config    python2.6         python2.7-32      pythonw-32        pythonw2.5        pythonw2.7-32     
Lucian-Novosels-MacBook-Pro:wikiCrawler lucstencildude$ python2.6
Python 2.6.1 (r261:67515, Jun 24 2010, 21:47:49) 
[GCC 4.2.1 (Apple Inc. build 5646)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import mwapi
>>> api = mwapi.MWApi('http://en.wikipedia.org')
>>> f = api.get({'action': 'parse', 'page': 'Great Depression', 'prop': 'wikitext'})
>>> f

