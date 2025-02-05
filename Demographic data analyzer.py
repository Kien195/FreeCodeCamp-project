import pandas as pd
import math

pd.set_option("display.max_columns", 500)

df = pd.read_csv("adult.data.csv")

print(df)
print()

race_count = df["Race"].value_counts()
print(race_count)
print()

average_age_men = df[df["Sex"] == "Male"]["Age"].mean()
print(f"The average age of men is: {math.ceil(average_age_men)}")
print()

percentage_bachelors = (df['Education'] == 'Bachelors').mean() * 100
print(f"The percentage of people who have Bachelors degree is: {math.ceil(percentage_bachelors)}%")
print()

higher_education = df['Education'].isin(['Bachelors', 'Masters', 'Doctorate'])
percentage_high_edu_salary = (df[higher_education & (df['Salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100
print(f"The percentage of people who have high education with salary more than 50K is: {math.ceil(percentage_high_edu_salary)}%")
print()

min_week_hours = df["Hours_per_week"].min()
print(f"The minimum number of hours a person works per week is: {min_week_hours} hours")
print()

min_workers = df[df["Hours_per_week"] == min_week_hours]
min_percentage_salary = (min_workers[min_workers["Salary"] == ">50K"].shape[0] / min_workers.shape[0]) * 100
print(f"The percentage of people who work the minimum number of hours pr week with a salary more than 50K is :{math.floor(min_percentage_salary)}%")
print()

country_salary = df[df['Salary'] == '>50K']['Native_country'].value_counts() / df['Native_country'].value_counts() * 100
highest_earning_country = country_salary.idxmax()
highest_earning_country_percentage = country_salary.max()

print(highest_earning_country)
print(f"{highest_earning_country_percentage}%")

top_IN_occupation = df[(df['Native_country'] == 'India') & (df['Salary'] == '>50K')]['Occupation'].value_counts().idxmax()
print(top_IN_occupation)