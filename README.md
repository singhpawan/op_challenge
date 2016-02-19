**Overview**:
The Folder Structure is as follows:
code: contains all the .py files
plots: contains the plots
and other necessary files required by the program.

The task is divided into three parts:

**Part 1**: In this part we will calculate the character frequency and eliminate ','.

To run the code:
```
python count_characters.py resume.txt

```
![Histogram of character frequency in the resume.txt](/plots/character_count.png)
---

**Part 2**: In this part we are going to answer three key questions:
1. Department with the max number of job openings
2. Departments with the maximum and minimum salary
3. In end, we will try to determine which jobs are likely to be filled last.

To run the code:
```
python nycjobs.py nycjobs.csv
```
1.The department with the maximum job openings is the **DEPT OF HEALTH/MENTAL HYGIENE** with **2456** job openings.

2. Department with the Max salary is **DEPT OF ENVIRONMENT PROTECTION** and the Department with lowest salary is 
**OFFICE OF COLLECTIVE BARGAININ** with an **hourly salary of 10$**.

3. To determine which salary are less likely to be filled, I hypothesized that it would depend on two parameters, the 
**Posting Type** and **Salary Frequency** and I segmented users based on that. In addition to that I calculated the average differecne in days between the posting updated and posting date. Since job which are filled will be updated less frequently and hence the difference will be smaller. Therefore I **segemented** the users based on these parameters and calculate the mean difference for each categories. Although I didn't find any statistical signnificance for **Posting Type**. I found that the difference in **salary frequency** was statistically significant with a confidence internval of **84%** and a p-value of **0.16**. In future I would futher take salary into consideration and binning them appropriately.
```
 tvalue, pvalue = scipy.stats.ttest_ind(annual_difference_list, hourly_difference_list, equal_var = False)
 ```
equal_var = False. I didn't make any assumptions about the underlying distribution.

Following is the sample outoput of running the above code.
```
  The average difference in days between the posting updated and posting created for column  Posting Type and field  Internal is :  13.9731838128
The average difference in days between the posting updated and posting created for column  Posting Type and field  External is :  14.7495987159
The average difference in days between the posting updated and posting created for column  Salary Frequency and field  Annual is :  14.5101248266
The average difference in days between the posting updated and posting created for column  Salary Frequency and field  Hourly is :  11.2436363636
 The result at least has a confidence interval of 80% and p value is :  0.168781896985

```

---
---

**Part 3**: In this case we scraped two different databases from the labor statistics website and I tried to determine the 
industries with the maximum number of job openings and on the contrary industry which has the most number of layoffs. The code is highly automated you just need to run the program and sit back. To ensure standardization we use data for the month of jan 2013. The BLS stopped collecting data after May 2013 on layoffs.

To run the code:
```
python bls_munging.py
```

The industry with the most job openings is **Trade, Transportation and Utilities** with **735** jobs followed by **Business Services** at **676**.

![ Most job openigns](/plots/most_job_openings.png)

On the Other hand the industry with the most layoffs was **Manufacturing** with **455** jobs followed by **Administrative and waste services** with **237** jobs.
![Most layoffs in the industries](/plots/most_layoffs.png)

The full list is here.
```
Construction of buildings 21
Heavy and civil engineering construction 88
Specialty trade contractors 79
Manufacturing 455
Food 58
Beverage and tobacco products 3
Textile mills 35
Textile product mills 5
Apparel 16
Leather and allied products 4
Wood products 26
Paper 5
Printing and related support activities 5
Petroleum and coal products 3
Chemicals 10
Plastics and rubber products 20
Nonmetallic mineral products 19
Primary metals 26
Fabricated metal products 29
Machinery 34
Computer and electronic products 15
Electrical equipment and appliances 18
Transportation equipment 86
Furniture and related products 32
Miscellaneous manufacturing 7
Wholesale trade 28
Retail trade (4) 136
Building material and garden supply stores 8
Food and beverage stores 25
Clothing and clothing accessories stores 14
General merchandise stores 52
Transportation and warehousing (4) 87
Truck transportation 22
transportation 35
Support activities for transportation 7
Information 36
Finance and insurance 25
Real estate and rental and leasing 3
Professional and technical services 41
Management of companies and enterprises 7
Administrative and waste services 237
Educational services 10
Health care and social assistance 23
Arts, entertainment, and recreation 32
Accommodation and food services 86
Accommodation 29
Food services and drinking places 57
Other services, except public administration 12
Unclassified 3

```


