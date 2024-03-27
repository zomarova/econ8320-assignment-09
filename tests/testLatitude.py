import unittest
import json
from io import StringIO
import pandas as pd
import plotly


with open("Lesson.ipynb", "r") as file:
    f_str = file.read()

doc = json.loads(f_str)

code = [i for i in doc['cells'] if i['cell_type']=='code']
si = {}
for i in code:
    for j in i['source']:
        if "#si-exercise" in j:
            exec(compile("".join(i['source']), '<string>', 'exec'))

answer = 'state,capital,abbrev,lat,lon\r\nAlabama,Montgomery,AL,32.357,-86.2578\r\nAlaska,Juneau,AK,58.3628,-134.5294\r\nArizona,Phoenix,AZ,33.704,-112.3518\r\nArkansas,Little Rock,AR,34.9074,-92.1397\r\nCalifornia,Sacramento,CA,38.3805,-121.5554\r\nColorado,Denver,CO,39.7263,-104.8568\r\nConnecticut,Hartford,CT,41.8468,-73.0104\r\nDelaware,Dover,DE,39.1564,-75.4955\r\nFlorida,Tallahassee,FL,30.4286,-84.2593\r\nGeorgia,Atlanta,GA,33.8444,-84.474\r\nHawaii,Honolulu,HI,24.8598,-168.0218\r\nIdaho,Boise,ID,43.6038,-116.2729\r\nIllinois,Springfield,IL,39.8,-89.6495\r\nIndiana,Indianapolis,IN,39.775,-86.1093\r\nIowa,Des Moines,IA,41.5805,-93.7447\r\nKansas,Topeka,KS,38.9881,-95.7807\r\nKentucky,Frankfort,KY,38.2281,-84.8697\r\nLouisiana,Baton Rouge,LA,30.4492,-91.1856\r\nMaine,Augusta,ME,44.3232,-69.7665\r\nMaryland,Annapolis,MD,39.1332,-76.7988\r\nMassachusetts,Boston,MA,42.3706,-71.027\r\nMichigan,Lansing,MI,42.7388,-84.4764\r\nMinnesota,Saint Paul,MN,44.8344,-92.9873\r\nMississippi,Jackson,MS,32.3205,-90.2076\r\nMissouri,Jefferson City,MO,38.5462,-92.1525\r\nMontana,Helena,MT,46.6131,-112.0213\r\nNebraska,Lincoln,NE,40.8651,-96.8231\r\nNevada,Carson City,NV,39.1507,-119.7459\r\nNew Hampshire,Concord,NH,43.2185,-71.5277\r\nNew Jersey,Trenton,NJ,40.2805,-74.712\r\nNew Mexico,Santa Fe,NM,35.6975,-105.9821\r\nNew York,Albany,NY,42.6149,-73.9708\r\nNorth Carolina,Raleigh,NC,35.7727,-78.6324\r\nNorth Dakota,Bismarck,ND,46.8234,-100.7748\r\nOhio,Columbus,OH,40.0999,-83.0157\r\nOklahoma,Oklahoma City,OK,35.3513,-97.4953\r\nOregon,Salem,OR,44.949,-123.004\r\nPennsylvania,Harrisburg,PA,40.2618,-76.8831\r\nRhode Island,Providence,RI,41.8228,-71.4145\r\nSouth Carolina,Columbia,SC,33.995,-81.0888\r\nSouth Dakota,Pierre,SD,44.3695,-100.3211\r\nTennessee,Nashville,TN,36.1657,-86.7781\r\nTexas,Austin,TX,30.3264,-97.7713\r\nUtah,Salt Lake City,UT,40.7559,-111.8967\r\nVermont,Montpelier,VT,44.1991,-72.5596\r\nVirginia,Richmond,VA,37.5242,-77.4932\r\nWashington,Olympia,WA,47.0129,-122.8763\r\nWest Virginia,Charleston,WV,38.349,-81.6306\r\nWisconsin,Madison,WI,43.0696,-89.4239\r\nWyoming,Cheyenne,WY,41.1437,-104.7962\r\n'
truth = pd.read_csv(StringIO(answer))

class testCases(unittest.TestCase):
    
    def test_lat(self):
        test1 = all([round(float(capitals.loc[i, "lat"]), 0)==round(float(truth.loc[i, "lat"]), 0) for i in capitals.index])
        self.assertTrue(test1,
                        msg="Your latitude values don't match truth! Just grab the first value for each city.")
