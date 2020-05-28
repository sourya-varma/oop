class Deer:
    def __init__(self, age_in_months,breed,required_food_in_kgs):
        self.age_in_months = age_in_months
        self.breed = breed
        self.required_food_in_kgs = required_food_in_kgs
        if(self.age_in_months!=1):
            raise ValueError('Invalid value for field age_in_months: {}'.format(self.age_in_months))
        if(self.breed != 'ELK'):
            raise ValueError('Invalid value for field breed: {}'.format(self.breed))
        if(self.required_food_in_kgs !=10):
            raise ValueError('Invalid value for field required_food_in_kgs: {}'.format(self.required_food_in_kgs))    
    
    def grow    
        