class Faction():
   
    def __init__(self,numberofunits,attackpoint,healthpoint,unitregenerationnumber,name="Default"):
        self.name=name
        self.numberofunits=numberofunits
        self.attackpoint=attackpoint
        self.healthpoint=healthpoint
        self.unitregenerationnumber=unitregenerationnumber
        self.total_health=self.numberofunits*self.healthpoint
        self.alive=alive=True if self.numberofunits*self.healthpoint >0 else False

    def AssgnEnemies(self,enemy_name1,enemy_name2):
        self.firstEnemy = enemy_name1
        self.secondEnemy = enemy_name2
        
        
        
    # def PerformAttack(self):
    #     self.firstEnemy.ReceiveAttack(self,self.attackpoint)
    #     return
        
    # def ReceiveAttack(self,damage):
    #     self.total_health=self.total_health-damage
    #     return self.total_health
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


class Dwarves(Faction):
    
    
    def __init__(self, numberofunits, attackpoint, healthpoint, unitregenerationnumber, name="Dwarves"):
        super().__init__(numberofunits, attackpoint, healthpoint, unitregenerationnumber, name)
    
    def PerformAttack(self):
        if self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            self.firstEnemy.ReceiveAttack(self,self.attackpoint/2)
            self.secondEnemy.ReceiveAttack(self,self.attackpoint/2)
        elif self.firstEnemy.aliveness() and not self.secondEnemy.aliveness():
            self.firstEnemy.ReceiveAttack(self,self.attackpoint)
        elif  not self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            self.secondEnemy.ReceiveAttack(self,self.attackpoint)
        return
        
        
    def Print(self):
        print("Taste the power of our axes!")
        return super().Print()
    def ReceiveAttack(self,attacker,damage):
        self.numberofunits=self.numberofunits-(damage/self.healthpoint)
        if type(attacker)==Orcs:
            print("Dwarves have received attack from Orcs")
        elif type(attacker)==Elves:
            print("Dwarvevs have received attack from Elves")
        
    def PurchaseArmors(self):
        return super().PurchaseArmors()
    def PurchaseWeapons(self):
        return super().PurchaseWeapons()

class Orcs(Faction):
    def __init__(self, numberofunits, attackpoint, healthpoint, unitregenerationnumber, name="Orcs"):
        super().__init__(numberofunits, attackpoint, healthpoint, unitregenerationnumber, name)
    
    def PerformAttack(self):
        if self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            if type(self.firstEnemy)== Elves:
                self.firstEnemy.ReceiveAttack(self,self.attackpoint*0.7)
                self.secondEnemy.ReceiveAttack(self,self.attackpoint*0.3)
            elif type(self.secondEnemy)==Elves:
                self.secondEnemy.ReceiveAttack(self,self.attackpoint*0.7)
                self.firstEnemy.ReceiveAttack(self,self.attackpoint*0.3)
        elif self.firstEnemy.aliveness() and not self.secondEnemy.aliveness():
            self.firstEnemy.ReceiveAttack(self,self.attackpoint)
        elif  not self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            self.secondEnemy.ReceiveAttack(self,self.attackpoint)
    def ReceiveAttack(self,attacker, damage):
        if type(attacker)==Dwarves:
            print("Orcs have received attack from Dwarves")
        elif type(attacker)==Elves:
            print("Orcs have received attack from Elves")
    
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
    
    # def PerformAttack(self):
    #     if (Dwarves.alivenesss() and not Elves.aliveness()) or (not Dwarves.aliveness() and Elves.aliveness() ):
    #         damage= numberofunits*attackpoint
    #     elif Dwarves.aliveness() and Elves.aliveness():
    #         #attack who?
    #         damage=numberofunits*attackpoint*0.6
    #         damage=numberofunits*attackpoint*0.4
    def ReceiveAttack(self,attacker, damage):
        if type(attacker)==Orcs:
            print("Elves have received attack from Orcs")
        elif type(attacker)==Dwarves:
            print("Elves have received attack from Dwarves")

   
    def Print(self):
        print("You cannot reach our elegance.")
        return super().Print()

    def PurchaseArmors(self):
        return super().PurchaseArmors()
    def PurchaseWeapons(self):
        return super().PurchaseWeapons()

# class Merchant():
    # def __init__(self,starting_weapon_point,starting_armor_point):
    #     self.starting_weapon_point=starting_weapon_point
    #     self.starting_armor_point=starting_armor_point
    #     self.revenue=0
    # weapon_point=starting_weapon_point
    # def AssgnFactions():
    #     pass
    # def SellWeapons():
    #     pass
    # def SellArmors():
    #     pass
    # def EndTurn():
    #     pass
    
savasci= Orcs(50,30,150,10)
navin=Dwarves(40,30,150,15)
thor=Elves(45,35,150,5)



savasci.AssgnEnemies(navin, thor)
navin.Print()
savasci.PerformAttack()
savasci.EndTurn()
navin.Print()