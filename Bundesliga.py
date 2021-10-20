import pandas as pd
import numpy as np
import networkx
import networkx.convert_matrix as nx
import pyvis
import os
os.chdir("C:\\Users\\Tobias\\Documents\\Promotion\\Netzwerke")


# https://towardsdatascience.com/social-network-analysis-from-theory-to-applications-with-python-d12e9a34c2c7
# https://github.com/ewenme/transfers
# https://towardsdatascience.com/visualizing-networks-in-python-d70f4cbeb259

Edges = pd.DataFrame({"source": ["a", "b", "b", "c", "a"],
                      "target": ["b", "a", "c", "a", "d"],
                      "weight": [3, 0.5, 2,0.1, 0.5], })

G = nx.from_pandas_edgelist(Edges,
                            source = "source",
                            target = "target",
                            edge_attr="weight",
                            create_using=networkx.DiGraph())
networkx.draw_networkx(G)




BuLi19 = pd.read_csv("2019_german_bundesliga_1.csv")

BuLi19.head()



def DelCol(DF):
    DF = DF.loc[DF["transfer_movement"]=="in"] # only one direction of transfers should be considered
    DF = DF.loc[DF["fee_cleaned"]>0] # only "real" transfers
    del DF["player_name"]
    del DF["transfer_movement"]
    del DF["age"]
    del DF["position"]
    del DF["fee"]
    del DF["transfer_period"]
    del DF["league_name"]
    del DF["year"]
    del DF["season"]
    return(DF)



BuLi19 = DelCol(BuLi19)



G = nx.from_pandas_edgelist(BuLi19,
                            source = "club_name",
                            target = "club_involved_name",
                            edge_attr="fee_cleaned",
                            create_using=networkx.DiGraph()



                )


networkx.draw_kamada_kawai(G, with_labels=False)
networkx.show()
