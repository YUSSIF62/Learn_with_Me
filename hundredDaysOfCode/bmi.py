w_as_int = weight
h_as_int = height
height= input("Enter height in m: ")
weight = input("Enter weight in KG: ")
bmi = w / float(height) ** 2
bmi_as_int= int(bmi)
print(bmi_as_int)