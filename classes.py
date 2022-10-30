


class Faction():
   
    def __init__(self,numberofunits,attackpoint,healthpoint,unitregenerationnumber,name="Default"):
        self.name=name
        self.numberofunits=numberofunits
        self.attackpoint=attackpoint
        self.healthpoint=healthpoint
        self.unitregenerationnumber=unitregenerationnumber
        self.total_health=self.numberofunits*self.healthpoint
        self.alive=alive=True if self.numberofunits*self.healthpoint >0 else False
    #Some attributes initially introduced.

    def AssgnEnemies(self,enemy_name1,enemy_name2):
        self.firstEnemy = enemy_name1
        self.secondEnemy = enemy_name2
    #Enemies are assigned.

    def aliveness(self):
        return self.alive
    #Return aliveness

    def Print(self):
        print("Faction Name: ",self.name,"\n","Status: ",format("Alive" if self.alive else "Defeated"),"\n","Number of Units: ",self.numberofunits,"\n","Attack Point: ",self.attackpoint,"\n","Health Point: ",self.healthpoint,"\n","Unit Regen Number: ",self.unitregenerationnumber,"\n","Total Faction Health:",self.total_health)        
    #Print Faction information

    def EndTurn(self):
        if self.numberofunits<=0 or self.total_health<=0:
            self.numberofunits=0
            self.total_health=0
            self.alive=False
            
        return self.numberofunits,self.total_health
        #Endturn


class Dwarves(Faction):
    
    
    def __init__(self, numberofunits, attackpoint, healthpoint, unitregenerationnumber, name="Dwarves"):
        super().__init__(numberofunits, attackpoint, healthpoint, unitregenerationnumber, name)
    
    def PerformAttack(self):
        if self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint/2)
            self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint/2)
        elif self.firstEnemy.aliveness() and not self.secondEnemy.aliveness():
            self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint)
        elif  not self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint)
        else:
            print("All Enemies Dead")  
        #Performing attack
        
    def Print(self):
        print("Taste the power of our axes!")
        return super().Print()

    def ReceiveAttack(self,attacker,damage):
        self.numberofunits=self.numberofunits-(damage/self.healthpoint)
        if type(attacker)==Orcs:
            print("Dwarves have received attack from Orcs")
        elif type(attacker)==Elves:
            print("Dwarvevs have received attack from Elves")
        self.total_health=self.numberofunits*self.healthpoint
        if self.numberofunits<=0 or self.total_health<=0:
            self.numberofunits=0
            self.total_health=0
            self.alive=False
        #Receiving Attack

    def PurchaseArmors(self,armor_point,merchant):
        gold=0
        if self.alive:
            self.healthpoint=self.healthpoint +2*armor_point
            gold=armor_point*3
            print("Armor sold to Dwarves")
        else:
            print("Armor not sold to Dwarves")
        merchant.SellArmors(self.alive,armor_point,gold)
        #Purchasing Armor
        
    def PurchaseWeapons(self,weapon_point,merchant):
        gold=0
        if self.alive:
            self.attackpoint=self.attackpoint+ weapon_point
            gold=weapon_point*10
            print("Weapon sold to Dwarves")
        else:
            print("Weapon not sold to Dwarves")
        merchant.SellWeapons(self.alive,weapon_point,gold)
        #Purchasing Weapon

class Orcs(Faction):
    def __init__(self, numberofunits, attackpoint, healthpoint, unitregenerationnumber, name="Orcs"):
        super().__init__(numberofunits, attackpoint, healthpoint, unitregenerationnumber, name)
    
    def PerformAttack(self):
        if self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            if type(self.firstEnemy)== Elves:
                self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*0.7)
                self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*0.3)
            elif type(self.secondEnemy)==Elves:
                self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*0.7)
                self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*0.3)
        elif self.firstEnemy.aliveness() and not self.secondEnemy.aliveness():
            self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint)
        elif  not self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint)
        else:
            print("All Enemies Dead") 

    def ReceiveAttack(self,attacker, damage):
        if type(attacker)==Dwarves:
            damage=damage*0.8
            self.numberofunits=self.numberofunits-(damage/self.healthpoint)
            print("Orcs have received attack from Dwarves")
        elif type(attacker)==Elves:
            damage=damage*0.75
            self.numberofunits=self.numberofunits-(damage/self.healthpoint)
            print("Orcs have received attack from Elves")
        
        self.total_health=self.numberofunits*self.healthpoint
        if self.numberofunits<=0 or self.total_health<=0:
            self.numberofunits=0
            self.total_health=0
            self.alive=False
    
    def Print(self):
        print("Stop runnig, you""ll only die tired!\n")
        return super().Print()
  
    def PurchaseArmors(self,armor_point,merchant):
        gold=0
        
        if self.alive:
            self.healthpoint=self.healthpoint +3*armor_point
            gold=armor_point*1
            print("Armor sold to Orcs")
        else:
            print("Armor not sold to Orcs")
        merchant.SellArmors(self.alive,armor_point,gold)

        
    def PurchaseWeapons(self,weapon_point,merchant):
        gold=0
        
        if self.alive:
            self.attackpoint=self.attackpoint+ weapon_point*2
            gold=weapon_point*20
            print("Weapon sold to Orcs")
        else:
            print("Weapon not sold to Orcs")
        merchant.SellWeapons(self.alive,weapon_point,gold)
        

class Elves(Faction):
    def __init__(self, numberofunits, attackpoint, healthpoint, unitregenerationnumber, name="Elves"):
        super().__init__(numberofunits, attackpoint, healthpoint, unitregenerationnumber, name)
    
    def PerformAttack(self):
        
        if self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            if type(self.firstEnemy)== Orcs:
                self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*0.6)
                self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*0.4*1.5)
            elif type(self.secondEnemy)==Orcs:
                self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*0.6)
                self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*0.4*1.5)
        elif self.firstEnemy.aliveness() and not self.secondEnemy.aliveness():
            if type(self.firstEnemy)== Dwarves:
                self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*1.5)
            else:
                self.firstEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint)
        elif  not self.firstEnemy.aliveness() and self.secondEnemy.aliveness():
            if type(self.secondEnemy)== Dwarves:
                self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint*1.5)
            else:
                self.secondEnemy.ReceiveAttack(self,self.numberofunits*self.attackpoint)
        else:
            print("All Enemies Dead")   
            
    def ReceiveAttack(self,attacker, damage):
        if type(attacker)==Orcs:
            damage=damage*1.25
            self.numberofunits=self.numberofunits-(damage/self.healthpoint)
            print("Elves have received attack from Orcs")
        elif type(attacker)==Dwarves:
            damage=damage*0.75
            self.numberofunits=self.numberofunits-(damage/self.healthpoint)
            print("Elves have received attack from Dwarves")
        self.total_health=self.numberofunits*self.healthpoint
        if self.numberofunits<=0 or self.total_health<=0:
            self.numberofunits=0
            self.total_health=0
            self.alive=False
   
    def Print(self):
        print("You cannot reach our elegance.")
        return super().Print()

    def PurchaseArmors(self,armor_point, merchant):
        gold=0
        if self.alive:
            self.healthpoint=self.healthpoint +4*armor_point
            gold=armor_point*5
            print("Armor sold to Elves")
        else:
            print("Armot not sold to Elves")
        merchant.SellArmors(self.alive,armor_point,gold)
        return

        
    def PurchaseWeapons(self,weapon_point,merchant):
        gold=0
        
        if self.alive:
            self.attackpoint=self.attackpoint+ weapon_point*2
            gold=weapon_point*15
            print("Weapon sold to Elves")
        else:
            print("Weapon not sold to Elves")
        merchant.SellWeapons(self.alive,weapon_point,gold)
        return
        


class Merchant():
    def __init__(self,starting_weapon_point=10,starting_armor_point=10):
        self.weapon_point=starting_weapon_point
        self.armor_point=starting_armor_point
        self.starting_weapon_point=starting_weapon_point
        self.starting_armor_point=starting_armor_point
        self.revenue=0
    
    def AssgnFactions(self,faction1_name,faction2_name):
        self.faction1=faction1_name
        self.faction2=faction2_name

    def SellWeapons(self,live,weapon_value,gold):
        self.revenue=self.revenue+gold
        if not live :
            print("The faction you want to sell weapons is dead!")
            return False
        elif live and self.weapon_point< weapon_value:
            print("You try to sell more weapons than you have in possession.")
            return False
        elif live and self.weapon_point >= weapon_value:
            self.weapon_point=self.weapon_point-weapon_value
            print("Weapons sold!")
            return True
    #Selling Weapon

    def SellArmors(self,live,armor_value,gold):
        self.revenue=self.revenue+gold
        if not live :
            print("The faction you want to sell armor is dead!")
            return False
        elif live and self.armor_point< armor_value:
            print("You try to sell more armors than you have in possession.")
            return False
        elif live and self.armor_point >= armor_value:
            self.armor_point=self.armor_point- armor_value
            print("Armors sold!")
            return True
        #Selling Armor

    def Print(self):
        print("Profit: ",self.revenue,"")

    def EndTurn(self):
        self.weapon_point= self.starting_weapon_point
        self.armor_point= self.starting_armor_point
        print("Profit:",self.revenue)
    
savasci= Orcs(50,30,150,10)#defining objects
navin=Dwarves(40,50,150,15)
joker=Dwarves(60,50,80,15)
thor=Elves(45,35,100,5)
demirci=Merchant()


navin.AssgnEnemies(savasci, thor)#Assign Enemies
thor.AssgnEnemies(savasci,navin)
thor.AssgnEnemies(navin,joker)
savasci.AssgnEnemies(navin,thor)
joker.AssgnEnemies(savasci,thor)

print("BAşlangıç")
savasci.Print()
thor.Print()
navin.Print()
joker.Print()
demirci.Print()


navin.PerformAttack()
thor.PerformAttack()
savasci.PerformAttack()
navin.PerformAttack()
thor.PerformAttack()
savasci.PerformAttack()
navin.PerformAttack()
thor.PerformAttack()
savasci.PerformAttack()
joker.PerformAttack()

joker.Print()
savasci.Print()
thor.Print()
navin.Print()
demirci.Print()

savasci.EndTurn()
thor.EndTurn()
navin.EndTurn()
demirci.EndTurn()
joker.EndTurn()

print("satın alımlar")

savasci.PurchaseWeapons(2,demirci)
thor.PurchaseArmors(5,demirci)
thor.PurchaseWeapons(6,demirci)
navin.PurchaseWeapons(7,demirci)

savasci.Print()
thor.Print()
navin.Print()
demirci.Print()

navin.PerformAttack()
thor.PerformAttack()
savasci.PerformAttack()

savasci.EndTurn()
thor.EndTurn()
navin.EndTurn()
demirci.EndTurn()

print("2.tur bitti")
savasci.Print()
thor.Print()
navin.Print()
demirci.Print()

