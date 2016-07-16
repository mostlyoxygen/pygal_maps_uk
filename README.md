# pygal_maps_uk
Maps of the United Kingdom, for use in [pygal](http://www.pygal.org/).

| Maps Provided | |
| --- | --- |
| Administrative counties | Todo |
| Geographic / ceremonial counties | Todo |
| Postcode areas | Done |

## Installation

1. Clone the repository.
2. Navigate to the clone in the terminal / command prompt.
3. `python setup.py install`

I'll add it to pypi when all of the maps are ready.

## Usage

### Postcode Areas

```python
from pygal.maps.uk import Postcodes

map = Postcodes()
map.add("Some postcode areas", ["iv", "bt", "sa", "tr"])
map.render()
```

| Postcode Area | Postcode Area Name |
| --- | --- |
| ab | Aberdeen |
| al | St Albans |
| b | Birmingham |
| ba | Bath |
| bb | Blackburn |
| bd | Bradford |
| bh | Bournemouth |
| bl | Bolton |
| bn | Brighton |
| br | Bromley |
| bs | Bristol |
| bt | Belfast |
| ca | Carlisle |
| cb | Cambridge |
| cf | Cardiff |
| ch | Chester |
| cm | Chelmsford |
| co | Colchester |
| cr | Croydon |
| ct | Canterbury |
| cv | Coventry |
| cw | Crewe |
| da | Dartford |
| dd | Dundee |
| de | Derby |
| dg | Dumfries |
| dh | Durham |
| dl | Darlington |
| dn | Doncaster |
| dt | Dorchester |
| dy | Dudley |
| e | East London |
| ec | East Central London |
| eh | Edinburgh |
| en | Enfield |
| ex | Exeter |
| fk | Falkirk |
| fy | Blackpool |
| g | Glasgow |
| gl | Gloucester |
| gu | Guildford |
| ha | Harrow |
| hd | Huddersfield |
| hg | Harrogate |
| hp | Hemel Hempstead |
| hr | Hereford |
| hs | Outer Hebrides |
| hu | Hull |
| hx | Halifax |
| ig | Ilford |
| ip | Ipswich |
| iv | Inverness |
| ka | Kilmarnock |
| kt | Kingston upon Thames |
| kw | Kirkwall |
| ky | Kirkcaldy |
| l | Liverpool |
| la | Lancaster |
| ld | Llandrindod Wells |
| le | Leicester |
| ll | Llandudno |
| ln | Lincoln |
| ls | Leeds |
| lu | Luton |
| m | Manchester |
| me | Rochester |
| mk | Milton Keynes |
| ml | Motherwell |
| n | North London |
| ne | Newcastle upon Tyne |
| ng | Nottingham |
| nn | Northampton |
| np | Newport |
| nr | Norwich |
| nw | North West London |
| ol | Oldham |
| ox | Oxford |
| pa | Paisley |
| pe | Peterborough |
| ph | Perth |
| pl | Plymouth |
| po | Portsmouth |
| pr | Preston |
| rg | Reading |
| rh | Redhill |
| rm | Romford |
| s | Sheffield |
| sa | Swansea |
| se | South East London |
| sg | Stevenage |
| sk | Stockport |
| sl | Slough |
| sm | Sutton |
| sn | Swindon |
| so | Southampton |
| sp | Salisbury |
| sr | Sunderland |
| ss | Southend-on-Sea |
| st | Stoke-on-Trent |
| sw | South West London |
| sy | Shrewsbury |
| ta | Taunton |
| td | Galashiels |
| tf | Telford |
| tn | Tunbridge Wells |
| tq | Torquay |
| tr | Truro |
| ts | Cleveland |
| tw | Twickenham |
| ub | Southall |
| w | West London |
| wa | Warrington |
| wc | Western Central London |
| wd | Watford |
| wf | Wakefield |
| wn | Wigan |
| wr | Worcester |
| ws | Walsall |
| wv | Wolverhampton |
| yo | York |
| ze | Lerwick |
| gy | Guernsey |
| je | Jersey |
| im | Isle of Man|

See https://en.wikipedia.org/wiki/List_of_postcode_areas_in_the_United_Kingdom

## Attributions

### Postcode Map File (uk.postcodes.svg)

Contains Ordnance Survey and Royal Mail data (C) Crown copyright and database
right  [CC-BY-SA 3.0](http://creativecommons.org/licenses/by-sa/3.0) or
[OS OpenData](https://www.ordnancesurvey.co.uk/business-and-government/licensing/using-creating-data-with-os-products/os-opendata.html)

Original file: https://commons.wikimedia.org/wiki/File%3ABritish_postcode_areas_map.svg
