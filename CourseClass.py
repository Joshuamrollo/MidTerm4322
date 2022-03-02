class Course:

    def __init__(self,name,crn,seats,status):
        self.__name = name
        self.__crn = crn
        self.__seats = seats
        self.__status = status


    def get_name(self):
        return self.__name

    def get_crn(self):
        return self.__crn

    def get_seats(self):
        return self.__seats

    def get_status(self):
        return self.__status


    def update_seat_count(self):
        if self.__seats == 0:
            self.__status = 'closed'
        else:
            self.__seats -= 1
            if self.__seats == 0:
               self.__status = 'closed' 

class Register:

    def __init__(self,name,crn):
        self.__studentname = name
        self.__crn = crn

    def get_name(self):
        return self.__studentname

            
