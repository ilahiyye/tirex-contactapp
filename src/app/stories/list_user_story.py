# command : show contact list
# Validate Input:
# if Input is OK -  send user contact list (self.collection)
# else send Wrong input (Validation error message)

class ListUserStory:
    def __init__(self, phone_book):
        self.phone_book = phone_book

    def run(self):
        validated = self.validate_input(keyword)
        if validated:
            results = self.show_list()
        else:
            results = self.validation_error_message(validated)

        return results


    def show_list(self):
        for person in self.phon_book.collection:
            print(f'{person.first_name}\t{person.last_name}\t{person.phone_number}')
            return person

    def validate_input(self, keyword):
        return True if keyword == "show_list" else False

    
    def validation_error_message(self, validated):
        return {"message": "Error: Wrong Keyword!"}


    