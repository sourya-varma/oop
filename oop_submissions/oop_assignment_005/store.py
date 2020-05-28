class Item:
    def __init__(self,name,category,price):
        if(price<=0):
            raise ValueError('Invalid value for price, got {}'.format(price))
        self.price=price   
        self.name=name
        self.category=category
        
        
    def __str__(self):
        return('{}@{}-{}'.format(self.name,self.price,self.category))
        
class Query:
    def __init__(self,field,operation,value):
        self.field=field
        self.operation=operation
        self.value=value
        operators = ['IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS']
        if self.operation not in operators:
            raise ValueError("Invalid value for operation, got {}".format(self.operation))
        
    def __str__(self):
        return('{} {} {}'.format(self.field,self.operation,self.value))    
    

class Store():
    def __init__(self):
        self.item=[]
    
    def add_item(self,a):
        self.item.append(a)
        
    def __str__(self):
        if len(self.item)>=1:
            return '\n'.join(map(str,self.item))
        else:
            return 'No items'
    
    def count(self):
        return len(self.item)
        
    def filter(self,query):
        filter_item = Store()
        if query.operation == 'EQ':
            for i in self.item:
                if query.field == 'name' and i.name == query.value:
                    filter_item.add_item(i)
                
                elif query.field == 'price' and i.price == query.value:
                    filter_item.add_item(i)
                
                elif query.field == 'category' and i.category == query.value:
                    filter_item.add_item(i)
      
            return(filter_item)        
        elif query.operation =='GT':
            for i in self.item:
                if i.price > query.value:
                    filter_item.add_item(i)
            return(filter_item)
        
        elif query.operation =='GTE':
            for i in self.item:
                if i.price >= query.value:
                    filter_item.add_item(i)
            return(filter_item)
            
        elif query.operation =='LT':
            for i in self.item:
                if i.price < query.value:
                    filter_item.add_item(i)
            return(filter_item)    
        
        elif query.operation =='LTE':
            for i in self.item:
                if i.price <= query.value:
                    filter_item.add_item(i)
            return(filter_item)    
        
        elif query.operation =='STARTS_WITH':
            for i in self.item:
                if query.field == 'name' and i.name == query.value:
                    filter_item.add_item(i)
                elif query.field == 'price' and i.price == query.value:
                    filter_item.add_item(i)
                
                elif query.field == 'category' and i.category == query.value:
                    filter_item.add_item(i)    
        
        
store = Store()  
item = Item(name="Oreo Biscuits", price=30, category="Food")  
store.add_item(item)  
item = Item(name="Boost Biscuits", price=20, category="Food")  
store.add_item(item)
item = Item(name="Butter", price=10, category="Grocery")  
store.add_item(item)  
query = Query(field="name", operation="STARTS_WITH", value='BU')  
results = store.filter(query)  
print(results)

