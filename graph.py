import networkx as nx
import pandas as pd

df=pd.read_csv('hero-network.csv')
df.columns = ["char1", "char2"]

#Creating the Graph
G = nx.Graph()
n = len(df.char1)
for i in range(0,n):
  G.add_node(df.char1[i])
  G.add_node(df.char2[i])

#Initializing the weights to 1
for i in range(0,n):
  G.add_edge(df.char1[i], df.char2[i], weight=1)

#Updating weights for existing edges
for i in range(0,n):
  if(G.has_edge(df.char1[i], df.char2[i])):
    G[df.char1[i]][df.char2[i]]["weight"] += 1

#Pruning the graph
SG = nx.Graph([(u,v,d) for u,v,d in G.edges(data=True) if d['weight']>50])

#Converting subgraph into GML format
nx.write_gml(SG,"SG.gml")

