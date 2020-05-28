class Animal:
    breathes=''
    make_sounds=''
    grows=0
    def __init__(self,age_in_months,required_food_in_kgs,breed):
        if age_in_months !=1:
            raise ValueError("Invalid value for field age_in_months: {}".format(age_in_months))
            
        if required_food_in_kgs <=0:
            raise ValueError("Invalid value for field required_food_in_kgs: {}".format(required_food_in_kgs))
            
        self._age_in_months=age_in_months
        self._required_food_in_kgs=required_food_in_kgs
        self._breed=breed
        
        
    @property
    def age_in_months(self):
        return self._age_in_months
    @property
    def required_food_in_kgs(self):
        return self._required_food_in_kgs
    @property
    def breed(self):
        return self._breed


    @classmethod
    def make_sound(cls):
        print(cls.make_sounds)
       
    def grow(self):
        self._age_in_months += 1
        self._required_food_in_kgs +=self.grows
        
    
class land_animals:
    @classmethod
    def breathe(cls):
        print('Breathe in air')
    
class water_animals:
    @classmethod
    def breathe(cls):
        print('Breathe oxygen from water')
    
    
class Deer(Animal,land_animals):
    make_sounds='Buck Buck'
    grows=2


class Lion(Animal,land_animals):
    make_sounds='Roar Roar'
    grows=4
    def hunt(self,lis):
        if 'Deer' in lis.animals_list:
            lis.animals_list.remove('Deer')
        else:
            print('No deers to hunt')
    
    
class Shark(Animal,water_animals):
    make_sounds='Shark Sound'
    grows=8
    def hunt(self,lis):
        if 'GoldFish' in lis.animals_list:
            lis.animals_list.remove('GoldFish')
        else:
            print('No GoldFish to hunt')


class GoldFish(Animal,water_animals):
    make_sounds='Hum Hum'
    grows=0.2


class Snake(Animal,land_animals):
    make_sounds='Hiss Hiss'
    grows=0.5
    def hunt(self,lis):
        if 'Deer' in lis.animals_list:
            lis.animals_list.remove('Deer')
        else:
            print('No deers to hunt')
    
    
class Zoo:
        all= []
        def __init__(self):
            self._reserved_food_in_kgs = 0
            self._animals_list = []
            
        @property
        def reserved_food_in_kgs(self):
            return self._reserved_food_in_kgs
        @property
        def animals_list(self):
            return self._animals_list
            
        def add_food_to_reserve(self,food):
            self._reserved_food_in_kgs +=food
        def count_animals(self):
            return len(self._animals_list)
        def add_animal(self,a):
            self._animals_list.append(type(a).__name__)
            self.all.append(type(a).__name__)
            
        def feed(self,fish):
            if(self._reserved_food_in_kgs > 0):
                self._reserved_food_in_kgs-=fish._required_food_in_kgs
                fish.grow()
        @classmethod
        def count_animals_in_all_zoos(cls):
            return len(cls.all)
        @staticmethod
        def count_animals_in_given_zoos(zoos):
            counts=0
            for i in zoos:
                counts=counts+i.count_animals()
            return counts