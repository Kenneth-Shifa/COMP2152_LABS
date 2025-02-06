#Author: Kenneth Shifa
#Assignment: #1


# Defining variables with data type comments
gym_member = "Alex Alliton"  # Name of the gym member (string)
preferred_weight_kg = 20.5  # Preferred weight (float)
highest_reps = 25   # Highest number of reps performed (integer)
membership_active = True  # Membership status (boolean)

# Creating a dictionary with workout stats
# Data type: dict[str, tuple[int, int, int]]
workout_stats = {
    "Sara": (65, 60, 70),  # Yoga, Running, Weightlifting
    "Ana": (60, 35, 25),
    "Ashley": (20, 50, 35),
    "Rami": (15, 30, 45)
}

# Calculate total workout minutes separately for each friend
totals = {f"{friend}_Total": sum(times) for friend, times in workout_stats.items()}

# Update the dictionary after iteration
workout_stats.update(totals)

# Convert workout data into a 2D list where each row is a friend's workout details
workout_list = [list(times) for friend, times in workout_stats.items() if "_Total" not in friend]

# Extract minutes spent on Yoga & Running for all friends
yoga_and_running = [row[:2] for row in workout_list]
# Extract minutes spent on Weightlifting for the last two friends
weightlifting_last_two = [row[2] for row in workout_list[-2:]]

# Display sliced workout data
print("Yoga and Running Minutes:", yoga_and_running)
print("Weightlifting for Last Two Friends:", weightlifting_last_two)

# Check for friends who worked out for 120 minutes or more
for friend, total in totals.items():
    if total >= 120:
        print(f"Great job staying active, {friend.replace('_Total', '')}!")

# User input to check workout details of specific friend
friend_name = input("Enter a friend's name: ")
if friend_name in workout_stats and isinstance(workout_stats[friend_name], tuple):
    activities = workout_stats[friend_name]
    total = workout_stats.get(f"{friend_name}_Total", 0)
    print(
        f"{friend_name}'s workout stats: Yoga={activities[0]}, Running={activities[1]}, Weightlifting={activities[2]}, Total={total}"
    )
else:
    print(f"Friend {friend_name} not found in the records.")

# Finding the friend with highest and lowest total workout minutes
max_friend = max(totals, key=totals.get).replace("_Total", "")
min_friend = min(totals, key=totals.get).replace("_Total", "")

# Display the result of most and least active friend
print(f"Highest Total Workout: {max_friend} with {totals[max_friend + '_Total']} minutes")
print(f"Lowest Total Workout: {min_friend} with {totals[min_friend + '_Total']} minutes")
