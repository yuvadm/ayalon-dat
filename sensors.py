
def get_sensor_list():
    dict = {}
    from csv import reader
    with open('dtslist.csv', 'r') as f:
        c = reader(f)
        for row in c:
            dict[row[0]] = row[2]
    return dict
