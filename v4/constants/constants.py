############################################
################ PARAMETERS ################
############################################

#Name of the normalizations
NORMA_A = 'A'
NORMA_O = 'C'
#ID norma in generation # not used ?
ID_NORMA_A = 'normaA'
ID_NORMA_O = 'normaO'

#PATH
PATH_PNG = "v4/png/"
PATH_XP = "v4/generation/xp/"
PATH_RESULTS = "v4/results/"
PRIOR_PATH  ="v4/priors_file/"
PROP_PATH  ="v4/prop_files/"

############ADD NEW METHOD############
### Add a new methods to test and generate Plot
####### in this file add the name in NAMES; ORDER; NAMES_NONORMA; ID_METHODS_SOURCES(if test on metrics src); 
####### PARA_PLOT: PLOT_ORDER; LEGEND_ORDER
####### in graph_method.py add the methods in the list to run the metrics on it

####################################
#### if we do not want to RUN a method, removes it from RUN_METHODS
#### if we do not want to PLOT the result of a method, removes it from PLOT_METHODS

RUN_METHODS = []
PLOT_METHODS = []
NAMES_NONORMA = []
NAMES = []
ORDER = []
PLOT_ORDER = []
LEGEND_ORDER = []
PARA_PLOT = []
ID_METHODS_SOURCES = []
NB_METHODS = len(RUN_METHODS)
NB_METHODS_SOURCES = len(ID_METHODS_SOURCES)

# FORMULA = False
FORMULA = True
    
if FORMULA:
    RUN_METHODS = ["SFsum", "SFmax", "SFmin", "SFprod", 
                   "RMSA", "RMCSA", "RMWA", "RRA", "RDH",
                   "CSUM", "CMAX", "CMIN"]
    PLOT_METHODS = ["SFsum", 
                    "RMSA", "RMCSA", "RMWA", "RRA", "RDH",
                    "CSUM", "CMAX"]
    NAMES_NONORMA = ["SFsum", "SFmax", "SFmin", "SFprod", 
                   "RMSA", "RMCSA", "RMWA", "RRA", "RDH",
                   "CSUM", "CMAX", "CMIN"]
    NAMES = ["SFsum", "SFmax", "SFmin", "SFprod", 
                   "RMSA", "RMCSA", "RMWA", "RRA", "RDH",
                   "CSUM", "CMAX", "CMIN"]
    ORDER = ["SFsum", "SFmax", "SFmin", "SFprod", 
                   "RMSA", "RMCSA", "RMWA", "RRA", "RDH",
                   "CSUM", "CMAX", "CMIN"]
    PLOT_ORDER = ["RDH", "RMSA", "RMCSA", "RMWA", "CMAX","CMIN", "CSUM", "RRA",
                  "SFsum", "SFmax", "SFmin", "SFprod"]
    LEGEND_ORDER = ["SFsum", "SFmax", "SFmin", "SFprod", 
                   "RMSA", "RMCSA", "RMWA", "RRA", "RDH",
                   "CMIN", "CMAX", "CSUM"]
    # same order as name
    #https://matplotlib.org/stable/gallery/color/named_colors.html
    #https://matplotlib.org/stable/api/markers_api.html
    #https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    PARA_PLOT = [("--+", 'blue', r"$SF^{\sum}$"),
                 ("--v", 'black', r"$SF^{leximax}$"),
                 ("--+", 'red', r"$SF^{leximin}$"),
                 ("--x", 'orange', r"$SF^{\prod}$"),
                 (":*", 'forestgreen', r"$R_{MSA}$"),
                 ("-.p", 'lime', r"$R_{MCSA}$"),
                 ("-.X", 'fuchsia', r"$R_{MWA}$"),
                 (":X", 'cyan', r"$R_{RA}$"),
                 ("-p", 'deepskyblue', r"$R^{dH,max}$"),
                 (":>", 'mediumslateblue', r"$\delta^{sum}$"),
                 ("-<", 'indianred', r"$\delta^{leximax}$"),
                 ("-.^", 'goldenrod', r"$\delta^{leximin}$")]
    
    # Add another method and it will write the results for the sources metrics
    ID_METHODS_SOURCES = [ORDER.index(NAMES[i]) for i in range(len(NAMES))]
                          # ,ORDER.index(NAMES[12]),ORDER.index(NAMES[13]),ORDER.index(NAMES[14]),ORDER.index(NAMES[15])]
    #Number of methods we test
    # NB_METHODS = len(NAMES)
    NB_METHODS = len(RUN_METHODS)
    #Number of methods that use the metrics for the sources
    NB_METHODS_SOURCES = len(ID_METHODS_SOURCES)
    
else:

    RUN_METHODS = [f"Plurality {NORMA_A}", f"Plurality {NORMA_O}", f"Borda {NORMA_A}", f"Borda {NORMA_O}",
             "Sums", "Usums", "H\&A", "TruthFinder", "Voting",
             "AverageLog", "Investment", "PooledInvestment"]
    
    PLOT_METHODS = [f"Plurality {NORMA_A}", f"Plurality {NORMA_O}", f"Borda {NORMA_A}", f"Borda {NORMA_O}", 
                    "Sums", "Usums", "H\&A", "TruthFinder", "Voting",
                    "AverageLog", "Investment", "PooledInvestment"]
    
    #Names of the methods when graph is complete
    NAMES_NONORMA = ["Plurality", "Plurality", "Borda", "Borda", 
                     "Sums", "Usums", "H\&A", "TruthFinder", "Voting",
                     "AverageLog", "Investment", "PooledInvestment"]
                     # ,"Derive","Derive","Prio","Prio"]
    
    #Names of the methods
    NAMES = [f"Plurality {NORMA_A}", f"Plurality {NORMA_O}", f"Borda {NORMA_A}", f"Borda {NORMA_O}",
             "Sums", "Usums", "H\&A", "TruthFinder", "Voting",
             "AverageLog", "Investment", "PooledInvestment"]
             # ,f"Derive {NORMA_A}", f"Derive {NORMA_O}", f"Prio {NORMA_A}", f"Prio {NORMA_O}"]
    
    #Order of the methods in the latex when we write the file
    ORDER = [f"Plurality {NORMA_A}", f"Plurality {NORMA_O}", f"Borda {NORMA_A}", f"Borda {NORMA_O}",
             "Sums", "Usums", "H\&A", "TruthFinder", "Voting",
             "AverageLog", "Investment", "PooledInvestment"]
            # ,f"Derive {NORMA_A}", f"Derive {NORMA_O}", f"Prio {NORMA_A}", f"Prio {NORMA_O}"]
    
    #Order to plot the methods [0]=first ploted [-1]=last ploted
    PLOT_ORDER = ["AverageLog", "Investment", "PooledInvestment",
                  "TruthFinder", "H\&A", "Sums", "Usums", "Voting",
                    f"Borda {NORMA_A}", f"Borda {NORMA_O}",f"Plurality {NORMA_O}", f"Plurality {NORMA_A}"]
                    # ,f"Derive {NORMA_A}", f"Derive {NORMA_O}", f"Prio {NORMA_A}", f"Prio {NORMA_O}"]
    
    #Order for the legends in the plot [0]=highest [-1]=lowest
    LEGEND_ORDER = [f"Plurality {NORMA_A}", f"Plurality {NORMA_O}", f"Borda {NORMA_O}",
                    "Sums", "Usums", "H\&A", "TruthFinder", 
                    f"Borda {NORMA_A}", "Voting",
                    "AverageLog", "Investment", "PooledInvestment"]
    # f"Derive {NORMA_A}", f"Derive {NORMA_O}", f"Prio {NORMA_A}", f"Prio {NORMA_O}",
    
    #https://matplotlib.org/stable/gallery/color/named_colors.html
    #https://matplotlib.org/stable/api/markers_api.html
    #https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html
    PARA_PLOT = [("--d", 'blue', f"Pl{NORMA_A}"), 
           ("-v", 'black', f"Pl{NORMA_O}"),
           ("--s", 'red', f"Bo{NORMA_A}"),
           ("-h", 'orange', f"Bo{NORMA_O}"),
           ("-p", 'forestgreen', "Sums"),
           ("-p", 'lime', "Usums"),
           ("-p", 'fuchsia', "H&A"),
           ("-p", 'cyan', "TF"),
           (":*", 'deepskyblue', "Voting"),
           ("-p", 'darkviolet', "AL"),
           ("-p", 'mediumslateblue', "Inv"),
           ("-p", 'darkgoldenrod', "PInv")]
           # ,       
           # ("--*", 'darkviolet', f"drv{NORMA_A}"),
           # ("--*", 'mediumslateblue', f"drv{NORMA_O}"),
           # ("--*", 'darkgoldenrod', f"pio{NORMA_A}"),
           # ("--*", 'goldenrod', f"pio{NORMA_O}")]
           
    # Add another method and it will write the results for the sources metrics
    ID_METHODS_SOURCES = [ORDER.index(NAMES[i]) for i in range(len(NAMES))]
    # ID_METHODS_SOURCES = [ORDER.index(NAMES[0]),ORDER.index(NAMES[1]),ORDER.index(NAMES[2]),ORDER.index(NAMES[3]),
    #                       ORDER.index(NAMES[4]),ORDER.index(NAMES[5]),ORDER.index(NAMES[6]),ORDER.index(NAMES[7]),ORDER.index(NAMES[8]),
    #                       ORDER.index(NAMES[9]),ORDER.index(NAMES[10]),ORDER.index(NAMES[11])]
                          # ,ORDER.index(NAMES[12]),ORDER.index(NAMES[13]),ORDER.index(NAMES[14]),ORDER.index(NAMES[15])]
    #Number of methods we test
    # NB_METHODS = len(NAMES)
    NB_METHODS = len(RUN_METHODS)
    #Number of methods that use the metrics for the sources
    NB_METHODS_SOURCES = len(ID_METHODS_SOURCES)       
# return RUN_METHODS, PLOT_METHODS, NAMES_NONORMA, NAMES, ORDER, PLOT_ORDER, LEGEND_ORDER, PARA_PLOT

def is_tested(met):
    """
    met = ORDER
    """
    tmp = []
    for m in met:
        if m in RUN_METHODS:
            tmp.append(m)
    return tmp

def id_is_tested():
    """
    met = RUN_METHODS
    """
    tmp = []
    for m in NAMES:
        if m in RUN_METHODS:
            tmp.append(ORDER.index(m))
    return tmp

def plot_index_fct(list_met):
    """
    Return the list with the order of the legends for the plot
    """
    res = []
    for i in range(len(LEGEND_ORDER)):
        if LEGEND_ORDER[i] in list_met:
            res.append(list_met.index(LEGEND_ORDER[i]))
    return res

############ADD NEW METHOD############

############ADD NEW METRIC############
#In this file : METRICS_NAMES;PLOT_Y;PLOT_FILE;PLOT_YLIM; and in ID_METRICS_SRC or ID_METRICS_TD
#respect the order when you add a new metric
#In metrics.py : the function; in metrics
METRICS_NAMES = ["Swaps", "Normalize Swaps", 
                     "Euclidean distance", "Normalize euclidean distance",
                     "Difference", "Sources Reliability", 
                     "Ranking Order",
                     "Precision", "Accuracy", "Recall", "CSI", 
                     "Average iteration", "Max iteration",
                     "Number answers",
                     "Precision Mean", "Precision Unanimous",
                     "CSI Mean", "CSI Unanimous",
                     "CSI Min", "CSI Max",
                     "Precision Min", "Precision Max",
                     "CSI Majority", "Precision Majority",
                     "Majority Consistent ALGO", "Majority Consistent MAJO",
                     "Truth is majority", "Same outcome"]

FR = False
def PLOT_L(FR):
    if not FR:
        # Y Descrption of metrics in plot
        PLOT_Y = ["Number of swaps", "Percentage of swaps (divide by max)",
                        "Euclidean distance", "Euclidean distance (divide by max)", 
                        "Averaged difference", "Average reliability",
                        "Ranking",
                        "Precision (facts)", "Accuracy (facts)", "Recall (facts)", "CSI (facts)", 
                        "Average iterations", "Maximum iterations",
                        "Number of judgment proposed",
                        "Mean Precision on judgment", "Precision on unanimous judgment",
                        "Mean CSI on judgment", "CSI on unanimous judgment",
                        "Min CSI on judgment", "Max CSI on judgment",
                        "Min Precision on judgment", "Max Precision on judgment",
                        "CSI on Majority", "Precision on Majority",
                        "Number of SF graphs that are majority-consistant", "Number of graphs with a consistent majority",
                        "Number of truth equal majority", "Same outcome methods 1,2,3"]
        if FORMULA:
            X_LABEL = "Average reliability of the agents (in percent)"
        else:
            X_LABEL = "Average reliability of the sources (in percent)"
    else:
        #PLOT FR
        PLOT_Y = ["Nombre de swaps", "Nombre de swaps (divisé par le max)",
                        "Distance euclidienne", "Distance euclidienne (divisé par le max)", 
                        "Différence moyenne", "Fiabilité moyenne",
                        "Classement",
                        "Precision (faits)", "Accuracy (faits)", "Recall (faits)", "CSI (faits)", 
                        "Itérations moyennes", "Itérations maximum",
                        "Nombre de jugements proposées",
                        "Précision moyenne sur les jugements", "Précision sur l'unanimité des jugements",
                        "CSI moyenne sur les jugements", "CSI sur l'unanimité des jugements",
                        "Minimum CSI", "Maximum CSI",
                        "Minimum Précision", "Maximum Précision",
                        "CSI sur la Majorité", "Précision sur la Majorité",
                        "Nombre de graphes où SF est majority-consistant", "Nombre de graphes où la majorité est cohérente",
                        "Nombre de fois où la vérité est la majorité", "Même résultat methodes 1,2,3"]
        
        if FORMULA:
            X_LABEL = "Probabilité moyenne des agents (en pourcentage)"
        else:
            X_LABEL = "Probabilité moyenne des sources (en pourcentage)"
    return PLOT_Y, X_LABEL

PLOT_Y, X_LABEL = PLOT_L(FR)

def X_LABEL_SPE(label, nvalue, tmpsplit, FR):
    if nvalue == "FCT":
        if FR:
            return f"Nombre de faits {tmpsplit}"
        else:
            return f"Number of facts {tmpsplit}"
    elif nvalue == "SRC" or nvalue == "SPR" or nvalue == "SDR":
        if not FORMULA:
            if FR:
                return f"Nombre de sources {tmpsplit}"
            else:    
                return f"Number of sources {tmpsplit}"
        else:
            if FR:
                return f"Nombre d'agents {tmpsplit}"
            else:    
                return f"Number of agents {tmpsplit}"
    elif nvalue == "OBJ":
        if FR:
            return f"Nombre d'objets {tmpsplit}"
        else:    
            return f"Number of objects {tmpsplit}"
    elif nvalue == "VRN":
        if FR:
            return f"Variance sur les affirmations des agents {tmpsplit}"
        else:    
            return f"Variance on agent's claims {tmpsplit}"
    else:
        return label

# name of the file 
PLOT_FILE = ["swp", "swn", 
                  "ecd", "edn", 
                  "dif", "ars",
                  "rnk",
                  "prc", "acc", "rec", "csi", 
                  "avi", "mxi",
                  "nba",
                  "pra", "pru",
                  "csa", "csu",
                  "csl", "csh",
                  "prl", "prh",
                  "csm", "prm",
                  "mca", "mcm",
                  "tem", "sam"]

# PLOT_YLIM = [[0], [0,100], 
#              [0], [0,100],
#              [0], [0],
#              [0],
#              [0,100], [0,100], [0,100], [0,100], 
#              [0], [0]]
#p = value must be min or max when you read the file
#100.1 to see the curve
PLOT_YLIM = [['m','m'], [0,'m'], 
             [0,'m'], [0,'m'],
             [0,'m'], [0,'m'],
             [0,'m'],
             ['m',100.1], ['m',100.1], ['m',100.1], ['m',100.1], 
             [0,'m'], [0,'m'],
             [0,'m'],
             ['m',100.1],['m',100.1],
             ['m',100.1],['m',100.1],
             ['m',100.1],['m',100.1],
             ['m',100.1],['m',100.1],
             ['m',100.1],['m',100.1],
             [0,'m'],[0,'m'],
             [0,'m'], [0,'m']]

ID_METRICS_SRC = {"S":METRICS_NAMES.index("Swaps"), "SN":METRICS_NAMES.index("Normalize Swaps"), 
                  "E":METRICS_NAMES.index("Euclidean distance"), "EN":METRICS_NAMES.index("Normalize euclidean distance"), 
                  "D":METRICS_NAMES.index("Difference"), "Mt":METRICS_NAMES.index("Sources Reliability"), 
                  "RO":METRICS_NAMES.index("Ranking Order")}

ID_METRICS_TD = {"P":METRICS_NAMES.index("Precision"), "A":METRICS_NAMES.index("Accuracy"),
                 "R":METRICS_NAMES.index("Recall"), "CSI":METRICS_NAMES.index("CSI"), 
                 "Ia":METRICS_NAMES.index("Average iteration"), "Im":METRICS_NAMES.index("Max iteration")}

ID_METRICS_PRP = {"Na":METRICS_NAMES.index("Number answers"),
                  "Pra":METRICS_NAMES.index("Precision Mean"),"Pru":METRICS_NAMES.index("Precision Unanimous"),
                  "Csa":METRICS_NAMES.index("CSI Mean"),"Csu":METRICS_NAMES.index("CSI Unanimous"),
                  "Csl":METRICS_NAMES.index("CSI Min"),"Csh":METRICS_NAMES.index("CSI Max"),
                  "Prl":METRICS_NAMES.index("Precision Min"),"Prh":METRICS_NAMES.index("Precision Max"),
                  "Csm":METRICS_NAMES.index("CSI Majority"),"Prm":METRICS_NAMES.index("Precision Majority"),
                  "Mca":METRICS_NAMES.index("Majority Consistent ALGO"),"Mcm":METRICS_NAMES.index("Majority Consistent MAJO"),
                  "Tem":METRICS_NAMES.index("Truth is majority"), "Sam":METRICS_NAMES.index("Same outcome")}


ID_METRICS = {**ID_METRICS_SRC,**ID_METRICS_TD,**ID_METRICS_PRP}

#Number of metrics for the sources
NB_METRICS_SOURCES = len(ID_METRICS_SRC)
############ADD NEW METRIC############
