# Make sure to import all libraries used
import untangle

def calculateFractionOfOutage( xml_file,REASON ):
    
    # downloads and and untangles xml file
    doc = untangle.parse(xml_file);
    outages = doc.NYCOutages.outage;
    
    totalNrOfOutages = len(outages);
    totalNrOfOutagesDueToReason =0;
    
    for i in range(0,totalNrOfOutages):
        if(outages[i].reason.cdata==REASON):
            totalNrOfOutagesDueToReason=totalNrOfOutagesDueToReason+1
            
    fraction =float(totalNrOfOutagesDueToReason)/float(totalNrOfOutages);
    outString = 'The fraction of the outages that was due to '+REASON+ ' was '+str(totalNrOfOutagesDueToReason)+'/'+str(totalNrOfOutages)+' ('+fraction+')'
    print str;
    return;


