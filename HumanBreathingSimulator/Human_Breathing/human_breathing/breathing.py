# breathing.py

# Calculates the ideal body weight (IBW) based on height and sex.
# The formula uses inches for height and returns IBW in pounds.
def ideal_body_weight(height_inches, sex):
    if sex.lower() == 'male':
        ibw = 50 + 2.3 * (height_inches - 60)
    elif sex.lower() == 'female':
        ibw = 45.5 + 2.3 * (height_inches - 60)
    else:
        raise ValueError("Sex must be 'male' or 'female'")
    return ibw

# Calculates tidal volume (mL) based on ideal body weight (pounds).
# It uses an approximate constant of 5 mL per pound of IBW.
def tidal_volume(ibw):
    return ibw * 7

# Calculates minute ventilation (mL/min) using tidal volume (mL) and
# respiratory rate (breaths per minute).
def minute_ventilation(tidal_volume, respiratory_rate):
    return tidal_volume * respiratory_rate

# Class for simulating human breathing based on input parameters.
class BreathingSimulation:
    def __init__(self, height_inches, age, sex, respiratory_rate):
        self.height_inches = height_inches
        self.sex = sex
        self.respiratory_rate = respiratory_rate
        self.ideal_body_weight = self.calculate_ideal_body_weight()
        self.user_tidal_volume = self.calculate_tidal_volume()
        self.user_minute_ventilation = self.calculate_user_minute_ventilation()

    def calculate_ideal_body_weight(self):
        if self.sex == "male":
            ibw = 50 + 2.3 * (self.height_inches - 60)
        else:
            ibw = 45.5 + 2.3 * (self.height_inches - 60)

        print(f"")
        print(f"Begin Ideal Body Weight Calculation...")
        print("ibw = 50 kg + 2.3 * (height_inches - 60)" if self.sex == "male" else "ibw = 45.5 + 2.3 * (height_inches - 60)")
        print(f"ibw = 50 kg + 2.3 * ({self.height_inches} - 60)" if self.sex == "male" else f"ibw = 45.5 + 2.3 * ({self.height_inches} - 60)")
        print(f"ibw = 50 kg + 2.3 * {self.height_inches - 60}" if self.sex == "male" else f"ibw = 45.5 + 2.3 * {self.height_inches - 60}")
        print(f"ibw = 50 kg + {2.3 * (self.height_inches - 60):.1f}" if self.sex == "male" else f"ibw = 45.5 + {2.3 * (self.height_inches - 60):.1f}")
        print(f"ibw = {ibw:.1f} kg")
        print(f"Ideal Body Weight Calculation Completed.")
        print(f"")

        return ibw

    def calculate_tidal_volume(self):
        tidal_volume = self.ideal_body_weight * 7

        print("")
        print("Apply the Ideal Body Weight to the NBRC Recommended")
        print("Tidal Volume per Kilogram dosing schedule.")
        print("")
        print("Beginning Calculation with 7 mL/kg...")
        print("vt = ibw * 7 mL/kg")
        print(f"vt = {self.ideal_body_weight:.1f} kg * 7 mL/kg")
        print(f"vt = {tidal_volume:.1f} mL/breath")
        print("Calculation Completed.")
        print("")


        return tidal_volume

    def calculate_user_minute_ventilation(self):
        user_minute_ventilation = self.respiratory_rate * self.user_tidal_volume
        
        print("")
        print("Calculate a Minute Ventilation assuming a fixed volume at 7 mL/kg")
        print("with the Ideal Body Weight")
        print("")
        print("Calculating...")
        print("ve = respiratory_rate * user_tidal_volume")
        print(f"ve = {self.respiratory_rate} breaths per minute * {self.user_tidal_volume:.1f} mL/breath")
        print(f"ve = {user_minute_ventilation / 1000:.1f} L/min")
        print("Calculation Complete.")
        print("")


        return user_minute_ventilation

    def calculate_normal_minute_ventilation(self):
        normal_minute_ventilation_low = self.ideal_body_weight * 6 * 12
        normal_minute_ventilation_high = self.ideal_body_weight * 8 * 20
        print("")
        print("Calculate the absolute minimum and maximum safe minute ventilation according to")
        print("NBRC Recommended Tidal Volume per Kilogram dosing schedule if assuming a Respiratory")
        print("Rate of 12 at 6 mL/kg and a Respiratory Rate of 20 at 8 mL/kg.")
        print("")
        print("Calculating Low End...")
        print("ve low normal = ideal_body_weight * 6 ml/kg  * 12")
        print(f"ve low normal = {self.ideal_body_weight:.1f} kg * 6 ml/kg  * 12 breaths per minute")
        print(f"ve low normal = {normal_minute_ventilation_low:.0f} mL/min")
        print("Calculation Completed.")
        print("")
        print("Calculating High End...")
        print("ve high normal = ideal_body_weight * 8 ml/kg * 20")
        print(f"ve high normal = {self.ideal_body_weight:.1f} kg * 8 ml/kg  * 20 breaths per minute")
        print(f"ve high normal = {normal_minute_ventilation_high:.0f} mL/min")
        print("Calculation Completed.")
        print("")
        print("Converting the Minute Ventilation Ranges given a Specified Respiratory Rate, Sex, Height, and mL/kg into Liters...")
        print(f"ve low normal = {normal_minute_ventilation_low:.1f} mL/min / 1000")
        print(f"ve low normal = {normal_minute_ventilation_low / 1000:.2f} L/min")
        print(f"ve high normal = {normal_minute_ventilation_high:.1f} mL/min / 1000")
        print(f"ve high normal = {normal_minute_ventilation_high / 1000:.2f} L/min")
        print("Conversion Completed.")
        print("")
        print("Compiling Normal Minute Ventilation Range given the above")
        print(f"Normal Minute Ventilation Range: {normal_minute_ventilation_low / 1000:.2f}-{normal_minute_ventilation_high / 1000:.2f} L/min")

