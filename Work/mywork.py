# mywork

total_cost = 0

with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        nshares = int(row[1])
        price = float(row[2])
        total_cost = nshares*price
        row.append(total_cost)
        print(row, end='')
    print(total_cost)
            
          
            

