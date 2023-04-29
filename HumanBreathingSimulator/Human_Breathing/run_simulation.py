import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))

from human_breathing.breathing import BreathingSimulation

def get_positive_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Please enter a positive number.")
        except ValueError:  
            print("Invalid input. Please enter a number.")

def get_sex(prompt):
    while True:
        sex = input(prompt).lower()
        if sex in ["male", "female"]:
            return sex
        else:
            print("Invalid input. Please enter 'male' or 'female'.")

# Get user input
def main():
    # Prompt user for input
    height = get_positive_float("Enter your height in inches: ")
    age = get_positive_int("Enter your age in years: ")
    sex = get_sex("Enter your sex (male/female): ")
    respiratory_rate = get_positive_int("Enter your respiratory rate (breaths per minute): ")

    # Check for age or height conditions
    if age < 18 or height < 60:
        print("Warning: The results may be incorrect for individuals under 18 years of age or under 60 inches in height.")

    # Create a BreathingSimulation instance with the user's input
    simulation = BreathingSimulation(height, age, sex, respiratory_rate)
    
    # Calculate user's minute ventilation and normal minute ventilation range
    user_mv = simulation.user_minute_ventilation
    normal_mv_range = simulation.calculate_normal_minute_ventilation()

if __name__ == "__main__":
    main()

