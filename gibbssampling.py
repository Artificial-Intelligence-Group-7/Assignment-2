class Network(object):
	def __init__(self):
		self.graph = {'amenities'	 : ['location'],
			      'neighbourhood'	 : ['location', 'children'],
			      'location'	 : ['age', 'price'],
			      'children'	 : ['schools'],
			      'age'		 : ['price'],
			      'schools'	 	 : ['price'],
			      'size'		 : ['price']}


class gibbsSampling(Network):
	def __init__(self,evidence,state,interest):
		Network.__init__(self)
		self.markovBlanket 	= []
		self.markovBlanket_temp = []
		self.evidenceNode	= evidence
		self.evidenceState 	= state
		self.interestNode 	= interest
		self.temp_interest = None
		self.Query = 'None'
		self.evidenceNodes = []
		self.evidenceValues = []
		self.iterations = 1
		self.discard_value = 0

    def read_arguments(self):
		parser = argparse.ArgumentParser(prog = 'gibbs', description = "Pass in all the arguments")
		parser.add_argument('QueryNode', type = str, help = "Enter the node to be queried")
		parser.add_argument('Evidence', nargs = '+', help = 'Enter the evidence nodes with its value')
		parser.add_argument('-u', type = int, help = "Number of Iterations")
		parser.add_argument('-d', type = int, default = 0, help = "Number of initial samples to drop")
		args = parser.parse_args()
		self.Query = args.QueryNode
		temp = args.Evidence
		self.evidenceNodes = [i.split('=', -1)[0] for i in temp]
		self.evidenceValues = [i.split('=', -1)[1] for i in temp]
		self.iterations = args.u
		self.discard_values = args.d
	
	def getParents(self,node):
		for parents,child in self.graph.iteritems():
			try:
				if child.index(node)+1:
					#print(parents)
					if parents not in self.markovBlanket_temp and parents!=self.temp_interest:
						self.markovBlanket_temp.append(parents)							
			except ValueError:
				pass

	def getChildren(self,node):
		children = self.graph[node]
		#print(children)		
		self.markovBlanket_temp.extend(children)
		for child in children:
			self.getParents(child)
	
	def getMarkovBlanket(self,node):
		self.temp_interest = node				
		self.markovBlanket_temp = []
		self.getParents(node)
		self.getChildren(node)
		if node == self.interestNode:
			self.markovBlanket = self.markovBlanket_temp[:]
		
if __name__ == "__main__":
	a = gibbsSampling('location','good','amenities')
	a.getMarkovBlanket('amenities')
	print(a.markovBlanket,a.markovBlanket_temp)
	a.getMarkovBlanket('location')
	print(a.markovBlanket,a.markovBlanket_temp)
