# ========================================
#        PERSONAL GROWTH TRACKER
# ========================================

# Welcome, Yahya!

# 1. Add Habit
# 2. View Habits
# 3. Complete Habit
# 4. View Today's Progress
# 5. View Statistics
# 6. Search / Filter Habits
# 7. Generate Report
# 8. Exit

# Enter your choice:

def habits_display ():
    print()
    print('========HABIT TRACKER========')
    print()
    count = 1
    for habit in habits:
        print(f'{count} . {habit}')
        count +=1
    print()


habits = ['Workout','Meditation','Prayer','Quran','Reading','Writing','Walking','English']


while True:
    print("""
    1. Add Habit
    2. View Habits
    3. Complete Habit
    4. View Today's Progress
    5. View Statistics
    6. Search / Filter Habits
    7. Generate Report
    8. Exit
    """)

    choice = int(input('Enter Your Choice : '))

    if choice == 1:
        habits_display ()
        new_habit = input('Enter the habit to be added :')
        habits.append(new_habit)

        print('Here is your updated Habit Tracker :')
        habits_display ()
    if choice == 2 :
        habits_display ()

    if choice == 8 :
        break







