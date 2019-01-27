# sonnet

Files: 
sonnet_dataset.txt - This the text file containing the sonnets.
sonnet_helper.py - Python file that contains helper methods.
sonnet_csv.csv - CSV file containing some useful datapoints that have been used for recommedation.
sonnet_solution_one.py - Python file containing solution to problem statement 1.
sonnet_solution_two.py - Python file containing solution to problem statement 2.


APIs used:
NLTK - Natural Language Toolkit: Used for identifying the stop words which is defined in one of the nltk inbuild corpus.


Problem Statement-1: Tag each sonnet with a keyword:
  
Simply used the word frequency to find whether or not a word occurs frequently.
Marked every stopword as a frequently occuring word.
Created a dictionary with keys as the words in the sonnet and value as the keyword.
On input of the sonnet number, a dictionary output is printed which contains the tagged keywords.
  

Problem Statement-2: Show related sonnets:

Recommedation systems work based on parameters; as I'm not a sonnets guy, I chose the parameter to be length of the sonnet(something basic) and with the help of an online resource (http://charleswolff.tripod.com/ROTS/r3.html) I could obtain some information on how to classify these sonnets. I made labels for each, made a csv file that I used with the help of pandas to get recommendations.

For recommendations I made use of Pearsons Correlation to find the correlation of the given sonnet with every other sonnet, a list of recommendations are generated. Here, there are two types of results:

i) List of relations: where for each sonnet input we get all the recommendation and not recommended sonnets.

ii) Top recommendations: where a list of top 5 recommendations are generated, one giving one those inputs we can display
                             the required sonnet.
