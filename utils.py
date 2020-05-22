def holiday_announcer(month):
    Holidays = {'Jan': {1: ["New Year's Day"]}, 'Apr': {10: ['Good Friday'],
                                                        12: ['Easter Day'], 13: ['Easter Monday'],
                                                        27: ["King's Birthday"]}, 'May': {5: ['Liberation Day'],
                                                                                          21: ['Ascension Day'],
                                                                                          31: ['Pentecost Sunday']},
                'Jun': {1: ['Whit Monday']}, 'Dec': {25: ['Christmas Day'],
                                                     26: ["St.Stephen's Day"]}}
    print(f'The Holidays on the Month of {month} is/are: ')

    return list( Holidays[month].values())
