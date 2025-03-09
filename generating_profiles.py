import pandas as pd
import random

eye_colors = ["Brown", "Blue", "Green", "Yellow", "Hasel", "Gray", "Other"]
skin_colors = ["Brown", "Black", "Beige", "Tanned", "White", "Other"]
ethnicities = ["English", "American", "Arab", "Asian", "Middle Eastern", "Caucasian", "African", "African American", "Hispanic", "Indigenous", "Other"]
religions = ["Christian", "Hindu", "Muslim", "Sikh", "Atheist", "Agnostic", "Buddhist", "Jewish", "Other"]
sexualities = ["Male", "Female", "Other"]
locations = ["America", "Europe", "Asia", "Africa", "Australia", "Other"]
body_types = ["Fat", "Fit", "Slim", "Obese", "Skinny", "Other"]
languages_spoken = ["English", "French", "Arabic", "Mandarin", "Russian"]
education_levels = ["High School Diploma", "University", "College", "Other"]
smoker_status = ["Yes", "No"]
drinker_status = ["Yes", "No"]

users = []
for i in range(1000):
    user = {
        "User ID": i + 1,
        "Eye Color": random.choice(eye_colors),
        "Height": round(random.uniform(4.5, 6.5), 1), 
        "Skin Color": random.choice(skin_colors),
        "Ethnicity": random.choice(ethnicities),
        "Religion": random.choice(religions),
        "Sexuality": random.choice(sexualities),
        "Location": random.choice(locations),
        "Body Type": random.choice(body_types),
        "Primary Language": random.choice(languages_spoken),
        "Education Level": random.choice(education_levels),
        "Income": random.randint(40000, 400000),
        "Smoker": random.choice(smoker_status),
        "Drinker": random.choice(drinker_status),
    }
    users.append(user)

df = pd.DataFrame(users)

file_path = "dating_profiles_updated.csv"
df.to_csv(file_path, index=False)


