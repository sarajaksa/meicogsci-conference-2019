# Topic Analysis of MeiCogSci Conference Abstracts

This is the data ans analysis for the abstract How Can Computers Help Us Understand Text? Topic Modeling on Example of MeiCogSci Abstracts preseted at MeiCogSci conference in June 2019. I was the only person working on this project, with occasional advice from other people.

This was the peliminary work for my master thesis. In my master thesis I am researching the attributes that make ideas spread. For this, I would need to find a way to track the spread of ideas from post to post. Topic analysis came as one of the possible ways of how to so this. So I decided to analyse another dataset with these tehniques to show the usefulness of it. I picked the MeiCogSci conference, since I assume that people attending this conference are interested in it.

## Abstract

The published abstract can be found in file Abstract.md.

The report of how I came up with these topics can be found in the file Methodology.md. 

## Data

The data that I analized is in folders data and data_2109. The abstracts that I filtered out are in data_duplicate (filtered, because they were duplicate) and data_filtered (abstracts that were not peer-reviewed talks or posters).

In the folder personality is the API response for the individual differences for each abstract. 

## Download Abstracts

Run donwload_meicogsci_abstracts.py script. Script takes two arguments, the folder in which to save the abstracts in (--folder) and an optional argument of year, which indicates the year for which to download the abstracts (--year).

## Preanalysis

These are some of the scripts, that I used to get data for analysis:

* Personality-IBM (using IBM's API in order to get the personality of each abstract author)
* Choosing the number of topics: NumberOfTopics-FullScope-ver1.ipynb, NumberOfTopics-FullScope-ver2.ipynb, NumberOfTopics-NarrowScope.ipynb
* MostFrequentWords (which words are the most popular)
* VizualizingTopicsInText.ipynb (testing the test set and vizualizing topics for test set - the results of test set can be found in file MeiCogSci_TestSet_Results.csv)
* DescriptionOfTopics.ipynb (the description of all topics)
* Similarity of the Articles (what I used to filter them): ArticleSimilarity.ipynb

## Testing different models:

These are the different algoritms, that I also tested:

* Hierarchical Dirichlet Process

The model was also tested on test data. The results are in the file: MeiCogSci_TestSet_Results.csv

## Analysis

This is a list of analysis, that are present here:

* Human Research
* Time analysis
* Interdisciplinarity
* Personality
* Values
* Needs

## Additional files

In file constants.py I collected constants, that are constantlly used. 

In the file helping_functions.py I collected functions, that I frequently used. In the file GetTopicsForEachWord.ipynb I have a script that gets me the most representative topic for each word, which I used on my website: https://sarajaksa.eu/2019/meicogsci-topics/text-modeling/ 

Model can be found in folder models.

The vizualization of model with name of the topics is in vis/Model-Names.html. Original vizualization of the model is in vis/LDA_21.html.

Sildes from my presentation at the conference can be found in the folder presentation.

## Thanks

I would like to thank Toma and Urban for conversation about this work and Enja, Gašper and Tomaž for answering my query and Peter for sending me the data. 

I would also like to thank all the people that listened to my talks and to all the questions that I got. 
