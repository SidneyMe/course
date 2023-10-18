import lab_1
import lab_2

def main():
    labs = {
        'lab_1': lab_1.main,
        'lab_2': lab_2.main,
    }

    #labs['lab_1']()
    labs['lab_2']()

if __name__ == '__main__':
    main()