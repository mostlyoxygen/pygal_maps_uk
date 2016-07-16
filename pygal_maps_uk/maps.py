# This file is part of pygal_maps_uk.
#
# A package for pygal that adds support for UK maps.
# Copyright (C) 2016 mostlyoxygen
#
# This library is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option) any
# later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU Lesser General Public License for more
# details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with pygal_maps_uk. If not, see <http://www.gnu.org/licenses/>.
"""
Various maps of the United Kingdom.

"""

import os

from pygal.graph.map import BaseMap
from pygal._compat import is_str


POSTCODES = {
    "ab": "Aberdeen",
    "al": "St Albans",
    "b": "Birmingham",
    "ba": "Bath",
    "bb": "Blackburn",
    "bd": "Bradford",
    "bh": "Bournemouth",
    "bl": "Bolton",
    "bn": "Brighton",
    "br": "Bromley",
    "bs": "Bristol",
    "bt": "Belfast",
    "ca": "Carlisle",
    "cb": "Cambridge",
    "cf": "Cardiff",
    "ch": "Chester",
    "cm": "Chelmsford",
    "co": "Colchester",
    "cr": "Croydon",
    "ct": "Canterbury",
    "cv": "Coventry",
    "cw": "Crewe",
    "da": "Dartford",
    "dd": "Dundee",
    "de": "Derby",
    "dg": "Dumfries",
    "dh": "Durham",
    "dl": "Darlington",
    "dn": "Doncaster",
    "dt": "Dorchester",
    "dy": "Dudley",
    "e": "East London",
    "ec": "East Central London",
    "eh": "Edinburgh",
    "en": "Enfield",
    "ex": "Exeter",
    "fk": "Falkirk",
    "fy": "Blackpool",
    "g": "Glasgow",
    "gl": "Gloucester",
    "gu": "Guildford",
    "ha": "Harrow",
    "hd": "Huddersfield",
    "hg": "Harrogate",
    "hp": "Hemel Hempstead",
    "hr": "Hereford",
    "hs": "Outer Hebrides",
    "hu": "Hull",
    "hx": "Halifax",
    "ig": "Ilford",
    "ip": "Ipswich",
    "iv": "Inverness",
    "ka": "Kilmarnock",
    "kt": "Kingston upon Thames",
    "kw": "Kirkwall",
    "ky": "Kirkcaldy",
    "l": "Liverpool",
    "la": "Lancaster",
    "ld": "Llandrindod Wells",
    "le": "Leicester",
    "ll": "Llandudno",
    "ln": "Lincoln",
    "ls": "Leeds",
    "lu": "Luton",
    "m": "Manchester",
    "me": "Rochester",
    "mk": "Milton Keynes",
    "ml": "Motherwell",
    "n": "North London",
    "ne": "Newcastle upon Tyne",
    "ng": "Nottingham",
    "nn": "Northampton",
    "np": "Newport",
    "nr": "Norwich",
    "nw": "North West London",
    "ol": "Oldham",
    "ox": "Oxford",
    "pa": "Paisley",
    "pe": "Peterborough",
    "ph": "Perth",
    "pl": "Plymouth",
    "po": "Portsmouth",
    "pr": "Preston",
    "rg": "Reading",
    "rh": "Redhill",
    "rm": "Romford",
    "s": "Sheffield",
    "sa": "Swansea",
    "se": "South East London",
    "sg": "Stevenage",
    "sk": "Stockport",
    "sl": "Slough",
    "sm": "Sutton",
    "sn": "Swindon",
    "so": "Southampton",
    "sp": "Salisbury",
    "sr": "Sunderland",
    "ss": "Southend-on-Sea",
    "st": "Stoke-on-Trent",
    "sw": "South West London",
    "sy": "Shrewsbury",
    "ta": "Taunton",
    "td": "Galashiels",
    "tf": "Telford",
    "tn": "Tunbridge Wells",
    "tq": "Torquay",
    "tr": "Truro",
    "ts": "Cleveland",
    "tw": "Twickenham",
    "ub": "Southall",
    "w": "West London",
    "wa": "Warrington",
    "wc": "Western Central London",
    "wd": "Watford",
    "wf": "Wakefield",
    "wn": "Wigan",
    "wr": "Worcester",
    "ws": "Walsall",
    "wv": "Wolverhampton",
    "yo": "York",
    "ze": "Lerwick",
    "gy": "Guernsey",
    "je": "Jersey",
    "im": "Isle of Man"
}


with open(os.path.join(os.path.dirname(__file__), "uk.postcodes.svg")) as file:
    PC_MAP= file.read()


class Postcodes(BaseMap):
    """ United Kingdom postcode map. """
    x_labels = list(POSTCODES.keys())
    area_names = POSTCODES
    area_prefix = ""
    kind = "postcode"
    svg_map = PC_MAP

    def adapt_code(self, area_code):
        """ Convert the postcode to lower case. """
        if is_str(area_code):
            return area_code.lower()
        return super(Postcodes, self).adapt_code(area_code)
