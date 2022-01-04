# hackernews_scraper
Python (v3.8) script to scrap the news off Y-Combinators Hacker news site and only return the articles that scored over 100 points (ie. very famous articles). Note, this script was hard coded for hackerNews but can be easily modified for other news sites by changing the Beautiful soup tags to your specific usecase.

RUN IMPLEMENTATION

Download single file
Run following python command from the CLI (below example is for mac)
Pass the HackerNews site (ie. ycombinator.com) and number of pages to scrap from to python script command below:

program to run = scrape.py
URL = ycombinator.com
pages to scrap = 3

INPUT EXAMPLE: (venv) Username@Users-MacBook-Air % **python3 scrape.py ycombinator.com 3**

Output will show a sorted list of articles with the most points to the less (that scored at least over 100 points)

{Example output was pulled on Jan 3rd, 2022}

_https://news.ycombinator.com/news?p=1
https://news.ycombinator.com/news?p=2
{'title': 'Elizabeth Holmes found guilty',
'url': 'https://www.axios.com/theranos-elizabeth-holmes-verdict-df20ad3f-95bd-400c-bf42-a379ade65c2c.html',
'votes': 666}
{'title': 'Search engines and SEO spam'
'url': 'https://twitter.com/paulg/status/1477760548787920901',
'votes': 531}
{'title': 'Dura is a background process that watches your Git repositories',
'url': 'https://github.com/tkellogg/dura',
'votes': 366}
{'title': 'Vanta.js: Animated 3D backgrounds for websites',
'url': 'https://www.vantajs.com/',
'votes': 353}
{'title': 'Using a mild Twitter addiction to get things done',
'url': 'https://nick.comer.io/post/ios-shortcuts',
'votes': 339}
{'title': 'Hacking a VW Golf Power Steering ECU',
'url': 'https://blog.willemmelching.nl/carhacking/2022/01/02/vw-part1/',
'votes': 336}
{'title': "Copyright doesn't need 95 years to get the job done",
'url': 'https://fullstackeconomics.com/winnie-the-pooh-should-have-been-free-decades-ago/',
'votes': 326}
{'title': 'Compiling a Go program into a native binary for Nintendo Switch',
'url': 'https://ebiten.org/blog/native_compiling_for_nintendo_switch.html',
'votes': 324}
{'title': 'Show HN: Clone your voice and speak a foreign language',
'url': 'https://coqui.ai/',
'votes': 307}
{'title': 'Healthy soil is key to feeding the world',
'url': 'https://worldsensorium.com/healthy-soil-is-the-real-key-to-feeding-the-world/',
'votes': 278}
{'title': 'Ask HN: Who is hiring? (January 2022)',
'url': 'item?id=29782099',
'votes': 273}
{'title': 'Ask HN: Why is there a chip shortage?',
'url': 'item?id=29781027',
'votes': 254}
{'title': 'Lab Leak 2.0?',
'url': 'https://bprice.substack.com/p/lab-leak-20',
'votes': 247}
{'title': 'Poll: Which FAANG is the most likely to decline in the years ahead?',
 'url': 'item?id=29785046',
 'votes': 236}
{'title': 'High beef prices and the destruction of independent cattle ranching',
 'url': 'https://mattstoller.substack.com/p/economists-to-cattle-ranchers-stop',
 'votes': 202}
{'title': 'The Matrix looks dramatically different on Hulu versus on HBO Max',
 'url': 'https://www.echevarria.io/blog/the-matrix-looks-different-hulu-hbo-max/index.html',
 'votes': 193}
{'title': 'C Runtime Overhead (2015)',
 'url': 'http://ryanhileman.info/posts/lib43',
 'votes': 182}
{'title': 'Tips for making writing more fun',
 'url': 'https://davnicwil.com/tips-for-making-writing-more-fun/',
 'votes': 162}
{'title': 'Surviving the desert by building a motorcycle from a broken car? '
          '(2017)',
 'url': 'https://historygarage.com/emile-leray-survived-the-desert-by-building-a-motorcycle-from-his-broken-car/',
 'votes': 157}
{'title': 'GnuPG is now financially self-sustaining',
 'url': 'https://lwn.net/Articles/880248/',
 'votes': 140}
{'title': 'The World of Vintage Operating Systems',
 'url': 'https://winworldpc.com/library/operating-systems',
 'votes': 135}
{'title': 'When WikiLeaks bumped into the CIA: Operation Kudo exposed [video]',
 'url': 'https://media.ccc.de/v/rc3-2021-chaoszone-409-when-wikileaks-bu',
 'votes': 128}
{'title': 'When WikiLeaks bumped into the CIA: Operation Kudo exposed [video]',
 'url': 'https://media.ccc.de/v/rc3-2021-chaoszone-409-when-wikileaks-bu',
 'votes': 128}
{'title': 'NASM Assembly Language Tutorials',
 'url': 'https://asmtutor.com/',
 'votes': 127}
{'title': 'Show HN: Changedetection.io detect changes in websites and JSON '
          'feeds',
 'url': 'https://github.com/dgtlmoon/changedetection.io',
 'votes': 123}
{'title': 'The Drenching Richness of Andrei Tarkovsky',
 'url': 'https://www.newyorker.com/magazine/2021/02/15/the-drenching-richness-of-andrei-tarkovsky',
 'votes': 110}
{'title': 'ASML reports fire at its Berlin factory',
 'url': 'https://www.reuters.com/technology/asml-reports-fire-its-berlin-factory-2022-01-03/',
 'votes': 104}
'/n there are 27 articles with more then 100 points'_
