def eventParser():
    Weekdays = {'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'}
    
    events = []
    
    with open('my_sched') as inFile:
        for line in inFile:
            line = line.rstrip()
            if len(Weekdays.intersection(line.split())) > 0:
                rawEvent = line.split('\t')
                
                
                
                temp = rawEvent[1].split()[1].split('/')
                newDate = '{yyyy}-{mm}-{dd}T'.format(yyyy = temp[2], mm = temp[0], dd = temp[1])
                
                
                
                if ' PM' in rawEvent[2]:
                    newTime = rawEvent[2].split(':')
                    newHour = int(newTime[0]) + 12
                    newTime[0] = str(newHour)
                    newTime[1] = newTime[1].replace(' PM', '')
                    newTime.append('00')
                    startDateTime = '{hh}:{min}:{secTZ}'.format(hh = newTime[0], min = newTime[1], secTZ = newTime[2])
                else:
                    startDateTime = rawEvent[2].replace(' AM', ':00')
                    
                
                if ' PM' in rawEvent[3]:
                    newTime = rawEvent[3].split(':')
                    newHour = int(newTime[0]) + 12
                    newTime[0] = str(newHour)
                    newTime[1] = newTime[1].replace(' PM', '')
                    newTime.append('00')
                    endDateTime = '{hh}:{min}:{secTZ}'.format(hh = newTime[0], min = newTime[1], secTZ = newTime[2])
                else:
                    endDateTime = rawEvent[3].replace(' AM', ':00')
                    
                    
                events.append({'colorId':'1' ,'summary' : rawEvent[0], 'start' : {'dateTime' : newDate + startDateTime, \
                'timeZone': 'America/Los_Angeles'}, 'end' : {'dateTime' : newDate + endDateTime, \
                'timeZone': 'America/Los_Angeles'}})
                
    return events

  
            
            