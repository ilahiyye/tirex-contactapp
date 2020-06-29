class PhoneBook:
	def __init__(self):
		self.collection = []

	def add_person(self, person):
		self.collection.append(person)
		return True

	def remove_person(self, person):
		if person in self.collection:
			self.collection.remove(person)
			return True
		return False 


class Person:
	def __init__(self, first_name, last_name, phone_number):
		self.first_name = first_name
		self.last_name = last_name
		self.phone_number = phone_number

