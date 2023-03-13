
height= input("Enter height in m: ")
weight = input("Enter weight in KG: ")

w_as_int = int(weight)
h_as_int = float(height)

bmi = w_as_int / h_as_int ** 2
bmi_as_int= int(bmi)
print(bmi_as_int)