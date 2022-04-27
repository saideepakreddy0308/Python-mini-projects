from tabulate import tabulate
data = [["Name","Place","Gender"],["Deepak","New Delhi","Male"],["Arjun","Hyderabad","Male"],["Divya","Bangalore","Female"]]
print(tabulate(data,headers='firstrow',tablefmt='fancy_grid'))