class Exercise:
    def __init__(self, topic, course_name, link, problems):
        self.topic = topic
        self.course_name = course_name
        self.link = link
        self.problems = problems


data = input()

list_exercises = []

while data != "go go go":
    split_data = data.split(" -> ")
    topic = split_data[0]
    course_name = split_data[1]
    link = split_data[2]
    problems = split_data[3].split(", ")

    exercise = Exercise(topic, course_name, link, problems)
    list_exercises.append(exercise)

    data = input()

for e in list_exercises:
    print(f"Exercises: {e.topic}")
    print(f'Problems for exercises and homework for the \"{e.course_name}\" course @ SoftUni.')
    print(f"Check your solutions here: {e.link}")
    for index in range(0, len(e.problems)):
        print(f" {index+1}. {e.problems[index]}")

