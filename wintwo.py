def weight_to_height():
    """
    Inputs body measurements and gender, and outputs whether you are at a healthy ratio or not.
    :param gender: int.
    :param height: int.
    :param weight: int.
    :print: 
    """
    gendercheck = int(input("What is your birth gender? Enter an even number for female, or an odd number for male."))
    if gendercheck % 2 == 0:
        gender = 0
    else:
        gender = 1
    height = int(input("What is your height in inches?"))
    waist = int(input("What is your waist in inches?"))
    ratio = waist / height
    if gender == 0:
        if ratio <= 0.4919:
            print("Looks like your waist to height ratio of "+str(ratio)+" is great, young lady!")
        else:
            print("Looks like you currently have an increased risk of insulin resistance, type 2 diabetes and heart disease at "+str(ratio)+"! Aim to get below .4920.")
    else:
        if ratio <= 0.5359:
            print("Looks like your waist to height ratio of "+str(ratio)+" is great, young man!")
        else:
            print("Looks like you currently have an increased risk of insulin resistance, type 2 diabetes and heart disease at "+str(ratio)+"! Aim to get below .5260.")
