# Candidate Confidential
### Stephen Li, Sam Cook, Adam Eldefrawy, Sydney Essex
From the makers of College Confidential… we bring you Candidate Confidential, the simple and concise place to view the new candidates' policies and stances on various political topics for the 2020 election.

**What problem does it solve?**
Candidate Confidential solves the ever-growing issue of uninformed or overwhelmed voters. Some people don’t know who to vote for and don’t want to spend time searching the positions politicians take. Others just don’t know what’s fake news and may make misinformed voting decisions. And others just don’t care! With an important election coming in one and a half years, get up to speed with all of the candidates that have announced their running. After meeting with a TA, we decided that because the only two Republican candidates are Trump (whose policies and stances on topics have been made clear in his presidency) and one other minor candidate, we decided to focus solely on all of the democratic candidates because there are so many running (20 so far).

**What similar projects exist?**
There is a company called Emporis that is a provide of building data. They ran something called Emporis Community which was a website where people in the crowd could submit building information. This helps them provide information to their clients which is similar in that we ask the crowd so that we can help provide information to the general public regarding political candidates.

**What type of project is it?**
Human computation algorithm
Social science experiment with the crowd
A tool for crowdsourcing
A business idea that uses crowdsourcing
Other

**What was the main focus of your team’s effort**
Conducting an in depth analysis of data

How does your project work? Describe each of the steps involved in your project. What parts are done by the crowd, and what parts will be done automatically.

**Link to our final video:**
https://vimeo.com/334918988

## The Crowd
**Who are the members of your crowd?**
The members of the crowd for our experiment were both our classmates but also the general public on Mechanical Turk when we made HITs and published them for people to participate. 

**For your final project, did you simulate the crowd or run a real experiment?**
Real crowd
We recruited participants by offering economic incentive on Amazon MTurk. By posting the HITs, they were able to be paid for completing our tasks and that was the primary way we recruited/incentivized workers. 

**How many unique participants did you have?**
200

## Incentives
**What motivation does the crowd have for participating in your project?**
Pay, Altruism

**How do you incentivize the crowd to participate? Please write 1-3 paragraphs giving the specifics of how you incentivize the crowd. If your crowd is simulated, then what would you need to do to incentivize a real crowd?**
As mentioned above, the primary incentive we provided the crowd was an economic incentive. We essentially hired them to provide us with data by completing our HITs. By providing them with pay, this motivated people to participate in our tasks of gathering information on various political candidates. In our case, we thought economic incentive would be the primary reason people would complete our task.

But, another incentive that our project involves is altruistic in nature. The goal of our tasks was to help to inform the general public about various presidential candidates for the 2020 election and thus, there was the additional incentive of helping to inform the general public. Although we don't anticipate this to be a primary form of incentive for the crowd, we do believe that there are individuals and workers who would participate because they wish to help improve awareness regarding the candidates. For those incentivized to participate for these reasons, we believe care about this issue and thus, would be more inclined to participate. 

**Did you perform any analysis comparing different incentives?**
No, but something to consider in the future is to use our quality control model analyzing the scores of quality of work of the crowd and determine if different pay levels yields different scores for workers. For example, if higher pay leads to a higher score for workers in our model. 

## What the crowd gives you
**What does the crowd provide for you?**
The crowd provides valuable data regarding their views on a candidate's positions on various toppics. This data is related to their research, and their opinions regarding where along the spectrum these candidates would lie for these topics. 

**Is this something that could be automated?**
Finding the stances these candidates have on topics could be automated with a scraper that would just search the internet for this information, but the data that the crowd is providing us cannot be. Our data is unique in that it involves the observatios of where people think different candidates lie along the spectrum. This is something that cannot be automated because it requires the subjective views and opinions (informed as well) that people have who participate.

**Did you train a machine learning component from what the crowd gave you?**
No

## Skills
**Do your crowd workers need specialized skills**
No, they just need to be able to research about the candidate and topics they are given and be able to differentiate between what is a reliable source and what is something that is completely fake. 

**What sort of skills do they need?**
Other than the ability to run searches on Google and the ability to read, they don't require any other skills. What they are doing is relatively simple and only requires that they provide their views on where the candidate lies along the spectrum for a given topic.

**Do the skills of individual workers vary widely?**
We don't believe the skills of individual workers varies that widely. The biggest difference from worker to worker would be initial knowledge of the candidates and their stances or how well informed they are regarding the election and the political topics. This would help them better discern their responses and provide potentially more accurate data which may make one worker better than the other. But, these things can all be done by searching online and using intuition and thus, the skills will not vary widely. 

**Did you analyze the skills of the crowd?**
Other than using gold standard questions for quality control, we did not test any other skills of the crowd. In order to complete our task, all the worker has to do is some basic research on google.

## Quality Control
**Is the quality of what the crowd gives you a concern?**
Like all crowdsourcing, the quality of what the crowd gives is a concern. What's the point in gathering data and information on candidates if the information is incorrect or if the quality is extremely low and the crowd doesn't put any effort? Then our efforts would be futile. Nevertheless, we have taken measures to improve the quality of the work the crowd provides or detect if the quality is not high enough. 

**How do you ensure the quality of the crowd provides?**
In general, there are many ways to ensure the quality the crowd provides. The first can be ensuring that the skills and knowledge are there for the workers. If they workers don't have the proper skills (ie speaking a language), then they cannot provide quality work in many cases. This is the same for knowledge regarding a subject like political candidates in our case. Another way to ensure the quality of the crowd is through financial incentives. By providing this financial incentive, it can help to ensure that the workers are more motivated to provide higher quality work as a result of the financial incentive. Something we learned in class is embedding gold standards within the crowdsourcing component. This includes having an answer that can be measured as a standard against to determine the quality of the work. 

**If quality if a concern, then what did you do for quality control? If it is not a concern, then what about the design of your system obviates the need for explicit QC? This answer should be substantial (several paragraphs long).**
The first thing we did to ensure the quality of the crowd is by providing a tiny paragraph of background information about the candidates. This way, at the very least, if the workers do not go and actually do the research, there is some level of understanding of who the candidate is and their position along the political spectrum. Providing them with this baseline level of knowledge is important in improving their knowledge going into their selections.

The second thing we did was the ensure that the workers were motivated to provide quality responses and thus usable data. By providing an adequate financial incentive, we hoped that the workers would conduct the work we asked of them properly. Although we did not test different levels of pay, we did pay workers a fair amount that would ensure that they were being compensated for good work. On top of financial incentive, we also made it so that each workers work is not significant. They are responsible for only a single topic for a candidate which makes it a straightforward and simple task.

Finally, we wrote a program to score each of the workers. For a few of the candidates, it is very easy to tell what value they should have for a specific topic. In the case of our project, we know that Bernie Sanders is very far on the liberal side so we as a team gave him a value for specific topics. These topics that we decided were relatively easy to determine and are serving as our gold standard questions and values that are embedded in the HITs. We can determine the quality of work and whether a worker is not trying at all based off of how far away from the answer we expect their answer is. By incorporating gold standards, we can measure the quality of the work that is being done and accept or deny it accordingly.

These are te primary ways we are trying to ensure the quality of the work, but, it is important to note that in terms of the scale of this class, there were still limits. To are larger degree, quality control will always be a concern with regards to crowdsourcing because it is impossible to ensure the quality of each person's work and their desire to do the work. These were just ways that our team decided to stabilize the quality to the best of our abilities. 

**Did you analyze the quality of what you got back? For instance, did you compare the quality of results against a gold standard? Did you compare different QC strategies?**
We used gold standard questions in order to rate the quality of worker responses to our HIT. The two candidates who are the most well-known, Bernie Sanders and Elizabeth Warren, were used as our "gold standard candidates". We determined correct ranges of scores through our own research and used these ranges to score our workers' responses. For example, our range for Bernie Sanders view on taxation is 8-10, where 10 is the most liberal. If a worker responded within this range, their quality score increases by 1. If a worker responded within 3 of the range, their quality score remains the same. Finally, if a worker was far off from the gold standard established range, their quality score is decremented by 1. Workers are then rated on a qaulity control scale ranging from -10 to 10. Any worker with a score lower than 0 is considered unreliable, while scores between 0 and 5 are considered semi-reliable. Scores over 5 are considered very reliable. Through this means of a quality rating, we are able to determine which workers are generally accurate with their responses and which are not.

**What analysis did you perform on quality?**
We analyzed the results of the gold standard questions to determine how many of our responses were usable. We found that a large majority of the crowd gave accurate responses to our HIT, while only a small percent gave poor answers to the gold standard questions and thus proved to give unreliable results. 

**Do you have a graph analyzing quality? If you have a graph analyzing quality, include the graph here.**

INSERT GRAPH HERE

## Aggregation
**How do you aggregate the results from the crowd?**

To aggregate the results from the crowd, we summed 10 political ratings that the crowd provided for each political candidate. Thus, for each position for each candidate, we had 10 ratings out of 10 from 10 workers, where 10 was the most liberal and 1 is the most conservative. Summing these 10 ratings yielded a rating out of 100 (where 100 is most liberal and 10 is most conservative).

**Did you analyze the aggregated results?**

Yes, then we took an average of all the political ratings for each candidate. That is, we summed the political ratings for all the positions and then dividied it by the number of political positions for each candidate. This is supposed to be an all-included (from the political positions we polled for) rating of the political stance of each candidate. With this info, we created a bar graph for visual representation and found that our findings were consistent with what one might expect.

**What analysis did you perform on the aggregated results? What questions did you investigate? Did you compare aggregated responses against individual responses? What conclusions did you reach?**

On the aggregated results, we compiled a graph that shows clearly where candidates are on the scale of 10-100 for how liberal they are. We found that our findings are consistent with exactly what is expected. For example, the one outlier on the conservative side is the only Republican candidate that we polled for. He is the only candidate that received an overall political position score of under 50. Furthermore, the outlier on the liberal side was Bernie Sanders, who is generally known as an extremely liberal progressive candidate. Thus, we reached the conclusions that the crowd generally perceived the candidates correctly.

**Do you have a graph analyzing the aggregated results? If you have a graph analyzing the aggregated results, include the graph here.**

INSERT GRAPH HERE

**Did you create a user interface for the end users to see the aggregated results? If yes, pleaseinclude a screenshot of the user interface for the end user in your final report. You can include multiple screenshots, if you want.**

No, we did not create a user interface as there is nothing for a user to interact with.

## Scaling Up
**What is the scale of the problem that you are trying to solve?**
The scale of the problem is mainly within the US, but can extend internationally as the US presidential election is a concern for more than just US citizens. That being said, the main focus of our project is to inform US voters about their potential presidential nominees.

**Would your project benefit if you could get contributions from thousands of people?**
Our project would continue to benefit as more and more people contributed. Adding new peoples opinions and ratings of candidates just increases the accuracy as the volume of responses increases.

**If it would benefit from a huge crowd, how would it benefit?**
Our project would become more accurate as the number of contributers increased. With a relatively small crowd, we were able to give an accurate representation of the presidential candidates on 5 key issues previously determined as the most important to the US population by the crowd. With a larger crowd, we would be able to not only gain more accurate results, but also increase the number of issues we analyzed and provide a better picture of the presidential race to people across the country.

**What challenges would scaling to a large crowd introduce?**
If we were faced with scaling to a large crowd, we would most likely have to use a different means of quality control. Although our current quality control algorithm provides a relaitively accurate depiction of the crowd's accuracy, our project could benefit with a more full-proof quality control algorithm that could eliminate any unreliable sources from the crowd.

**Did you perform an analysis about how to scale up your project? For instance, a cost analysis?**
No, we did not perform any analysis on how we would scale up our project. For our project, scaling up would cost us much more money as we pay workers $0.01 for each HIT they complete.

**What analysis did you perform on the scaling up?**

**What questions did you investigate? What conclusions did you reach?**

**Do you have a graph analyzing scaling? If you have a graph analyzing scaling, include the graph here.**

## Project Analysis

**Did your project work? How do you know? Analyze some results, discuss some positive outcomes of your project.**
Our project did work. We know this because we were able to gain accurate ratings on candidates for 5 of the most important issues to the public. Also, through our quality control algorithm, we were able to eliminate void crowd responses from our data and keep the overall ratings accurate and consistent with other internet sources. After researching further into the 20 different candidates, we found that the crowd's responses to the different issues for each candidate were very accurate. With further work, we could create a platform for people to visit to find how their fellow US citizens have rated these different candidates on the important issues in our nation.

**Do you have a graph analyzing your project? If you have a graph analyzing your project, include the graph here.**

INSERT GRAPH HERE

**What were the biggest challenges that you had to deal with?**
The biggest challenge we had to deal with was finding an effective means of quality control. With our method of gold standard ranges, we can find and eliminate the inaccurate responses effectively, however it is somewhat subjective. With our own research as a team, we created these gold standard questions and responses, but one person's idea of a 6/10 could be different from anothers. If we could find an entirely objective means of quality control, that would be beneficial. We tried our best with the data we had and were able to obtain accurate results, but there is always room for improvement when it comes to controlling the quality of your crowd responses. Another challenge we had to deal with was narrowing down the issues we asked about to the 5 most important. We eventually decided to have the crowd choose this for us as well and were able to find 5 issues that the crowd voted overwhelmingly as the most important to the US population.

**Where there major changes between what you originally proposed and your final product?**
No, we were able to complete what we proposed originally.

**If so, what changed between your original plan and your final product?**

**What are some limitations of your product? If yours is an engineering-heavy project, what would you need to overcome in order to scale (cost/incentives/QC…)? If yours was a scientific study, what are some sources of error that may have been introduced by your method.**
One consistent source of error that could occur with our project is its relative subjectivity. The responses to our HIT do not have one correct answer, but this is what makes it more helpful to users in the end. Although two crowd workers could know the same information about a candidate yet still give a different rating on certain issues, this works to our benefit as our data provides an average citizens opinions on candidates rather than a potentially biased news source. These other sources on candidates can be easily found online but can also be tailored to certain audiences and could leave out certain information. Another source of error could arise from our quality control algorithm or from crowd workers misreading the prompt. Our algorithm was able to identify certain responses that were the complete opposite of what was expected. This could be because the worker thought that 1 meant ultra liberal and 10 ultra conservative rather than the other way around. Although this is explained in the HIT introduction, misreading is always a possibility when dealing with large amounts of responses.

**Did your results deviate from what you would expect from previous work or what you learned in the class?**
No, our responses were as accurate as expected, with exceptions as always when dealing with the crowd.

**If your results deviated, why might that be?**

## Technical Challenges
**Did your project require a substantial technical component? Did it require substantial software engineering? Did you need to learn a new language or API?**
No, we used MTurk for our crowdsourcing platform which we had already learned how to use earlier in the class. We also used python for our aggregation and quality control algorithms.

**If project required a substantial technical component, describe the largest technical challenge you faced.**

**How did you overcome this challenge? What new tools or skills were required? Feel free to nerd out a bit, to help us understand the amount of work that was required.**

**Do you have any screen shots or flow diagrams to illustrate the technical component you described? If so, include the graph here.**
