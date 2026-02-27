"""
author: Viktoriia Hromiak
date: 2026/02/10
Investigating Variables
"""

# Input
name = "Viktoriia"
grade = 11
favourite_exclamation = "duh"
least_favourite_colour = "green"
is_cool = False
math_test_score = 67
sister_name = "Emily"
study_time = 15
feeling = "worried"
parent = "mom"


slope = 2
y_intercept = 10
x = 3
y = slope * x + y_intercept

# Processing / Output
print(
    f"Hey guys, my name is {name} and I am currently in grade {grade}. "
    + f"Yesterday, there was a spider in the classroom that made me yell {favourite_exclamation} while I was taking a math test with my {least_favourite_colour} pen :/ "
    + f"I was really {feeling} because yesterday I prepared for this test for only {study_time} minutes. "
    + f"One of the questions on the test was wether or not I thought Elvis was cool, so I obviously put {is_cool} to get the answer right... "
    + f"Turns out that I only scored a {math_test_score} on the test. My {parent} told me that I need to study more. One of the qusetions was asking me to write the equation for a line "
    + f"with a slope of {slope} and a y-intercept of {y_intercept} so I wrote y = {slope}x + {y_intercept}, but I did not notice the x value of {x} in the question "
    + f"so I needed to, on the next line, say that the value of y was {y}. "
    + f"I told my sister {sister_name} about this and she just laughed at me 🙄"
    + "Anyway, that's the story of my math test."
)