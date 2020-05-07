# SEOaudit
This project is intended to scan and analyze the most important pages of a given website. 
The aspects examined are relevant for SEO (Search Engine Optimization) purposes.
The script checks for and prints the Title, H1 tag, and Meta-Description of each web page.
In addition, Google Dev Tools "Lighthouse" tool is used to determine the performance score of a page's loading time.
The results are saved in a xlsx (excel) file.

*NODE.JS must be installed in order for the lighthouse tool to work, you can [download it here](https://nodejs.org/en/download/).

For practice purposes, I used the script to determine the New York Times main pages SEO values. The main pages I chose are the pages 
 accessible from the navigation bar on the homepage. 
 
 Example of results:
 
 ![sample of SEOaudit outcome](https://github.com/AmirZimhony/SEOaudit/blob/master/NYtimes%20example.png)
 
 
 There are many more possibilities for the information we extract on a webpage's attributes. 
 Once we have made a successfull get request, basically we can decide on any html tag info we want to extract from the page. 
 Furthermore, the Lighthouse tool provides us with information regarding a page's Loading performance, accessibility, best practices, additional SEO tests and progressive web app performance. In the json output of the Lighthouse audit there are endless pieces of data,including a more specific de-construction of the "performance" score a page recieves (and is presented in the version of the code in this example).
 
 For any questions, suggestions of improvement or whatever comes to mind, here is my email:
 yesiamamir@gmail.com
 
 
