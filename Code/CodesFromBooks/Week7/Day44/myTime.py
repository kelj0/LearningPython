
class MyTime:
    def __init__(self,hrs =0, mins=0, secs=0):
        """ Create a mytime obj initialized to hrc, mins, secs """
        self.hours = hrs
        self.minutes = mins
        self.seconds = secs

    def to_seconds(self):
        return self.hours*3600+self.minutes*60+self.seconds

    def add_time(self,t1,t2):
        secs = t1.to_seconds() + t2.to_seconds()
        return MyTime(0, 0, secs)

    def after(self, time2):
        return self.to_seconds() > time2.to_seconds()

    def __add__(self, other):
        sec = self.to_seconds() + other.to_seconds()
        hours = sec//3600
        leftoversec = sec%3600
        minutes = leftoversec//3600
        seconds = abs(leftoversec%3600) 
        while seconds>60:
            seconds=seconds-60
            minutes+=1        
        while minutes>60:
            minutes= minutes-60
            hours+=1
        if hours<10:
            hours = "0"+str(hours)
        if minutes<10:
            minutes = "0"+str(minutes)
        if seconds<10:
            seconds = "0"+str(seconds)
        
        return MyTime(hours,minutes,seconds)

    def __str__(self):
        return str(self.hours)+":"+str(self.minutes)+":"+str(self.seconds)

def main():
    t1 = MyTime(1,15,42)
    t2 = MyTime(3,50,30)
    t3 = t1+t2
    print(t3)



if __name__ == '__main__':
    main()