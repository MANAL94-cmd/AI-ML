#we have to create 2 dimentional array for the table given.
#read csv file
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#we have to create 2 dimentional array for the table given.
#read csv file
file="PA1.xlsx"
purchase_list=pd.read_excel(file)
print(purchase_list)
#Qn_1.A "joint probability of the people who planned to purchase and actually placed an order"
Answer_1A=purchase_list['Actually placed order for Product A - Yes'][0]/purchase_list['total'][2]
print(Answer_1A)
