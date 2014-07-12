
import time
start_time = time.time()
fi = open('dijkstraData.txt')
#fi = open('test_case.txt')
Graph={}
n=0
for line in fi:
    li = line.split()
    vertex = li[0]
    for we in li[1:]:
        we = we.split(',')
        #we[0] int(we[1])
        Graph[vertex] = Graph.get(vertex,{})
        Graph[we[0]] = Graph.get(we[0],{})
        Graph[vertex][we[0]] = int(we[1])
        Graph[we[0]][vertex] = int(we[1])
    n+=1
#print Graph    
#created a dictionary with each vertex as the key
#& the value as an inner dictionary. Each key of this inner dictionary is
# the connected vertex and the value is the edge cost  
fi.close()

dict_shortest_path={}
dict_shortest_path['1']=0
while True:
    minimum = 1000000
    for v in dict_shortest_path.keys():
        #print v
        dests= Graph[v]
        for d in dests:
            if dict_shortest_path.get(d,-1)==-1:
                sp = dict_shortest_path[v]+Graph[v][d]
                if sp < minimum:
                    minimum = sp
                    w_star = d
    dict_shortest_path[w_star]=minimum
    #print "Shortest paths : ", dict_shortest_path        
    if len(dict_shortest_path)==n:
        break
#print dict_shortest_path
print dict_shortest_path['7']

print "The time taken by the algorithm to run"
print time.time() - start_time, "seconds"
