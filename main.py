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
