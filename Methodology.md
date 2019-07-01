## Methodology and Results

In the first part, I had downloaded the data. I used the [https://www.univie.ac.at/meicogsci/php/ocs/index.php/meicog/index/schedConfs/archive](https://www.univie.ac.at/meicogsci/php/ocs/index.php/meicog/index/schedConfs/archive) as the starting site. For the links to each conference on the list, I have created the link to all the presentations. On the site of the presentation, I searched for all links, and saved the ones that were presentations. Then on each site, I found the text of the abstract and saved it to a separate file. 

After I had all the presentation, I manually did the filtering. The only presentations that I wanted were second-year talks and first-year posters. I have first removed all the keynotes, workshops and student initiatives presentations. There were 57 presentations like that. After some exploratory analysis, I then also tired to find the duplicate entries. In the early years, each member of the group project could submit their own abstract. So what I did was calculate the cosine difference in the TF-IDF representation of each text. There were 7 groups of texts, that were identical, 6 groups with 1 text and 1 group with three texts. 6 of these groups were group projects in the same year. One was a case of a person, who published the same abstract in two different years. In all of these I kept one version. There were additional cases with abstracts, that were very similar. If I put the threshold distance at 0.05, I would have gotten all of these kinds with only one false positive. The false positive was a case of a person working on the same project for their poster and talk. So I have picked one from each, except for false positive one, where I kept both. All together this removed 20 abstracts. So this left me with 744 abstracts, that I could use. 

After that, I put all the text through preprocessing. All of this was done automatically. I first tried to eliminate the references, by checking the last 7 lines, if they start with the [ + digit + ]. I then tired to eliminate thanks based on the phrases, that were frequent in thanks, but did not exist in the rest of the text. I also eliminated headers for abstract and references. 

The remaining text was converted into lower case and split into words. The punctuation was removed. After that, the most frequent five words were the, of, and, to and in, so I decided to also remove the standard stop words and words shorter than 3 letters. I lemmatized the words. 

After this, I checked the most frequent words by type, to see which ones hold the most explanatory value. I checked the nouns, verbs, adjectives and adverbs, to see which ones hold the meaning of the text. Putting all these categories together, the most frequent five words are: study, research, result, task and cognitive. In the table below, you can see the most frequent 10 words by type. 

| Nouns       | Verbs     | Adjectives | Adverbs    |
| ----------- | --------- | ---------- | ---------- |
| study       | used      | cognitive  | also       |
| research    | based     | different  | well       |
| result      | using     | social     | however    |
| task        | presented | human      | thus       |
| participant | learning  | visual     | even       |
| model       | use       | first      | therefore  |
| system      | show      | new        | still      |
| language    | found     | neural     | often      |
| process     | make      | possible   | yet        |
| effect      | related   | specific   | especially |

Based on the inspection of the most frequent words in each group, I decided to only include nouns and adjectives in the model.


I have created 2-grams and 3-grams in the same way. Except in these cases, I did not have a criteria, that words have to be longer than two letters. But the rest of the criteria had to apply to all the words in the phrase. In this way, I have put some of the word order in the model. 

After I had the list of words, I eliminated the most frequent ones and the least frequent ones. I have removed all the words and phrases that appear in less than 5 abstracts. 

These were my texts for topic modeling. For topic modeling I used the LDA model in the python package gensim. Except when mentioned different, I used default attributes. 

Next I needed to decide, how many topics would my model had. There are different criteria for this. The ones that I used were perplexity, cv coherence and umass coherence. For this, I have created models in increments of 5 with 50 passes with all but 50 texts as data. So I had a model for 5 topic, 10 topic, 15 topics up to 200.  

Based on the perplexity on the test data, any model with less than 175 topics would work. The perplexity on the training data showed a bit more granular picture, were the perplexity was slowly rising. But based on the picture, anything until 75 topic was still low. 

The UMass was a bit different. UMass should be a high as possible. But it had a downward trend. In the test dataset, the UMass was lowering up to 30 topics, and then stayed there. The one on the training set was similar, with an additional peak at 25 topics. 

The CV can only be calculated on the train dataset. This one needs to be higher. There are three peaks or group of peaks, one at 25 topics, the other at 65 topics as the highest peak and the third at around 140 as the highest peak. 

Based on this, I decided to evaluate the topics models with topics between 20 and 30. Based on the coherence measures, the CV indicates that 21 and maybe 26 are good candidates. Based on the UMass, it seems that 22 and 26 are good candidates. So I am going to evaluate these three models in my further work. 

For each word in the model, I have calculated the score based on their importance to the topic and based on how the topic is important to the word. In the following table, I have written down three highest scoring words based on this (only for model with 21 topics, since this one ended up being the best).

Model with 21 topics with words

| Topic | Name                  | Words                               |
| ----- | --------------------- | ----------------------------------- |
| 0     | Music                 | pitch, tone, musical                |
| 1     | Movement              | movement, eye, mu rhythm            |
| 2     | Art                   | aesthetic, verbal, artwork          |
| 3     | Modeling              | model, simulation, strategy         |
| 4     | Socialization         | social, behaviour, psychotherapy    |
| 5     | Decision Making       | decision, decision making, making   | 
| 6     | Disease               | patient, disease, response          |
| 7     | Brain Imaging         | receptor, brain, eeg                |
| 8     | First-person          | experience, emotions, consciousness |
| 9     | Sleep                 | sleep, memory, deprivation          |
| 10    | Visual perception     | target, color, visual               |
| 11    | Cognition             | child, cognitive, student           |
| 12    | Mental states         | sound, meditation, metaphor         |
| 13    | Language              | word, language, text                |
| 14    | Working memory        | spatial, working memory, memory     | 
| 15    | Attention             | face, attention, gaze               |
| 16    | Legal                 | legal, gesture, article             |
| 17    | Games                 | game, player, serious               |
| 18    | TMS                   | tms, simulation, cortex             |
| 19    | Neural networks       | network, problem, neuron            |
| 20    | Reinforcement learning | agent, action, reward               |

More detailed description of topics is in file DescriptionOfTopics.ipynb. Some of the final names changed based on the additional information.

Next, I went over 50 test articles, to see if their topics make sense. I read the article and checked with topics were represented with more than 10%. 

During this process I realized that the first-person group also has a lot of sense-making. Since even before, I could not decide between these two, I decided to rename the first-person into sense-making. I added games to the individual differences. 

| Year | ID   | Expected | Clearly | So-So | Not | Strongest right              |
| ---- | ---- | -------- | ------- | ----- | --- | ---------------------------- |
| 2013 | 461  | 4        | 2       | 1     | 1   | reinforcement learning - NO   |
| 2011 | 245  | 5        | 4       | 0     | 1   | abnormality - YES            |
| 2016 | 899  | 3        | 1       | 1     | 1   | neuroscience - YES           |
| 2010 | 136  | 5        | 2       | 2     | 1   | perception - NO              |
| 2017 | 1020 | 5        | 4       | 1     | 0   | society - NO                 |
| 2015 | 793  | 4        | 2       | 1     | 1   | first person - YES           |
| 2017 | 1060 | 4        | 3       | 0     | 1   | neural network - NO          |
| 2017 | 1064 | 3        | 2       | 0     | 1   | society - YES                |
| 2013 | 459  | 1        | 1       | 0     | 0   | movement - YES               |
| 2012 | 370  | 3        | 2       | 0     | 1   | movement - YES               |
| 2014 | 607  | 3        | 3       | 0     | 0   | sense-making - YES           |
| 2017 | 1052 | 4        | 4       | 0     | 1   | decision making - NO         |
| 2017 | 1014 | 3        | 3       | 0     | 0   | sense-making - YES           | 
| 2015 | 761  | 4        | 1       | 2     | 1   | abnormality - YES            |
| 2017 | 1012 | 6        | 3       | 0     | 3   | categorization - YES         |
| 2016 | 888  | 5        | 2       | 2     | 1   | society - YES                |
| 2013 | 440  | 4        | 1       | 2     | 1   | sense-making - NO            |
| 2012 | 300  | 1        | 1       | 0     | 0   | neuroscience - YES           |
| 2018 | 1103 | 4        | 2       | 2     | 0   | society - YES                |
| 2008 | 6    | 3        | 1       | 2     | 0   | learning - NO                |
| 2016 | 863  | 4        | 2       | 1     | 1   | language - YES               |
| 2017 | 959  | 5        | 3       | 0     | 2   | neuroscience - NO            |
| 2010 | 149  | 5        | 4       | 0     | 1   | neural networks - NO         |
| 2017 | 952  | 2        | 1       | 1     | 0   | TMS - YES                    |
| 2012 | 309  | 5        | 1       | 0     | 4   | movement - NO                |
| 2017 | 1039 | 4        | 1       | 1     | 2   | neuroscience - YES           |
| 2014 | 564  | 3        | 3       | 0     | 0   | reinforcement learning - YES  | 
| 2017 | 971  | 5        | 3       | 2     | 0   | decision making - NO         |
| 2013 | 404  | 4        | 4       | 0     | 0   | attention - NO               |
| 2011 | 246  | 4        | 2       | 2     | 0   | reinforcement learning - NO   |
| 2016 | 890  | 4        | 1       | 0     | 3   | neuroscience - YES           |
| 2013 | 484  | 2        | 1       | 0     | 1   | neuroscience - YES           |
| 2014 | 595  | 4        | 2       | 1     | 0   | games - YES                  |
| 2016 | 905  | 3        | 2       | 0     | 1   | sense-making - YES           |
| 2013 | 441  | 3        | 2       | 0     | 1   | TMS - NO                     |
| 2012 | 302  | 5        | 4       | 0     | 1   | reasoning - YES              |
| 2014 | 617  | 4        | 4       | 0     | 1   | neural networks - NO         |
| 2016 | 847  | 3        | 0       | 2     | 1   | decision making - NO         | 
| 2012 | 362  | 4        | 3       | 1     | 0   | perception - YES             |
| 2014 | 587  | 4        | 2       | 1     | 1   | decision making - NO         |
| 2016 | 809  | 2        | 1       | 0     | 1   | neuroscience - YES           |
| 2015 | 741  | 1        | 1       | 0     | 0   | decision making - YES        |
| 2016 | 849  | 4        | 2       | 1     | 1   | perception - NO              |
| 2012 | 322  | 4        | 2       | 1     | 1   | neuroscience - YES           |
| 2018 | 1122 | 4        | 3       | 0     | 1   | sound - YES                  |
| 2017 | 1031 | 2        | 2       | 0     | 0   | TMS - YES                    |
| 2011 | 2013 | 2        | 2       | 0     | 0   | language - YES               |
| 2017 | 976  | 3        | 2       | 1     | 0   | society - YES                |
| 2015 | 700  | 1        | 1       | 0     | 0   | language - YES               |
| 2016 | 855  | 3        | 3       | 0     | 0   | movement - NO                |

These were then the topics that I used for all the rest of the analysis. 
