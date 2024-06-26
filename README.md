# goit-algo-hw-04

Аналіз результатів експерименту
Ми провели емпіричні тестування трьох алгоритмів сортування — сортування вставками, сортування злиттям, і Timsort (вбудований у Python алгоритм) — на масивах різного розміру. Наступні дані показують час виконання (у секундах) для кожного алгоритму та розміру масиву:

Розміри масивів:

1000
2000
5000
10000
Час виконання для сортування вставками:

0.0315 сек
0.1133 сек
0.9157 сек
4.1450 сек
Час виконання для сортування злиттям:

0.0022 сек
0.0047 сек
0.0171 сек
0.0399 сек
Час виконання для Timsort:

0.0001 сек
0.0003 сек
0.0011 сек
0.0027 сек

Висновки:

Сортування вставками показує значне зростання часу виконання при збільшенні розміру масиву, що відповідає його теоретичній складності O(n 2). Це робить його непрактичним для великих масивів.
Сортування злиттям має набагато кращі результати, особливо на великих масивах, завдяки його теоретичній складності O(nlogn). Воно добре підходить для сортування великих масивів, але потребує додаткової пам'яті для своєї роботи.
Timsort демонструє найкращі часові показники серед всіх алгоритмів у всіх тестах. Цей гібридний алгоритм, що поєднує сортування злиттям та сортування вставками, оптимізований для реальних даних, які часто містять впорядковані субмасиви, з чого Timsort отримує свою високу ефективність.

