import pandas as pd
from visualization import average_marks_chart, grade_distribution

df = pd.read_csv("data/students.csv")

def assign_grade(avg):

    if avg >= 90:
        return "A+"

    elif avg >= 80:
        return "A"

    elif avg >= 70:
        return "B"

    elif avg >= 60:
        return "C"

    else:
        return "D"

df["Total"] = df["Math"] + df["Science"] + df["English"]

df["Average"] = df["Total"] / 3

df["Grade"] = df["Average"].apply(assign_grade)

print(df)

top_student = df.sort_values(
    by="Average",
    ascending=False
)

print("\nTop 3 Students:")
print(top_student.head(3))

print("\nMath Statistics")
subjects = ["Math", "Science", "English"]

for subject in subjects:

    print(f"\n{subject} Statistics")

    print("Highest:", df[subject].max())
    print("Lowest:", df[subject].min())
    print("Average:", round(df[subject].mean(), 2))

average_marks_chart(df)
grade_distribution(df)