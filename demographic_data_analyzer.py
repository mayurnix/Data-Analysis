"""    freecodecamp data analysis project2    """

import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv("/workspace/boilerplate-demographic-data-analyzer/adult.data.csv")

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(),1)

    # What is the percentage of people who have a Bachelor's degree?
    number_bachelors = len(df[df['education'] == "Bachelors"])
    total = len(df)
    percentage_bachelors = round(number_bachelors/total * 100,1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    higher_education_rich = round(len(higher_education[higher_education['salary'] == '>50K'])/len(higher_education)*100, 1)
    lower_education_rich = round(len(lower_education[lower_education['salary'] == '>50K'])/len(lower_education)*100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df["hours-per-week"])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = len(df[((df['hours-per-week'] == min(df['hours-per-week'])) & (df['salary']=='>50K'))])

    rich_percentage = round( num_min_workers / len(df[df['hours-per-week'] == min(df['hours-per-week'])]) * 100, 1)

    # What country has the highest percentage of people that earn >50K?
    df2 = df[df['salary']=='>50K']['native-country'].value_counts()
    df3 = df['native-country'].value_counts()
    df4 = df2/df3*100
    highest_earning_country = df4.index[df4 == max(df4)][0]
    highest_earning_country_percentage = round(max(df4), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[((df['native-country'] == 'India') & (df['salary']=='>50K'))]['occupation'].value_counts().index[0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }




# # l = df.columns
# Index(['age', 'workclass', 'fnlwgt', 'education', 'education.num',
#        'marital.status', 'occupation', 'relationship', 'race', 'sex',
#        'capital.gain', 'capital.loss', 'hours.per.week', 'native.country',
#        'income'],
#       dtype='object')

# age,workclass,fnlwgt,education,education-num,marital-status,occupation,
# relationship,race,sex,capital-gain,capital-loss,hours-per-week,native-country,salary


# list1 = list(df['race'])
# set_race = set(df['race'])
# Dict_race = {}
# for i in set_race:
#     Dict_race[i] = list1.count(i)
# df1 = pd.Series(Dict_race)
# print("Q1. How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.","ans:",df1,sep="\n")



# list2 =[]
# # set_sex = set(df['sex'])      {'Female', 'Male'}
# for j in range(len(df)):
#     if df['sex'].iloc[j] == 'Male':
#         list2.append(df['age'].iloc[j])
# print("Q2. What is the average age of men?",'ans:',round(np.average(list2)),sep='\n')

# list3 = list(df["education"])
# # print(set(df["education"]))  {'Masters', 'HS-grad', 'Assoc-acdm', '12th', 'Doctorate', '10th', 'Assoc-voc', '1st-4th', '9th', '5th-6th', '7th-8th', 'Prof-school', 'Bachelors', '11th', 'Preschool', 'Some-college'}
# a = list3.count("Bachelors")
# b = len(df["education"])
# print("Q3. What is the percentage of people who have a Bachelor's degree?")
# print('ans: ',round((a*100)/b,2),'%',sep='')

# list4 = []
# list_ed = ['Bachelors', 'Masters', 'Doctorate']
# # print(set(df['income'])) {'<=50K', '>50K'}
# m = 0
# for k in range(len(df)):
#     if df["education"].iloc[k] in list_ed:
#         if df['income'].iloc[k] == '>50K' :
#             m += 1
# n = len(df['income'])
# print('Q4. What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?')
# print('ans: ',round((m*100)/n,2),'%',sep='')


# list5 = []
# o = 0
# for j in range(len(df)):
#     if df["education"].iloc[j] not in list_ed:
#         if df['income'].iloc[j] == '>50K' :
#             o += 1
# p = len(df['income'])
# print("Q5. What percentage of people without advanced education make more than 50K?")
# print('ans: ',round((o*100)/p,2),'%',sep='')

# print("What is the minimum number of hours a person works per week?",min(df["hours.per.week"]))
# print("What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?")
# print(df)
# print(set(df['income']))
