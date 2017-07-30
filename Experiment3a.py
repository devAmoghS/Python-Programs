class Time:
	def __init__(self):
		self.hours=0
		self.minutes=0
		self.seconds=0
	def input_values(self):
		self.hours=int(input('Enter the hours: '))
		self.minutes=int(input('Enter the minutes: '))
		self.seconds=int(input('Enter the seconds: '))
	def print_details(self):
		print(self.hours,':',self.minutes,':',self.seconds)
	def __add__(self,other):
		t=Time()
		t.seconds=self.seconds+other.seconds
		t.minutes=self.minutes+other.minutes+t.seconds//60
		t.seconds=t.seconds%60
		t.hours=self.hours+other.hours+t.minutes//60
		t.minutes=t.minutes%60
		t.hours=t.hours%24
		t.print_details()
		return t
	def __sub__(self,other):
		t=Time()
		t.hours=self.hours-other.hours
		t.minutes=self.minutes-other.minutes
		if(t.minutes<0):
			t.minutes=t.minutes+60
			t.hours=t.hours-1
		t.seconds=self.seconds-other.seconds
		if(t.seconds<0):
			t.seconds=t.seconds+60
			t.minutes=t.minutes-1
		t.print_details()
		return t
t1=Time()
print('Enter the time 1')
t1.input_values()
t1.print_details()
t2=Time()
print('Enter the time 2')
t2.input_values()
t2.print_details()
print('Added time')
t3=t1+t2
print('Subtracted time')
t3=t1-t2


