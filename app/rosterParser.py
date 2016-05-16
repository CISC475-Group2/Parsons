from .models import  Student, Section
def parse_csv():
    """parse CSV and return elements in list

    """
    studentList= []
    with open('name.txt') as f:
        data = f.readlines()
        #del data[0]
        for line in data:
            if len(line.split(',')) ==6:
                studentList.append(line.split(','))
                print(line.split(','))

       # data = line.split(',')
        #studentList.append(data)
    return studentList

def parse(file):
    """reads input into temporary file,adds elements to database, and deletes temporary file  """
    with open('name.txt', 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    list = parse_csv()
    add_to_database(list)

def add_to_database(list):
    for item in list:
        name= item[0]
        section = item[4]
       # s = Student.objects.create(user = name,section= section )