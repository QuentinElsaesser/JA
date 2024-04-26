# from v4.constants import constants
# from v4.vote import normalize as nm

# import matplotlib.pyplot as plt
# import re

# class BoxPlot():
#     def __init__(self, name, index_m, nb_metrics_sources, percent, directory="../png/"):
#         """
#         gen box plot depending on the percent
#         """
#         self.name_file_error = name
#         self.directory = directory

#         self.metric = "Sources Reliability"
#         self.nb_metrics_sources = nb_metrics_sources
#         self.index_m = index_m
#         self.curr_src = -1
        
#         self.res = []
#         self.percent = percent
        
#         self.normaA = constants.NORMA_A
#         self.normaO = constants.NORMA_O
    
        
#         self.xlabel = ""
#         self.ylabel = ""
#         self.ylim = [0,1]
#         self.name_file = "bxp"
        
#         #index0=normaA / index1=normaC
#         #index00=normaA s1 proba;trust plu;trust bor
#         self.data = []
#         self.options = []
        
#         self.para_plot = [("-d", 'blue', f"pl{self.normaA}"), 
#                           ("-v", 'black', f"pl{self.normaO}"),
#                           ("-s", 'red', f"bor{self.normaA}"),
#                           ("-h", 'orange', f"bor{self.normaO}")]
        
#         self.file = open(name, "r")
        
#         self.read_file()
        
#         self.file.close()
        
#         self.draw()
    
#     def get_info(self, line):
#         """
#         """
#         x = line.find("&")
#         v1 = self.to_digit(line[:x])
#         line = line[x+1:]
        
#         x = line.find("&")
#         v2 = self.to_digit(line[:x])
#         line = line[x+1:]
        
#         x = line.find("&")
#         v3 = self.to_digit(line[:x])
#         line = line[x+1:]
        
#         return [v1,v2,v3], line
        
#     def isfloat(self, num):
#         try:
#             float(num)
#             return True
#         except ValueError:
#             return False
        
#     def to_digit(self, elt):
#         """
#         get a float from \textbf{7.017} or 9.58\\ or 9.58
        
#         elts : string
#         index : index of the current string 
#         length : number of string in the line
#         """
#         elt = elt.strip()
#         if not self.isfloat(elt):
#             elt = elt[:-2]
#         return float(elt)   
    
#     def read_file(self):
#         line = self.file.readline()
#         while (self.metric not in line):
#             line = self.file.readline()
#             if "\end{document}" in line:
#                 raise ValueError(f"END OF FILE : metric {self.metric} isn't in {self.name_file_error}.")

#         while True:
#             if line.startswith("\subsection"):
#                 tmpprc = line[12:-4]
#                 if tmpprc.isnumeric():
#                     if int(tmpprc) == self.percent:
#                         break
#                 else:
#                     t = tmpprc.split("-")
#                     if int(t[0]) <= self.percent <= int(t[1]):
#                         break
#             line = self.file.readline()
            
#             if "\end{document}" in line:
#                 raise ValueError(f"END OF FILE : percentage {self.percent} isn't in {self.name_file_error}.")
        
#         #ignore line with the percentage
#         line = self.file.readline()
#         data = []
#         proba = []
#         plu = []
#         bor = []
        
#         while "section" not in line:
#             # print(line)
#             if line.startswith("\\noindent Results"):
#                 src = re.findall(r'\d+',line)
#                 if "Plurality A" in line:
#                     norma = constants.NORMA_A
#                 else:
#                     norma = constants.NORMA_O_NAME
#                 self.options.append([src[0], line[-6:-2], self.percent, norma])
                
#             if line.startswith('s'):
#                 line = line[line.find("&")+1:]
#                 proba,line = self.get_info(line)
#                 plu,line = self.get_info(line)
#                 bor,line = self.get_info(line)
#                 data.append([proba, plu, bor])
                
#             if line.startswith('\\end{tabular}'):
#                 self.data.append(data)
#                 data = []
            
#             line = self.file.readline()
#         # print(self.data)
#         # print()
#         # print(self.data[0])
#         # print(self.options)
        
#     def my_plot(self, i, j):
#         tmp = []
#         for k in range(len(self.data[i])):
#             tmp.append(self.data[i][k][j])
#         print(tmp)
        
#         plt.boxplot(tmp, showfliers=False, patch_artist=True,
#                     boxprops=dict(facecolor=self.para_plot[j][1], 
#                                   color=self.para_plot[j][1]))
        
#     def draw(self):
#         """
#         https://stackoverflow.com/questions/41997493/python-matplotlib-boxplot-color
#         """
#         # fig, ax = plt.subplots()
        
#         for i in range(len(self.options)):
#             print(self.options[i])
#             for j in range(len(self.data[i])):
#                 print(self.data[i][j])
        

#         # #normaA - proba
#         self.my_plot(0, 0)
#         # #normaA - trust pl
#         # self.my_plot(0, 1)
#         # #normaA - trust bor
#         # self.my_plot(0, 2)
        
#         # #normaC - proba
#         # self.my_plot(0, 0)
#         # #normaC - trust pl
#         # self.my_plot(0, 1)
#         # #normaC - trust bor
#         # self.my_plot(0, 2)
        
#         plt.ylim(self.ylim)
        
#         ticks_size = 15
#         plt.xticks(fontsize=ticks_size)
#         plt.yticks(fontsize=ticks_size)
        
#         fontsize = 30
#         plt.xlabel(self.xlabel, fontsize=fontsize)
#         plt.ylabel(self.ylabel, fontsize=fontsize)
#         plt.legend(fontsize=fontsize)
        
#         plt.show()
        
#         # print(plt.boxplot.__dict__)
        
#         # plt.save()
        
#         #normaA - proba
#         # self.my_plot(0, 0)
#         #normaA - trust bor
#         # self.my_plot(0, 2)
                


        
        
        
        
        
#         # plt.save()
