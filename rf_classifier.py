import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score

FEATURES_FOR_CONVERSION = ["Year_1_Grades", "Year_2_Grades", "Year_3_Grades",
                           "Year_1_Absences", "Year_2_Absences", "Year_3_Absences",
                           "Year_1_Late_HW", "Year_2_Late_HW", "Year_3_Late_HW",
                           "Year_1_Participation", "Year_2_Participation", "Year_3_Participation"]


def float_features(df_row):
    # Convert grades string to list of grades
    year_1_grades_list = [float(x) for x in df_row["Year_1_Grades"].split(", ")]
    year_2_grades_list = [float(x) for x in df_row["Year_2_Grades"].split(", ")]
    year_3_grades_list = [float(x) for x in df_row["Year_3_Grades"].split(", ")]
    year_4_grades_list = [float(x) for x in df_row["Year_4_Grades"].split(", ")]

    # Make grades lists
    df_row["Year_1_Grades"] = year_1_grades_list
    df_row["Year_2_Grades"] = year_2_grades_list
    df_row["Year_3_Grades"] = year_3_grades_list
    df_row["Year_4_Grades"] = year_4_grades_list

    # Float necessary features
    for i in range(1,5):
        df_row[f"Year_{i}_Participation"] = float(df_row[f"Year_{i}_Participation"])
        df_row[f"Year_{i}_Late_HW"] = float(df_row[f"Year_{i}_Late_HW"])
        df_row[f"Year_{i}_Absences"] = float(df_row[f"Year_{i}_Absences"])

    return df_row


def separate_lists(df_row):
    for i in range(1, 5):
        for j in range(7):
            df_row[f"Y{i}G{j}"] = df_row[f"Year_{i}_Grades"][j]

    return df_row


def find_average_grades(df_row):
    total = 0
    for i in range(1, 5):
        for grade in df_row[f"Year_{i}_Grades"]:
            total = total + grade
        df_row[f"Average_grade_year_{i}"] = total / 7
        total = 0

    return df_row


def rf_classifier_access(minimum_passing_grade, choice):
    data = pd.read_csv("students.csv")

    # Float all the values in the dataframe
    data = data.apply(float_features, axis=1)

    # Add a column for each value in the grade list for each year
    data = data.apply(separate_lists, axis=1)

    features = data[["Y1G0", "Y1G1", "Y1G2", "Y1G3", "Y1G4", "Y1G5", "Y1G6",
                     "Y2G0", "Y2G1", "Y2G2", "Y2G3", "Y2G4", "Y2G5", "Y2G6",
                     "Y3G0", "Y3G1", "Y3G2", "Y3G3", "Y3G4", "Y3G5", "Y3G6",
                     "Year_1_Absences", "Year_2_Absences", "Year_3_Absences",
                     "Year_1_Late_HW", "Year_2_Late_HW", "Year_3_Late_HW",
                     "Year_1_Participation", "Year_2_Participation", "Year_3_Participation"]]

    data = data.apply(find_average_grades, axis=1)

    # Get third year cumulative average grade
    data["cumulative_average_year_4"] = (
        data["Average_grade_year_1"] +
        data["Average_grade_year_2"] +
        data["Average_grade_year_3"] +
        data["Average_grade_year_4"]
    ) / 4

    # If cumulative average for year 4 is less than 70 mark with 1 for fail 0 for pass
    data["Pass_Fail_Year_4"] = (data["cumulative_average_year_4"] < int(minimum_passing_grade)).astype(int)

    target = data["Pass_Fail_Year_4"]

    # Split data for training and testing.
    X_train, X_test, Y_train, Y_test, IDS_Train, IDS_Test = (
        train_test_split(features, target, data["Student_id"], test_size=0.2, random_state=42))

    model = RandomForestClassifier(n_estimators=100, random_state=42)

    model.fit(X_train, Y_train)

    prediction = model.predict(X_test)

    results = pd.DataFrame({
        "Student ID": IDS_Test,
        # This value can be used to determine the validity of the prediction.
        # Not necessary with the gui version of the program
        # "True Label": Y_test,
        "Prediction Label": prediction,
    })

    students_to_check = results[results["Prediction Label"] == 1]

    if int(choice) == 1:
        print("These are the students at risk of failure:")
        print(students_to_check)
    else:
        accuracy = accuracy_score(Y_test, prediction)
        precision = precision_score(Y_test, prediction)
        recall = recall_score(Y_test, prediction)

        print(f"Accuracy: {accuracy}")
        print(f"Precision: {precision}")
        print(f"Recall: {recall}")
