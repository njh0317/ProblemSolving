def solution(fees, records):
    answer = []
    acctime = calTime(fees, records)
    print(acctime)
    for time in acctime:
        fee = fees[1]
        if time[1] > fees[0]:
            remain = (time[1] - fees[0]) // fees[2]
            remain += 1 if (time[1] - fees[0]) % fees[2] > 0 else 0
            fee += remain * fees[3]
        answer.append(fee)
    return answer

def calTime(fees, records):
    intime = dict()
    acctime = dict()
    for record in records:
        time, car, tag = map(str, record.split())
        if tag == 'IN':
            intime[car] = time
        elif tag == 'OUT':
            if car not in acctime:
                acctime[car] = 0
            in_h, in_m = map(int, intime[car].split(':'))
            out_h, out_m = map(int, time.split(':'))
            acctime[car] += (out_h - in_h) * 60 + out_m - in_m
            intime[car] = 0
    
    # no Out cars
    for car, time in intime.items():
        if time != 0:
            if car not in acctime:
                acctime[car] = 0
            in_h, in_m = map(int, intime[car].split(':'))
            out_h, out_m = 23, 59
            acctime[car] += (out_h - in_h) * 60 + out_m - in_m
            intime[car] = 0
            
    return sorted(acctime.items())