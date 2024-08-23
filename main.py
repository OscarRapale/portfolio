
class User:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.current_xp = 0
        self.xp_to_next_level = 100
        self.tasks_completed = 0

    def gain_xp(self, amount):
        self.current_xp += amount
        print(f"{self.name} gained {amount} XP.")
        self.check_level_up()  # Check if the user has enough XP to level up

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


class Task:
    def __init__(self, description, exp_reward):
        self.description = description
        self.exp_reward = exp_reward
        self.completed = False

    def complete_task(self, user):
        if not self.completed:
            user.gain_xp(self.exp_reward)  # User gains XP for completing the task
            self.completed = True
            print(f"Task '{self.description}' completed!\n")
        else:
            print(f"Task '{self.description}' has already been completed.")


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