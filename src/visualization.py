import matplotlib.pyplot as plt


def average_marks_chart(df):

    subjects = ["Math", "Science", "English"]

    averages = [
        df["Math"].mean(),
        df["Science"].mean(),
        df["English"].mean()
    ]

    plt.figure(figsize=(8,5))

    bars = plt.bar(subjects, averages)

    plt.title("Average Marks by Subject")
    plt.xlabel("Subjects")
    plt.ylabel("Average Marks")

    for bar in bars:

        height = bar.get_height()

        plt.text(
            bar.get_x() + bar.get_width()/2,
            height,
            f"{height:.1f}",
            ha="center"
        )

    plt.savefig("reports/average_marks.png")
    plt.show()


def grade_distribution(df):

    grade_counts = df["Grade"].value_counts()

    plt.figure(figsize=(6,6))

    plt.pie(
        grade_counts,
        labels=grade_counts.index,
        autopct="%1.1f%%"
    )

    plt.title("Grade Distribution")

    plt.savefig("reports/grade_distribution.png")
    plt.show()