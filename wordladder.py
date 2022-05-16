from collections import deque

class WordLadder:
  
  def __init__(self):
    pass

  def shortest_path(self, start, target, dictionary):
      
      if start == target:
        return ShortestPath(0, [])
      
      if target not in dictionary:
          return ShortestPath(0, [])
      
      umap = {}

      def add_intermediate(intermediate, word):
        words = umap.get(intermediate)
        if not words: words = []           
        if not word in words: words.append(word)
        if intermediate != word: umap[intermediate] = words
      
      def create_intermediates(word):
        for pos in range(-1, len(word), 1):      
          add = word[:pos+1] + "*" + word[pos+1:]      

          if pos == -1:
            pos = 0

          replace = word[:pos] + "*" + word[pos+1:]        
          delete = word[:pos] + "" + word[pos+1:]      
        
          intermediates = [add, replace, delete]      
          for intermediate in intermediates:
            add_intermediate(intermediate, word)   
      
      create_intermediates(start)

      for word in dictionary:      
        create_intermediates(word)      
                

      queue = deque()
      visited = {}
      path = {}      
      queue.append((start, 1))
      visited[start] = 1
      path[start] = []
      
      while (len(queue) > 0):          
          pair = queue.popleft()

          word = pair[0]
          dist = pair[1]

          if word == target:                        
            return ShortestPath(dist, path[target])

          for pos in range(-1, len(word), 1):      
            add = word[:pos+1] + "*" + word[pos+1:]      

            if pos == -1:
              pos = 0

            replace = word[:pos] + "*" + word[pos+1:]        
            delete = word[:pos] + "" + word[pos+1:]      

            intermediates = [add, replace, delete]
            for intermediate in intermediates:
              if not intermediate in umap: continue
              
              words = umap[intermediate]
                            
              for adjacent in words:
                if not adjacent in visited:
                  visited[adjacent] = 1
                  if path.get(word):
                    path[adjacent] = path.get(word) + [adjacent]
                  else:                    
                    path[adjacent] = [word, adjacent]                  
                  queue.append((adjacent, dist + 1))

      return ShortestPath(0, [])
 

class ShortestPath:

  def __init__(self, distance, path):
    self.distance = distance
    self.path = path
    pass
