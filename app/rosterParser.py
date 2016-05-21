from .models import  Student, Section
from django.contrib.auth.models import User
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
        lastName = item[0]
        firstName = item[1]

        lastName = lastName[1:]
        firstName = firstName[:-1]
        firstName= firstName.lstrip(' ')
        username = firstName[0]+lastName
        print (firstName[0])
        id = item[2]
        password = id[0:4]
        section= item[4]
        if not (User.objects.filter(username=username).exists()):
            #sectionList = item[4].split(",")

            #for item in sectionList:
            #   item=item.lstrip()

            user = User.objects.create_user(
                username = username,
                email = "",
                password = password,
                first_name = firstName,
                last_name = lastName
            )
            student = Student()

            #for section in sectionList:
            #   section = section.strip()
            #  if not (Section.objects.get(section=section)):
            #     Section.objects.create(section=section)
            if not (Section.objects.filter(section = section).exists()):
                section = Section.objects.create(section=section)
            else:
               section = Section.objects.get(section= section)


            student.user = user
            student.section = section
            student.save()

            user.student = student
            user.save()
