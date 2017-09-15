import networkx as nx
from networkx.algorithms import bipartite
import pandas
import os

def get_data(filepath): # get raw data from csv file
	raw_data = pandas.read_csv(filepath).drop_duplicates()
	return raw_data

def get_input_data(raw_data): # format input data
    input_data = []
    for i in range(len(raw_data)):
        row = raw_data.iloc[i]
        actor = row[0]
        film = row[1]
        input_data.append((actor, film))
    return input_data

def create_bipartite_network(input_data): # create bipartite network by using networkx
    g = nx.Graph()
    g.add_edges_from(input_data)
    if bipartite.is_bipartite(g):
        NSet = nx.bipartite.sets(g) 
        Net1 = nx.project(g,NSet[0])
        Net2 = nx.project(g,NSet[1])
        return Net1, Net2
    else:
        print "Can't create bipartite network from input data"

def get_nodelist(net, filename): # output node list
    d = net.node
    with open(filename, 'w') as f:
        for node in d.keys():
            f.write(node + '\n')

def get_edgelist(net, filename): # output edgelist list
    d = net.edge
    with open(filename,'w') as f:
        for key in d:
            source = key
            for k in d[key]:
                target = k
                f.write(source + ',' + target + '\n')

def agg_fun(filepath):
	raw_data = get_data(filepath)
	input_data = get_input_data(raw_data)
	net1, net2 = create_bipartite_network(input_data)
	get_nodelist(net1, 'academics_node.txt')
	get_nodelist(net2, 'disciplines_node.txt')
	get_edgelist(net1, 'academics_edgelist.txt')
	get_edgelist(net2, 'disciplines_edgelist.txt')


if __name__ == '__main__':
	try:
		filepath = str(raw_input("Please input your .csv filepath: "))
		agg_fun(filepath)
		print 'Finished!'

	except Exception, e:
		print e
		print 0
