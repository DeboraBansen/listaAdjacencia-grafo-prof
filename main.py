class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.explored = 0
        
    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

cc={}#variável global de componentes conexos

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()

    def bfs(self, v):
      for i in self.vert_dict:
        self.vert_dict[i].explored = 0
      self.vert_dict[v].explored = 1
      Queue = []
      Queue.append(v)
      while(len(Queue)>0):
        w = Queue.pop(0)
        for j in self.vert_dict[w].get_connections():
          if(j.explored==0):
            print("Explorado: ",j.get_id())
            j.explored=1
            Queue.append(j.get_id())

    def dfs(self, v):
      for i in self.vert_dict:
        self.vert_dict[i].explored = 0
      Queue = []
      Queue = [v]+Queue
      while(len(Queue)>0):
        w = Queue.pop(0)
        print("Explorado: ",w)
        self.vert_dict[w].explored = 1
        for j in self.vert_dict[w].get_connections():
          if(j.explored==0):
            
            Queue=[j.get_id()]+Queue

 #Componentes conexos busca bfs
    def ccBfs(self):
      id=0
      for v in self.vert_dict:
        cc[v]=-1
      for v in self.vert_dict:
        if cc[v]==-1:
          id=id+1
          self.BFS(v,id) 
    
    def BFS(self,s,id):
      for i in self.vert_dict:
        self.vert_dict[i].explored = 0
      self.vert_dict[s].explored = 1
      cc[s]=id
      Queue = []
      Queue.append(s)
      while(len(Queue)>0):
        w = Queue.pop(0)
        for j in self.vert_dict[w].get_connections():
          if(j.explored==0):
            j.explored=1
            cc[j.get_id()]=id
            Queue.append(j.get_id())
  #---------------------------------------------------        
    def dijkstra(self,a ,b):
      for i in self.vert_dict:
        self.vert_dict[i].explored = 0
      self.vert_dict[a].explored = 1
      custo=500
      lista=[]
      Queue = []
      Queue.append(a)
      while(len(Queue)>0):
        w = Queue.pop(0)
        print(w)
        self.vert_dict[w].explored = 1
        custo=500
        for j in self.vert_dict[w].get_connections():
          if(j.get_id()!=b):
            #print(j.get_id())
            if(j.explored==0):
              
              if(self.vert_dict[w].get_weight(j)<custo):
                
                custo=self.vert_dict[w].get_weight(j)
                #print(custo)

                if(len(Queue)>0):
                  Queue.pop(0)
                  Queue.append(j.get_id())  
                else:  
                  Queue.append(j.get_id()) 
          else:
            if(len(Queue)>0):
              Queue.pop(0)
            break        
      print(b)
      #lista.append(b)       
      #if i in lista:
       # print(i)
        


    

if __name__ == '__main__':

    g = Graph()

    g.add_vertex('a')
    g.add_vertex('b')
    g.add_vertex('c')
    g.add_vertex('d')
    g.add_vertex('e')
    g.add_vertex('f')

    g.add_edge('a', 'b', 7)  
    g.add_edge('a', 'c', 9)
    g.add_edge('a', 'f', 14)
    g.add_edge('b', 'c', 10)
    g.add_edge('b', 'd', 15)
    g.add_edge('c', 'd', 11)
    g.add_edge('c', 'f', 2)
    g.add_edge('d', 'e', 6)
    g.add_edge('e', 'f', 9)

    for v in g:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print ('( %s , %s, %3d)'  % ( vid, wid, v.get_weight(w)))

    for v in g:
        print ('g.vert_dict[%s]=%s' %(v.get_id(), g.vert_dict[v.get_id()]))

    '''g.ccBfs()
    print('\nComponentes Conexos:')
    for i in cc:
      print('vertice[%s]=%d'%(i,cc[i]))'''

    #g.dijkstra('e','a')  
      

    