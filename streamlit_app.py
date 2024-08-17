import streamlit as st

# Title of the Streamlit app
st.title("Fitness Stretch Recommendation App")

# Description
st.write("This app recommends stretches based on different attributes like muscle group, difficulty, and type.")

# Define the dataset
stretches = [
 # 1-5: Neck and Shoulders
    {
        'name': 'Neck Tilt Stretch',
        'muscle_group': 'Neck',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Shoulder Roll',
        'muscle_group': 'Shoulders',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Mobility'
    },
    {
        'name': 'Upper Trapezius Stretch',
        'muscle_group': 'Trapezius',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Arm Across Chest Stretch',
        'muscle_group': 'Shoulders',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Levator Scapulae Stretch',
        'muscle_group': 'Neck',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },

    # 6-10: Chest and Upper Back
    {
        'name': 'Chest Opener Stretch',
        'muscle_group': 'Chest',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Doorway Pec Stretch',
        'muscle_group': 'Chest',
        'difficulty': 'Medium',
        'equipment': 'Doorframe',
        'type': 'Flexibility'
    },
    {
        'name': 'Thoracic Spine Rotation',
        'muscle_group': 'Upper Back',
        'difficulty': 'Medium',
        'equipment': 'Foam Roller',
        'type': 'Mobility'
    },
    {
        'name': 'Cat-Cow Stretch',
        'muscle_group': 'Spine',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Mobility'
    },
    {
        'name': 'Child’s Pose',
        'muscle_group': 'Upper Back',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },

    # 11-15: Arms and Wrists
    {
        'name': 'Bicep Stretch',
        'muscle_group': 'Biceps',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Tricep Stretch',
        'muscle_group': 'Triceps',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Wrist Flexor Stretch',
        'muscle_group': 'Forearms',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Wrist Extensor Stretch',
        'muscle_group': 'Forearms',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Shoulder Rotator Stretch',
        'muscle_group': 'Shoulders',
        'difficulty': 'Medium',
        'equipment': 'Resistance Band',
        'type': 'Flexibility'
    },

    # 16-20: Core and Lower Back
    {
        'name': 'Seated Torso Twist',
        'muscle_group': 'Obliques',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Cobra Stretch',
        'muscle_group': 'Lower Back',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Kneeling Hip Flexor Stretch',
        'muscle_group': 'Hip Flexors',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Supine Spinal Twist',
        'muscle_group': 'Spine',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Lying Hamstring Stretch',
        'muscle_group': 'Hamstrings',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },

    # 21-25: Hips and Glutes
    {
        'name': 'Pigeon Pose',
        'muscle_group': 'Glutes',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Hip Flexor Stretch',
        'muscle_group': 'Hip Flexors',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Figure Four Stretch',
        'muscle_group': 'Glutes',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Butterfly Stretch',
        'muscle_group': 'Hips',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Hip Circles',
        'muscle_group': 'Hips',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Mobility'
    },

    # 26-30: Quads and Hamstrings
    {
        'name': 'Standing Quad Stretch',
        'muscle_group': 'Quads',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Hamstring Stretch with Band',
        'muscle_group': 'Hamstrings',
        'difficulty': 'Medium',
        'equipment': 'Resistance Band',
        'type': 'Flexibility'
    },
    {
        'name': 'Standing Forward Bend',
        'muscle_group': 'Hamstrings',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Wall Quad Stretch',
        'muscle_group': 'Quads',
        'difficulty': 'Medium',
        'equipment': 'Wall',
        'type': 'Flexibility'
    },
    {
        'name': 'Seated Hamstring Stretch',
        'muscle_group': 'Hamstrings',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },

    # 31-35: Calves and Feet
    {
        'name': 'Standing Calf Stretch',
        'muscle_group': 'Calves',
        'difficulty': 'Easy',
        'equipment': 'Wall',
        'type': 'Flexibility'
    },
    {
        'name': 'Seated Calf Stretch',
        'muscle_group': 'Calves',
        'difficulty': 'Medium',
        'equipment': 'Resistance Band',
        'type': 'Flexibility'
    },
    {
        'name': 'Downward Dog',
        'muscle_group': 'Calves',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Plantar Fascia Stretch',
        'muscle_group': 'Feet',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Toe Touch Stretch',
        'muscle_group': 'Calves',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },

    # 36-40: Full Body and Dynamic Stretches
    {
        'name': 'Standing Side Bend',
        'muscle_group': 'Obliques',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Dynamic Lunge with Twist',
        'muscle_group': 'Hip Flexors',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Mobility'
    },
    {
        'name': 'Inchworm',
        'muscle_group': 'Full Body',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Mobility'
    },
    {
        'name': 'World’s Greatest Stretch',
        'muscle_group': 'Full Body',
        'difficulty': 'Hard',
        'equipment': 'None',
        'type': 'Mobility'
    },
    {
        'name': 'Arm Circles',
        'muscle_group': 'Shoulders',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Mobility'
    },

    # 41-45: Hamstrings and Glutes
    {
        'name': 'Standing Hamstring Stretch',
        'muscle_group': 'Hamstrings',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Glute Bridge Stretch',
        'muscle_group': 'Glutes',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Supine Hamstring Stretch',
        'muscle_group': 'Hamstrings',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Lying Glute Stretch',
        'muscle_group': 'Glutes',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
   {
        'name': 'Bridge Pose',
        'muscle_group': 'Glutes',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    }
      # 46-50: Lower Body Focus
    {
        'name': 'Standing IT Band Stretch',
        'muscle_group': 'IT Band',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Piriformis Stretch',
        'muscle_group': 'Piriformis',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Deep Squat Stretch',
        'muscle_group': 'Glutes',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Adductor Stretch',
        'muscle_group': 'Adductors',
        'difficulty': 'Medium',
        'equipment': 'None',
        'type': 'Flexibility'
    },
    {
        'name': 'Seated Groin Stretch',
        'muscle_group': 'Groin',
        'difficulty': 'Easy',
        'equipment': 'None',
        'type': 'Flexibility'
    },
]

# Example: Displaying the dataset as a table
if st.button('Show Stretches'):
    for stretch in stretches:
        st.write(stretch)

# Further code for matching algorithm and other functionalities will go here...
