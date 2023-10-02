ticket = None
tickets_list = []
sum_tickets = 0
numt = int(input('Количество билетов:'))
for i in range(numt):
    aget = int(input('Введите возраст посетителя (лет):'))
    if aget < 18:
        tickets_list.append(0)
    elif 18<=aget<25: 
        tickets_list.append(990)
    elif aget>=25:
        tickets_list.append(1390)
print(tickets_list)
if numt > 3:
    print('Действует скидка 10%')
    sum_tickets = sum(tickets_list)
    discount_price = (sum_tickets*10) / 100
    sum_tickets = sum_tickets - discount_price
    sum_tickets = int(sum_tickets)
    print('Общая сумма к оплате:',sum_tickets, 'руб.')
else:
    print('Общая сумма к оплате:',sum(tickets_list),'руб.')
