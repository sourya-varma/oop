from car import Car
class Truck(Car):
    def __init__(self,color=None,max_speed=0,acceleration=0,tyre_friction=0,max_cargo_weight=0):
        super().__init__(color,max_speed,acceleration,tyre_friction)
        self._max_cargo_weight=max_cargo_weight
        if self._max_cargo_weight<0:
            raise ValueError('Invalid value for cargo_weight')
        self._loads=0
        #self._unloads=0
        
    @property
    def loads(self):
        return self._loads
    @property
    def max_cargo_weight(self):
        return self._max_cargo_weight
    def sound_horn(self):
        if self._is_engine_started==True:
            print('Honk Honk')
        else:
            print('Start the engine to sound_horn')
    
    def load(self,Load):
        if Load <0:
            raise ValueError('Invalid value for cargo_weight')
        if self._current_speed==0:
            if Load<=self._max_cargo_weight and self._is_engine_started==False:
                self._loads+=Load
            else:
                print('Cannot load cargo more than max limit: {}'.format(self._max_cargo_weight))    
        else:
            print('Cannot load cargo during motion')
    
    def unload(self,Loads):
        if Loads<0:
            raise ValueError('Invalid value for cargo_weight')
        if self._current_speed==0:
            self._loads-=Loads
            
        else:
            print('Cannot unload cargo during motion')