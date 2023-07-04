import matplotlib.pyplot as plt


def generate_bar_chart():
    labels = ['a','b', 'c']
    values = [100, 200, 80]
    
    fig, ax =plt.subplots()
    ax.bar(labels, values)
    plt.show()
    
if __name__ == '__main__':
 generate_bar_chart()
    
    
    
def generate_bar_chart(labels, values):
    ig, ax =plt.subplots()
    ax.bar(labels, values)
    plt.show()
    
if __name__ == '__main__':
    labels = ['a','b', 'c']
    values = [10, 40, 800 ]
    
    #generate_bar_chart(labels, values)
    
    
    # creando un bar.pie   
    
def generate_pie_chart(labels, values):
    fig, ax =plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()
    
    
if __name__ == '__main__':
    labels = ['a','b', 'c']
    values = [10, 40, 800 ]
    
    generate_pie_chart(labels, values)