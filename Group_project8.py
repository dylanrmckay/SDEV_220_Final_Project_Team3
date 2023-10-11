import tkinter as tk

questions = [
    "1. I prefer taking art classes. (True/False)",
    "2. I enjoy playing sports. (True/False)",
    "3. I like science and math classes. (True/False)",
    "4. I prefer music or band classes. (True/False)",
    "5. I enjoy drama or theater activities. (True/False)",
    "6. I like history and social studies classes. (True/False)",
    "7. I enjoy joining clubs and organizations. (True/False)",
    "8. Physical education classes are my favorite. (True/False)",
    "9. I like literature and English classes the most. (True/False)",
    "10. I enjoy participating in debate or public speaking. (True/False)",
    "11. I prefer computer science and coding classes. (True/False)",
    "12. I like taking cooking or culinary arts classes. (True/False)",
    "13. I enjoy outdoor activities and nature. (True/False)",
    "14. I prefer foreign language classes. (True/False)",
    "15. I most enjoy volunteering and community service. (True/False)",
    "16. I like mathematics and find it challenging. (True/False)",
    "17. I enjoy being apart of theater productions, it doesn't matter if i am on stage or behind. (True/False)",
    "18. I like history and learning about past civilizations. (True/False)",
    "19. I prefer individual sports such as cycling or martial arts, over team sports. (True/False)",
    "20. I enjoy participating in science experiments. (True/False)",
    "21. I like participating in student government or leadership roles. (True/False)",
    "22. I enjoy reading and analyzing literature. (True/False)",
    "23. I prefer learning and speaking multiple languages. (True/False)",
    "24. I like participating in environmental or nature-related activities. (True/False)",
    "25. I enjoy programming and coding as a hobby. (True/False)"
]

preferences = {
    "Art": 0,
    "Sports": 0,
    "Music/Band": 0,
    "Physical Education": 0,
    "Debate/Public Speaking": 0,
    "Computer Science/Coding": 0,
    "Cooking/Culinary Arts": 0,
    "Volunteering/Community Service": 0,
    "Mathematics": 0,
    "Drama/Theater": 0,
    "History/Social Studies": 0,
    "Individual Sports": 0,
    "Science/Math": 0,
    "Clubs/Organizations": 0,
    "Literature/English": 0,
    "Foreign Language": 0,
    "Outdoor Activities": 0,
}

current_question = 0


def handle_answer():
    user_answer = answer_var.get()
    if current_question < len(preferences):
        category = list(preferences.keys())[current_question]
        if user_answer == 1:
            preferences[category] += 1
        next_question()
    else:
        show_results()

def next_question():
    global current_question
    if current_question < len(questions) - 1:
        current_question += 1
        question_label.config(text=questions[current_question])
        answer_var.set(-1)
    else:
        show_results()


def show_results():
    result_window = tk.Toplevel(root)
    result_window.title("Survey Results")

    result_label = tk.Label(result_window, text="Your class and extracurricular activity preferences are as follows:")
    result_label.pack()

    for category, count in preferences.items():
        category_label = tk.Label(result_window, text=f"{category}: {count} preferences")
        category_label.pack()

    dominant_label = tk.Label(result_window,
                              text=f"Your dominant preference is for {max(preferences, key=preferences.get)}.")
    dominant_label.pack()


root = tk.Tk()
root.title("Preference Survey")

question_label = tk.Label(root, text=questions[0])
question_label.pack()

answer_var = tk.IntVar()
true_radio = tk.Radiobutton(root, text="True", variable=answer_var, value=1)
true_radio.pack()
false_radio = tk.Radiobutton(root, text="False", variable=answer_var, value=0)
false_radio.pack()

next_button = tk.Button(root, text="Next", command=handle_answer)
next_button.pack()

root.mainloop()
