print('print 6digit number')
while True:
    lucky = [int(i) for i in input()]
    if sum(lucky[:3]) == sum(lucky[3:]):
        print('lucky')
        break
    else:
        print('wrong')
