# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 11:28:54 2025

@author: Edward, Marion
"""
import folium
import heapq
from class_sommet import Sommet
from math import sin, cos, sqrt, atan2, radians
import csv

# Lire le CSV et stocker les stations dans une liste de dictionnaires
stations_list = []
with open("base_ratp.csv", newline="", encoding="utf-8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=";")  # Adapter le séparateur si besoin
    for row in reader:
        stations_list.append(row)

# Liste pour stocker les objets Sommet
sommets = []

# Créer un objet Sommet pour chaque station
for station in stations_list:
    sommet = Sommet(**station)  # Décompression du dictionnaire pour remplir les arguments
    sommets.append(sommet)



stations_par_ligne = {}

# Remplir le dictionnaire avec les objets Sommet
for sommet in sommets:
    # Si la ligne n'existe pas encore dans le dictionnaire, l'initialiser comme une liste vide
    if sommet.route_id not in stations_par_ligne:
        stations_par_ligne[sommet.route_id] = []
    
    # Ajouter la station à la liste correspondante à la ligne
    stations_par_ligne[sommet.route_id].append(sommet)

# Créer une carte centrée sur Paris
m = folium.Map(location=[48.8566, 2.3522], zoom_start=12)



# Définir des couleurs pour les lignes (tu peux personnaliser ici)
couleurs_lignes = {
    "1": "beige", "2": "blue", "3": "green", "4": "purple", "5": "orange",
    "6": "lightgreen", "7": "pink", "8": "lightgray", "9": "red", "10": "gray",
    "11": "darkblue", "12": "darkgreen", "13": "lightblue", "14": "black", "3B": 'darkred', "7B": 'cadetblue'
}
def afficher_tout(stations_par_ligne, couleurs_lignes):
    """
    Entrée : un dictionnaire ayant pour clé une ligne (id_route), et valeur un tableau de stations
    But : afficher les lignes et les stations qui sont présentent dans le
    dictinnaire en entrée
    """
    # Ajouter les lignes du métro sur la carte (reliées uniquement entre stations adjacentes)
    for ligne, stations in stations_par_ligne.items():
        # Extraire les coordonnées des stations dans l'ordre
        coords = [(s.station_lat, s.station_lon) for s in stations]
        
        # Relier uniquement les stations adjacentes en créant une PolyLine
        for i in range(1, len(coords)):
            folium.PolyLine(
                locations=[coords[i-1], coords[i]],  # Relier la station i-1 à la station i
                color=couleurs_lignes.get(stations[0].service_short_name, "black"),  # Couleur de la ligne
                weight=4,
                opacity=1,
                popup=f"Ligne {stations[0].service_short_name} - {stations[i-1].station_name} → {stations[i].station_name}"
            ).add_to(m)
    
    # Récupérer toutes les stations présentes dans stations_par_ligne
    stations_presentes = {s for stations in stations_par_ligne.values() for s in stations}

    # Ajouter les stations avec des marqueurs (uniquement celles présentes dans stations_par_ligne)
    for sommet in sommets:
        if sommet in stations_presentes:  # Vérifie que la station est bien dans stations_par_ligne
            couleur_ligne = couleurs_lignes.get(sommet.service_short_name, "blue")
            
            folium.Marker(
                location=[sommet.station_lat, sommet.station_lon],
                popup=f"{sommet.station_name} (Ligne {sommet.service_short_name})",
                tooltip=sommet.station_name,
                icon=folium.Icon(color=couleur_ligne, icon="subway", prefix='fa')
            ).add_to(m)
    
    # Afficher la carte
    m.save("metro_paris.html")
    print("Carte générée : ouvre 'metro_paris.html' dans un navigateur.")

#------------------------------------------------------------------------------------------------------

#lignes = { "1":["2280236"], "2":"1544644", "3":"2280265", "4":"2280284", "5":"2280297", 
          # "6":"2280310", "7":"2280325", "8":"2280344", "9":"2280360", "10":"2280372",
          # "11":"2280382", "12":"2280396", "13":"2280400", "14":"2280413",
          # "3B":"2280278", "7B":"2280337"}

"""
Ce dictionnaire permet de savoir quels sont les 'route_id' associés au numéro de ligne
car une ligne a plusieurs route_id qui représentent la direction du métro
"""
numero_lignes = { "1":["1577980","1577981"], "2":["1577985","1577986"], "3":["1197626","1197627"], "4":["1577987","1577988"], "5":["1197630","1197631"], 
          "6":["1495356","1495357"], "7":["1197634","1197635","1197637","1197636"], "8":["1197658","1197659"], "9":["1419803","1419804"], "10":["1577982","1577984"],
          "11":["1197616","1197617"], "12":["1488308","1488309"], "13":["1197621","1197620","1197622","1197623"], "14":["1382497","1382498"],
          "3B":["708898","708899"], "7B":["656103","656104"]}


def correspondance_ligne(ligne, stations_par_ligne, numero_lignes):
    """
    Entrée : la ligne en str -> '1'
    But: fonctionnalité 1 : l'utilisateur choisi une ligne de métro, affichage
    console des stations et leurs correspondances
    Sortie: None, affichage console.
    """
    route = numero_lignes[ligne]
    tab = set()  
    stations_index = {}

    # 🔥 Indexer les stations pour une recherche rapide
    for lignes, stations in stations_par_ligne.items():
        for station in stations:
            stations_index.setdefault(station.station_name, set()).add(lignes)

    # 🔥 Parcours des stations des lignes sélectionnées
    for lignes, stations in stations_par_ligne.items():
        if int(route[0]) == lignes or int(route[1]) == lignes:
            for station in stations:
                if station.station_name not in tab:
                    tab.add(station.station_name)  
                    
                    # 🔥 Stocker les correspondances uniques
                    correspondances = set()
                    for lignes2 in stations_index.get(station.station_name, []):
                        if lignes2 != lignes:
                            lignes_corr = tuple(parcours_dico(numero_lignes, str(lignes2)))
                            if lignes_corr and lignes_corr[0] != ligne:
                                correspondances.update(lignes_corr)

                    # 🔥 Affichage formaté
                    if correspondances:
                        print(f"\n{station.station_name} - Correspondances : {', '.join(correspondances)}")
                    else:
                        print("\n",station.station_name)

    print(f"\nNombre total de stations uniques : {len(tab)}")

def parcours_dico(dico, valeur):
    """Retourne les clés correspondant à une valeur dans un dictionnaire"""
    return [cle for cle, valeurs in dico.items() if valeur in valeurs]



def correspondances_station(station_recherchee, stations_par_ligne, numero_lignes):
    """
    Entrée : la staion dont on aimerais connaitre les correspondances en str
    But: trouver les lignes correspondante d'une station
    Sortie : les correspondances
    """
    correspondances = set()  
    lignes_station = set()   

    # 🔍 Trouver les lignes où se trouve la station recherchée
    for ligne, stations in stations_par_ligne.items():
        if any(station.station_name == station_recherchee for station in stations):
            lignes_station.add(ligne)

    # 🔍 Trouver les lignes en correspondance (en utilisant parcours_dico)
    for ligne in lignes_station:
        for station in stations_par_ligne[ligne]:  
            if station.station_name == station_recherchee:
                for ligne_corr, stations_corr in stations_par_ligne.items():
                    if ligne_corr != ligne and any(s.station_name == station_recherchee for s in stations_corr):
                        num_ligne_corr = parcours_dico(numero_lignes, str(ligne_corr))
                        correspondances.update(num_ligne_corr)  # 🔥 Ajouter les numéros de ligne

    # 🔹 Affichage formaté
    if correspondances:
        print(f"🚇 Correspondances pour {station_recherchee} : {', '.join(sorted(correspondances))}")
    else:
        print(f"❌ Aucune correspondance trouvée pour {station_recherchee}")

    return correspondances


def afficher_correspondances_station(station_recherchee, stations_par_ligne, numero_lignes):
    """
    Entrée : la station dont on aimerais connaitre les correspondances en str
    But : Fonctionnalité 2: afficher les correspondance d'une station dans la carte folium
    Sortie : None
    """
    correspondances = correspondances_station(station_recherchee, stations_par_ligne, numero_lignes)
    route=[]
    routes=[]
    for ligne in correspondances:
        route+=numero_lignes[ligne]
    for ligne in route:
        routes.append(int(ligne))
    dictionnaire_filtre = {cle: stations_par_ligne[cle] for cle in routes if cle in stations_par_ligne}
    afficher_tout(dictionnaire_filtre, couleurs_lignes)
    

    
    
def calcul_distance(station1, station2, stations_par_ligne):
    """
    Entrée: deux stations en str ou objet
    But : calculer la distance entre deux stations
    Sortie : la distance en kilomètres
    """
    # SI LES STATIONS SONT DONNéES EN CHAINE DE CARACTERE ET NON OBJET
    if isinstance(station1, str):
        station1_obj = None  # Initialiser une variable pour stocker l'objet trouvé
        
        for ligne, stations in stations_par_ligne.items():
            for station in stations:
                if station.station_name == station1 and station1_obj is None:
                    station1_obj = station  # Assigner uniquement si elle est encore None
                    station1 = station
    
    if isinstance(station2, str):
        station2_obj = None  # Initialiser une variable pour stocker l'objet trouvé
        
        for ligne, stations in stations_par_ligne.items():
            for station in stations:
                if station.station_name == station2 and station2_obj is None:
                    station2_obj = station  # Assigner uniquement si elle est encore None
                    station2 = station

    # Approximate radius of earth in km
    R = 6373.0
    
    lat1 = radians(float(station1.station_lat))
    lon1 = radians(float(station1.station_lon))
    lat2 = radians(float(station2.station_lat))
    lon2 = radians(float(station2.station_lon))
    
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    
    distance = R * c
    
    return distance
    
    
def dijkstra_metro(depart, arrivee, stations_par_ligne):
    """
    Entrée : deux stations
    But : (fonctionnalité 4) Trouve le plus court chemin entre deux stations en utilisant Dijkstra directement sur stations_par_ligne
    """
    
    # File de priorité (min-heap) : (distance accumulée, station actuelle, chemin parcouru)
    heap = [(0, depart, [])]
    
    # Dictionnaire des distances minimales
    distances = {s.station_name: float('inf') for stations in stations_par_ligne.values() for s in stations}
    distances[depart] = 0
    
    while heap:
        distance_actuelle, station_actuelle, chemin = heapq.heappop(heap)

        # Si on atteint la station d'arrivée, retourner le chemin et la distance
        if station_actuelle == arrivee:
            return chemin + [station_actuelle], distance_actuelle

        # Vérifier les stations adjacentes en parcourant stations_par_ligne
        for ligne, stations in stations_par_ligne.items():
            for i, station in enumerate(stations):
                if station.station_name == station_actuelle:
                    # Vérifier les voisins adjacents (précédent et suivant sur la ligne)
                    voisins = []
                    if i > 0:  # Station précédente
                        voisins.append(stations[i - 1])
                    if i < len(stations) - 1:  # Station suivante
                        voisins.append(stations[i + 1])

                    for voisin in voisins:
                        nouvelle_distance = distance_actuelle + calcul_distance(station_actuelle, voisin.station_name, stations_par_ligne)

                        if nouvelle_distance < distances[voisin.station_name]:
                            distances[voisin.station_name] = nouvelle_distance
                            heapq.heappush(heap, (nouvelle_distance, voisin.station_name, chemin + [station_actuelle]))
    print(chemin)
    return None, float('inf')  # Aucun chemin trouvé



def afficher_chemin_sur_carte(chemin, stations_par_ligne, couleurs_lignes):
    """Affiche uniquement le chemin trouvé sur la carte Folium."""
    chemin_stations = set(chemin)  # Convertir en set pour une recherche rapide
    stations_par_ligne_filtré = {}

    for ligne, stations in stations_par_ligne.items():
        stations_filtrées = [s for s in stations if s.station_name in chemin_stations]
        if stations_filtrées:
            stations_par_ligne_filtré[ligne] = stations_filtrées

    afficher_tout(stations_par_ligne_filtré, couleurs_lignes)

def temps_trajet(chemin,distance):
    """
    Calcul le temps de trajet pour un chemin le plus cours entre 2 stations trouvé
    """
    duree=0
    for i in range(len(chemin)):
        #pour chaque arret : on rajoute 1 min de stop.
        duree+=60
    #vitesse moyenne du métro parisien = 27km/h =7,5m/s
    duree+= distance*100/7.5
    print('Le trajet durera',int(duree/60),'min et parcourera', int(distance),'km.')
    pass


afficher_tout(stations_par_ligne, couleurs_lignes)


#correspondances_station("République", stations_par_ligne, numero_lignes)
#afficher_correspondances_station("République", stations_par_ligne, numero_lignes)

#correspondance_ligne('1', stations_par_ligne, numero_lignes)

#Exemple d'utilisation :
# chemin, distance = dijkstra_metro("Robespierre", "Balard", stations_par_ligne)
# afficher_chemin_sur_carte(chemin, stations_par_ligne, couleurs_lignes)
# print(' Chemin optimal : ',chemin, '(Distance :' ,distance, 'km)')
# temps_trajet(chemin, distance)






