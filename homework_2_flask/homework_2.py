from flask import Flask

app = Flask(__name__)


@app.route("/avr_data")
def get_avr_data():
    with open('hw.csv') as file:
        total_weigh = total_heigh = 0

        while True:
            line = file.readline()
            line_lst = line.replace('\n', '').split(', ')

            try:
                lines_number = int(line_lst[0])
                total_heigh += float(line_lst[1])
                total_weigh += float(line_lst[2])
            except:
                pass

            if not line:
                break
    # Значения возвращаются переведенные в сантиметры и килограммы
    return 'Average height of all students: %.2f cm<br>' \
           'Average weight of all students: %.2f kg' % (total_heigh / lines_number * 2.54,
                                                        total_weigh / lines_number * 0.453)

@app.route("/requirements")
def get_requirements():
    """
    Returns a list of required dependencies
    """
    with open ('requirements.txt') as req_file:
        res=req_file.read().replace('\n','<br>')
        return f'List of required dependencies: <br>' \
               f'{res}'


@app.route("/random_students")
def get_random_students():
    from faker import Faker
    fake = Faker()
    std_num=20
    res=[fake.name() for _ in range (std_num)]
    res='<br>'.join(res)
    return f'Students list:<br><br>{res}'

app.run(debug=True)