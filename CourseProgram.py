'''
You have been given partial code. The objective is to reproduce the output as shown in the file - Output.png
1) Create an instance of the Course object
2) Create an instance of the Register object for EACH student in the students list using a For loop.
3) Print out the student name, course name, CRN and number of seats left for each iteration using
   ONLY get methods.
4) Take note that student 'Joanne' cannot register since there are only 4 seats in the course and
   and the output should reflect that as shown in the picture.
'''



from CourseClass import Course, Register

def main():

   name = 'MIS 4322 - Advanced Python'
   crn = '250309'
   seats = 4
   status = 'open'
   students = ['John','James','Jill','Jack','Joanne']

   course_object = Course(name,crn,seats,status)

   for student in students:
      cur_reg = Register(student, crn)
      if course_object.get_status() != 'closed':
         course_object.update_seat_count()
         print('Student Name: ' + cur_reg.get_name())
         print('Course Name: ' + course_object.get_name())
         print('CRN: ' + course_object.get_crn())
         print('Seats left: ' + str(course_object.get_seats()))
      else:
         print('Sorry ' + cur_reg.get_name() + ', registration is closed for ' + course_object.get_name())
      print('\n')


    
main()



        
    
    
