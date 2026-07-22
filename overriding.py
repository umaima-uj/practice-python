class vehical:  
    def __init__ (self,name ,days):
        self.name=name
        self.days=days
            
    def calculate_rent(self):
        print("the rent of cars")
class car(vehical):
    def calculate_rent(self):
        rent=self.days* 2000
        print(f"{self.name} rent per day is 2000 and your {self.days} days rent amount is :{rent}")
class bus(vehical):
    def calculate_rent(self):
        rent=self.days*5000
        print (f"{self.name} rent per day is 5000 and your {self.days} days ammout is:{rent}")  
vehicals=[car("civic",2) , bus("faisal_movers",5)]
for vehical in vehicals:
    vehical.calculate_rent()
    print("--")
        
                        