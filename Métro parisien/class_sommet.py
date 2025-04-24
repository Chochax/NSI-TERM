# -*- coding: utf-8 -*-
"""
Created on Tue Mar  4 08:25:51 2025

@author: Edward, Marion
"""

class Sommet:
    def __init__(self, station_id, station_name, station_desc, station_lat, station_lon, stop_sequence, route_id, service_id, direction_id, service_short_name, long_name_first, long_name_last):
        """Constructeur de la classe Sommet"""
        self.station_id = int(station_id)  # Convertir en entier
        self.station_name = station_name
        self.station_desc = station_desc
        self.station_lat = float(station_lat)  # Convertir en float
        self.station_lon = float(station_lon)  # Convertir en float
        self.stop_sequence = int(stop_sequence)
        self.route_id = int(route_id)
        self.service_id = int(service_id)
        self.direction_id = int(direction_id)
        self.service_short_name = service_short_name
        self.long_name_first = long_name_first
        self.long_name_last = long_name_last

    def afficher_info(self):
        """Méthode pour afficher les informations du sommet"""
        print(f"Station {self.station_name} (ID: {self.station_id}) - {self.station_desc}")
        print(f"Coordonnées : {self.station_lat}, {self.station_lon}")

