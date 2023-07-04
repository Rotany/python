import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('./world.csv')
    country = input('Type Country=>')
    

    result =  utils.population_by_country(data, country)
    if len(result)> 0:
         
        country = result[0]  
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
    else:
        print("No hay resultados, prueba con otro nombre, fiera")
    
if __name__ == '__main__':
    run()
    
    
    
    
    
# def run():
#     data = read_csv.read_csv('./app/data.csv')
#     data = list(filter(lambda item: item['Continent'] == 'South America', data))
#     countries=list(map(lambda x: x['Country'], data))
#     percentage = list(map(lambda x: x['Wold Population Percentage'], data))
#     charts.generate_pie_chart(countries, percentage)
    
    
          

    
    


    
    '''
    
    country = input('Type Country =>')
    

    result =  utils.population_by_country(data, country)
    
    if len(result)> 0:
         
        country = result[0]  
        labels, values =utils.get_population(country)
        charts.generate_bar_chart(labels, values)
    '''
    
    # if __name__ == '__main__':
    #  run()
          
     