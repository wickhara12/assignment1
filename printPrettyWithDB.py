""" this is Rebecca's code for task 15"""

import model.Database

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

style.use('fivethirtyeight')


def graph_data():
    model.Database.cursor.execute('SELECT * from classDiagramInfo ')
    dates = []
    values = []
    for row in model.Database.cursor.fetchall():
        # print(row[0])
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(model.Database.datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])
    plt.plot_date(dates, values, '-')
    plt.show()

# graph_data()
# model.Database.cursor.close()
# model.Database.connection.close()
