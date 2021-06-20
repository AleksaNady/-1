top5 = 'Первые 5 мест на соревнованиях: 1. Иван, 2. Лена, 3. Коля, 4. Надя, 5. Оля'
start = top5.find('1')
end = top5.find('4')

#срезы
top3 = top5[start: end]

result = 'Поздравляем {} с упехами!'.format(top3.upper())

print(result)