import pandas as pd
import random

MINIMUM_PASSING_GRADE = 60

MATH_LIST = ["Algebra 1", "Geometry", "Algebra 2", "Pre-Calculus",
             "Math For College Readiness",
             "Math For Financial Literacy"]

ENGLISH_LIST = ["English 1", "English 2", "English 3",
                "English 4", "Creative Writing"]

SCIENCE_LIST = ["Biology", "Environmental Science",
                "Anatomy And Physiology", "Chemistry",
                "Forensic Science", "Physical Science"]

SOCIAL_STUDIES_LIST = ["World History", "US History", "Economics", "Government"]

PERFORMING_ARTS_LIST = ["Film", "Theater", "Band", "Chorus"]

PHYSICAL_EDUCATION_LIST = ["Weight Lifting", "Basketball",
                           "Volleyball", "Team Sports",
                           "Individual Sports"]

LANGUAGE_LIST = ["Spanish", "French"]

MATH_MIN = 4
ENGLISH_MIN = 4
SCIENCE_MIN = 3
SOCIAL_STUDIES_MIN = 4
PERFORMING_ARTS_MIN = 1
PERSONAL_FITNESS_MIN = 1
PHYSICAL_EDUCATION_MIN = 1
FINANCIAL_LITERACY_MIN = 1
ELECTIVES_MIN = 8
ONLINE_CLASS_MIN = 1

df = pd.DataFrame({
    'StudentID': studnet_ids,
    'Age': ages,
    'Year1': year1,
    'Year2': year2,
    'Year3': year3,
    'Year4': year4,
})

def make_student_csv():
    # Start by making 900 students who are doing just fine to okay
    Year_1 = []
    Year_2 = []
    Year_3 = []
    Year_4 = []

    for i in range(900):
        # Year 1 list
        Year_1.append(MATH_LIST[0])
        Year_1.append(ENGLISH_LIST[0])
        rand_int = random.randint(0, 5)
        Year_1.append(SCIENCE_LIST[rand_int])
        Year_1.append(SOCIAL_STUDIES_LIST[0])
        rand_int = random.randint(0, 3)
        Year_1.append(PERFORMING_ARTS_LIST[rand_int])
        rand_int - random.randint(0, 4)
        Year_1.append(PHYSICAL_EDUCATION_LIST[rand_int])
        Year_1.append("Financial Literacy")

        # Year 2 List
        # Math
        Year_2.append(MATH_LIST[1])
        # English
        Year_2.append(ENGLISH_LIST[1])
        choice_list = SCIENCE_LIST
        index_of_previous_science = choice_list.index(Year_1[2])
        choice_list = choice_list.pop(index_of_previous_science)
        rand_choice = random.choice(choice_list)
        # Science
        Year_2.append(SCIENCE_LIST[rand_choice])
        # Social Studies
        Year_2.append(SOCIAL_STUDIES_LIST[1])
        # Spot 5
        spot_five_previous_class = Year_1[4]
        rand_int = random.randint(0, 2)
        if rand_int == 0:
            if spot_five_previous_class in PERFORMING_ARTS_LIST:
                index_of_previous_spot_five = PERFORMING_ARTS_LIST.index(spot_five_previous_class)
                choice_list = PERFORMING_ARTS_LIST
                choice_list = choice_list.pop(index_of_previous_spot_five)
                Year_2.append(random.choice(choice_list))
        elif rand_int == 1:
            if spot_five_previous_class in PHYSICAL_EDUCATION_LIST:
                index_of_previous_spot_five = PHYSICAL_EDUCATION_LIST.index(spot_five_previous_class)
                choice_list = PHYSICAL_EDUCATION_LIST
                choice_list = choice_list.pop(index_of_previous_spot_five)
                Year_2.append(random.choice(choice_list))
        else:
            index_of_previous_spot_five = LANGUAGE_LIST.index(spot_five_previous_class)
            choice_list = LANGUAGE_LIST
            choice_list = choice_list.pop(index_of_previous_spot_five)
            Year_2.append(random.choice(choice_list))
        # Spot 6
        rand_int - random.randint(0, 4)
        Year_2.append(PHYSICAL_EDUCATION_LIST[rand_int])
        Year_2.append("Financial Literacy")

