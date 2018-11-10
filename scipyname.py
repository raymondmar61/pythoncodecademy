#https://www.codecademy.com/paths/data-science/tracks/scipy

#Statistical Concepts
import numpy as np

#We will cover the fundamental concepts that will help us create tests to measure our confidence in our statistical results:  Sample means and population means, The Central Limit Theorem, Why we use hypothesis tests, What errors we can come across and how to classify them.
#A sample is a subset of the entire population. The mean of each sample is the sample mean and it is an estimate of the population mean.  e.g.  the sample means (32 ft., 35 ft., and 31 ft.) were all close to the population mean (32.8 ft.), but were all slightly different from the population mean and from each other.
#From a sample mean, we can then extrapolate the mean of the population as a whole. There are many reasons we might use sampling, such as:  We don't have data for the whole population; We have the whole population data, but it is so large that it is infeasible to analyze; We can provide meaningful answers to questions faster with sampling.
#For a population, the mean is a constant value no matter how many times it's recalculated. But with a set of samples, the mean will depend on exactly what samples we happened to choose. From a sample mean, we can then extrapolate the mean of the population as a whole.
#It is a natural consequence a set of samples has less data than the population to which it belongs. If our sample selection is poor then we will have a sample mean seriously skewed from our population mean.
#There is one surefire way to mitigate the risk of having a skewed sample mean — take a larger set of samples. The sample mean of a larger sample set will more closely approximate the population mean. This phenomenon, known as the Central Limit Theorem, states that if we have a large enough sample size, all of our sample means will be sufficiently close to the population mean.
population = np.random.normal(loc=65, scale=100, size=3000) #create a random population
population_mean = np.mean(population) #calculate random population mean
#create samples from random population
extra_small_sample = population[:10]
small_sample = population[:50]
medium_sample = population[:100]
large_sample = population[:500]
extra_large_sample = population[:1000]
#calculate samples mean
extra_small_sample_mean = np.mean(extra_small_sample)
small_sample_mean = np.mean(small_sample)
medium_sample_mean = np.mean(medium_sample)
large_sample_mean = np.mean(large_sample)
extra_large_sample_mean = np.mean(extra_large_sample)
print(extra_small_sample) #print [  68.01881414 -179.91123062  -12.84576032  107.93761825   46.12399578  124.44094334  152.62298701  -47.08522394  -37.24355388  280.66762011]
print(extra_small_sample_mean) #print 50.27262098781722
#print samples mean
print("Extra Small Sample Mean: {}".format(extra_small_sample_mean)) #print 50.27262098781722
print("Small Sample Mean: {}".format(small_sample_mean)) #print 59.248699012964714
print("Medium Sample Mean: {}".format(medium_sample_mean)) #print 55.96442610937122
print("Large Sample Mean: {}".format(large_sample_mean)) #print 60.99166463830473
print("Extra Large Sample Mean: {}".format(extra_large_sample_mean)) #print 62.30140735601075
print("Population Mean: {}".format(population_mean)) #print 64.21159540498508  RM:  compare the population mean with the sample means.
#A null hypothesis is a statement that the observed difference is the result of chance; i.e., The null hypothesis states that any difference observed within sample means is coincidental.  Hypothesis testing is a mathematical way of determining whether we can be confident that the null hypothesis is false. Different situations will require different types of hypothesis testing.
#There are two types of error in statistical hypothesis testing. The first kind of error, known as a Type I error, is finding a correlation between things that are not related. This error is sometimes called a "false positive" and occurs when the null hypothesis is rejected even though it is true.  The second kind of error, a Type II error, is failing to find a correlation between things that are actually related. This error is referred to as a "false negative" and occurs when the null hypothesis is accepted even though it is false.
def intersect(list1, list2):
  return [sample for sample in list1 if sample in list2]
# the true positives and negatives:
actual_positive = [2, 5, 6, 7, 8, 10, 18, 21, 24, 25, 29, 30, 32, 33, 38, 39, 42, 44, 45, 47]
actual_negative = [1, 3, 4, 9, 11, 12, 13, 14, 15, 16, 17, 19, 20, 22, 23, 26, 27, 28, 31, 34, 35, 36, 37, 40, 41, 43, 46, 48, 49]
# the positives and negatives we determine by running the experiment:
experimental_positive = [2, 4, 5, 7, 8, 9, 10, 11, 13, 15, 16, 17, 18, 19, 20, 21, 22, 24, 26, 27, 28, 32, 35, 36, 38, 39, 40, 45, 46, 49]
experimental_negative = [1, 3, 6, 12, 14, 23, 25, 29, 30, 31, 33, 34, 37, 41, 42, 43, 44, 47, 48]
#define type_i_errors false positive and type_ii_errors here false negative
type_i_errors = intersect(experimental_positive, actual_negative)
print(type_i_errors) #print [4, 9, 11, 13, 15, 16, 17, 19, 20, 22, 26, 27, 28, 35, 36, 40, 46, 49]
type_ii_errors = intersect(experimental_negative, actual_positive)
print(type_ii_errors) #print [6, 25, 29, 30, 33, 42, 44, 47]
#A hypothesis test provides a numerical answer, called a p-value, that helps us decide how confident we can be in the result. A p-value is the probability that the null hypothesis is true.  A p-value of 0.05 would mean that there is a 5% chance that the null hypothesis is true. This generally means there is a 5% chance that there is no difference between the two population means.  A higher p-value is more likely to give a false positive so if we want to be very sure that the result is not due to just chance, we will select a very small p-value.  Generally, we want a p-value of less than 0.05, meaning that there is a less than 5% chance that our results are due to random chance.

#Statistical Concepts Quiz
'''
Which of the following describes a Type II error?  A survey on preferred ice cream flavors not establishing a clear favorite when the majority of people prefer chocolate.
What is a statistical hypothesis test?  A way of quantifying the truth of a statement.
Suppose we were exploring the relationship between local honey and allergies. Which of these would be a statement of the null hypothesis?  Local honey has no effect on allergies, any relationship between consuming local honey and allergic outbreaks is due to chance.  The null hypothesis states that any difference observed within sample means is coincidental.
Which of the following hypothesis tests would be used to compare two sets of numerical data?  2 Sample T-Test.
Which of these describes a sample mean?  The mean of a subset of our population which is hopefully, but not necessarily, representative of the overall average.
What is a p-value?  In a hypothesis test, a p-value is the probability that the null hypothesis is true.
Which of these is an accurate statement of the Central Limit Theorem?  For a large enough sample size, our sample mean will be sufficiently close to the population mean.
'''

#Hypothesis Testing.
from scipy.stats import ttest_1samp, ttest_ind

#When we are trying to compare datasets, we often need a way to be confident knowing if datasets are significantly different from each other.  Some situations involve correlating numerical data.
#SciPy has built-in functions that perform all of these tests for us, normally using just one line of code.
#For numerical data, we will cover: One Sample T-Tests, Two Sample T-Tests, ANOVA, Tukey Tests
#For categorical data, we will cover: Binomial Tests, Chi Square

#A univariate T-test compares a sample mean to a hypothetical population mean. It answers the question "What is the probability that the sample came from a distribution with the desired mean?"  We want to first create a null hypothesis, which is a prediction that there is no significant difference. The null hypothesis that this test examines can be phrased as such: "The set of samples belongs to a population with the target mean".  The result of the 1 Sample T Test is a p-value, which will tell us whether or not we can reject this null hypothesis. Generally, if we receive a p-value of less than 0.05, we can reject the null hypothesis and state that there is a significant difference.  RM:  In contrast, if we receive a p-value of more than 0.05, we accept the null hypothesis and state that there is no significant difference.
#SciPy has a function called ttest_1samp, which performs a 1 Sample T-Test.  ttest_1samp requires two inputs, a distribution of values and an expected mean:  tstat, pval = ttest_1samp(example_distribution, expected_mean) print (pval).  It also returns two outputs: the t-statistic (which we won't cover in this course), and the p-value — telling us how confident we can be that the sample of values came from a distribution with the mean specified.
ages = [32, 34, 29, 29, 22, 39, 38, 37, 38, 36, 30, 26, 22, 22]
ages = np.array(ages)
ages_mean = np.mean(ages)
print(ages_mean) #print 31.0
#Use ttest_1samp with ages to see what p-value the experiment returns for this distribution, where we expect the mean to be 30.  We don't use tstat the first output, the t-statistic.
tstat, pval = ttest_1samp(ages, 30)
print(pval) #print 0.5605155888171379
tstat, pval = ttest_1samp(ages, 31)
print(pval) #print 1
#P-values give us an idea of how confident we can be in a result. Just because we don’t have enough data to detect a difference doesn’t mean that there isn’t one. Generally, the more samples we have, the smaller a difference we’ll be able to detect.  For instance, If we get a pval p-value < 0.05, we can conclude that it is unlikely that our sample has a true mean of 30. Thus, the hypothesis test has correctly rejected the null hypothesis, and we call that a correct result.  Let's explore some distributions with different means and how our p-values from the 1 Sample T-Tests change.
#Suppose that last week, the average amount of time spent per visitor to a website was 25 minutes. This week, the average amount of time spent per visitor to a website was 28 minutes. Did the average time spent per visitor change? Or is this part of natural fluctuations?
#One way of testing whether this difference is significant is by using a 2 Sample T-Test. A 2 Sample T-Test compares two sets of data, which are both approximately normally distributed.  The null hypothesis, in this case, is that the two distributions have the same mean.
week1 = [23.90506824, 26.67631982, 27.27433886, 24.25757125, 32.40423483, 39.56919357, 23.07010059, 29.82068109, 27.59433809, 28.05639569, 27.06757262, 30.41192979, 25.71358554, 24.94294823, 28.23123807, 24.95337555, 18.51231639, 27.46234762, 28.38016611, 13.91205901, 29.02615866, 26.90746774, 22.8677726,  24.8938289,  25.96947935, 26.86869621, 20.72676456, 27.35988314, 20.68408581, 21.19846143, 16.25800931, 23.92517681, 24.47923229, 29.47050863, 27.28425372, 26.93339272, 28.61026924, 18.88377042, 33.65468651, 25.69470077, 20.98291356, 22.69700387, 28.60278855, 21.36000443, 30.77685156, 20.83415999, 23.79367158, 19.7556718,  29.54421084, 20.1433138]
week2 = [18.63431907, 31.28788036, 34.96797943, 21.81678117, 28.21619974, 39.39313736, 35.52223207, 27.54222109, 33.64395433, 25.31673581, 28.81392191, 30.7358016, 26.37241881, 26.0945555,  26.34073477, 19.42196017, 32.58797652, 24.84001926, 28.93348335, 20.43667584, 22.72495967, 32.31728012, 35.384306, 29.66709637, 24.53512973, 30.91406007, 19.56117513, 24.90816833, 30.13163726, 31.47466199, 27.77683598, 16.51307462, 35.0770162, 31.74818107, 36.36053496, 27.70500593, 29.49869936, 27.65575346, 37.18504075, 25.16055104, 29.26553553, 38.22163057, 28.92102091, 24.8215439, 38.30155495, 34.76020645, 22.26869162, 28.82593733, 32.00975127, 36.46437665]
#We can use SciPy's ttest_ind function to perform a 2 Sample T-Test. It takes the two distributions as inputs and returns the t-statistic (which we don't use), and a p-value.
week1 = np.array(week1)
week2 = np.array(week2)
week1_mean = np.mean(week1)
week2_mean = np.mean(week2)
print(week1_mean) #print 25.4480593952
print(week2_mean) #print 29.0215681076
week1_std  = np.std(week1) #standard deviation
week2_std  = np.std(week2) #standard deviation
print(week1_std) #print 4.531693386680561
print(week2_std) #print 5.497966708987187
#Run a 2 Sample T-Test using the SciPy function ttest_ind.  Save the p-value in a variable called pval and print it out.
tstatstic, pval = ttest_ind(week1, week2)
print(pval) #print 0.000676767690454633
#We know that the p-value is the probability that we incorrectly reject the null hypothesis on each t-test. The more t-tests we perform, the more likely that we are to get a false positive, a Type I error.  For a p-value of 0.05, if the null hypothesis is true then the probability of obtaining a significant result is 1 – 0.05 = 0.95. When we run another t-test, the probability of still getting a correct result is 0.95 * 0.95, or 0.9025. That means our probability of making an error is now close to 10%! This error probability only gets bigger with the more t-tests we do.
alist = [73.57195018, 38.36736256, 49.36398786, 61.9617142, 38.73959044, 55.94532269, 36.65062484, 60.67437231, 63.07900236, 87.32085001, 50.34422982, 57.1090334, 78.67520953, 61.03927418, 82.28774307, 53.58957582, 72.92461536, 74.5603031, 55.02980576, 41.25844438, 53.79588118, 64.79609893, 70.6964892, 66.74072317, 75.0132205, 95.1255286, 49.455128, 66.03612649, 53.02736305, 73.36372418, 40.25571098, 71.04422625, 50.5013845, 38.22366664, 42.75767497, 52.50694334, 38.604658, 59.67850535, 44.19604564, 46.92727224, 55.24050064, 64.52773077, 34.09865429, 42.23778758, 52.86937388, 90.10958086, 59.77157363, 65.57718324, 67.40180559, 56.73021714, 63.26785746, 45.37055306, 80.38995288, 87.65807685, 51.45634914, 65.99748438, 72.47729986, 64.30071533, 19.73984606, 46.23986878, 52.34828788, 61.11952527, 56.20838268, 39.34468135, 57.93250947, 53.37617284, 48.81742261, 80.03593773, 42.25474002, 44.4620247, 63.2401429, 53.75811252, 41.12354869, 70.37251822, 58.0428706, 53.80533131, 33.5540081, 50.05772819, 59.01472301, 63.18681147, 56.36447661, 79.54804111, 57.58182513, 41.80650266, 63.29608989, 69.20391058, 79.07999732, 68.87071256, 54.61550389, 41.62384273, 58.05435004, 57.19652908, 69.06753866, 76.73936006, 61.71461742, 90.44575864, 44.97285945, 14.93461323, 60.22982158, 37.03612975, 38.57973403, 56.3595887, 95.82780236, 82.89304549, 48.08376399, 41.40360494, 39.62295003, 68.15395305, 62.5134759, 48.39594647, 43.4393662, 53.8693371, 45.40197091, 42.65484356, 77.56769986, 42.21598943, 80.22825438, 52.2077973, 41.85889516, 83.40105978, 63.19638331, 61.35383468, 80.02929924, 48.89037458, 53.97640552, 56.44664214, 50.13546236, 41.93267706, 62.23540804, 60.02470794, 71.94323655, 59.379194, 42.88128137, 79.18722897, 79.31010058, 48.44544746, 51.91236908, 41.13612282, 65.07530571, 49.21085783, 82.5097768, 60.94264609, 56.83480824, 64.73765846, 69.44225076, 47.86210011, 72.52226994, 68.98808623, 58.23601966, 63.84862398]
blist = [95.51107316, 54.35829107, 40.89339787, 96.22353646, 64.81786939, 100.90155489, 78.54371076, 59.59291719, 79.48038581, 54.66464299, 88.84487501, 40.47846496, 58.27460403, 69.65150113, 63.21398533, 65.76638702, 72.46903172, 45.64426381, 48.23050528, 62.69144945, 34.56458104, 63.62735445, 84.85317912, 56.85383866, 58.40653944, 76.59643535, 69.62906865, 53.5649532, 90.80202537, 44.34749437, 82.75294036, 54.54636759, 59.28521879, 98.0624434, 35.48488824, 63.59656234, 56.29808521, 74.86351436, 75.28815749, 49.4767936, 69.11564253, 58.05069424, 62.00459751, 80.07716843, 66.64741314, 72.13568466, 78.67823188, 61.99336972, 76.61204807, 54.85681764, 56.21160097, 56.00129702, 67.63557996, 53.00881798, 80.55109674, 65.74169472, 54.63449953, 85.95156336, 66.65507739, 61.5340027, 68.90062598, 68.06498338, 60.96360522, 15.24926295, 66.66054068, 53.68125976, 56.74759425, 69.33342288, 61.59578214, 71.00365297, 67.31074216, 62.87895144, 68.35549125, 72.20999775, 39.00453971, 51.13076193, 63.05896081, 50.83457587, 108.84737794, 53.73542747, 62.15577427, 56.30614198, 41.63092894, 55.45243144, 51.16821352, 50.74359272, 71.89978089, 51.56051365, 69.53539597, 60.26211341, 57.44339045, 93.93447473, 68.30820523, 56.61341491, 56.10959985, 75.62629462, 65.44541815, 68.18516356, 65.50772246, 76.31090438, 61.80989525, 88.8933164, 71.08091152, 82.17523782, 78.60739662, 54.3602904, 75.08530859, 56.54428911, 97.10558503, 84.45764995, 87.90484503, 80.3778012, 53.98146126, 53.37233661, 51.79312409, 79.49538024, 81.87824195, 72.86410169, 69.07213372, 87.6403637, 71.60326174, 81.25535168, 42.73029202, 79.4130614, 75.40287281, 73.63099667, 64.15710739, 60.89237825, 58.45719716, 69.63467031, 50.83088441, 63.82982648, 66.37162001, 95.68584767, 59.76675547, 77.181057, 62.47386631, 48.22514518, 58.15663425, 61.84176007, 62.2596448, 76.82598328, 67.50075764, 38.4958405, 58.66025288, 58.97670339, 42.63240541, 54.82778663, 76.66808086, 82.03854026]
clist = [62.80215823, 54.62836519, 49.87267902, 71.37979508, 85.12967256, 49.81457321, 75.35136467, 54.45595669, 86.7241256, 75.56591744, 63.03183392, 57.3843091, 39.23348399, 82.69868909, 55.96390617, 61.76459869, 62.1037224, 66.92666631, 49.93339614, 51.13778227, 31.67316587, 38.49802083, 49.36472683, 69.04306874, 45.20762281, 73.5836671, 100.61092317, 30.92480424, 37.15912948, 53.73782208, 69.36703357, 60.15384459, 43.20003949, 51.12609883, 64.77507512, 63.28721074, 62.754003, 71.7590419, 73.08977513, 75.48485174, 47.8968874, 62.25258739, 66.33673312, 43.71093919, 80.65634624, 72.25758668, 100.91480345, 32.02761357, 58.31892089, 71.4399215, 45.07120452, 69.71137689, 85.37226652, 55.67710588, 70.25367706, 55.81488767, 61.21107415, 55.42183671, 66.80712926, 36.99284828, 42.37050081, 79.61120896, 58.88769703, 79.59158327, 59.16570772, 70.02097967, 85.29993197, 32.41236279, 52.6081084, 68.17342096, 65.32976073, 60.00672926, 26.30035248, 87.44943179, 55.35068819, 60.28778429, 33.03668105, 80.18693884, 77.27496626, 76.7616852, 100.94978198, 59.46503936, 78.07629437, 51.6102307, 86.95385235, 85.41984014, 54.83564532, 58.06315164, 66.17243082, 62.27966342, 83.35735441, 44.7213871, 42.8362959, 71.72428838, 68.4553881, 55.93152855, 52.33224863, 65.53344277, 48.19362864, 64.92300871, 56.23992888, 78.11260866, 55.80999334, 82.06126322, 67.03112813, 51.22917649, 51.6408127, 63.48194033, 71.77803695, 71.3696262, 45.12124272, 82.24703749, 70.91202908, 62.51210475, 71.71280187, 66.37758047, 49.28266126, 41.29074798, 61.81010589, 39.62654933, 73.54046019, 71.08493364, 61.88315174, 57.41521882, 69.83162524, 65.90217343, 77.11136925, 86.72149744, 81.81406049, 65.85430935, 94.96433541, 69.97078382, 73.34687737, 75.05530607, 57.51618582, 62.3665881, 58.80615169, 63.38469779, 35.87580831, 46.22850701, 56.05164877, 55.33599773, 45.84709985, 51.93706339, 70.16258619, 65.97686424, 50.51337502, 46.76635411, 70.39019472, 42.0636888]
alist = np.array(alist)
blist = np.array(blist)
clist = np.array(clist)
alist_mean = np.mean(alist)
blist_mean = np.mean(blist)
clist_mean = np.mean(clist)
alist_std = np.std(alist)
blist_std = np.std(blist)
clist_std = np.std(clist)
#Perform a 2 Sample T-test between each pair of location data.
tstatstic, a_b_pval = ttest_ind(alist, blist)
tstatstic, a_c_pval = ttest_ind(alist, clist)
tstatstic, b_c_pval = ttest_ind(blist, clist)
#Store the probability of error in a variable called error_prob. Print it out to the console.
#For one t-test, the probability of making an error is 1-0.95. For two t-tests, it is 1-0.95**2. what would it be for three t-tests?
error_prob = 1-(.95**3)
print(error_prob) #print 0.142625
#When comparing more than two numerical datasets, the best way to preserve a Type I error probability of 0.05 is to use ANOVA. ANOVA (Analysis of Variance) tests the null hypothesis that all of the datasets have the same mean. If we reject the null hypothesis with ANOVA, we're saying that at least one of the sets has a different mean; however, it does not tell us which datasets are different.
#We can use the SciPy function f_oneway to perform ANOVA on multiple datasets. It takes in each dataset as a different input and returns the t-statistic and the p-value.  from scipy.stats import f_oneway; fstat, pval = f_oneway(scores_mathematicians, scores_writers, scores_psychologists).
#If we reject this null hypothesis (if we get a p-value less than 0.05), we can say that we are reasonably confident that a pair of datasets is significantly different.  After using only ANOVA, we can't make any conclusions on which two populations have a significant difference.
from scipy.stats import f_oneway
fstat, pval = f_oneway(alist, blist, clist)
print(pval) #print 0.00015341166007885106
'''
Assumptions of Numerical Hypothesis Tests
1. The samples should each be normally distributed...ish.  If your dataset is definitively not normal, the numerical hypothesis tests won't work as intended.
2. The population standard deviations of the groups should be equal.  For ANOVA and 2 Sample T-Tests, using datasets with standard deviations that are significantly different from each other will often obscure the differences in group means.  To check for similarity between the standard deviations, it is normally sufficient to divide the two standard deviations and see if the ratio is "close enough" to 1. "Close enough" may differ in different contexts but generally staying within 10% should suffice.
3. The samples must be independent
'''
#Let's say that we have performed ANOVA to compare three sets of data from the three VeryAnts stores. We received the result that there is some significant difference between datasets.  Now, we have to find out which datasets are different.
#We can perform a Tukey's Range Test to determine the difference between datasets.  If we feed in three datasets, such as the sales at the VeryAnts store locations A, B, and C, Tukey's Test can tell us which pairs of locations are distinguishable from each other.
#The function to perform Tukey's Range Test is pairwise_tukeyhsd, which is found in statsmodel, not scipy.  from statsmodels.stats.multicomp import pairwise_tukeyhsd
#We have to provide the function with one list of all of the data and a list of labels that tell the function which elements of the list are from which set. We also provide the significance level we want, which is usually 0.05.
#For example, if we were looking to compare mean scores of movies that are dramas, comedies, or documentaries, we would make a call to pairwise_tukeyhsd like this:
'''
movie_scores = np.concatenate([drama_scores, comedy_scores, documentary_scores])
labels = ['drama'] * len(drama_scores) + ['comedy'] * len(comedy_scores) + ['documentary'] * len(documentary_scores)
tukey_results = pairwise_tukeyhsd(movie_scores, labels, 0.05)
'''
#It will return a table of information, telling you whether or not to reject the null hypothesis for each pair of datasets.
# Using our data from ANOVA, we create v and l
from statsmodels.stats.multicomp import pairwise_tukeyhsd
v = np.concatenate([alist, blist, clist])
labels = ['alist'] * len(alist) + ['blist'] * len(blist) + ['clist'] * len(clist)
tukey_results = pairwise_tukeyhsd(v, labels, 0.05)
print(tukey_results)
'''
Multiple Comparison of Means - Tukey HSD,FWER=0.05
=============================================
group1 group2 meandiff  lower   upper  reject
---------------------------------------------
alist  blist   7.2767   3.2266 11.3267  True 
alist  clist   4.0115  -0.0385  8.0616 False 
blist  clist  -3.2651  -7.3152  0.7849 False 
---------------------------------------------
'''
#We analyze the percentage of customers who make a purchase after visiting a website. We have a set of 1000 customers from this month, 58 of whom made a purchase. Over the past year, the number of visitors per every 1000 who make a purchase hovers consistently at around 72. Thus, our marketing department has set our target number of purchases per 1000 visits to be 72. We would like to know if this month's number, 58, is a significant difference from that target or a result of natural fluctuations.
#How do we begin comparing this, if there's no mean or standard deviation that we can use? The data is divided into two discrete categories, "made a purchase" and "did not make a purchase".
#If we have a dataset where the entries are not numbers, but categories instead, we have to use different methods.  To analyze a dataset like this, with two different possibilities for entries, we can use a Binomial Test. A Binomial Test compares a categorical dataset to some expectation.
#Examples include:  Comparing the actual percent of emails that were opened to the quarterly goals; Comparing the actual percentage of respondents who gave a certain survey response to the expected survey response; Comparing the actual number of heads from 1000 coin flips of a weighted coin to the expected number of heads.
#The null hypothesis, in this case, would be that there is no difference between the observed behavior and the expected behavior. If we get a p-value of less than 0.05, we can reject that hypothesis and determine that there is a difference between the observation and expectation.  
#SciPy has a function called binom_test, which performs a Binomial Test for you.  from scipy.stats import binom_test
#binom_test requires three inputs, the number of observed successes, the number of total trials, and an expected probability of success.
#For example, with 1000 coin flips, we expect a "success rate" (the rate of getting heads), to be 0.5, and the number of trials to be 1000. Let's imagine we get 525 heads. Is the coin weighted?  This function call would look like:  pval = binom_test(525, n=1000, p=0.5).  It returns a p-value, telling us how confident we can be that the sample of values was likely to occur with the specified probability. If we get a p-value less than 0.05, we can reject the null hypothesis and say that it is likely the coin is actually weighted, and that the probability of getting heads is statistically different than 0.5.
from scipy.stats import binom_test
pval = binom_test(510, n=10000, p=0.06)
print(pval) #print 0.00011592032724546606.  Reject null hypothesis.  There is significant difference.
pval2 = binom_test(590, n=10000, p=0.06)
print(pval2) #print 0.6891529835730346.  Fail to reject or accept null hypothesis.  There is no significant difference.
#Generally, if we receive a p-value of less than 0.05, we can reject the null hypothesis and state that there is a significant difference.  RM:  In contrast, if we receive a p-value of more than 0.05, we accept the null hypothesis and state that there is no significant difference.
#If we have two or more categorical datasets that we want to compare, we should use a Chi Square test. It is useful in situations like:  An A/B test where half of users were shown a green submit button and the other half were shown a purple submit button. Was one group more likely to click the submit button?;  Men and women were both given a survey asking "Which of the following three products is your favorite?" Did the men and women have significantly different preferences?
#In SciPy, you can use the function chi2_contingency to perform a Chi Square test.  The input to chi2_contingency is a contingency table where:  The columns are each a different condition, such as men vs. women or Interface A vs. Interface B; The rows represent different outcomes, like "Survey Response A" vs. "Survey Response B" or "Clicked a Link" vs. "Didn't Click".  This table can have as many rows and columns as you need.  from scipy.stats import chi2_contingency
from scipy.stats import chi2_contingency
# Contingency table
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12
X = [[30, 10],[35, 5],[28, 12]]
# their two most popular species of ants, the Leaf Cutter and the Harvester, vary in popularity between 1st, 2nd, and 3rd graders.  Answer is yes.  Accept null hypothesis.  No significant differrence
chi2, pval, dof, expected = chi2_contingency(X)
print(pval) #print 0.15508230807673704
# Contingency table 2
#         harvester |  leaf cutter
# ----+------------------+------------
# 1st gr | 30       |  10
# 2nd gr | 35       |  5
# 3rd gr | 28       |  12
# 4th gr | 20       |  20
X4th = [[30, 10],[35, 5],[28, 12],[20,20]]
#A class of 40 4th graders comes into VeryAnts in the next week and buys 20 sets of Leaf Cutter ants and 20 sets of Harvester ants.  Answer is no.  Reject null hypothesis.  Yes significant difference
chi2, pval4th, dof, expected = chi2_contingency(X4th)
print(pval4th) #print 0.002812834559546625

#Hypothesis Test Types Quiz.
'''
You've surveyed 10 people who work in finance, 10 people who work in education, and 10 people who work in the service industry on how many cups of coffee they drink per day. What test can you use to determine if there is a significant difference between the average coffee consumption of these three groups?  ANOVA
Let's say we run a 1 Sample T-Test on means for an exam. We expect the mean to be 75%, but we want to see if the actual scores are significantly better or worse than what we expected. After running the T-Test, we get a p-value of 0.25. What does this result mean?  We cannot confidently reject the null-hypothesis, so we do not have enough data to say that the mean on this exam is different from 75%.
What kind of test would you use to see if men and women identify differently as "Republican", "Democrat", or "Independent"?  Chi Square.  This is a comparison between 3 categorical sets, so Chi Square is the way to go.
You regularly order delivery from two different Pho restaurants, "What the Pho" and "Pho Tonic". You want to know if there's a significant difference between these two restaurants' average time to deliver to your house. What test could you use to determine this?  2 Sample T-Test
You own a juice bar and you theorize that 75% of your customers live in the surrounding 5 blocks. You survey a random sample of 12 customers and find that 7 of them live within those 5 blocks. What test do you run to determine if your results significantly differ from your expectation?  Binomial Test.
Let's say that last month 7% of free users of a site converted to paid users, but this month only 5% of free users converted. What kind of test should we use to see if this difference is significant?  Chi square
You just bought a new tea kettle that is supposed to heat water to boiling in 2 minutes. What kind of test can you run to determine if the time-to-boil is averaging significantly more than 2 minutes?  1 Sample T Test
If we perform an ANOVA test on 3 datasets and reject the null hypothesis, what test should we perform to determine which pairs of datasets are different?  Tukey's Range Test
Let's say we are comparing the time that users spend on three different versions of a landing page for a website. What test do we use to determine if there is a significant difference between any two of the sets? ANOVA
You've collected data on 1000 different sites that end with .com, .edu, and .org and have recorded the number of each that have Times New Roman, Helvetica, or another font as their main font. What test can you use to determine if there's a relationship between top-level domain and font type?  Chi Square
'''

#Familiar: A Study In Data Analysis
veinlifespans = [76.93767431, 75.99335913, 74.79815012, 74.50202147, 77.48888898, 72.14256573, 75.99303167, 76.34155048, 77.48475563, 76.53210148, 76.25508955, 77.58398317, 77.04737035, 72.87475175, 77.43504547, 77.49234141, 78.32672047, 73.34370247, 79.96915765, 74.83800583]
#we want to show is that our most basic package, the Vein Pack, actually has a significant impact on the subscribers.
veinlifespans = np.array(veinlifespans)
print(np.mean(veinlifespans)) #print 76.169013356
#If the average lifespan of a Vein Pack subscriber is significantly different from the average life expectancy of 71 years.  Use the 1-Sample T-Test to compare vein_pack_lifespans to the average life expectancy 71 with the average veinlifespans 76.169013356. Save the result into a variable called vein_pack_test.
tstat, pval = ttest_1samp(veinlifespans, 71)
vein_pack_test = pval
#Let's check if the results are significant! Check the pvalue of vein_pack_test. If it's less than 0.05, we've got significance!  If the test's p-value is less than 0.05, print "The Vein Pack Is Proven To Make You Live Longer!". Otherwise print "The Vein Pack Is Probably Good For You Somehow!"
#Generally, if we receive a p-value of less than 0.05, we can reject the null hypothesis and state that there is a significant difference.  RM:  In contrast, if we receive a p-value of more than 0.05, we accept the null hypothesis and state that there is no significant difference.
print(vein_pack_test) #print 2.7463118036299626e-10
if vein_pack_test < 0.05:
  print("The Vein Pack Is Proven to Make You Live Longer") #print The Vein Pack Is Proven to Make You Live Longer.  RM:  there is significnat difference between the average life psan 71 and the Vein Pack average life 76.169013356
else:
  print("The Vein Pack Is Probably Good For You Somehow!")
#We'd like to compare this lifespan data between our different packages. Our next step up from the Vein Pack is the Artery Pack. Let's get the lifespans of Artery Pack subscribers.
arterylifespans = [76.33537008, 76.92308232, 75.95244164, 74.54498348, 76.40450428, 73.07924889, 77.02354461, 74.11742042, 77.38650656, 73.04476584, 74.96311851, 73.31954302, 75.85740138, 76.15265351, 73.35510286, 73.90221256, 73.77121195, 68.3148983,  74.63975718, 78.38547731]
print(arterylifespans)
#we want to show that the subscribers to the Artery Pack experience a significant improvement even beyond what a Vein Pack subscriber's benefits. Import the 2 Sample T-Test and we'll use that to see if there is a significant difference between the two subscriptions.
arterylifespans = np.array(arterylifespans)
print(np.mean(arterylifespans)) #print 74.87366223500001
tstatstic, pval = ttest_ind(veinlifespans, arterylifespans)
package_comparison_results = pval
print(package_comparison_results) #print 0.05588883085502891
if package_comparison_results < 0.05:
  print("The Artery Package guarantees even stronger results!")
else:
  print("The Artery Package is also a great product!!") #print The Artery Package is also a great product!!  RM:  there is no significant difference between the Vein Pack average 76.169013356 and the Artery Life Pack average 74.87366223500001

#Shame that it's not significantly better, but maybe there's a way to demonstrate the benefits of the Artery Package yet.
#we've sent out a survey collecting the iron counts for our subscribers, and filtered that data into "low", "normal", and "high".  We received 200 responses from our Vein Package subscribers. 70% of them had low iron counts 140, 20% had normal 40, and 10% of them have high iron counts 20.  We were only able to get 145 responses from our Artery Package subscribers, but only 20% of them had low iron counts 29. 60% had normal 87, and 20% have high iron counts 29.
iron_contingency_table = [[140, 29], [40, 87], [20, 29]]  #rows top to bottom low, normal, high.  columns left to right Vein Package subscribers and Artery Package subscribers
#We want to be able to tell if what seems like a higher number of our Artery Package subscribers is a significant difference from what was reported by Vein Package subscribers. Import the Chi-Squared test so that we can find out.  Run the Chi-Squared test on the iron_contingency_table and save the p-value in a variable called iron_pvalue.
chi2, pval, dof, expected = chi2_contingency(iron_contingency_table)
print(pval) #print 2.9227133549883315e-19
iron_pvalue = pval
#If the iron_pvalue is less than 0.05, print out "The Artery Package Is Proven To Make You Healthier!" otherwise we'll have to use our other marketing copy: "While We Can't Say The Artery Package Will Help You, I Bet It's Nice!"
if iron_pvalue < 0.05:
  print("The Artery Package Is Proven To Make You Healthier!") #print The Artery Package Is Proven To Make You Healthier!  RM:  there is significant difference between the Artery Package and the Vein Package survey responses.  RM:  Shouldn't there be no significant difference because you want both Vein and Artery to make humans healthier?  Not Vein yes healthier and Artery no healthier?

else:
  print("While We Can't Say The Artery Package Will Help You, I Bet It's Nice!")
#Fantastic! With proven benefits to both of our product lines, we can definitely ramp up our marketing and sales. RM:  The chi2_contingency statistic proves the Artery Package is healthy because we used the survey reponses.  The 2 Sample T-Test proves the ARtery Package is not as healthy.
#Generally, if we receive a p-value of less than 0.05, we can reject the null hypothesis and state that there is a significant difference.  RM:  In contrast, if we receive a p-value of more than 0.05, we accept the null hypothesis and state that there is no significant difference.

#FetchMaker: A Study In Data Analysis
#RM:  create file scipyfetchmaker.py
