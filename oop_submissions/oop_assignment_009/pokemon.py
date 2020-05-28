class Pokemon:
    make_sounds=' '
    flys=''
    runs=''
    swims=''
    attacks=''
    another_attacks=''
    def __init__(self,name,level):
        if level <=0:
            raise ValueError('level should be > 0')
        if name =='':
            raise ValueError('name cannot be empty')    
        self._name=name
        self._level=level
        
    @property
    def name(self):
        return self._name
    @property
    def level(self):
        return self._level
        
    @classmethod
    def make_sound(cls):
        print(cls.make_sounds)    
        
    @classmethod
    def run(cls):
        print(cls.runs)
    @classmethod
    def fly(cls):
        print(cls.flys)
    @classmethod
    def swim(cls):
        print(cls.swims)
    def __str__(self):
        return '{} - Level {}'.format(self._name,self._level)    
        
class Pikachu(Pokemon):
    make_sounds='Pika Pika'
    runs='Pikachu running...'
    def attack(self):
        print('Electric attack with {} damage'.format(10*self._level))
    # def another_attack(self):
    #     print('Electric attack with {} damage'.format(10*self._level))    
    

class Squirtle(Pokemon):
    make_sounds='Squirtle...Squirtle'
    runs='Squirtle running...'
    swims='Squirtle swimming...'
    def attack(self):
        print('Water attack with {} damage'.format(9*self._level))
        
    
class Pidgey(Pokemon):
    make_sounds='Pidgey...Pidgey'
    flys='Pidgey flying...'
    def attack(self):
        print('Air attack with {} damage'.format(5*self._level))

class Swanna(Pokemon):
    make_sounds='Swanna...Swanna'
    flys='Swanna flying...'
    swims='Swanna swimming...'
    def attack(self):
        print('Water attack with {} damage'.format(9*self._level))
        print('Air attack with {} damage'.format(5*self._level))

class Zapdos(Pokemon):
    make_sounds='Zap...Zap'
    flys='Zapdos flying...'
    def attack(self):
        print('Electric attack with {} damage'.format(10*self._level))
        print('Air attack with {} damage'.format(5*self._level))
        
class Island:
    pokemon_list=[]
    def __init__(self,name,max_no_of_pokemon,total_food_available_in_kgs):
        self._name=name
        self._max_no_of_pokemon=max_no_of_pokemon
        self._total_food_available_in_kgs=total_food_available_in_kgs
        self._pokemon_left_to_catch=0
        Island.pokemon_list.append(self)
        self._count=0
    @property
    def name(self):
        return self._name
    @property
    def max_no_of_pokemon(self):
        return self._max_no_of_pokemon
    @property
    def total_food_available_in_kgs(self):
        return self._total_food_available_in_kgs   
    @property
    def pokemon_left_to_catch(self):
        return self._pokemon_left_to_catch    
        
    def __str__(self):
        return ('{} - {} pokemon - {} food'.format(self._name,self._pokemon_left_to_catch,self._total_food_available_in_kgs))    
    
    def add_pokemon(self,a):
        if self._pokemon_left_to_catch<self._max_no_of_pokemon:
            self._pokemon_left_to_catch+=1
        else:
            print('Island at its max pokemon capacity')
    @classmethod
    def get_all_islands(cls):
        return cls.pokemon_list
        
class Trainer(Island):
    def __init__(self,name):
        self._name=name
        self._experience=100
        self._max_food_in_bag=100*10
        self._food_in_bag=0
        self._current_island=None
        
    @property
    def name(self):
        return self._name
    @property
    def experience(self):
        return self._experience
    @property
    def max_food_in_bag(self):
        return self._max_food_in_bag
    @property
    def food_in_bag(self):
        return self._food_in_bag
    @property
    def current_island(self):
        return self._current_island    
    
    def __str__(self):
        return ('{}'.format(self._name))
    
    def move_to_island(self,island):
        self._current_island=island
        if self._current_island == None:
            print('You are not on any island')
        else:
            self._current_island = island
    
    def collect_food(self):
        if self._current_island != None:
            if self._current_island.total_food_available_in_kgs >self._max_food_in_bag:
                if self._food_in_bag < self._max_food_in_bag:
                    self._food_in_bag+=self._food_in_bag
                    self._current_island.total_food_available_in_kgs-=self._max_food_in_bag
                else:
                    self._food_in_bag=self._max_food_in_bag
                        
            else:
                self._food_in_bag=self._current_island.total_food_available_in_kgs
                self._current_island.total_food_available_in_kgs=0
        else:
            print('Move to an island to collect food')