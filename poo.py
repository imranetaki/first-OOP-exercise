class Rectangle :
    def __init__(self,longueur,largeur):
        self.longueur = longueur
        self.largeur = largeur
    
    # def __init__(self):
    #     self.longueur=0
    #     self.largeur=0
    
    # def __init__(self,R1):
    #     self.longueur=R1.longueur
    #     self.largeur=R1.largueur
    
    def perimetre(self) :
        perimetre = 2 * (self.longueur + self.largeur)
        return perimetre
    
    def aire(self) :
        aire =  (self.longueur * self.largeur)
        return aire
    
    def IsCarre(self):
        if self.largeur == self.longueur :
            return True
        else:
            return False
        
    
    def AfficheRectangle(self) :
        print(f"longueur : {self.longueur} , la largeur est {self.largeur} , le perimetre est {self.perimetre()} , l'aire est {self.aire()} " )
        if not self.IsCarre() == True :
            print("il s'agit d'un rectangle ")
        else :
            print("il s'agit d'un carré ")
            
        

    
        