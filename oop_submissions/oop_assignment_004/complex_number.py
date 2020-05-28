import math
class ComplexNumber:
    
    def __init__(self,real_part=0,imaginary_part=0):
        self.real_part=real_part
        self.imaginary_part=imaginary_part
        if self.real_part==str:
            raise ValueError('Invalid value for real_part')
        
        if self.imaginary_part==str:
            raise ValueError('Invalid value for imaginary_part')
        
    def __str__(self):
        if self.imaginary_part >=0:
            return('{}+{}{}'.format(self.real_part,self.imaginary_part,'i'))
        else:
            return('{}{}i'.format(self.real_part,self.imaginary_part))
            
    def __add__(self,other):
        return ComplexNumber(self.real_part+other.real_part,self.imaginary_part+other.imaginary_part)


    def __sub__(self,add):
        return ComplexNumber(self.real_part-add.real_part,self.imaginary_part-add.imaginary_part)
    
    def __mul__(self,add):
        return ComplexNumber(self.real_part*add.real_part-self.imaginary_part*add.imaginary_part,self.real_part*add.imaginary_part+self.imaginary_part*add.real_part)

    def __truediv__(self,add):
        import math
        k=math.sqrt(add.real_part**2+add.imaginary_part**2)**2
        return ComplexNumber((self.real_part*add.real_part+self.imaginary_part*add.imaginary_part)/k,(self.imaginary_part*add.real_part-self.real_part*add.imaginary_part)/k)
    
    def __abs__(self):
        return round(math.sqrt(self.real_part**2+self.imaginary_part**2),3)

    def __eq__(self,equ):
        return(self.real_part==equ.real_part and self.imaginary_part==equ.imaginary_part)
        
    def conjugate(self):
        a=-self.imaginary_part
        return(self.real_part,a)