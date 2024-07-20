# Define category mappings
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


def map_to_class_category(class_list):
    mapped_list = []
    for a_class in class_list:
        if a_class in MATH_LIST:
            mapped_list.append("Math")
        elif a_class in ENGLISH_LIST:
            mapped_list.append("English")
        elif a_class in SCIENCE_LIST:
            mapped_list.append("Science")
        elif a_class in SOCIAL_STUDIES_LIST:
            mapped_list.append("Social Studies")
        elif a_class in PERFORMING_ARTS_LIST:
            mapped_list.append("Performing Arts")
        elif a_class in PHYSICAL_EDUCATION_LIST:
            mapped_list.append("Physical Education")
        elif a_class in LANGUAGE_LIST:
            mapped_list.append("Language")

    return mapped_list
