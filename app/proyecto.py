
import  charts
from read_csv import read_csv
import matplotlib.pyplot as plt
from read_csv import red_caraculo




  
if __name__  == '__main__':
    data = read_csv('./world.csv')
    print(red_caraculo())
    print(data[0])

# def run():
#     data = read_csv.read_csv('./world.csv')
#     countries = list(map(lambda x: x['Country/Territory'], data))
#     porcentage = list(map(lambda x: x ['World Population Percentage'], data))
#     charts.generate_pie_chart( countries, porcentage)
    
# if __name__ == '__main__':
#     run()


# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv('./world.csv')

# new_data = df[df['Continent'] == 'South America']
# plt.pie(new_data['World Population Percentage'],labels=new_data['Country/Territory'])
# plt.rcParams ['figure.figsize'] = (10,8)
# plt.show()

    
    
    
    

    


