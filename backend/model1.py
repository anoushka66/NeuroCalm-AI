def recommend_management(stress_level, age, chronic_diseases):
    # Define management techniques based on age groups and stress levels
    management_techniques = {
        "0-30": {
            0: {"Physical Activity": ["Regular exercise", "Walking", "Swimming"],
                "Diet and Sleep": ["Healthy diet", "Adequate sleep", "Hydration"],
                "Mental Well-being": ["Mindfulness meditation", "Deep breathing exercises", "Progressive muscle relaxation"]},
            1: {"Physical Activity": ["Yoga", "Tai chi", "Pilates"],
                "Stress Reduction": ["Journaling", "Art therapy", "Music therapy"],
                "Social Support": ["Spending time with loved ones", "Joining social groups", "Supportive therapy groups"]},
            2: {"Therapeutic Support": ["Professional counseling", "Cognitive-behavioral therapy", "Stress management workshops"],
                "Hobbies and Leisure": ["Engaging in hobbies", "Reading", "Gardening"],
                "Time Management": ["Time management techniques", "Setting boundaries", "Prioritizing tasks"]},
            3: {"Medication and Therapy": ["Medication under doctor's supervision", "Psychotherapy", "Group therapy"],
                "Self-care Practices": ["Relaxation techniques", "Healthy lifestyle habits", "Self-compassion practices"],
                "Support System": ["Seeking social support", "Joining support groups", "Peer counseling"]},
            4: {"Specialized Treatment": ["Consulting a mental health professional", "Hospitalization if necessary", "Intensive therapy programs"],
                "Community Support": ["Support groups", "Community mental health resources", "Online forums"],
                "Integrated Care": ["Medication and therapy", "Integration of mental health with chronic disease management", "Holistic treatment approaches"]}
        },
        "30-60": {
            0: {"Physical Activity": ["Gentle exercises", "Walking", "Swimming"],
                "Diet and Sleep": ["Healthy diet", "Adequate sleep", "Hydration"],
                "Mental Well-being": ["Mindfulness meditation", "Deep breathing exercises", "Progressive muscle relaxation"]},
            1: {"Physical Activity": ["Yoga", "Tai chi", "Pilates"],
                "Stress Reduction": ["Journaling", "Art therapy", "Music therapy"],
                "Social Support": ["Spending time with loved ones", "Joining social groups", "Supportive therapy groups"]},
            2: {"Therapeutic Support": ["Professional counseling", "Cognitive-behavioral therapy", "Stress management workshops"],
                "Hobbies and Leisure": ["Engaging in hobbies", "Reading", "Gardening"],
                "Time Management": ["Time management techniques", "Setting boundaries", "Prioritizing tasks"]},
            3: {"Medication and Therapy": ["Medication under doctor's supervision", "Psychotherapy", "Group therapy"],
                "Self-care Practices": ["Relaxation techniques", "Healthy lifestyle habits", "Self-compassion practices"],
                "Support System": ["Seeking social support", "Joining support groups", "Peer counseling"]},
            4: {"Specialized Treatment": ["Consulting a mental health professional", "Hospitalization if necessary", "Intensive therapy programs"],
                "Community Support": ["Support groups", "Community mental health resources", "Online forums"],
                "Integrated Care": ["Medication and therapy", "Integration of mental health with chronic disease management", "Holistic treatment approaches"]}
        },
        "60 above": {
            0: {"Physical Activity": ["Gentle exercises", "Walking", "Water aerobics"],
                "Diet and Sleep": ["Healthy diet", "Adequate sleep", "Hydration"],
                "Mental Well-being": ["Mindfulness meditation", "Deep breathing exercises", "Light stretching"]},
            1: {"Physical Activity": ["Gentle yoga", "Tai chi", "Pilates"],
                "Stress Reduction": ["Journaling", "Art therapy", "Music therapy"],
                "Social Support": ["Spending time with loved ones", "Joining social groups", "Supportive therapy groups"]},
            2: {"Therapeutic Support": ["Professional counseling", "Cognitive-behavioral therapy", "Stress management workshops"],
                "Hobbies and Leisure": ["Engaging in hobbies", "Reading", "Gardening"],
                "Time Management": ["Time management techniques", "Setting boundaries", "Prioritizing tasks"]},
            3: {"Medication and Therapy": ["Medication under doctor's supervision", "Psychotherapy", "Group therapy"],
                "Self-care Practices": ["Relaxation techniques", "Healthy lifestyle habits", "Self-compassion practices"],
                "Support System": ["Seeking social support", "Joining support groups", "Peer counseling"]},
            4: {"Specialized Treatment": ["Consulting a mental health professional", "Hospitalization if necessary", "Intensive therapy programs"],
                "Community Support": ["Support groups", "Community mental health resources", "Online forums"],
                "Integrated Care": ["Medication and therapy", "Integration of mental health with chronic disease management", "Holistic treatment approaches"],
                "Physical Activity": ["Yoga", "Tai chi", "Pilates"]}  # Ensure "Physical Activity" is initialized
        }
    }

    # Adjust management techniques based on chronic diseases if needed
    if age > 60:
        if "Regular exercise" in management_techniques["60 above"][0]["Physical Activity"]:
            management_techniques["60 above"][0]["Physical Activity"].remove("Regular exercise")
        management_techniques["60 above"][0]["Physical Activity"].append("Gentle exercises")
    if "arthritis" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        if "Yoga" in management_techniques["60 above"][1]["Physical Activity"]:
            management_techniques["60 above"][1]["Physical Activity"].remove("Yoga")
        management_techniques["60 above"][1]["Physical Activity"].append("Water aerobics")
    if "diabetes" in chronic_diseases:
        if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
            management_techniques["60 above"][2]["Diet and Sleep"].append("Monitoring blood sugar levels")
        if "Physical Activity" in management_techniques["60 above"][2]:  # Check if "Physical Activity" exists
            management_techniques["60 above"][2]["Physical Activity"].append("Regular blood sugar monitoring")
    if "hypertension" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][3]["Medication and Therapy"].append("Blood pressure monitoring")
        management_techniques["60 above"][3]["Diet and Sleep"].append("Low sodium diet")
    if "asthma" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][4]["Specialized Treatment"].append("Inhaler usage guidance")
        management_techniques["60 above"][4]["Physical Activity"].append("Breathing exercises")
    if "chronic obstructive pulmonary disease (COPD)" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][4]["Specialized Treatment"].append("Bronchodilator therapy")
        management_techniques["60 above"][4]["Physical Activity"].append("Pulmonary rehabilitation exercises")
    if "fibromyalgia" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][2]["Therapeutic Support"].append("Physical therapy")
        management_techniques["60 above"][2]["Self-care Practices"].append("Heat therapy")
    if "migraine" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][1]["Stress Reduction"].append("Headache diary")
        management_techniques["60 above"][1]["Stress Reduction"].append("Avoiding trigger foods")
    if "osteoporosis" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][0]["Physical Activity"].append("Weight-bearing exercises")
        management_techniques["60 above"][0]["Physical Activity"].append("Fall prevention strategies")
    if "depression" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][3]["Medication and Therapy"].append("Antidepressant medication")
        management_techniques["60 above"][3]["Support System"].append("Cognitive-behavioral therapy (CBT)")
    if "chronic kidney disease" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][2]["Diet and Sleep"].append("Low-protein diet")
        management_techniques["60 above"][2]["Support System"].append("Dialysis support groups")
    if "irritable bowel syndrome (IBS)" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][3]["Self-care Practices"].append("FODMAP diet")
        management_techniques["60 above"][3]["Self-care Practices"].append("Stress management techniques")
    if "rheumatoid arthritis" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][1]["Physical Activity"].append("Joint protection techniques")
        management_techniques["60 above"][1]["Physical Activity"].append("Assistive devices")
    if "multiple sclerosis" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][4]["Specialized Treatment"].append("Disease-modifying therapies")
        management_techniques["60 above"][4]["Support System"].append("MS support groups")
    if "thyroid disorders" in chronic_diseases:
      if "Diet and Sleep" in management_techniques["60 above"][2]:  # Check if "Diet and Sleep" exists
        management_techniques["60 above"][2]["Diet and Sleep"].append("Balanced diet with iodine-rich foods")
        management_techniques["60 above"][2]["Therapeutic Support"].append("Thyroid hormone replacement therapy")

    # Return the recommended management techniques
    if age <= 30:
        age_group = "0-30"
    elif age <= 60:
        age_group = "30-60"
    else:
        age_group = "60 above"

    return management_techniques[age_group][stress_level]

# Get user input
age = int(input("Enter your age: "))
if(age>110):
  print("Age is not possible")
else:

  stress_level = int(input("Enter your stress level (0-4): "))
  chronic_diseases_input = input("Enter if you have any of the below mentioned chronic diseases:\n- arthritis\n- diabetes\n- hypertension\n- asthma\n- chronic obstructive pulmonary disease (COPD)\n- fibromyalgia\n- migraine\n- osteoporosis\n- depression\n- chronic kidney disease\n- irritable bowel syndrome (IBS)\n- rheumatoid arthritis\n- multiple sclerosis\n- thyroid disorders\nEnter any chronic diseases you have (comma-separated, or 'none' if none): ").lower()
  chronic_diseases = chronic_diseases_input.split(", ") if chronic_diseases_input != 'none' else []

# Recommend management techniques
  recommended_techniques = recommend_management(stress_level, age, chronic_diseases)
  print("\nRecommended management techniques:")
  for category, techniques in recommended_techniques.items():
    print(f"\n{category}:")
    for technique in techniques:
        print("- " + technique)
    if "Physical Activity" in recommended_techniques and recommended_techniques["Physical Activity"] == ["Yoga", "Tai chi", "Pilates"]:
      print("\nYoga Support Groups:")
      print("- Check out local yoga studios or community centers for group classes.")
      print("- Online platforms like Yoga Alliance or Yoga Journal offer directories for finding certified instructors and studios.")
      print("- YouTube channels such as Yoga with Adriene and Yoga with Tim offer free instructional videos suitable for all levels.")
