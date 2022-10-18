def wr_to_csv(temp, humidity):
#     import matplotlib
#     matplotlib.use('Agg')
#     import matplotlib.pyplot as plt
    from csv import writer
    from datetime import date
    import datetime
    from weather import get_weather
    import pandas as pd
    
    # List 
    weat = get_weather()
    t = datetime.datetime.now()
    t = t.replace(second=0, microsecond=0)
    List=[t, date.today(), temp, humidity, weat]
      
    # Open our existing CSV file in append mode
    # Create a file object for this file
    with open('event.csv', 'a') as f_object:
      
        # Pass this file object to csv.writer()
        # and get a writer object
        writer_object = writer(f_object)
      
        # Pass the list as an argument into
        # the writerow()
        writer_object.writerow(List)
      
        #Close the file object
        f_object.close()
    # Read the csv file in
    df = pd.read_csv('event.csv')
    # Save to file
    df.to_html('website/templates/myTable.html')
    # Assign to string
    # htmTable = df.to_html()
    #Draw the matplotlib plot
#     x = [i for i in df['Time']]
#     y = df[' Humidity']
#     plt.savefig('website/static/Humidity.png')
#     z = df[' Temperature']
#     plt.savefig('website/static/Temperature.png')
#     for i in range(len(df['Time'])):
#         df['Time'][i] = datetime.datetime.strptime(df['Time'][i].replace("'",""), '%Y-%m-%d %H:%M:%S')
    


def check_time():
    with open("event.csv","r") as file: 
        data = file.readlines() 
    lastRow = data[-1]
    lastRow = lastRow.split(',')
    # from datetime import datetime
    import datetime
    date_time_str = lastRow[0]

    date_time_obj = datetime.datetime.strptime(date_time_str.replace("'",""), '%Y-%m-%d %H:%M:%S')

    # print ("The type of the date is now",  type(date_time_obj))
    # print ("The date is", date_time_obj)
    start = date_time_obj
    e1 = datetime.datetime.now()
    time_elapsed = e1 - start
    to = datetime.timedelta(hours=3)
    if time_elapsed > to:
        return True
    else:
        return False
    