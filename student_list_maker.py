import pandas as pd
import random

MINIMUM_PASSING_GRADE = 60

MATH_LIST = ["Algebra 1", "Geometry", "Algebra 2", "Pre-Calculus",
             "Math For College Readiness",
             "Math For Financial Literacy"]

ENGLISH_LIST = ["English 1", "English 2", "English 3",
                "English 4", "Creative Writing", "Technical Writing"]

SCIENCE_LIST = ["Biology", "Environmental Science",
                "Anatomy And Physiology", "Chemistry",
                "Forensic Science", "Physical Science"]

SOCIAL_STUDIES_LIST = ["World History", "US History", "Economics", "Government"]

PERFORMING_ARTS_LIST = ["Film", "Theater", "Band", "Chorus"]

PHYSICAL_EDUCATION_LIST = ["Weight Lifting", "Basketball",
                           "Volleyball", "Team Sports",
                           "Individual Sports"]

LANGUAGE_LIST = ["Spanish", "French", "Latin"]

ELECTIVES_LIST = ["Spanish", "French", "Weight Lifting",
                  "Basketball", "Volleyball", "Team Sports",
                  "Individual Sports", "Film", "Theater",
                  "Band", "Chorus", "Biology", "Environmental Science",
                  "Anatomy And Physiology", "Chemistry",
                  "Forensic Science", "Physical Science", "Creative Writing",
                  "Math For College Readiness", "Latin", "Technical Writing"]

columns = []

df = pd.DataFrame(columns=["Student_id", "Age_at_year_4", "Year_1_Classes",
                           "Year_2_Classes", "Year_3_Classes", "Year_4_Classes",
                           "Year_1_Grades", "Year_2_Grades", "Year_3_Grades", "Year_4_Grades",
                           "Year_1_Absences", "Year_2_Absences", "Year_3_Absences", "Year_4_Absences",
                           "Year_1_Late_HW", "Year_2_Late_HW", "Year_3_Late_HW", "Year_4_Late_HW",
                           "Year_1_Participation", "Year_2_Participation", "Year_3_Participation",
                           "Year_4_Participation"])


def make_student_csv():
    year_1 = []
    year_2 = []
    year_3 = []
    year_4 = []

    student_id_number = 1

    for i in range(1, 1001):
        # Age at year_4
        student_age = random.randint(17, 20)

        # Year 1 list
        year_1.append(MATH_LIST[0])
        year_1.append(ENGLISH_LIST[0])
        rand_int = random.randint(0, 5)
        year_1.append(SCIENCE_LIST[rand_int])
        year_1.append(SOCIAL_STUDIES_LIST[0])
        rand_int = random.randint(0, 3)
        year_1.append(PERFORMING_ARTS_LIST[rand_int])
        rand_int - random.randint(0, 4)
        year_1.append(PHYSICAL_EDUCATION_LIST[rand_int])
        year_1.append("Math For Financial Literacy")

        # Year 2 List
        # Math
        year_2.append(MATH_LIST[1])
        # English
        year_2.append(ENGLISH_LIST[1])
        choice_list = SCIENCE_LIST.copy()
        index_of_previous_science = choice_list.index(year_1[2])
        del choice_list[index_of_previous_science]
        rand_choice = random.choice(choice_list)
        # Science
        year_2.append(rand_choice)
        choice_list.clear()
        # Social Studies
        year_2.append(SOCIAL_STUDIES_LIST[1])
        # Spot 5
        spot_five_previous_class = year_1[4]
        rand_int = random.randint(0, 2)
        if rand_int == 0:
            index_of_previous_spot_five = PERFORMING_ARTS_LIST.index(spot_five_previous_class)
            choice_list = PERFORMING_ARTS_LIST.copy()
            del choice_list[index_of_previous_spot_five]
            year_2.append(random.choice(choice_list))
            choice_list.clear()
        elif rand_int == 1:
            index_of_physed_year1 = PHYSICAL_EDUCATION_LIST.index(year_1[5])
            choice_list = PHYSICAL_EDUCATION_LIST.copy()
            del choice_list[index_of_physed_year1]
            year_2.append(random.choice(choice_list))
            choice_list.clear()
        else:
            choice_list = LANGUAGE_LIST.copy()
            year_2.append(random.choice(choice_list))
            choice_list.clear()
        # Spot 6
        year_2.append("Personal Fitness")
        available_electives_list = ELECTIVES_LIST.copy()
        for a_class in year_1:
            if a_class in available_electives_list:
                index_of_class = available_electives_list.index(a_class)
                del available_electives_list[index_of_class]
        for a_class in year_2:
            if a_class in available_electives_list:
                index_of_class = available_electives_list.index(a_class)
                del available_electives_list[index_of_class]
        rand_int = random.randint(0, len(available_electives_list) - 1)
        year_2.append(available_electives_list[rand_int])
        # Year 3
        # Math
        available_math_list = MATH_LIST.copy()
        math_taken = 0
        for a_class in year_1:
            if a_class in available_math_list:
                index_of_class = available_math_list.index(a_class)
                del available_math_list[index_of_class]
                math_taken = math_taken + 1
        for a_class in year_2:
            if a_class in available_math_list:
                index_of_class = available_math_list.index(a_class)
                del available_math_list[index_of_class]
                math_taken = math_taken + 1
        if math_taken < 4:
            year_3.append(MATH_LIST[2])
            math_taken = math_taken + 1
        # English
        year_3.append(ENGLISH_LIST[2])
        # Check last year's elective for a science class
        available_science_classes = SCIENCE_LIST.copy()
        if year_2[6] in SCIENCE_LIST:
            index_of_class = available_science_classes.index(year_2[6])
            del available_science_classes[index_of_class]
        index_of_class = available_science_classes.index(year_1[2])
        del available_science_classes[index_of_class]
        index_of_class = available_science_classes.index(year_2[2])
        del available_science_classes[index_of_class]
        rand_int = random.randint(0, len(available_science_classes) - 1)
        # Add 3rd science class. Science requirement complete
        year_3.append(available_science_classes[rand_int])
        # Social Studies
        year_3.append(SOCIAL_STUDIES_LIST[2])
        # Spot 5
        spot_five_previous_class = year_2[4]
        available_electives_list = ELECTIVES_LIST.copy()
        for a_class in year_1:
            if a_class in available_electives_list:
                index_of_class = available_electives_list.index(a_class)
                del available_electives_list[index_of_class]
        for a_class in year_2:
            if a_class in available_electives_list:
                index_of_class = available_electives_list.index(a_class)
                del available_electives_list[index_of_class]
        rand_int = random.randint(0, len(available_electives_list) - 1)
        year_3.append(available_electives_list[rand_int])
        # Spot 6
        del available_electives_list[rand_int]
        rand_int = random.randint(0, len(available_electives_list) - 1)
        year_3.append(available_electives_list[rand_int])
        # Spot 7
        del available_electives_list[rand_int]
        rand_int = random.randint(0, len(available_electives_list) - 1)
        year_3.append(available_electives_list[rand_int])

        # Year 4
        # Remove all taken class from electives list
        for a_class in year_1:
            if a_class in available_electives_list:
                index_of_class = available_electives_list.index(a_class)
                del available_electives_list[index_of_class]
        for a_class in year_2:
            if a_class in available_electives_list:
                index_of_class = available_electives_list.index(a_class)
                del available_electives_list[index_of_class]
        for a_class in year_3:
            if a_class in available_electives_list:
                index_of_class = available_electives_list.index(a_class)
                del available_electives_list[index_of_class]
        if math_taken < 4 and year_3[0] == "Algebra 2":
            year_4[0] = "Pre-Calculus"
        else:
            rand_int = random.randint(0, len(available_electives_list) - 1)
            year_4.append(available_electives_list[rand_int])
            del available_electives_list[rand_int]
        # English requirement met
        year_4.append(ENGLISH_LIST[3])
        rand_int = random.randint(0, len(available_electives_list) - 1)
        year_4.append(available_electives_list[rand_int])
        del available_electives_list[rand_int]
        # Social Studies requirement met
        year_4.append(SOCIAL_STUDIES_LIST[3])
        if len(available_electives_list) - 1 == 0:
            rand_int = 0
        else:
            rand_int = random.randint(0, len(available_electives_list) - 1)
        year_4.append(available_electives_list[rand_int])
        del available_electives_list[rand_int]
        if len(available_electives_list) - 1 == 0:
            rand_int = 0
        else:
            rand_int = random.randint(0, len(available_electives_list) - 1)
        year_4.append(available_electives_list[rand_int])
        del available_electives_list[rand_int]
        if len(available_electives_list) - 1 == 0:
            rand_int = 0
        else:
            rand_int = random.randint(0, len(available_electives_list) - 1)
        year_4.append(available_electives_list[rand_int])

        print("Students created: " + str(i))

        year_1_as_string = ', '.join(year_1)
        year_2_as_string = ', '.join(year_2)
        year_3_as_string = ', '.join(year_3)
        year_4_as_string = ', '.join(year_4)

        df.loc[i - 1] = [
            student_id_number,
            student_age,
            year_1_as_string,
            year_2_as_string,
            year_3_as_string,
            year_4_as_string,
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
            "",
        ]

        # Increment student number
        student_id_number = student_id_number + 1

        # Set math_taken back to 0
        math_taken = 0

        # Clear lists for next student
        year_1.clear()
        year_2.clear()
        year_3.clear()
        year_4.clear()

    # Grades part
    year_1_grades = []
    year_2_grades = []
    year_3_grades = []
    year_4_grades = []

    # Add random grades for each class for regular students
    for j in range(1, 901):
        for i in range(7):
            year_1_grades.append(str(round(random.uniform(70.0, 100.0), 1)))
            year_2_grades.append(str(round(random.uniform(70.0, 100.0), 1)))
            year_3_grades.append(str(round(random.uniform(70.0, 100.0), 1)))
            year_4_grades.append(str(round(random.uniform(70.0, 100.0), 1)))

        year_1_grades_as_string = ', '.join(year_1_grades)
        year_2_grades_as_string = ', '.join(year_2_grades)
        year_3_grades_as_string = ', '.join(year_3_grades)
        year_4_grades_as_string = ', '.join(year_4_grades)

        df.loc[df['Student_id'] == j, 'Year_1_Grades'] = year_1_grades_as_string
        df.loc[df['Student_id'] == j, 'Year_2_Grades'] = year_2_grades_as_string
        df.loc[df['Student_id'] == j, 'Year_3_Grades'] = year_3_grades_as_string
        df.loc[df['Student_id'] == j, 'Year_4_Grades'] = year_4_grades_as_string

        year_1_grades_as_string = ""
        year_2_grades_as_string = ""
        year_3_grades_as_string = ""
        year_4_grades_as_string = ""

        year_1_grades.clear()
        year_2_grades.clear()
        year_3_grades.clear()
        year_4_grades.clear()

    # Adds grades for possible failing students
    for j in range(901, 1001):
        for i in range(7):
            year_1_grades.append(str(round(random.uniform(50.0, 100.0), 1)))
            year_2_grades.append(str(round(random.uniform(50.0, 100.0), 1)))
            year_3_grades.append(str(round(random.uniform(50.0, 100.0), 1)))
            year_4_grades.append(str(round(random.uniform(50.0, 100.0), 1)))

        year_1_grades_as_string = ', '.join(year_1_grades)
        year_2_grades_as_string = ', '.join(year_2_grades)
        year_3_grades_as_string = ', '.join(year_3_grades)
        year_4_grades_as_string = ', '.join(year_4_grades)

        df.loc[df['Student_id'] == j, 'Year_1_Grades'] = year_1_grades_as_string
        df.loc[df['Student_id'] == j, 'Year_2_Grades'] = year_2_grades_as_string
        df.loc[df['Student_id'] == j, 'Year_3_Grades'] = year_3_grades_as_string
        df.loc[df['Student_id'] == j, 'Year_4_Grades'] = year_4_grades_as_string

        year_1_grades_as_string = ""
        year_2_grades_as_string = ""
        year_3_grades_as_string = ""
        year_4_grades_as_string = ""

        year_1_grades.clear()
        year_2_grades.clear()
        year_3_grades.clear()
        year_4_grades.clear()

    # This will add absences for regular students
    year_1_absences = ""
    year_2_absences = ""
    year_3_absences = ""
    year_4_absences = ""

    for j in range(1, 901):
        for i in range(7):
            year_1_absences = str(random.randint(0, 10))
            year_2_absences = str(random.randint(0, 10))
            year_3_absences = str(random.randint(0, 10))
            year_4_absences = str(random.randint(0, 10))

        df.loc[df['Student_id'] == j, 'Year_1_Absences'] = year_1_absences
        df.loc[df['Student_id'] == j, 'Year_2_Absences'] = year_2_absences
        df.loc[df['Student_id'] == j, 'Year_3_Absences'] = year_3_absences
        df.loc[df['Student_id'] == j, 'Year_4_Absences'] = year_4_absences

    # This will add absences for possible failing students
    year_1_absences = ""
    year_2_absences = ""
    year_3_absences = ""
    year_4_absences = ""

    for j in range(901, 1001):
        for i in range(7):
            year_1_absences = str(random.randint(0, 20))
            year_2_absences = str(random.randint(0, 20))
            year_3_absences = str(random.randint(0, 20))
            year_4_absences = str(random.randint(0, 20))

        df.loc[df['Student_id'] == j, 'Year_1_Absences'] = year_1_absences
        df.loc[df['Student_id'] == j, 'Year_2_Absences'] = year_2_absences
        df.loc[df['Student_id'] == j, 'Year_3_Absences'] = year_3_absences
        df.loc[df['Student_id'] == j, 'Year_4_Absences'] = year_4_absences

    # This will add late homeworks for regular students
    year_1_late_hw = ""
    year_2_late_hw = ""
    year_3_late_hw = ""
    year_4_late_hw = ""

    for j in range(1, 901):
        for i in range(7):
            year_1_late_hw = str(random.randint(0, 10))
            year_2_late_hw = str(random.randint(0, 10))
            year_3_late_hw = str(random.randint(0, 10))
            year_4_late_hw = str(random.randint(0, 10))

        df.loc[df['Student_id'] == j, 'Year_1_Late_HW'] = year_1_late_hw
        df.loc[df['Student_id'] == j, 'Year_2_Late_HW'] = year_2_late_hw
        df.loc[df['Student_id'] == j, 'Year_3_Late_HW'] = year_3_late_hw
        df.loc[df['Student_id'] == j, 'Year_4_Late_HW'] = year_4_late_hw

    # This will add late homeworks for possible failing students
    year_1_late_hw = ""
    year_2_late_hw = ""
    year_3_late_hw = ""
    year_4_late_hw = ""

    for j in range(901, 1001):
        for i in range(7):
            year_1_late_hw = str(random.randint(0, 30))
            year_2_late_hw = str(random.randint(0, 30))
            year_3_late_hw = str(random.randint(0, 30))
            year_4_late_hw = str(random.randint(0, 30))

        df.loc[df['Student_id'] == j, 'Year_1_Late_HW'] = year_1_late_hw
        df.loc[df['Student_id'] == j, 'Year_2_Late_HW'] = year_2_late_hw
        df.loc[df['Student_id'] == j, 'Year_3_Late_HW'] = year_3_late_hw
        df.loc[df['Student_id'] == j, 'Year_4_Late_HW'] = year_4_late_hw

    # This will add class participation
    year_1_participation = ""
    year_2_participation = ""
    year_3_participation = ""
    year_4_participation = ""

    for j in range(1, 901):
        for i in range(7):
            year_1_participation = str(random.randint(6, 10))
            year_2_participation = str(random.randint(6, 10))
            year_3_participation = str(random.randint(6, 10))
            year_4_participation = str(random.randint(6, 10))

        df.loc[df['Student_id'] == j, 'Year_1_Participation'] = year_1_participation
        df.loc[df['Student_id'] == j, 'Year_2_Participation'] = year_2_participation
        df.loc[df['Student_id'] == j, 'Year_3_Participation'] = year_3_participation
        df.loc[df['Student_id'] == j, 'Year_4_Participation'] = year_4_participation

    # This will add class participation for possible failing students
    year_1_participation = ""
    year_2_participation = ""
    year_3_participation = ""
    year_4_participation = ""

    for j in range(901, 1001):
        for i in range(7):
            year_1_participation = str(random.randint(0, 6))
            year_2_participation = str(random.randint(0, 6))
            year_3_participation = str(random.randint(0, 6))
            year_4_participation = str(random.randint(0, 6))

        df.loc[df['Student_id'] == j, 'Year_1_Participation'] = year_1_participation
        df.loc[df['Student_id'] == j, 'Year_2_Participation'] = year_2_participation
        df.loc[df['Student_id'] == j, 'Year_3_Participation'] = year_3_participation
        df.loc[df['Student_id'] == j, 'Year_4_Participation'] = year_4_participation

    # # Save to csv file
    df.to_csv("students.csv", index=False)


if __name__ == "__main__":
    make_student_csv()
