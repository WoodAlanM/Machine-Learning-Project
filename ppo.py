import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import OneHotEncoder
import statistics as stat
from ppo_environment import StudentPerformanceEnv
from stable_baselines3 import PPO
from class_category_mapper import map_to_class_category

data = pd.read_csv("students.csv")

# Convert class string into class list
for year in range(1, 5):
    classes_column = f"Year_{year}_Classes"
    data[f"Year_{year}_Classes_List"] = data[classes_column].apply(lambda x: x.split(', '))

for year in range(1, 5):
    grades_column = f"Year_{year}_Grades"
    data[f"Year_{year}_Grades_List"] = data[grades_column].apply(lambda x: list(map(float, x.split(', '))))

outside_features = ["Age_at_year_4", "Year_1_Absences", "Year_2_Absences", "Year_3_Absences", "Year_4_Absences",
                    "Year_1_Late_HW", "Year_2_Late_HW", "Year_3_Late_HW", "Year_4_Late_HW", "Year_1_Participation",
                    "Year_2_Participation", "Year_3_Participation", "Year_4_Participation"]




print("1")

# Get all years average
for year in range(1, 5):
    column_name = f"Year_{year}_Grades_List"
    data[f"Average_grade_year_{year}"] = data[column_name].apply(
        lambda grades: stat.mean(grades) if grades else float('nan')
    )

print("2")

# Get third year cumulative average grade
data["cumulative_average_year_3"] = (
    data["Average_grade_year_1"] +
    data["Average_grade_year_2"] +
    data["Average_grade_year_3"]
) / 3


data["possible_failing_student"] = (data["cumulative_average_year_3"] < 70).astype(int)

encoder = OneHotEncoder(handle_unknown="ignore")

class_features = []
for year in range(1, 5):
    classes_column = f"Year_{year}_Classes_List"
    class_data = data[classes_column].apply(lambda x: x if isinstance(x, list) else []).tolist()
    encoded_classes = encoder.fit_transform(class_data)
    class_features.extend(encoded_classes.T)

data[outside_features] = StandardScaler().fit_transform(data[outside_features])

features = pd.concat([
    pd.DataFrame(class_features, index=data.index),
    data[outside_features].reset_index(drop=True)
], axis=1)

target = data["possible_failing_student"]

env = StudentPerformanceEnv(features, target)

model = PPO("MlpPolicy", env, verbose=1)

model.learn(total_timesteps=10000)

model.save("ppo_student_performance")

obs = env.reset()
