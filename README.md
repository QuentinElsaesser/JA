# Judgment Aggregation with Unknown Variable Reliability

In this repository, you can find all the code for the methods of the literature and the ICE methods, also the code to generate datasets and run the tests on the methods. The code is in Python3 (need numpy to run). 

You can also find the proofs in the file Proofs.pdf.

The code to generate the datasets is in v4/generation/generate_w_prop.py and run the tests with a specific dataset is in v4/generation/read_xp.py. 

The code to evaluate the reliability of the agents and the confidence of formulae is in v4/graph and v4/vote. 

The agendas and profiles used for the experiments are in :
  - Figure 1 is experiments number 470, agendas in v4/prop_files/470/ and profiles in v4/generation/xp/res470xp0spr.csv
  - Figure 2 is experiments number 473, agendas in v4/prop_files/473/ and profiles in v4/generation/xp/res473xp0prp.csv
  - Figure 3 is experiments number 469, agendas in v4/prop_files/469/ and profiles in v4/generation/xp/res469xp0prp.csv

The main to test a specific method is in v4/main/main_formule.py

The code of ICE methods is in v4/judag/sf*.py (with *=leximax/produit/sum).

The code of the methods from (Lang et al., 2011) is in v4/judag/*.py with (*=RRA/RMWA/RMSA/RMCSA/RDH).

The code of the methods from (Everaere et al., 2014) is in v4/judag/*.py with (*=COUNTSUM/COUTMAX).

The example used in Table 1 is in v4/examples/majo2.txt.
