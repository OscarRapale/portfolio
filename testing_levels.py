import json

class User:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.current_xp = 0
        self.xp_to_next_level = 100
        self.tasks_completed = 0
        self.load_data()  # Load user data from JSON file if it exists

    def gain_xp(self, amount):
        self.current_xp += amount
        print(f"{self.name} gained {amount} XP.")
        self.check_level_up()  # Check if the user has enough XP to level up
        self.save_data()  # Save user data to JSON file

    def check_level_up(self):
        while self.current_xp >= self.xp_to_next_level:
            self.level_up()  # Level up the user if they have enough XP

    def level_up(self):
        self.current_xp -= self.xp_to_next_level
        self.level += 1
        self.xp_to_next_level = self.calculate_xp_for_next_level()  # Calculate XP needed for the next level
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"XP needed for next level: {self.xp_to_next_level}\n")

    def calculate_xp_for_next_level(self):
        return 100 + (self.level - 1) * 50  # XP needed increases with each level

    # Just for testing purposes only, will be replaced by database
    def save_data(self):
        data = {
            'name': self.name,
            'level': self.level,
            'current_xp': self.current_xp,
            'xp_to_next_level': self.xp_to_next_level,
            'tasks_completed': self.tasks_completed
        }
        with open(f'{self.name}_data.json', 'w') as f:
            json.dump(data, f)  # Save user data to a JSON file

    # Just for testing purposes only, will be replaced by database
    def load_data(self):
        try:
            with open(f'{self.name}_data.json', 'r') as f:
                data = json.load(f)
                self.level = data['level']
                self.current_xp = data['current_xp']
                self.xp_to_next_level = data['xp_to_next_level']
                self.tasks_completed = data.get('tasks_completed', 0)  # Use default value if key is missing
        except FileNotFoundError:
            pass  # If the file doesn't exist, do nothing


class Task:
    def __init__(self, description, xp_reward):
        self.description = description
        self.xp_reward = xp_reward
        self.completed = False

    def complete_task(self, user):
        if not self.completed:
            user.gain_xp(self.xp_reward)  # User gains XP for completing the task
            self.completed = True
            user.tasks_completed += 1
            print(f"Task '{self.description}' completed!\n")
        else:
            print(f"Task '{self.description}' has already been completed.")


# Create user
user = User("User1")


# Print current XP and level of the user
current_xp = user.current_xp
current_level = user.level

#print(f"{user.name} currently has {current_xp} XP.")
#print(f"{user.name} is level {current_level}")

# Create a list of tasks
tasks = [
    Task("Clean room", 100),
    Task("Cook", 20)
]

# Complete tasks for the first user
tasks[0].complete_task(user)
tasks[1].complete_task(user)

print(user.tasks_completed)
