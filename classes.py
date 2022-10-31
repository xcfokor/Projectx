
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
            print("All Enemies Dead Game Over")
            return quit()
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
            print("Armors are trying to sold to Dwarves")
        else:
            print("Armor not sold to Dwarves")
        merchant.SellArmors(self.alive,armor_point,gold)
        #Purchasing Armor
        
    def PurchaseWeapons(self,weapon_point,merchant):
        gold=0
        if self.alive:
            self.attackpoint=self.attackpoint+ weapon_point
            gold=weapon_point*10
            print("Weapons are trying to sold to Dwarves")
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
            
            print("All Enemies Dead Game Over")
            return quit() 

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
        print("Stop runnig, you""ll only die tired!")
        return super().Print()
  
    def PurchaseArmors(self,armor_point,merchant):
        gold=0
        
        if self.alive:
            self.healthpoint=self.healthpoint +3*armor_point
            gold=armor_point*1
            print("Armors are trying to sold to Orcs")
        else:
            print("Armor not sold to Orcs")
        merchant.SellArmors(self.alive,armor_point,gold)

        
    def PurchaseWeapons(self,weapon_point,merchant):
        gold=0
        
        if self.alive:
            self.attackpoint=self.attackpoint+ weapon_point*2
            gold=weapon_point*20
            print("Weapons are trying to sold to Orcs")
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
            print("All Enemies Dead Game Over")
            return quit()
            
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
            print("Armors are trying to sold to Elves")
        else:
            print("Armot not sold to Elves")
        merchant.SellArmors(self.alive,armor_point,gold)
        return

        
    def PurchaseWeapons(self,weapon_point,merchant):
        gold=0
        
        if self.alive:
            self.attackpoint=self.attackpoint+ weapon_point*2
            gold=weapon_point*15
            print("Weapons are trying to sold to Elves")
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


def start():
    print("Welcome to The Game\n")
    print("Please define your Orcs name:")
    global orcs_name
    global elves_name
    global dwarves_name
    global merchant_name
    orcs_name=input()
    
    ad=orcs_name
    orcs_name=Orcs(50,30,150,10)
    print("Your Orcs' name is: ",ad, "and properties are:")
    orcs_name.Print()
    
    print("Please define your Elves name:")
    elves_name=input()
    ad=elves_name
    elves_name=Elves(45,35,100,5)
    print("Your Elves' name is: ",ad,"and properties are:")
    elves_name.Print()

    print("Please define your Dwarves name:")
    dwarves_name=input()
    ad=dwarves_name
    dwarves_name=Dwarves(40,50,150,15)
    print("Your Dwarves' name is: ",ad,"and properties are:")
    dwarves_name.Print()

    print("Please define your Merchant name:")
    merchant_name=input()
    ad=merchant_name
    merchant_name=Merchant()
    print("Your Merchant's name is: ",ad, "and revenue is :")
    merchant_name.Print()

    
    
def action_selection(orcs_name,dwarves_name,elves_name,merchant_name):
        print("------Day Begin------\n","Choose an Action: \n","1   Print Faction information\n","2   Sell weapons\n","3   Sell armors\n","4   End the day\n","5   End the game\n","6   Quit Game\n")
        inp=input()
        if inp=="1":
            orcs_name.Print()
            print("\n")
            dwarves_name.Print()
            print("\n")
            elves_name.Print()
            print("\n")
            merchant_name.Print()
            print("\n")
            return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
        elif inp=="2":
            print("Sell weapon to who?")
            print("Choose a Faction: \n","1   Orcs\n","2   Dwarves\n","3   Elves\n","4   All\n","5   Back\n")
            select=input()
            if select=="1":
                print("Choose Weapon Point:")
                point=input()
                orcs_name.PurchaseWeapons(int(point),merchant_name)
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
                
            elif select=="2":
                print("Choose Weapon Point:")
                point=input()
                dwarves_name.PurchaseWeapons(int(point),merchant_name)
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            elif select=="3":
                print("Choose Weapon Point:")
                point=input()
                elves_name.PurchaseWeapons(int(point),merchant_name)
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            elif select=="4":
                print("Choose Weapon Point:")
                point=input()
                dwarves_name.PurchaseWeapons(int(point),merchant_name)
                elves_name.PurchaseWeapons(int(point),merchant_name)
                orcs_name.PurchaseWeapons(int(point),merchant_name)
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            elif select=="5":
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            else :
                print("Plesase choose again")
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)

        elif inp=="3":
            print("Sell armor to who?")
            print("Choose a Faction: \n","1   Orcs\n","2   Dwarves\n","3   Elves\n","4   All\n","5   Back\n")
            select=input()
            if select=="1":
                print("Choose Armor Point:")
                point=input()
                orcs_name.PurchaseArmors(int(point),merchant_name)
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            elif select=="2":
                print("Choose Armor Point:")
                point=input()
                dwarves_name.PurchaseArmors(int(point),merchant_name)
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            elif select=="3":
                print("Choose Armor Point:")
                point=input()
                elves_name.PurchaseArmors(int(point),merchant_name)
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            elif select=="4":
                print("Choose Armor Point:")
                point=input()
                dwarves_name.PurchaseArmors(int(point),merchant_name)
                elves_name.PurchaseArmors(int(point),merchant_name)
                orcs_name.PurchaseArmors(int(point),merchant_name)
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            elif select=="5":
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
            else :
                print("Plesase choose again")
                return action_selection(orcs_name,dwarves_name,elves_name,merchant_name)

        elif inp=="4":
            print("End of the day")
            orcs_name.PerformAttack()
            dwarves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()
            elves_name.PerformAttack()

            elves_name.PerformAttack()
            orcs_name.EndTurn()
            print("\n")
            dwarves_name.EndTurn()
            print("\n")
            elves_name.EndTurn()
            print("\n")
            merchant_name.EndTurn()
            print("\n")

            
        elif inp=="5":
            print("End of the game")
            orcs_name.EndTurn()
            print("\n")
            dwarves_name.EndTurn()
            print("\n")
            elves_name.EndTurn()
            print("\n")
            merchant_name.EndTurn()
            print("\n")
            
            return quit()
        elif inp=="6":
            print("Quitting the game")

            return quit()
            


start()
orcs_name.AssgnEnemies(dwarves_name,elves_name)
dwarves_name.AssgnEnemies(elves_name,orcs_name)
elves_name.AssgnEnemies(orcs_name,dwarves_name)
i=1
while True:
    
    action_selection(orcs_name,dwarves_name,elves_name,merchant_name)
    print("End of the day",i)
    input("Press Enter to continue ...")
    i=i+1




