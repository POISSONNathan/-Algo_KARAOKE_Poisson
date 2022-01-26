class Joueur:
    def __init__(self,name):
        self.__name = name
        self.__scoreChanson = 0
        self.__scoreMoyen = 0
        self.__scoreTotal = 0
        self.__meilleurScore = 0
        self.__pireScore = 100

    def getName (self):
        return self.__name

    def getScoreChanson(self,score):
        self.__scoreChanson = score 
        if self.__scoreChanson < 50:
            self.__scoreChanson = 50
        if self.__scoreChanson > 100:
            self.__scoreChanson = 100
        return self.__scoreChanson

    def getScoreMoyen(self,nombreChanson):
        self.__scoreMoyen = self.__scoreTotal / nombreChanson
        return self.__scoreMoyen

    def getScoreTotal(self):
        self.__scoreTotal += self.__scoreChanson
        return self.__scoreTotal

    def getMeilleurScore(self):
        if (self.__scoreChanson > self.__meilleurScore):
            self.__meilleurScore = self.__scoreChanson
        return self.__meilleurScore

    def getPireScore(self):
        if (self.__scoreChanson < self.__pireScore):
            self.__pireScore = self.__scoreChanson
        return self.__pireScore 

class Karaoke:
    def __init__(self,nombreJoueur,numeroChanson,meilleurScoreChanson):
        self.__nombreJoueur = nombreJoueur
        self.__numeroChanson = numeroChanson
        self.__meilleurScoreChanson = meilleurScoreChanson

    def getNumeroChanson (self):
        return self.__numeroChanson

    def getNombreJoueur (self):
        return self.__nombreJoueur

    def getMeilleurScoreChansons(self,scoreChanson):
        if scoreChanson > self.__meilleurScoreChanson:
            self.__meilleurScoreChanson = scoreChanson
        return self.__meilleurScoreChanson

joueur1 = Joueur("N")
joueur2 = Joueur("P")

chansons = Karaoke(5)

scoreChanson1 = int(input("Quel est ton score pour la 1e chanson :\n"))

joueur1.getScoreChanson(scoreChanson1)
joueur1.getScoreTotal()
joueur1.getMeilleurScore()
joueur1.getPireScore()

scoreChanson2 = int(input("Quel est ton score pour la 2e chanson :\n"))

joueur1.getScoreChanson(scoreChanson2)
joueur1.getScoreTotal()
joueur1.getMeilleurScore()
joueur1.getPireScore()

scoreChanson3 = int(input("Quel est ton score pour la 3e chanson :\n"))

joueur1.getScoreChanson(scoreChanson3)


print (joueur1.getName(), " a obtenu ", joueur1.getScoreTotal())
print (joueur1.getName(), " a pour meilleur score ",joueur1.getMeilleurScore())
print (joueur1.getName(), " a pour pire score ",joueur1.getPireScore())

