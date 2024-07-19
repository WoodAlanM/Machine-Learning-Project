import pandas as pd
import statistics as stat
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

import seaborn

data = pd.read_csv('students.csv')

print(data.head())

averages_df = pd.DataFrame(columns=["Average_Grade", "Average_Absences", "Average_Late_HW", "Average_Participation"])


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

    ax.set_xlabel("Average Grade")
    ax.set_ylabel("Average Absences")
    ax.set_zlabel("Average Late Homework")
    ax.legend()

    plt.show()


def perform_kmeans_2d(list_of_features):
    features = averages_df[list_of_features]

    selected_columns = averages_df[list_of_features]

    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(selected_columns)

    optimal_clusters = 4

    kmeans = KMeans(n_clusters=optimal_clusters, random_state=42)
    kmeans.fit(scaled_features)

    selected_columns["Cluster"] = kmeans.labels_

    #cluster_mean = selected_columns.groupby("Cluster").mean()

    seaborn.pairplot(selected_columns, hue="Cluster", palette="tab10")
    plt.show()


def get_averages():
    for i in range(1, 1001):
        year_1_grades_string = data.at[i - 1, "Year_1_Grades"]
        year_2_grades_string = data.at[i - 1, "Year_2_Grades"]
        year_3_grades_string = data.at[i - 1, "Year_3_Grades"]
        year_4_grades_string = data.at[i - 1, "Year_4_Grades"]

        year_1_grades_list = year_1_grades_string.split(", ")
        year_2_grades_list = year_1_grades_string.split(", ")
        year_3_grades_list = year_1_grades_string.split(", ")
        year_4_grades_list = year_1_grades_string.split(", ")

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
    # perform_k_means_3d(["Average_Grade", "Average_Absences", "Average_Late_HW"])
    perform_kmeans_2d(["Average_Grade", "Average_Absences"])
