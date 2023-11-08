import lab_1 , lab_2 , lab_3, lab_4, lab_5

def main():
    labs = {
        'lab_1': lab_1.main,
        'lab_2': lab_2.main,
        'lab_3': lab_3.main,
        'lab_4': lab_4.main,
        'lab_4': lab_5.main,
        
    }

    #labs['lab_1']()
    #labs['lab_2']()
    #labs['lab_3']()
    #labs['lab_4']()
    labs['lab_5']()

if __name__ == '__main__':
    main()