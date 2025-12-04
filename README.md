# ДЗ 5: Алгоритми пошуку

## Задача 1: Hash Table

```bash
python task_1_hashtable.py
```

Хеш таблиця. Можна додавати, отримувати та видаляти дані по ключу.

---

## Задача 2: Двійковий пошук

```bash
python task_2_binary_search.py
```

Пошук числа в масиві. Повертає скільки разів шукали і яке число найменше але більше за шукане.

---

## Задача 3: Порівняння алгоритмів

```bash
python task_3_search_comparison.py
```

Три способи пошуку підрядка в тексті. Вимірює який найшвидший.

**Результат:** Boyer-Moore найшвидший.

---

## Файли

- `task_1_hashtable.py` - Задача 1
- `task_2_binary_search.py` - Задача 2  
- `task_3_search_comparison.py` - Задача 3
- `article1.txt` - Текст для тестування завдання 3
- `article2.txt` - Текст для тестування завдання 3

---

## Git

```bash
PS C:\Users\dmitz\Documents\GitHub\goit-algo-hw-05> python task_1_hashtable.py        
john
20
None
False
PS C:\Users\dmitz\Documents\GitHub\goit-algo-hw-05> ython task_2_binary_search.py
ython: The term 'ython' is not recognized as a name of a cmdlet, function, script file, or executable program.
Check the spelling of the name, or if a path was included, verify that the path is correct and try again.
PS C:\Users\dmitz\Documents\GitHub\goit-algo-hw-05> python task_2_binary_search.py
(3, 5.1)
(3, 5.1)
(3, 1.5)
(3, None)
PS C:\Users\dmitz\Documents\GitHub\goit-algo-hw-05> python task_3_search_comparison.py
Article 1:
Linear: real=0.000044s, fake=0.001867s
Boyer-Moore: real=0.000012s, fake=0.000240s
Hash: real=0.000100s, fake=0.004307s

Article 2:
Linear: real=0.000689s, fake=0.003295s
Boyer-Moore: real=0.000157s, fake=0.000399s
Hash: real=0.001389s, fake=0.007364s
PS C:\Users\dmitz\Documents\GitHub\goit-algo-hw-05> ```