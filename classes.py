class Faction():
    def __init__(self,numberofunits,attackpoint,healthpoint,unitregenerationnumber,name="Default"):
        self.name=name
        self.numberofunits=numberofunits
        self.attackpoint=attackpoint
        self.healthpoint=healthpoint
        self.unitregenerationnumber=unitregenerationnumber
        self.total_health=self.numberofunits*self.healthpoint
        self.alive=alive=True if self.numberofunits*self.healthpoint >0 else False

    def AssgnEnemies(self):
        pass
    def PerformAttack(self):
        pass
    def ReceiveAttack(self,damage):
        self.total_health=self.total_health-damage
        return self.total_health
    def PurchaseWeapons(self):
        pass
    def PurchaseArmors(self):
        pass
    def aliveness(self):
        return self.alive
    def Print(self):
        print("Faction Name: ",self.name,"\n","Status: ",format("Alive" if self.alive else "Defeated"),"\n","Number of Units: ",self.numberofunits,"\n","Attack Point: ",self.attackpoint,"\n","Health Point: ",self.healthpoint,"\n","Unit Regen Number: ",self.unitregenerationnumber,"\n","Total Faction Health:",self.total_health)        
    def EndTurn(self):
        if self.numberofunits<=0 or self.total_health<=0:
            self.numberofunits=0
            self.total_health=0
            self.alive=False
            
        return self.numberofunits,self.total_health

        
    



obje=Faction(50,30,150,10)

class Dwarves(Faction):
    def __init__(self, numberofunits, attackpoint, healthpoint, unitregenerationnumber, name="Dwarves"):
        super().__init__(numberofunits, attackpoint, healthpoint, unitregenerationnumber, name)
    
    def PerformAttack(self):
        if (Orcs.aliveness() and not Elves.aliveness()) or (not Orcs.aliveness() and Elves.aliveness() ):
            damage= numberofunits*attackpoint
        elif Orcs.aliveness() and Elves.aliveness():
            damage=numberofunits*attackpoint/2
        return damage , self.name
        #attack who?
    def Print(self):
        print("Taste the power of our axes!")
        return super().Print()
    def ReceiveAttack(self,damage):
        self.numberofunits=self.numberofunits-(damage/self.healthpoint)
        return super().ReceiveAttack()
    def PurchaseArmors(self):
        return super().PurchaseArmors()
    def PurchaseWeapons(self):
        return super().PurchaseWeapons()

class Orcs(Faction):
    def __init__(self, numberofunits, attackpoint, healthpoint, unitregenerationnumber, name="Orcs"):
        super().__init__(numberofunits, attackpoint, healthpoint, unitregenerationnumber, name)
    
    def PerformAttack(self):
        if (Orcs.aliveness() and not Elves.aliveness()) or (not Orcs.aliveness() and Elves.aliveness() ):
            damage= numberofunits*attackpoint
        elif Orcs.aliveness() and Elves.aliveness():
            #attack who?
            damage=numberofunits*attackpoint*0.7
            damage=numberofunits*attackpoint*0.3
        return damage
    def ReceiveAttack(self, damage):
        #attack from who?
        return super().ReceiveAttack(damage)
    
    def Print(self):
        print("Stop runnig, you""ll only die tired!\n")
        return super().Print()
  
    def PurchaseArmors(self):
        return super().PurchaseArmors()
    def PurchaseWeapons(self):
        return super().PurchaseWeapons()

class Elves(Faction):
    def __init__(self, numberofunits, attackpoint, healthpoint, unitregenerationnumber, name="Elves"):
        super().__init__(numberofunits, attackpoint, healthpoint, unitregenerationnumber, name)
    
    def PerformAttack(self):
        if (Dwarves.alivenesss() and not Elves.aliveness()) or (not Dwarves.aliveness() and Elves.aliveness() ):
            damage= numberofunits*attackpoint
        elif Dwarves.aliveness() and Elves.aliveness():
            #attack who?
            damage=numberofunits*attackpoint*0.6
            damage=numberofunits*attackpoint*0.4
    def ReceiveAttack(self, damage):
        #attack from who?
        return super().ReceiveAttack(damage)
    def Print(self):
        print("You cannot reach our elegance.")
        return super().Print()

    def PurchaseArmors(self):
        return super().PurchaseArmors()
    def PurchaseWeapons(self):
        return super().PurchaseWeapons()

class Merchant():
    def __init__(self,starting_weapon_point,starting_armor_point,):
        self.starting_weapon_point=starting_weapon_point
        self.starting_armor_point=starting_armor_point
    
savaşçı= Orcs(50,30,150,10)
navin=Dwarves(40,30,150,15)
thor=Elves(45,35,150,5)

savaşçı.EndTurn()
savaşçı.Print()