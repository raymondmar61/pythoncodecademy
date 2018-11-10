#FetchMaker: A Study In Data Analysis
import pandas as pd
import numpy as np

df = pd.read_csv("dogdata.csv")
#rottweilerrows = df[(df.breed=="rottweiler")]
#print(rottweilerrows["tail_length"])
#RM:  print the tail_length column only for rottweiler rows
rottweilertailrows = df[(df.breed=="rottweiler")]["tail_length"]
#print(rottweilertailrows)
rottweilertailrowslist = [eachrottweilertailrows for eachrottweilertailrows in rottweilertailrows]
#print(rottweilertailrowslist) #print [3.13, 3.32, 1.16, 2.23, 8.86, 8.44, 3.54, 8.44, 2.8, 5.32, 4.53, 0.95, 3.44, 4.58, 4.42, 6.4, 7.5, 1.0, 4.75, 3.99, 2.1, 5.47, 3.51, 3.24, 6.58, 2.91, 4.06, 2.18, 4.75, 1.4, 2.52, 2.52, 1.43, 2.36, 2.06, 5.99, 4.97, 8.17, 1.5, 6.47, 3.84, 5.65, 7.66, 4.0, 3.67, 3.85, 3.34, 3.76, 3.18, 2.2, 5.99, 7.47, 5.82, 7.79, 3.55, 2.53, 3.57, 5.36, 3.94, 1.8, 5.14, 4.42, 2.02, 6.08, 0.82, 5.67, 6.45, 4.22, 1.36, 3.25, 4.4, 5.16, 5.33, 9.32, 3.06, 8.41, 5.27, 4.54, 5.24, 4.32, 4.74, 1.98, 0.7, 6.59, 1.95, 2.04, 2.65, 1.86, 3.6, 6.77, 6.04, 9.01, 2.37, 4.32, 2.79, 3.28, 5.5, 2.95, 4.64, 3.39]  RM:  yes all rottweiler and its tail length
rottweilertailrowslist = np.array(rottweilertailrowslist)
print(np.mean(rottweilertailrowslist)) #print 4.2360999999999995
print(np.std(rottweilertailrowslist)) #print 2.0647536874891395

#Over the years, we have seen that we expect 8% of dogs in the FetchMaker system to be rescues. We want to know if whippets are significantly more or less likely to be a rescue.  Store the is_rescue values for "whippet"s in a variable called whippet_rescue.
whippet_rescue = df[(df.breed=="whippet") & (df.is_rescue == 1)]
#Get the number of rescue whippet
print(len(whippet_rescue)) #print 6
num_whippet_rescues = len(whippet_rescue)
#Get the number of samples in the whippet
whippetcount = df[(df.breed=="whippet")]["breed"]
num_whippet = len(whippetcount)
print(num_whippet)
#Use a binomial test to test the number of whippet rescues, num_whippet_rescues, against our expected percentage, 8%.
from scipy.stats import binom_test
pval = binom_test(num_whippet_rescues, n=num_whippet, p=0.08)
print(pval) #print 0.5811780106238098
#Generally, if we receive a p-value of less than 0.05, we can reject the null hypothesis and state that there is a significant difference.  RM:  In contrast, if we receive a p-value of more than 0.05, we accept the null hypothesis and state that there is no significant difference.

#Three of our most popular mid-sized dog breeds are whippets, terriers, and pitbulls. Is there a significant difference in the average weights of these three dog breeds? Perform a comparative numerical test to determine if there is a significant difference.  Use ANOVA for this scenario.
whippetweight = df[(df.breed=="whippet")]["weight"]
#print(whippetweight)
whippetweight = [x for x in whippetweight]
#print(whippetweight)
whippetweight = np.array(whippetweight)
#print(whippetweight)
terrierweight = df[(df.breed=="terrier")]["weight"]
terrierweight = [x for x in terrierweight]
terrierweight = np.array(terrierweight)
pitbullweight = df[(df.breed=="pitbull")]["weight"]
pitbullweight = [x for x in pitbullweight]
pitbullweight = np.array(pitbullweight)
print(np.mean(whippetweight)) #print 40.82
print(np.mean(terrierweight)) #print 30.92
print(np.mean(pitbullweight)) #print 44.16
from scipy.stats import f_oneway
fstat, pval = f_oneway(whippetweight,terrierweight,pitbullweight)
print(pval) #print 3.276415588274815e-17
#Now, perform another test to determine which of the pairs of these dog breeds differ from each other.  Use Tukey’s Range Test for this scenario.
from statsmodels.stats.multicomp import pairwise_tukeyhsd
v = np.concatenate([whippetweight, terrierweight, pitbullweight])
labels = ['Whippet'] * len(whippetweight) + ['Terrier'] * len(terrierweight) + ['Pitbull'] * len(pitbullweight)
tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print(tukey_results)
'''
Multiple Comparison of Means - Tukey HSD,FWER=0.05
==============================================
 group1  group2 meandiff  lower  upper  reject
----------------------------------------------
Pitbull Terrier  -13.24  -16.728 -9.752  True 
Pitbull Whippet  -3.34    -6.828 0.148  False 
Terrier Whippet   9.9     6.412  13.388  True 
----------------------------------------------
'''

#We want to see if "poodle"s and "shihtzu"s have significantly different color breakdowns.  Get the poodle colors and store it in a variable called poodle_colors.  Get the shih tzu colors and store it in a variable called shihtzu_colors.
#poodle_colors = df[(df.breed=="poodle")]["color"]
poodle_colors = df[(df.breed=="poodle")]
#shihtzu_colors = df[(df.breed=="shihtzu")]["color"]
shihtzu_colors = df[(df.breed=="shihtzu")]
# poodle_colors = [x for x in poodle_colors]
# poodle_colors = np.array(poodle_colors)
# shihtzu_colors = [x for x in shihtzu_colors]
# shihtzu_colors = np.array(shihtzu_colors)
#print(poodle_colors)
poodle_colorscount = poodle_colors.groupby("color").breed.count().reset_index()
shihtzu_colorscount = shihtzu_colors.groupby("color").breed.count().reset_index()
#print(poodle_colorscount)
'''
   color  breed
0  black     17
1  brown     13
2   gold      8
3   grey     52
4  white     10
'''
#print(shihtzu_colorscount)
'''
   color  breed
0  black     10
1  brown     36
2   gold      6
3   grey     41
4  white      7
'''
#Use this function to build a Chi Square contingency table, called color_table, with the following structure:
'''
Poodle	Shih Tzu
Black	x	x
Brown	x	x
Gold	x	x
Grey	x	x
White	x	x
'''
#Fill in the "x" entries with the number of each poodle or shih tzu with the specified color.
color_table = [[17, 10], [13, 36], [8, 6], [52, 41], [10, 7]]
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(color_table)
print(pval) #print 0.005302408293244593

#bonus
#source help:  https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list
frequencypoodle_colors = df[(df.breed=="poodle")]["color"]
frequencypoodle_colors = [x for x in frequencypoodle_colors]
#print(frequencypoodle_colors)
from itertools import groupby
poodlecolors = [len(list(group)) for key, group in groupby(frequencypoodle_colors)] #list must be sorted
print(poodlecolors) #print [17, 13, 8, 52, 10]

frequencyshihtzu_colors = df[(df.breed=="shihtzu")]["color"]
frequencyshihtzu_colors = [x for x in frequencyshihtzu_colors]
#print(frequencyshihtzu_colors)
from itertools import groupby
shihtzucolors = [len(list(group)) for key, group in groupby(frequencyshihtzu_colors)] #list must be sorted
print(shihtzucolors) #print [10, 36, 6, 41, 7]

colortable = []
for n in range(0,len(poodlecolors)):
	colortable.append([poodlecolors[n],shihtzucolors[n]])
print(colortable) #print [[17, 10], [13, 36], [8, 6], [52, 41], [10, 7]]
from scipy.stats import chi2_contingency
chi2, pval, dof, expected = chi2_contingency(colortable)
print(pval) #print 0.005302408293244593

