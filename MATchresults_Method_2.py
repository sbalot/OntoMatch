import os
import re
import shutil
import itertools
import rdflib
import numpy as np

# !/usr/bin/env python3

#Creating the './store/config_files/' , './store/alignment_files/' folder
#These folders will be used to store the config.ini and alignment.rdf files for 'for loop' interation from main()
if not os.path.exists('./store/config_files/'):
    os.makedirs('./store/config_files/')
if not os.path.exists('./store/alignment_files/'):
    os.makedirs('./store/alignment_files/')

#Writing config.ini files for each loop in main()
def create_config_file(arglist,count):
    if os.path.exists("./store/config.ini"):        ##Removing previous files
        os.remove("./store/config.ini")
    f = open("./store/config.ini", "w")             #Writing the paramters and their value combination for a particular loop
    f.write("""use_translator=false
    bk_sources=%s
    word_matcher=auto
    string_matcher=%s
    string_measure=ISub
    struct_matcher=%s
    match_properties=%s
    selection_type=%s
    repair_alignment=false""" % arglist)
    f.close()
    shutil.copyfile("./store/config.ini",
                    "./store/config_files/"+str(count)+"_Config_%s_%s_%s_%s_%s.ini" % arglist)

#Running the AgreementMakerLight.jar file and saving the result as an "alignment.rdf" file. 
def run_match(arglist,count):
    if os.path.exists("./alignment.rdf"):
        os.remove("./alignment.rdf")
    os.system(
        'java -jar ./AgreementMakerLight.jar -s BOT.owl -t DogOntW.owl -o alignment.rdf -m')
    shutil.copyfile("./alignment.rdf",
                    "./store/alignment_files/"+str(count)+"_alignment_%s_%s_%s_%s_%s" % arglist)

#*****UNDER CONSTRUCTION: yet to be Implemented*******************************************************************************
def generate_graph():
    g=rdflib.Graph()
    g.parse("alignment.rdf", format="xml")
    qres=g.query (
                """SELECT    ?entity1 ?entity2 ?measure
                WHERE {
                        ?s <http://knowledgeweb.semanticweb.org/heterogeneity/alignmentmeasure> ?measure.
                        ?s <http://knowledgeweb.semanticweb.org/heterogeneity/alignmententity1> ?entity1.
                        ?s <http://knowledgeweb.semanticweb.org/heterogeneity/alignmententity2> ?entity2.
                }""")
    return qres
#*****************************************************************************************************************************
#Curate the matches in the source and target ontologies and output the number of matches
def parse_alignment_file(arglist,count):
   # finalgraph=generate_graph()
    
    g = open("./alignment.rdf")
    h = open("./result", "a+")
    k = open("./count_result", "a+")
    entity1list = []
    entity2list = []
    measurelist = []
 
    for line in g:
         
        if "entity1 rdf:resource" in line:
            entity1list.append(line.split("\"")[1])
             
        if "entity2 rdf:resource" in line:
            entity2list.append(line.split("\"")[1])
         
        if "measure rdf:datatype" in line:
            measurelist.append(line.split("<")[1].split(">")[1])
         
    measure=np.array(measurelist,dtype=float)
    mean=np.mean(measure)
    for i1 in range(len(entity1list)):
        h.write(str(count)+" "+" ".join(arglist))
        h.write(" %s %s %s\n"%(entity1list[i1], entity2list[i1], measurelist[i1]))
 
    k.write(str(count)+" "+" "" ".join(arglist))
    k.write(" %i"%len(entity1list)+" "+" %f \n"%mean)
    
    
def removeOutputfiles():
    if os.path.exists("./result"):
        os.remove("./result")
    if os.path.exists("./count_result"):
        os.remove("./count_result")

#Defining the potential combinations for the config.ini file
def main():
    count=1
    removeOutputfiles()
    bk_sources =["all","none"]
    string_matcher = ["none", "auto"]
    struct_matcher = ["auto","maximum","minimum"]
    match_properties = ["true", "false" ]
    selection_type = ["strict", "permissive", "hybrid", "none"]

    for arglist in list(itertools.product(bk_sources,string_matcher, struct_matcher, match_properties, selection_type)):
        create_config_file(arglist,count)
        run_match(arglist,count)
        parse_alignment_file(arglist, count)
        count=count+1


if __name__ == '__main__':
    main()
