
def get_sensors():
    dict = {}
    from csv import reader
    with open('dtslist.csv', 'r') as f:
        c = reader(f)
        for id,status,name in c:
            dict[id] = name
    return dict
