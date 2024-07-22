import pandas as pd
import statistics as stat
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn
from rf_classifier import rf_classifier_access

# Read in the students csv file
data = pd.read_csv('students.csv')

averages_df = pd.DataFrame(columns=["Average_Grade", "Average_Absences", "Average_Late_HW", "Average_Participation"])

# Copy the dataframe for another use
df_for_searching = data.copy()

# Convert the student ids to strings
df_for_searching["Student_id"] = df_for_searching["Student_id"].astype(str)

# Sets the column width to unlimited for late student data display.
pd.set_option("display.max_colwidth", None)


def main_gui_loop():
    while True:
        print("-----------------------------------------------------------------")
        print("--------------- Student Failure Risk Determinator ---------------")
        print("-----------------------------------------------------------------\n")

        print("Select from the following:\n")
        print("1. Make plots")
        print("2. Predict student failure")
        print("3. Look at student data")
        print("4. Exit\n")

        selection_top_menu = input("Please make a selection (1-3): ")

        # Start top menu selection
        # Top menu selection 1
        if int(selection_top_menu) == 1:
            while True:
                print("\n")
                print("What type of plot would you like to make?")
                print("1. 3D Plot")
                print("2. 2D Plot")
                print("3. Back to main menu.\n")

                secondary_menu_1 = input("Please make a selection (1-3): ")
                # Secondary menu 3D plot
                if int(secondary_menu_1) == 1:
                    while True:
                        print("\n")
                        print("The following can be used to develop 3D plots:")
                        print("1. Average Grades")
                        print("2. Average Absences")
                        print("3. Average Late Homeworks")
                        print("4. Average Participation\n")

                        tertiary_menu_1 = input("Please select three values separated"
                                                " by a space (ie. 1 2 3) or 0 to exit: ")

                        values = tertiary_menu_1.split()
                        if len(values) == 1:
                            if int(values[0]) == 0:
                                break
                        elif len(values) != 3:
                            print("Error: Please enter only three values.")
                        else:
                            count = 0
                            for value in values:
                                if int(value) == 1:
                                    values[count] = "Average_Grade"
                                elif int(value) == 2:
                                    values[count] = "Average_Absences"
                                elif int(value) == 3:
                                    values[count] = "Average_Late_HW"
                                elif int(value) == 4:
                                    values[count] = "Average_Participation"
                                count = count + 1
                            perform_k_means_3d(values)
                            print("\n")
                            continue
                # Secondary menu 2D Plot
                if int(secondary_menu_1) == 2:
                    while True:
                        print("\n")
                        print("The following can be used to develop 2D plots:")
                        print("1. Average Grades")
                        print("2. Average Absences")
                        print("3. Average Late Homeworks")
                        print("4. Average Participation\n")

                        tertiary_menu_1 = input("Please select two values separated"
                                                " by a space (ie. 1 2) or 0 to exit: ")

                        values = tertiary_menu_1.split()
                        if len(values) == 1:
                            if int(values[0]) == 0:
                                break
                        elif len(values) != 2:
                            print("Error: Please enter only three values.")
                        else:
                            count = 0
                            for value in values:
                                if int(value) == 1:
                                    values[count] = "Average_Grade"
                                elif int(value) == 2:
                                    values[count] = "Average_Absences"
                                elif int(value) == 3:
                                    values[count] = "Average_Late_HW"
                                elif int(value) == 4:
                                    values[count] = "Average_Participation"
                                count = count + 1
                            perform_kmeans_2d(values)
                            print("\n")
                            continue
                # Secondary menu exit to main menu
                if int(secondary_menu_1) == 3:
                    break
                # End secondary menu 1

        # Top menu selection 2
        elif int(selection_top_menu) == 2:
            while True:
                print("\n")
                print("Please choose from the following:")
                print("1. Predict from data set")
                print("2. Show prediction stats")
                print("3. Back to main menu")

                secondary_menu_2 = input("Please make a selection (1-3): ")

                if int(secondary_menu_2) == 1:
                    print("\n")
                    minimum_grade = input("Please enter a minimum passing grade: ")
                    print("\n")
                    rf_classifier_access(minimum_grade, 1)
                    print("\n")

                    continue
                elif int(secondary_menu_2) == 2:
                    print("\n")
                    print("Loading prediction stats based on the "
                          "given dataset and a minimum passing grade of 70...")
                    print("\n")
                    rf_classifier_access(70, 2)
                    print("\n")
                    continue
                elif int(secondary_menu_2) == 3:
                    break
                # End secondary menu 2
        # Top menu selection 3
        elif int(selection_top_menu) == 3:
            print("\n")
            secondary_menu_3 = input("Please enter a list of student id's separated by a space "
                                     "or 0 to return to the main menu: ")

            student_ids = secondary_menu_3.split()

            if len(student_ids) == 1:
                if student_ids[0] == "0":
                    continue
                else:
                    student_data = df_for_searching[df_for_searching["Student_id"] == student_ids[0]]
                    print("\n")
                    display_student_data(student_data)
                    print("\n")
            else:
                for an_id in student_ids:
                    student_data = df_for_searching[df_for_searching["Student_id"] == an_id]
                    print("\n")
                    display_student_data(student_data)
                    print("\n")
        # Top menu selection 4
        elif int(selection_top_menu) == 4:
            break
        # End top menu selection


# This function displays student data for a specific student in the dataframe
def display_student_data(student):
    print(f"Student ID: {student["Student_id"].to_string(index=False)} "
          f"Student Age: {student["Age_at_year_4"].to_string(index=False)}")
    print("---------------------------------------------------------")
    print(f"Freshman courses: {student["Year_1_Classes"].to_string(index=False)}")
    print(f"Sophomore courses: {student["Year_2_Classes"].to_string(index=False)}")
    print(f"Junior courses: {student["Year_3_Classes"].to_string(index=False)}")
    print(f"Senior courses: {student["Year_4_Classes"].to_string(index=False)}")
    print("---------------------------------------------------------")
    print(f"Freshman grades: {student["Year_1_Grades"].to_string(index=False)}")
    print(f"Sophomore grades: {student["Year_2_Grades"].to_string(index=False)}")
    print(f"Junior grades: {student["Year_3_Grades"].to_string(index=False)}")
    print(f"Senior grades: {student["Year_4_Grades"].to_string(index=False)}")
    print("---------------------------------------------------------")
    print(f"Absences - Freshman: {student["Year_1_Absences"].to_string(index=False)}, "
          f"Sophomore: {student["Year_2_Absences"].to_string(index=False)}, "
          f"Junior: {student["Year_3_Absences"].to_string(index=False)}, "
          f"Senior: {student["Year_4_Absences"].to_string(index=False)}")
    print("---------------------------------------------------------")
    print(f"Late homework - Freshman: {student["Year_1_Late_HW"].to_string(index=False)}, "
          f"Sophomore: {student["Year_2_Late_HW"].to_string(index=False)}, "
          f"Junior: {student["Year_3_Late_HW"].to_string(index=False)}, "
          f"Senior: {student["Year_4_Late_HW"].to_string(index=False)}")
    print("---------------------------------------------------------")
    print(f"Participation - Freshman: {student["Year_1_Participation"].to_string(index=False)}, "
          f"Sophomore: {student["Year_2_Participation"].to_string(index=False)}, "
          f"Junior: {student["Year_3_Participation"].to_string(index=False)}, "
          f"Senior: {student["Year_4_Participation"].to_string(index=False)}")
    print("---------------------------------------------------------")


# This function develops a graph which is used to determine
# the number of clusters to use when performing k-means clustering
# This is held here in case there are significant changes later
def perform_elbow(features):
    sse = []
    k_range = range(1, 11)

    for k in k_range:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(features)
        sse.append(kmeans.inertia_)

    plt.figure(figsize=(10, 6))
    plt.plot(k_range, sse, marker='o')
    plt.xlabel("Number of Clusters")
    plt.ylabel("Sum of Square Errors (SSE)")
    plt.show()


# This function develops a 3d plot based on a list of features
# sent to the function.
def perform_k_means_3d(list_of_features):
    features = averages_df[list_of_features]

    # perform_elbow(features)
    # The elbow method seemed to establish that 4 clusters is the optimal number

    optimal_clusters = 4

    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(averages_df)

    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
    averages_df["Cluster"] = kmeans.fit_predict(scaled_data)

    fig = plt.figure(figsize=(10, 7))
    ax = fig.add_subplot(111, projection="3d")

    for cluster in range(optimal_clusters):
        cluster_data = averages_df[averages_df["Cluster"] == cluster]
        ax.scatter(cluster_data[list_of_features[0]], cluster_data[list_of_features[1]],
                   cluster_data[list_of_features[2]], label=f"Cluster {cluster}")

    ax.set_xlabel(list_of_features[0])
    ax.set_ylabel(list_of_features[1])
    ax.set_zlabel(list_of_features[2])
    ax.legend()

    plt.show()


# This function develops a 2d plot based on a list of features
# passed to the function
def perform_kmeans_2d(list_of_features):
    features = averages_df[list_of_features]

    selected_columns = averages_df[list_of_features].copy()

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(selected_columns)

    optimal_clusters = 4

    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
    kmeans.fit(scaled_features)

    selected_columns["Cluster"] = kmeans.labels_

    seaborn.pairplot(selected_columns, hue="Cluster", palette="tab10")
    plt.show()


# This function develops the average grades for each year
# as well as converting the absences, participation, and late
# homeworks to integer values for later use by plotting functions
def get_averages():
    for i in range(1, 1001):
        year_1_grades_string = data.at[i - 1, "Year_1_Grades"]
        year_2_grades_string = data.at[i - 1, "Year_2_Grades"]
        year_3_grades_string = data.at[i - 1, "Year_3_Grades"]
        year_4_grades_string = data.at[i - 1, "Year_4_Grades"]

        year_1_grades_list = year_1_grades_string.split(", ")
        year_2_grades_list = year_2_grades_string.split(", ")
        year_3_grades_list = year_3_grades_string.split(", ")
        year_4_grades_list = year_4_grades_string.split(", ")

        for j in range(7):
            year_1_grades_list[j] = float(year_1_grades_list[j])
            year_2_grades_list[j] = float(year_2_grades_list[j])
            year_3_grades_list[j] = float(year_3_grades_list[j])
            year_4_grades_list[j] = float(year_4_grades_list[j])

        # Get average grade for the student overall
        average_grade = (
                (stat.mean(year_1_grades_list)
                 + stat.mean(year_2_grades_list)
                 + stat.mean(year_3_grades_list)
                 + stat.mean(year_4_grades_list)) / 4
        )

        year_1_absences = int(data.at[i - 1, "Year_1_Absences"])
        year_2_absences = int(data.at[i - 1, "Year_2_Absences"])
        year_3_absences = int(data.at[i - 1, "Year_3_Absences"])
        year_4_absences = int(data.at[i - 1, "Year_4_Absences"])

        # Get average absences for each student
        average_absences = (
                (year_1_absences +
                 year_2_absences +
                 year_3_absences +
                 year_4_absences) / 4
        )

        year_1_late_hw = int(data.at[i - 1, "Year_1_Late_HW"])
        year_2_late_hw = int(data.at[i - 1, "Year_2_Late_HW"])
        year_3_late_hw = int(data.at[i - 1, "Year_3_Late_HW"])
        year_4_late_hw = int(data.at[i - 1, "Year_4_Late_HW"])

        # Get average late hw
        average_late_hw = (
            (year_1_late_hw +
             year_2_late_hw +
             year_3_late_hw +
             year_4_late_hw) / 4
        )

        year_1_participation = int(data.at[i - 1, "Year_1_Participation"])
        year_2_participation = int(data.at[i - 1, "Year_2_Participation"])
        year_3_participation = int(data.at[i - 1, "Year_3_Participation"])
        year_4_participation = int(data.at[i - 1, "Year_4_Participation"])

        average_participation = (
            (year_1_participation +
             year_2_participation +
             year_3_participation +
             year_4_participation) / 4
        )

        averages_row = {
            "Average_Grade": average_grade,
            "Average_Absences": average_absences,
            "Average_Late_HW": average_late_hw,
            "Average_Participation": average_participation
        }

        averages_df.loc[i - 1] = averages_row


if __name__ == "__main__":
    get_averages()
    main_gui_loop()
