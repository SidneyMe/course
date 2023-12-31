# Запуск
#### Встановити requirements
```python
pip install -r requirements.txt
```
#### Запустити main.py
```python
import lab_1, lab_2, lab_3, lab_4, lab_5, lab_7, lab_8, lab_9

def main():
    labs = {
        #'lab_1': lab_1.main, # it's a brute force you won't get to the next lab if it's not commented
        'lab_2': lab_2.main,
        'lab_3': lab_3.main,
        'lab_4': lab_4.main,
        'lab_5': lab_5.main,
        'lab_7': lab_7.main,
        'lab_8': lab_8.main,
        'lab_9': lab_9.main,
    }

    for lab_name, lab_function in labs.items():
        print(f"Running {lab_name}:")
        lab_function()
        print("\n")

if __name__ == '__main__':
    main()
```

# Lab 3
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

# Алгоритм P-блоку
#### Візуалізація формули перестановки
![P_box](/screenshots/P_Box.png)
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

#### Однобітовий тест
```python 
test_data = ['10000001']
```
![P_box_result](/screenshots/P_box_res.png)

#### Мультибітовий тест
```python 
test_data = ['10101010', '11110000', '00001111', '11001100', '00110011']
```
![P_box_multiple_test](/screenshots/P_box_multiple_test.png)

## Робота S та P блоків разом
#### Однобітовий тест
```python
test_data = ['10000001']
```
![S_and_P_res](/screenshots/S_and_P.png)

```python
test_data = ['10101010', '11110000', '00001111', '11001100', '00110011']
```
#### Мультибітовий тест
![S_and_P_multiple](/screenshots/S_and_P_multiple.png)
# Lab 5
### За результатами тестiв мiй агоритм в 200 разiв повiльнiший
![comparison libbrary with mine](/screenshots/comparison.png)