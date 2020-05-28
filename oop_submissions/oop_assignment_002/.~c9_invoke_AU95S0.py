class Truck:
    def __init__(self,color,max_speed,acceleration,tyre_friction,max_cargo_weight):
        self.max_speed=max_speed
        self.acceleration=acceleration
        self.tyre_friction=tyre_friction
        self.current_speed=0
        self.max_cargo_weight=max_cargo_weight
        if self.max_speed<0:
            raise ValueError('Invalid value for max_speed')
        if self.acceleration<0:
            raise ValueError('Invalid value for acceleration')
        if self.tyre_friction<0:
            raise ValueError('Invalid value for tyre_friction')
        if self.max_cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')
        self.color=color
        self.is_engine_started=False
        self.load=0
        
    # @property
    # def color(self):
    #     return self._color
        
    # @property
    # def acceleration(self):
    #     return self._acceleration
    
    # @property
    # def tyre_friction(self):
    #     return self._tyre_friction
    
    # @property
    # def current_speed(self):
    #     return self._current_speed
        
    # @property
    # def cargo_weight(self):
    #     return self._cargo_weight    
        
    # @property
    # def max_speed(self):
    #     return self._max_speed
        
    # @property
    # def is_engine_started(self):
    #     return self._is_engine_started
        
    
    def start_engine(self):
        self.is_engine_started=True
      

    
    def accelerate(self):
        if self.is_engine_started==True:
            if self.current_speed+self.acceleration<=self.max_speed:
                self.current_speed+=self.acceleration
            else:
                self.current_speed=self.max_speed
                
        else:
            print('Start the engine to accelerate')
            
    
    def apply_brakes(self):
        if self.current_speed>=self.tyre_friction:
            self.current_speed-=self.tyre_friction
        else:
            self.current_speed=0
    
    
    def sound_horn(self):
        if self.is_engine_started==True:
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')
    
    
    def stop_engine(self):
        if self.is_engine_started==True:
            self.is_engine_started=False
            
    def load_cargo(self,load):
        if a<=self.max_cargo_weight:
            self.load+=load
        else:
            print('Cannot load cargo more than max limit: {}'.format(self.max_cargo_weight))
    
            
i