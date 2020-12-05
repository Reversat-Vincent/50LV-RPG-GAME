#!/usr/bin/python
# -*-coding:Utf-8 -*

import pygame
from pygame.locals import *
from math import *
from random import *

pygame.init()
#820,600 soit 2/3 de la taille originelle des images de fond
window = pygame.display.set_mode((820,600))
#fps control
clock = pygame.time.Clock()
#mouse control
pygame.key.set_repeat(10, 10)

# phase
phase = pygame.image.load("phase.png").convert_alpha()
phasePlayer = pygame.Surface((200,200),SRCALPHA)
phasePlayer.blit(phase, (0,0), (0, 0, 200, 200))
phaseEnemy = pygame.Surface((200,200),SRCALPHA)
phaseEnemy.blit(phase, (0,0), (0, 200, 200, 200))

# dégat
degatImg = pygame.image.load("chiffreDegat.png").convert_alpha()
degat0 = pygame.Surface((56,64),SRCALPHA)
degat0.blit(degatImg, (0,0), (56*0, 0, 56, 64))
degat1 = pygame.Surface((56,64),SRCALPHA)
degat1.blit(degatImg, (0,0), (56*1, 0, 56, 64))
degat2 = pygame.Surface((56,64),SRCALPHA)
degat2.blit(degatImg, (0,0), (56*2, 0, 56, 64))
degat3 = pygame.Surface((56,64),SRCALPHA)
degat3.blit(degatImg, (0,0), (56*3, 0, 56, 64))
degat4 = pygame.Surface((56,64),SRCALPHA)
degat4.blit(degatImg, (0,0), (56*4, 0, 56, 64))
degat5 = pygame.Surface((56,64),SRCALPHA)
degat5.blit(degatImg, (0,0), (56*5, 0, 56, 64))
degat6 = pygame.Surface((56,64),SRCALPHA)
degat6.blit(degatImg, (0,0), (56*6, 0, 56, 64))
degat7 = pygame.Surface((56,64),SRCALPHA)
degat7.blit(degatImg, (0,0), (56*7, 0, 56, 64))
degat8 = pygame.Surface((56,64),SRCALPHA)
degat8.blit(degatImg, (0,0), (56*8, 0, 56, 64))
degat9 = pygame.Surface((56,64),SRCALPHA)
degat9.blit(degatImg, (0,0), (56*9, 0, 56, 64))


# soin
soinImg = pygame.image.load("chiffreSoin.png").convert_alpha()
soin0 = pygame.Surface((56,64),SRCALPHA)
soin0.blit(soinImg, (0,0), (56*0, 0, 56, 64))
soin1 = pygame.Surface((56,64),SRCALPHA)
soin1.blit(soinImg, (0,0), (56*1, 0, 56, 64))
soin2 = pygame.Surface((56,64),SRCALPHA)
soin2.blit(soinImg, (0,0), (56*2, 0, 56, 64))
soin3 = pygame.Surface((56,64),SRCALPHA)
soin3.blit(soinImg, (0,0), (56*3, 0, 56, 64))
soin4 = pygame.Surface((56,64),SRCALPHA)
soin4.blit(soinImg, (0,0), (56*4, 0, 56, 64))
soin5 = pygame.Surface((56,64),SRCALPHA)
soin5.blit(soinImg, (0,0), (56*5, 0, 56, 64))
soin6 = pygame.Surface((56,64),SRCALPHA)
soin6.blit(soinImg, (0,0), (56*6, 0, 56, 64))
soin7 = pygame.Surface((56,64),SRCALPHA)
soin7.blit(soinImg, (0,0), (56*7, 0, 56, 64))
soin8 = pygame.Surface((56,64),SRCALPHA)
soin8.blit(soinImg, (0,0), (56*8, 0, 56, 64))
soin9 = pygame.Surface((56,64),SRCALPHA)
soin9.blit(soinImg, (0,0), (56*9, 0, 56, 64))


# vivant=1 / mort=0
class SkinActifDeath:
	def __init__(self):
		self.skin1 = 1
		self.skin2 = 1
		self.skin3 = 1
		self.skin4 = 1
		self.skin5 = 1
		self.skin6 = 1
		self.skin7 = 1
		self.skin8 = 1

skinActifDeath = SkinActifDeath()


# unité du joueur
class Actor:
	def __init__(self, name, face, sprite, skin, niv, exp, pointStat, PV_max, PV, For, Vit, Def):
		self.name = name
		self.face = face
		self.sprite = sprite
		self.skin = skin
		self.niv = niv #1->50
		self.exp = exp # --> 100
		self.pointStat = pointStat #2.5 point / niv  -->  125 point au total soit ~ all stat = 40
		self.PV_max = PV_max # PV max en fonction du niv, f(X):((X^0.7)*3.25)+10
		self.PV = PV
		self.For = For # stat limit = niv*1.4
		self.Vit = Vit
		self.Def = Def

actor1 = Actor("Pseudo", "actor1f.png", "actor1s.png", 1, 5, 0, 13, 20, 20, 5, 5, 5)
actor2 = Actor("Pseudo", "actor2f.png", "actor2s.png", 2, 5, 0, 13, 20, 20, 5, 5, 5)
actor3 = Actor("Pseudo", "actor3f.png", "actor3s.png", 3, 5, 0, 13, 20, 20, 5, 5, 5)
actor4 = Actor("Pseudo", "actor4f.png", "actor4s.png", 4, 5, 0, 13, 20, 20, 5, 5, 5)
actor5 = Actor("Pseudo", "actor5f.png", "actor5s.png", 5, 5, 0, 13, 20, 20, 5, 5, 5)
actor6 = Actor("Pseudo", "actor6f.png", "actor6s.png", 6, 5, 0, 13, 20, 20, 5, 5, 5)
actor7 = Actor("Pseudo", "actor7f.png", "actor7s.png", 7, 5, 0, 13, 20, 20, 5, 5, 5)
actor8 = Actor("Pseudo", "actor8f.png", "actor8s.png", 8, 5, 0, 13, 20, 20, 5, 5, 5)


# inventaire du joueur
class Inv:
	def __init__(self):
		self.Item1 = "Potion Verte Niv1" #objet
		self.Item1Q = 20 #quantité
		self.Item1E = 1 #efficacité (PV rendu = 10*eff)
		self.Item2 = "Potion Rouge Niv1"
		self.Item2Q = 15
		self.Item2E = 2
		self.Item3 = "Potion Verte Niv2"
		self.Item3Q = 10
		self.Item3E = 3
		self.Item4 = "Potion Rouge Niv2"
		self.Item4Q = 5
		self.Item4E = 6

inv = Inv()


# ennemi
class Monstre:
	def __init__(self, name, face, sprite, PV, For, Vit, Def):
		self.name = name
		self.face = face
		self.sprite = sprite
		self.PV = PV # PV max en fonction du niv, f(X):((X^0.7)*2.6)+10
		self.For = For # stats × 20%niv
		self.Vit = Vit
		self.Def = Def

monstre1 = Monstre("Spectre", "monstre1f.png", "monstre1s.png", 1, 2.5, 2, 2) # faible
monstre2 = Monstre("Squelette", "monstre2f.png", "monstre2s.png", 1, 2.5, 1.5, 3) # +D =V -F
monstre3 = Monstre("Orc", "monstre3f.png", "monstre3s.png", 1, 3.5, 1, 2.5) # +F =D -V
monstre4 = Monstre("Gargouille", "monstre4f.png", "monstre4s.png", 1, 2.5, 3.5, 1) # +V =F -D
monstre5 = Monstre("Djinn", "monstre5f.png", "monstre5s.png", 1.2, 4, 1.5, 2.5) # +F =D -V
monstre6 = Monstre("Ondine", "monstre6f.png", "monstre6s.png", 1.2, 3, 1.5, 3.5) # +D =V -F
monstre7 = Monstre("Faucheur", "monstre7f.png", "monstre7s.png", 1.2, 2.5, 4, 1.5) # +V =F -D
monstre8 = Monstre("Vampire", "monstre8f.png", "monstre8s.png", 1.2, 3, 3, 3) # fort

boss1 = Monstre("Assassin", "boss1f.png", "boss1s.png", 1.4, 2.5, 3.5, 2.5) # +V
boss2 = Monstre("Caster", "boss2f.png", "boss2s.png", 1.4, 3.5, 2.5, 2.5) # +F
boss3 = Monstre("Saber", "boss3f.png", "boss3s.png", 1.4, 2.5, 2.5, 3.5) # +D
boss4 = Monstre("Berserker", "boss4f.png", "boss4s.png", 1.6, 3, 3, 3) # +fort
boss5 = Monstre("Dragon", "boss5f.png", "boss5s.png", 2, 4, 3, 3.5) # +++fort


#font
police = pygame.font.SysFont("arial", 30)
caraNameDisplay = police.render("Arcanin", True, (0,0,0))



#fenêtre de status
def status(offset,skinActif):
	"""
	:precond:
	:postcond: ne retourne rien

	menu de transition entre :
		- combat
		- sauvegarde
		- quit
	"""

	stageLock = [0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] #enregistre les stages débloqués

	menuLoop = 1
	while menuLoop:
		#speed limit of loop
		clock.tick(30)

		exec("cara = actor"+str(skinActif))

		if cara.niv < 15: #change le fond suivant le niveau du personnage
			fond = pygame.image.load("0.png").convert()
		elif cara.niv < 30:
			fond = pygame.image.load("15.png").convert()
		elif cara.niv < 40:
			fond = pygame.image.load("30.png").convert()
		elif cara.niv < 50:
			fond = pygame.image.load("40.png").convert()
		else:
			fond = pygame.image.load("50.png").convert()

		fond = pygame.transform.scale(fond, (820,600)) #ajuste la taille du fond
		window.blit(fond,(0,0))
		
		#affichage des données du personnage
		caraNameBox = pygame.draw.rect(window,(205,133,63),pygame.Rect(15,15,320,96+6*44))
		window.blit(caraNameDisplay,(115,22))
		stop = pygame.image.load("stop.png").convert_alpha()
		window.blit(stop,(300,25))
		caraPVDisplay = police.render("PV : "+str(cara.PV)+"/"+str(cara.PV_max), True, (0,0,0))
		window.blit(caraPVDisplay,(115,62))

		caraNivDisplay = police.render("Niv : "+str(cara.niv), True, (0,0,0))
		window.blit(caraNivDisplay,(20,116))
		caraExpDisplay = police.render("Exp : "+str(cara.exp), True, (0,0,0))
		window.blit(caraExpDisplay,(20,160))
		caraPointsStatDisplay = police.render("Points : "+str(cara.pointStat), True, (0,0,0))
		window.blit(caraPointsStatDisplay,(20,204))

		arrowUP = pygame.image.load("arrow_up.png").convert_alpha()
		caraForDisplay = police.render("For : "+str(cara.For), True, (0,0,0))
		window.blit(caraForDisplay,(20,248))
		window.blit(arrowUP,(20+caraForDisplay.get_width()+15,248+9))
		caraVitDisplay = police.render("Vit : "+str(cara.Vit), True, (0,0,0))
		window.blit(caraVitDisplay,(20,292))
		window.blit(arrowUP,(20+caraVitDisplay.get_width()+15,292+9))
		caraDefDisplay = police.render("Def : "+str(cara.Def), True, (0,0,0))
		window.blit(caraDefDisplay,(20,336))
		window.blit(arrowUP,(20+caraDefDisplay.get_width()+15,336+9))

		caraFace = pygame.image.load(cara.face).convert_alpha()
		window.blit(caraFace,(15,15))
		caraSprite = pygame.image.load(cara.sprite).convert_alpha()
		window.blit(caraSprite,(189,129))

		arrow = pygame.image.load("arrow.png").convert_alpha()
		window.blit(arrow,(189+96,129+(96/2)-(arrow.get_height()/2)))
		window.blit(pygame.transform.rotate(arrow,180),(189-arrow.get_width(),129+(96/2)-(arrow.get_height()/2)))


		#affichage des stages
		stageBlock = pygame.image.load("block.png").convert_alpha()
		stageNum = 0
		stageBox = pygame.draw.rect(window,(205,133,63),pygame.Rect(window.get_width()-15-320,15,320,570))
		stageBoxSub = pygame.Surface((320,56*25),SRCALPHA)
		stageGBox = stageBoxSub.subsurface(0,0,320,570)
		for n in xrange(1,50+1):
			exec("stageBox"+str(n)+" = pygame.image.load(\"stageBox.png\").convert_alpha()")

			pass

		s=0
		for y in xrange(1,25+1):
			for x in xrange(1,2+1):
				s+=1
				exec("stageGBox.blit(stageBox"+str(s)+", ("+str((x*5)+((x-1)*5)+((x-1)*150))+","+str((y*5)+((y-1)*5)+((y-1)*46)-offset)+"), (0, 0, 150, 46))")
				if s<10:
					exec("stageGBox.blit(police.render(\"Stage "+str(s)+"\", True, (0,0,0)), ("+str((x*5)+((x-1)*5)+((x-1)*150))+"+stageBox"+str(s)+".get_width()/2-102/2, "+str((y*5)+((y-1)*5)+((y-1)*46)-offset)+"+stageBox"+str(s)+".get_height()/2-34/2), (0, 0, 150, 46))")
				else:
					exec("stageGBox.blit(police.render(\"Stage "+str(s)+"\", True, (0,0,0)), ("+str((x*5)+((x-1)*5)+((x-1)*150))+"+stageBox"+str(s)+".get_width()/2-120/2, "+str((y*5)+((y-1)*5)+((y-1)*46)-offset)+"+stageBox"+str(s)+".get_height()/2-34/2), (0, 0, 150, 46))")
				if stageLock[s-1]:
					exec("stageGBox.blit(stageBlock, ("+str((x*5)+((x-1)*5)+((x-1)*150))+","+str((y*5)+((y-1)*5)+((y-1)*46)-offset)+"), (0, 0, 150, 46))")
				pass
			pass
		window.blit(stageGBox,(window.get_width()-15-320,15))

		#action du joueur
		mousePos = pygame.mouse.get_pos()

		for event in pygame.event.get():
			if event.type == MOUSEBUTTONUP:
				if event.button == 1:
					if mousePos[0] > 300 and mousePos[0] < 300+stop.get_width() and mousePos[1] > 25 and mousePos[1] < 25+stop.get_height(): #arrêt du jeu
						menuLoop = 0
					if mousePos[0] > 20+caraForDisplay.get_width()+15 and mousePos[0] < 20+caraForDisplay.get_width()+15+arrowUP.get_width() and mousePos[1] > 248+9 and mousePos[1] < 248+9+arrowUP.get_height(): #agmentation de la stat de For
						if cara.pointStat > 0:
							cara.For+=1
							cara.pointStat-=1
					if mousePos[0] > 20+caraVitDisplay.get_width()+15 and mousePos[0] < 20+caraVitDisplay.get_width()+15+arrowUP.get_width() and mousePos[1] > 292+9 and mousePos[1] < 292+9+arrowUP.get_height(): #agmentation de la stat de Vit
						if cara.pointStat > 0:
							cara.Vit+=1
							cara.pointStat-=1
					if mousePos[0] > 20+caraDefDisplay.get_width()+15 and mousePos[0] < 20+caraDefDisplay.get_width()+15+arrowUP.get_width() and mousePos[1] > 336+9 and mousePos[1] < 336+9+arrowUP.get_height(): #agmentation de la stat de Def
						if cara.pointStat > 0:
							cara.Def+=1
							cara.pointStat-=1
					if mousePos[0] > 189+96 and mousePos[0] < 189+96+arrow.get_width() and mousePos[1] > 129+(96/2)-(arrow.get_height()/2) and mousePos[1] < 129+(96/2)-(arrow.get_height()/2)+arrow.get_height(): #changement de personnage vers la gauche
						if skinActif < 8:
							skinActif+=1
							exec("skinTest = skinActifDeath.skin"+str(skinActif))
							while skinTest == 0:
								skinActif+=1
								if skinActif == 9:
									skinActif = cara.skin
									pass
								exec("skinTest = skinActifDeath.skin"+str(skinActif))
								pass
					if mousePos[0] > 189-arrow.get_width() and mousePos[0] < 189 and mousePos[1] > 129+(96/2)-(arrow.get_height()/2) and mousePos[1] < 129+(96/2)-(arrow.get_height()/2)+arrow.get_height(): #changement de personnage vers la droite
						if skinActif > 1:
							skinActif-=1
							exec("skinTest = skinActifDeath.skin"+str(skinActif))
							while skinTest == 0:
								skinActif-=1
								if skinActif == 0:
									skinActif = cara.skin
									pass
								exec("skinTest = skinActifDeath.skin"+str(skinActif))
								pass
					for z in xrange(1,50+1): #sélection du stage
						if mousePos[0] > window.get_width()-15-320+5+(10+150)*abs((z%2)-1) and mousePos[0] < window.get_width()-15-320+5+150+(10+150)*abs((z%2)-1) and mousePos[1] > 15+5+(((z+1)//2)-1)*10+(((z+1)//2)-1)*46-offset and mousePos[1] < 15+5+(((z+1)//2))*10+(((z+1)//2))*46-offset:
							if stageLock[z-1] == 0:
								stageNum = z
								pass
							pass
						pass

				if event.button == 4: #scroll menu stage
					if offset > 0:
						offset = offset - 5
				if event.button == 5: #scroll menu stage
					if offset < 830:
						offset = offset + 5

		exec("skinTestCombatAutoriser = skinActifDeath.skin"+str(skinActif))
		win = 0
		if stageNum and skinTestCombatAutoriser:
			if stageNum % 10 == 0: #vérifi le stage choisi pour décider si c'est le stage d'un boss ou pas
				nivByStage = stageNum
				exec("win = combat(stageNum,nivByStage,boss"+str(stageNum//10)+",cara)") #lance un combat contre un boss
			else:
				if stageNum < 15: #choisi un monstre aléatoire
					montreNum = randint(1,4)
				elif stageNum > 35:
					montreNum = randint(5,8)
				else:
					montreNum = randint(1,8)

				nivByStage = randint(stageNum-(stageNum//10),stageNum+5-(stageNum//10))
				exec("win = combat(stageNum,nivByStage,monstre"+str(montreNum)+",cara)") #lance un combat contre un monstre
		if win and (stageNum != 50):
			stageLock[stageNum] = 0 #unlock le prochain stage
			pass

		pygame.display.flip()

	return 0



def affichageStage(stage, nPhase, m, mn, mpvm, mpv, mf, mv, md, cara): #gère l'affichage du combat
	"""
	:precond:stage:int type stage, nPhase:str phase du combat, m:obj monstre, mn:int monstre niv, mpvm:int monstre PV max, mpv:int monstre PV, mf:int, mv:int, md:int montre stats
	:postcond:
	"""
	fond = pygame.image.load("stage"+str(stage)+".png").convert() #affiche le fond
	fond = pygame.transform.scale(fond, (820,600))
	window.blit(fond,(0,0))

	if nPhase == "player": #affiche la phase
		window.blit(phasePlayer,(window.get_width()/2-200/2,100))
	elif nPhase == "enemy":
		window.blit(phaseEnemy,(window.get_width()/2-200/2,100))
	

	#personnage
	caraNameBox = pygame.draw.rect(window,(205,133,63),pygame.Rect(15,15,300,96+(96/2)))
	window.blit(caraNameDisplay,(115,22))
	caraPVDisplay = police.render("PV : "+str(cara.PV)+"/"+str(cara.PV_max), True, (0,0,0))
	window.blit(caraPVDisplay,(115,62))

	nivDisplay = police.render("Niv "+str(cara.niv), True, (0,0,0))
	window.blit(nivDisplay,(20,15+96+(48/2)-nivDisplay.get_height()/2))
	expDisplay = police.render("Exp : "+str(cara.exp)+"/100", True, (0,0,0))
	window.blit(expDisplay,(20+100,15+96+(48/2)-expDisplay.get_height()/2))

	caraFace = pygame.image.load(cara.face).convert_alpha()
	window.blit(caraFace,(15,15))
	caraSprite = pygame.image.load(cara.sprite).convert_alpha()
	window.blit(caraSprite,(200,425))


	#monstre
	monstreNameBox = pygame.draw.rect(window,(205,133,63),pygame.Rect(window.get_width()-315,15,300,96+(96/2)))
	monstreNameDisplay = police.render(m.name, True, (0,0,0))
	window.blit(monstreNameDisplay,(window.get_width()-215,22))
	caraPVDisplay = police.render("PV : "+str(mpv)+"/"+str(mpvm), True, (0,0,0))
	window.blit(caraPVDisplay,(window.get_width()-215,62))

	nivDisplay = police.render("Niv "+str(mn), True, (0,0,0))
	window.blit(nivDisplay,(window.get_width()-310,15+96+(48/2)-nivDisplay.get_height()/2))

	monstreFace = pygame.image.load(m.face).convert_alpha()
	window.blit(monstreFace,(window.get_width()-315,15))
	monstreSprite = pygame.image.load(m.sprite).convert_alpha()
	window.blit(monstreSprite,(window.get_width()-(200+monstreSprite.get_width()),425-monstreSprite.get_height()+96))


	#affiche les icones des actions possible
	choixC = pygame.image.load("C.png").convert_alpha()
	window.blit(choixC,(15,170))
	choixF = pygame.image.load("F.png").convert_alpha()
	window.blit(choixF,(15,240))
	choixPV1 = pygame.image.load("PV1.png").convert_alpha()
	window.blit(choixPV1,(15,310))
	choixPV2 = pygame.image.load("PV2.png").convert_alpha()
	window.blit(choixPV2,(15,380))
	choixPR1 = pygame.image.load("PR1.png").convert_alpha()
	window.blit(choixPR1,(15,450))
	choixPR2 = pygame.image.load("PR2.png").convert_alpha()
	window.blit(choixPR2,(15,520))


	pygame.display.flip()



def affichageDegat(diff, effet, nPhase): #affiche les dégats infligés
	if effet == "sans effet": #0 dégat
		diff = 0
		degat = pygame.Surface((56,64),SRCALPHA)
		degat.blit(degat0, (0,0), (0, 0, 56, 64))
	else:
		if diff >= 10: #10 dégats ou +, il faut séparer la dixaine de l'unité
			diffD = (diff%100 - diff%10)/10
			diffU = diff%10
			degatD = pygame.Surface((56,64),SRCALPHA)
			exec("degatD.blit(degat"+str(diffD)+", (0,0), (0, 0, 56, 64))")
			degatU = pygame.Surface((56,64),SRCALPHA)
			exec("degatU.blit(degat"+str(diffU)+", (0,0), (0, 0, 56, 64))")
			degat = pygame.Surface((56*2,64),SRCALPHA)
			degat.blit(degatD, (0,0), (0, 0, 56, 64))
			degat.blit(degatU, (56,0), (0, 0, 56, 64))
		else: #- de 10 dégats
			degat = pygame.Surface((56,64),SRCALPHA)
			exec("degat.blit(degat"+str(diff)+", (0,0), (0, 0, 56, 64))")

	if nPhase == "enemy":
		window.blit(degat,(200+(96/2)-degat.get_width()/2,350)) #affichage coté ennemi
	else:
		window.blit(degat,(window.get_width()-(96+200)+(96/2)-degat.get_width()/2,350)) #affichage coté allié

	pygame.display.flip()

	pygame.time.delay(500)



def affichageSoin(effetSoin): #affiche les soins procurés

	soinD = pygame.Surface((56,64),SRCALPHA)
	exec("soinD.blit(soin"+str(effetSoin)+", (0,0), (0, 0, 56, 64))")
	soinU = pygame.Surface((56,64),SRCALPHA)
	soinU.blit(soin0, (0,0), (0, 0, 56, 64))
	soin = pygame.Surface((56*2,64),SRCALPHA)
	soin.blit(soinD, (0,0), (0, 0, 56, 64))
	soin.blit(soinU, (56,0), (0, 0, 56, 64))

	window.blit(soin,(200+(96/2)-soin.get_width()/2,350))

	pygame.display.flip()



def combat(stage, nivM, monstreObj, cara): #gère le gameplay du combat
	stage = ((stage-1)//10)+1
	PV_maxM = int((((nivM**0.7)*2.6)+10)*monstreObj.PV) #calcul PV montre en fonction du niveau
	PVM = PV_maxM
	forM = int(round(monstreObj.For*(nivM*0.2))) #calcul stat montre en fonction du niveau
	vitM = int(round(monstreObj.Vit*(nivM*0.2)))
	defM = int(round(monstreObj.Def*(nivM*0.2)))
	affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara) #affichage combat
	fuite = 1 # Fuite non confirmée
	while fuite:
		mousePos = pygame.mouse.get_pos()

		for event in pygame.event.get(): #gestion gameplay
			if event.type == MOUSEBUTTONUP:
				if event.button == 1:
					if mousePos[0] > 15 and mousePos[0] < 15+60:
						if mousePos[1] > 170 and mousePos[1] < 170+60:
							if (cara.Vit >= vitM):
								if (cara.For - defM) > 0:
									PVM = PVM - (cara.For - defM)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((cara.For - defM), eff, "player")
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
							if PVM > 0:								
								if (forM - cara.Def) > 0:
									cara.PV = cara.PV - (forM - cara.Def)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((forM - cara.Def), eff, "enemy")
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
							if (cara.PV > 0) and (cara.Vit < vitM):
								if (cara.For - defM) > 0:
									PVM = PVM - (cara.For - defM)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((cara.For - defM), eff, "player")
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
							if (cara.Vit - 5) >= vitM:
								if (cara.For - defM) > 0:
									PVM = PVM - (cara.For - defM)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((cara.For - defM), eff, "player")
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
							if (PVM > 0) and ((vitM - 5) >= cara.Vit):								
								if (forM - cara.Def) > 0:
									cara.PV = cara.PV - (forM - cara.Def)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((forM - cara.Def), eff, "enemy")
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
							if PVM <= 0:
								gainExp = int((nivM*0.4)+30-cara.niv)
								if gainExp < 0:
									gainExp = 0
								cara.exp+=gainExp
								if cara.exp>=100:
									cara.exp-=100
									cara.niv+=1
									cara.pointStat = cara.pointStat + 2 + (cara.niv%2)
									cara.PV_max = int(((cara.niv**0.7)*3.25)+10)
								affichageStage(stage, "end", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								pygame.time.delay(1000)
								return 1

						elif mousePos[1] > 240 and mousePos[1] < 240+60:
							fuite = 0 # Fuite

						elif mousePos[1] > 310 and mousePos[1] < 310+60:
							if inv.Item1Q:
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageSoin(inv.Item1E)
								inv.Item1Q-=1
								cara.PV=cara.PV+inv.Item1E*10
								if cara.PV > cara.PV_max:
									cara.PV = cara.PV_max
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								pygame.time.delay(500)
								if (forM - cara.Def) > 0:
									cara.PV = cara.PV - (forM - cara.Def)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((forM - cara.Def), eff, "enemy")
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								if ((vitM - 5) >= cara.Vit):
									if (forM - cara.Def) > 0:
										cara.PV = cara.PV - (forM - cara.Def)
										eff = "effet"
									else:
										eff = "sans effet"
									affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
									affichageDegat((forM - cara.Def), eff, "enemy")
									affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
						elif mousePos[1] > 380 and mousePos[1] < 380+60:
							if inv.Item2Q:
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageSoin(inv.Item2E)
								inv.Item2Q-=1
								cara.PV=cara.PV+inv.Item2E*10
								if cara.PV > cara.PV_max:
									cara.PV = cara.PV_max
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								pygame.time.delay(500)
								if (forM - cara.Def) > 0:
									cara.PV = cara.PV - (forM - cara.Def)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((forM - cara.Def), eff, "enemy")
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								if ((vitM - 5) >= cara.Vit):
									if (forM - cara.Def) > 0:
										cara.PV = cara.PV - (forM - cara.Def)
										eff = "effet"
									else:
										eff = "sans effet"
									affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
									affichageDegat((forM - cara.Def), eff, "enemy")
									affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
						elif mousePos[1] > 450 and mousePos[1] < 450+60:
							if inv.Item3Q:
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageSoin(inv.Item3E)
								inv.Item3Q-=1
								cara.PV=cara.PV+inv.Item3E*10
								if cara.PV > cara.PV_max:
									cara.PV = cara.PV_max
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								pygame.time.delay(500)
								if (forM - cara.Def) > 0:
									cara.PV = cara.PV - (forM - cara.Def)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((forM - cara.Def), eff, "enemy")
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								if ((vitM - 5) >= cara.Vit):
									if (forM - cara.Def) > 0:
										cara.PV = cara.PV - (forM - cara.Def)
										eff = "effet"
									else:
										eff = "sans effet"
									affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
									affichageDegat((forM - cara.Def), eff, "enemy")
									affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
						elif mousePos[1] > 520 and mousePos[1] < 520+60:
							if inv.Item4Q:
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageSoin(inv.Item4E)
								inv.Item4Q-=1
								cara.PV=cara.PV+inv.Item4E*10
								if cara.PV > cara.PV_max:
									cara.PV = cara.PV_max
								affichageStage(stage, "player", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								pygame.time.delay(500)
								if (forM - cara.Def) > 0:
									cara.PV = cara.PV - (forM - cara.Def)
									eff = "effet"
								else:
									eff = "sans effet"
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								affichageDegat((forM - cara.Def), eff, "enemy")
								affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
								if ((vitM - 5) >= cara.Vit):
									if (forM - cara.Def) > 0:
										cara.PV = cara.PV - (forM - cara.Def)
										eff = "effet"
									else:
										eff = "sans effet"
									affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)
									affichageDegat((forM - cara.Def), eff, "enemy")
									affichageStage(stage, "enemy", monstreObj, nivM, PV_maxM, PVM, forM, vitM, defM, cara)

		if cara.PV <= 0:
			exec("skinActifDeath.skin"+str(cara.skin)+" = 0") #enregistre la mort d'un personnage
			return 0

	return 0





loop = 1
while loop or loop == None: #boucle principale
	#speed limit of loop
	clock.tick(60)
	loop = status(0,1)
	pygame.display.flip()
