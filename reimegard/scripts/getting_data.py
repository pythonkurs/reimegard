#!/usr/bin/env python
from reimegard import calculateFractionOfOutage



xml_file =  'http://www.grandcentral.org/developers/data/nyct/nyct_ene.xml'
REASON= 'REPAIR'

calculateFractionOfOutage(xml_file,REASON)



