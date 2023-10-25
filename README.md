# Запуск

#### Запустити main.py
```python
import lab_1 , lab_2 , lab_3

def main():
    labs = {
        'lab_1': lab_1.main,
        'lab_2': lab_2.main,
        'lab_3': lab_3.main,
        
    }

#Для виклику конкретного завданяя поставити закоментувати не потрібні 
    labs['lab_1']()
    labs['lab_2']()
    labs['lab_3']()

if __name__ == '__main__':
    main()
```

# Lab_3
# Алгоритм P-блоку
#### Візуалізація формули перестановки
![P_box](/screenshots/P_box.png)
#### Перестановка бітів вхідного блоку відповідно до заданої формули перестановки
```python
def transform(input_bits):
        permutation_order = [7, 2, 5, 1, 6, 0, 4, 3]
        return ''.join(input_bits[i] for i in permutation_order)
```

#### Зворотне перетворення P-блоку включає в себе обернену перестановку бітів вихідного блоку відповідно до формули перестановки
```python 
def inverse(output_bits):
    permutation_order = [5, 3, 1, 7, 6, 2, 4, 0]
    return ''.join(output_bits[i] for i in permutation_order)
```

#### Результат перестановки
```python 
test_data = ['10000001']
```
![P_box_result](/screenshots/P_box_res.png)

#### Результат перестановки з кількома данними
```python 
test_data = ['10101010', '11110000', '00001111', '11001100', '00110011']
```
![P_box_multiple_test](/screenshots/P_box_multiple_test.png)


# Алгоритм S-блоку
#### Візуалізація S-блоку
![S_block](/screenshots/S_box.png)

#### Візуалізація роботи алгоритму
![S_block](/screenshots/S_box_vizualization.png)

#### Заміна блоків даних згідно таблиці заміни
```python
def transform(input_bits):
    # Розбиваємо вхідні біти на дві частини: ліву та праву
    left_bits = input_bits[:4]
    right_bits = input_bits[4:]

    # Визначаємо рядок та стовпець для кожної частини
    rows = [int(bits[0] + bits[3], 2) for bits in [left_bits, right_bits]]
    cols = [int(bits[1] + bits[2], 2) for bits in [left_bits, right_bits]]
    
    # Повертаємо значення з S_BOX, що відповідають визначеним рядкам та стовпцям для кожної частини
    return ''.join(format(SBlock.S_BOX[row][col], '04b') for row, col in zip(rows, cols))
```
#### Результат перестановки
![S_block](/screenshots/S_box_res.png)

#### INVERSE to be implemented