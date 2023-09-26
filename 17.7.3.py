per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = input("Введите сумму вклада:")
money = float(money)
tkb = (money*per_cent['ТКБ'])/100
tkb = int(tkb)
skb = (money*per_cent['СКБ'])/100
skb = int(skb)
vtb = (money*per_cent['ВТБ'])/100
vtb = int(vtb)
sber = (money*per_cent['СБЕР'])/100
sber = int(sber)
deposite = [tkb, skb, vtb, sber]
print(deposite)
print("Максимальная сумма, которую вы можете заработать —", max(deposite))