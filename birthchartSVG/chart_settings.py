# Main settings

main = {
    "cusp": "Cusp",
    "longitude": "Longitude",
    "latitude": "Latitude",
    "north": "North",
    "east": "East",
    "south": "South",
    "west": "West",
    "apparent_geocentric": "Apparent Geocentric",
    "true_geocentric": "True Geocentric",
    "topocentric": "Topocentric",
    "heliocentric": "Heliocentric",
    "fire": "Fire",
    "earth": "Earth",
    "air": "Air",
    "water": "Water"
  }


# Colr settings:

colors = {
  "paper_0": "#000000",
  "paper_1": "#ffffff",
  "zodiac_bg_0": "#ff7200",
  "zodiac_bg_1": "#6b3d00",
  "zodiac_bg_2": "#69acf1",
  "zodiac_bg_3": "#2b4972",
  "zodiac_bg_4": "#ff7200",
  "zodiac_bg_5": "#6b3d00",
  "zodiac_bg_6": "#69acf1",
  "zodiac_bg_7": "#2b4972",
  "zodiac_bg_8": "#ff7200",
  "zodiac_bg_9": "#6b3d00",
  "zodiac_bg_10": "#69acf1",
  "zodiac_bg_11": "#2b4972",
  "zodiac_icon_0": "#ff7200",
  "zodiac_icon_1": "#6b3d00",
  "zodiac_icon_2": "#69acf1",
  "zodiac_icon_3": "#2b4972",
  "zodiac_icon_4": "#ff7200",
  "zodiac_icon_5": "#6b3d00",
  "zodiac_icon_6": "#69acf1",
  "zodiac_icon_7": "#2b4972",
  "zodiac_icon_8": "#ff7200",
  "zodiac_icon_9": "#6b3d00",
  "zodiac_icon_10": "#69acf1",
  "zodiac_icon_11": "#2b4972",
  "zodiac_radix_ring_0": "#ff0000",
  "zodiac_radix_ring_1": "#ff0000",
  "zodiac_radix_ring_2": "#ff0000",
  "zodiac_transit_ring_0": "#ff0000",
  "zodiac_transit_ring_1": "#ff0000",
  "zodiac_transit_ring_2": "#0000ff",
  "zodiac_transit_ring_3": "#0000ff",
  "houses_radix_line": "#ff0000",
  "houses_transit_line": "#0000ff",
  "aspect_0": "#5757e2",
  "aspect_30": "#810757",
  "aspect_45": "#b14e58",
  "aspect_60": "#d59e28",
  "aspect_72": "#1f99b3",
  "aspect_90": "#dc0000",
  "aspect_120": "#36d100",
  "aspect_135": "#985a10",
  "aspect_144": "#7a9810",
  "aspect_150": "#26bbcf",
  "aspect_180": "#510060",
  "planet_0": "#984b00",
  "planet_1": "#150052",
  "planet_2": "#520800",
  "planet_3": "#400052",
  "planet_4": "#540000",
  "planet_5": "#47133d",
  "planet_6": "#124500",
  "planet_7": "#6f0766",
  "planet_8": "#06537f",
  "planet_9": "#713f04",
  "planet_10": "#4c1541",
  "planet_11": "#4c1541",
  "planet_12": "#ff7e00",
  "planet_13": "#FF0000",
  "planet_14": "#0000FF",
  "planet_15": "#000000",
  "lunar_phase_0": "#000000",
  "lunar_phase_1": "#FFFFFF",
  "lunar_phase_2": "#CCCCCC"
}


# Aspects settings

aspects = [
  {
    "degree": 0,
    "name": "conjunction",
    "color": "#5757e2",
    "visible": 1,
    "visible_grid": 1,
    "is_major": 1,
    "is_minor": 0,
    "orb": "10"
  },
  {
    "degree": 30,
    "name": "semi-sextile",
    "color": "#810757",
    "visible": 0,
    "visible_grid": 0,
    "is_major": 0,
    "is_minor": 1,
    "orb": "3"
  },
  {
    "degree": 45,
    "name": "semi-square",
    "color": "#b14e58",
    "visible": 0,
    "visible_grid": 0,
    "is_major": 0,
    "is_minor": 1,
    "orb": "3"
  },
  {
    "degree": 60,
    "name": "sextile",
    "color": "#d59e28",
    "visible": 1,
    "visible_grid": 1,
    "is_major": 1,
    "is_minor": 0,
    "orb": "6"
  },
  {
    "degree": 72,
    "name": "quintile",
    "color": "#1f99b3",
    "visible": 1,
    "visible_grid": 1,
    "is_major": 0,
    "is_minor": 1,
    "orb": "2"
  },
  {
    "degree": 90,
    "name": "square",
    "color": "#dc0000",
    "visible": 1,
    "visible_grid": 1,
    "is_major": 1,
    "is_minor": 0,
    "orb": "5"
  },
  {
    "degree": 120,
    "name": "trine",
    "color": "#36d100",
    "visible": 1,
    "visible_grid": 1,
    "is_major": 1,
    "is_minor": 0,
    "orb": "8"
  },
  {
    "degree": 135,
    "name": "sesquiquadrate",
    "color": "#985a10",
    "visible": 0,
    "visible_grid": 0,
    "is_major": 0,
    "is_minor": 1,
    "orb": "3"
  },
  {
    "degree": 144,
    "name": "biquintile",
    "color": "#7a9810",
    "visible": 1,
    "visible_grid": 1,
    "is_major": 0,
    "is_minor": 1,
    "orb": "2"
  },
  {
    "degree": 150,
    "name": "quincunx",
    "color": "#fff600",
    "visible": 1,
    "visible_grid": 1,
    "is_major": 0,
    "is_minor": 0,
    "orb": "3"
  },
  {
    "degree": 180,
    "name": "opposition",
    "color": "#510060",
    "visible": 1,
    "visible_grid": 1,
    "is_major": 1,
    "is_minor": 0,
    "orb": "10"
  }
]

# Planets settings

planets = [
  {
    "id": 0,
    "name": "sun",
    "color": "#984b00",
    "visible": 1,
    "element_points": 40,
    "zodiac_relation": "4",
    "label": "Sun",
    "label_short": "sun"
  },
  {
    "id": 1,
    "name": "moon",
    "color": "#150052",
    "visible": 1,
    "element_points": 40,
    "zodiac_relation": "3",
    "label": "Moon",
    "label_short": "moon"
  },
  {
    "id": 2,
    "name": "mercury",
    "color": "#520800",
    "visible": 1,
    "element_points": 15,
    "zodiac_relation": "2,5",
    "label": "Mercury",
    "label_short": "mercury"
  },
  {
    "id": 3,
    "name": "venus",
    "color": "#400052",
    "visible": 1,
    "element_points": 15,
    "zodiac_relation": "1,6",
    "label": "Venus",
    "label_short": "venus"
  },
  {
    "id": 4,
    "name": "mars",
    "color": "#540000",
    "visible": 1,
    "element_points": 15,
    "zodiac_relation": "0",
    "label": "Mars",
    "label_short": "mars"
  },
  {
    "id": 5,
    "name": "jupiter",
    "color": "#47133d",
    "visible": 1,
    "element_points": 10,
    "zodiac_relation": "8",
    "label": "Jupiter",
    "label_short": "jupiter"
  },
  {
    "id": 6,
    "name": "saturn",
    "color": "#124500",
    "visible": 1,
    "element_points": 10,
    "zodiac_relation": "9",
    "label": "Saturn",
    "label_short": "saturn"
  },
  {
    "id": 7,
    "name": "uranus",
    "color": "#6f0766",
    "visible": 1,
    "element_points": 10,
    "zodiac_relation": "10",
    "label": "Uranus",
    "label_short": "uranus"
  },
  {
    "id": 8,
    "name": "neptune",
    "color": "#06537f",
    "visible": 1,
    "element_points": 10,
    "zodiac_relation": "11",
    "label": "Neptune",
    "label_short": "neptune"
  },
  {
    "id": 9,
    "name": "pluto",
    "color": "#713f04",
    "visible": 0,
    "element_points": 10,
    "zodiac_relation": "7",
    "label": "Pluto",
    "label_short": "pluto"
  },
  {
    "id": 10,
    "name": "mean node",
    "color": "#4c1541",
    "visible": 0,
    "element_points": 20,
    "zodiac_relation": "-1",
    "label": "North Node",
    "label_short": "Node"
  },
  {
    "id": 11,
    "name": "true node",
    "color": "#4c1541",
    "visible": 0,
    "element_points": 0,
    "zodiac_relation": "-1",
    "label": "?",
    "label_short": "?"
  },
  {
    "id": 12,
    "name": "Asc",
    "color": "orange",
    "visible": 1,
    "element_points": 40,
    "zodiac_relation": "-1",
    "label": "Asc",
    "label_short": "Asc"
  },
  {
    "id": 13,
    "name": "Mc",
    "color": "#FF0000",
    "visible": 1,
    "element_points": 20,
    "zodiac_relation": "-1",
    "label": "Mc",
    "label_short": "Mc"
  },
  {
    "id": 14,
    "name": "Dsc",
    "color": "#0000FF",
    "visible": 0,
    "element_points": 0,
    "zodiac_relation": "-1",
    "label": "Dsc",
    "label_short": "Dsc"
  },
  {
    "id": 15,
    "name": "Ic",
    "color": "#000000",
    "visible": 0,
    "element_points": 0,
    "zodiac_relation": "-1",
    "label": "Ic",
    "label_short": "Ic"
  }
]