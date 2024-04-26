# generation

After the tests, we write all the results in a .tex file and read this file to generate with matplotlib the graphics.

# -- Judgment Aggregation Generation

`constants.FORMULA` must be `True`.

## generate_w_prop.py

generate the agendas and the profile. 

PRP to generate profile with different average reliability.

SPR to generate profile with a different number of agents.

to run the code : `python3 -m v4.generation.generate_w_prop` (change the parameters in the main inside the file)

## read_xp.py

to tests the dataset `python3 -m v4.generation.read_xp 469 spr` with 469 the number of the dataset and spr the type of generation used (you can find this information in the name of the dataset)

## Datasets in xp/

Each line represents a profile generated and used in our experiments. 

The ID starts at zéro.

_ VARIANCE : Variance allowed for the choice of agents (100=all is allowed)
- NB_OBJ : The number of formulae in the graph
- NB_SRC : The number of agents in the graph
- NB_FL : The minimum number of truth assignement associated with a formulae
- NB_FU : The maximum number of truth assignement associated with a formulae
- NBF : The number of formulae in the extended agenda
- TRUST : The average reliability of the agents
- SF : The truth assignment claimed by the agents. The agents are separated by a dash (-)
- OF : The formulae and the truth assignment. The formulae are separated by a dash (-)
- TRUTH : ID of the correct truth assignment chosen
- INTERVAL : the interval used to group the profiles
- The agenda used with this profile. 

# -- Truth Discovery Generation 

`constants.FORMULA` must be `False`.

## File in xp/

Each line represents a graph generated and used in our experiments. 

The ID of the facts starts at zéro.

- NB_OBJ : The number of objects in the graph
- NB_SRC : The number of sources in the graph
- NB_FL : The minimum number of facts associated with an object
- NB_FU : The maximum number of facts associated with an object
- NBF : The number of facts in the graph
- TRUST : The average reliability of the graph
- SF : The links between sources and facts. The sources are separated by a dash (-)
- First line, we have « 5,12,27,29,33,38-... » it means that the first source claim the fact 5,12,etc
- OF : The links between facts and objects. The objects are separated by a dash (-)
- First line, we have « 0,1,2,3-... » it means that the facts 0,1,2,3 are linked to the first
object.
- TRUTH : ID of the true facts in the graph
- INTERVAL : the interval used to group the graphs
- PRC/SRC/FCT : represent what we change in our graphs and it is linked to the INTERVAL (PRC : reliability of the sources; SRC : number of sources; FCT number of facts by object)

## att_metrics.py 

Compute the results for one graph.

## brutefrc_exp_para.py

- generate the graphs
- ask to change the parameters if needed (to find quickly the 1000 graphs for each interval)

## graph_methods.py

generate one graph and copy this graph for all the methods then run the algorithm and compute the value for the metrics

## latex.py

Write the results in a latex file

## main_generate.py

main to generate the results/plot

## metrics.py

compute the results for all the metrics with the 1000 graphs

## plot.py

create the plot

## priors.py

generate a file with the possible values for the a priori probability

## random_graph.py

generate a graph depending on the parameters given

## read_xp.py

read a file with the graphs already generated and run everything with the method from brutefrc_exp_para.py

## spe_metrics.py

specific class to write the reliability sources by sources in the .tex file
