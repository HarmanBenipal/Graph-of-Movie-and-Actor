#

class BSGraph:
	ActMov = []
	edges = [[], []]

	def __init__(self):
		pass

	# Path of file is provided as inputfile
	# movieIndex variable is used to store the index of a movie in ActMov
	# actorIndex variable is used to store the index of an actor in ActMov
	# Relations between actor and movie are maintained in edges matrix
	def readActMovfile(self, inputfile):
		# Reading file line by line
		with open(inputfile) as file:
			lines = file.read()
		file.close()

		for line in lines.split("\n"):
			temp = line.split("/")             				# temp list variable contains a movie and actors of a line
			movieIndex = len(self.ActMov)     				# Initially, movieIndex is initialized to length of ActMov

			movie = temp[0].strip()            				# to remove the leading and trailing space from the movie

			# Is the movie exist in ActMov list

			if movie in self.ActMov:
				movieIndex = self.ActMov.index(movie) 		# Exists, movieIndex is updated equal to that index
			else:
				self.ActMov.append(movie) 					# Doesn't exists,add movie to the list and index remains same

			# iterate through list
			for actor in temp[1:]:
				actor = actor.strip() 						# Removing leading and trailing space of an actor
				actorIndex = len(self.ActMov) 				# actorindex is initialized to length of ActMov

				# Is the actor exist in ActMov list

				if actor in self.ActMov:
					actorIndex = self.ActMov.index(actor)	# Exists, actorindex is updated equal to that index
				else:
					self.ActMov.append(actor)				# Doesn't exists,add actor to the list and actorindex remains same

				# to keep track of relationships between movie and actor, movieIndex is added at 0 and actorIndex is added at 1
				self.edges[0].append(movieIndex)
				self.edges[1].append(actorIndex)

	# print self.ActMov, self.edges

	def displayActMov(self):

		# Opening in writing mode and + sign, if file not present then create it
		f = open("outputPS2.txt", "w")
		f.write("--------Function displayActMov--------\n")
		movies = set(self.edges[0])							# movies set to store all unique movie index

		# length of unique movies set

		f.write("Total no. of movies: " + str(len(movies)) + "\n")

		actors = set(self.edges[1])							# actors set to store all unique actor index

		# length of unique actors set

		f.write("Total no. of actors: " + str(len(actors)) + "\n\n")

		# whether length of movies set is not zero

		if len(movies) != 0:
			f.write("List of movies:\n")

			# iterate over movies set that contains index of movies in ActMov

			for movieIndex in movies:
				f.write(self.ActMov[movieIndex] + "\n")
			f.write("\nList of actors:\n")

			# iterate over actors set that contains indexes of actors in ActMov

			for actorIndex in actors:
				f.write(self.ActMov[actorIndex] + "\n")

		f.write("-----------------------------------------\n")
		f.close()

	# This method is for displaying all actors of a given movie.
	def displayActorsOfMovie(self, movie):

		# 'a+' Open for reading and writing.The file is created if it does not exist.The stream is positioned at the end of the file.

		file = open("outputPS2.txt", "a+")
		file.write("--------Function displayActorsOfMovie--------\n")
		file.write("Movie name: " + movie + "\n")
		file.write("List of Actors:\n")

		# movieIndex is to store index of a given movie in ActMov list
		movieIndex = self.getIndex(movie)

		# check whether movieIndex is not equal to -1

		if movieIndex != -1:
			index = 0													# index is to keep the track of traversed movies in edges matrix to find index of actor

			# iterate through edges[0] (indexes of movies)
			for edge_movieIndex in self.edges[0]:
				if edge_movieIndex == movieIndex:						# check for movieIndex and edge_movieIndex are equal
					edge_actorIndex = self.edges[1][index]				# it results in index of actor
					try:
						actor = self.ActMov[edge_actorIndex]			# gives actor name at the calculated index
					except Exception:
						actor = "No actor found"
					file.write(actor + "\n")
				index = index + 1
		else:
			file.write("Sorry! Movie not Found.\n")
		file.close()

	# This method is for displaying all movies of a given actor.
	# Edges matrix is used to find out as it contains relation between actor and movie vertices.
	def displayMoviesOfActor(self, actor):

		# 'a+' Open for reading and writing.The file is created if it does not exist.The stream is positioned at the end of the file.
		file = open("outputPS2.txt", "a+")

		file.write("--------Function displayMoviesOfActor--------\n")
		file.write("Actor name: " + actor + "\n")
		file.write("List of Movies:\n")

		# actorIndex is to store index of a given actor in ActMov so that we can compare to find movies of the actor
		actorIndex = self.getIndex(actor)

		if actorIndex != -1:
			index = 0													# index is to keep the track of traversed actors in edges matrix to find index of movies

			# iterate through edges[1] (indexes of actors)

			for edge_actorIndex in self.edges[1]:
				if edge_actorIndex == actorIndex:						# check for actorIndex and edge_actorIndex are equal
					edge_movieIndex = self.edges[0][index]				# it results in index of movies
					try:
						movie = self.ActMov[edge_movieIndex]			# gives actor name at the calculated index
					except Exception:
						movie = "No movie found"
					file.write(movie+ "\n")
				index = index + 1
		else:
			file.write("Sorry! Actor not Found.\n")
		file.close()

		# to find index of an item in the ActMov list.Item can be an actor or a movie.
	def getIndex(self, item):
		index = 0
		for i in self.ActMov:
			if i == item:
				return index
			index = index + 1
		return -1

	#This method gives the list of actor in the movie
	def getActors(self, movie):
		movieIndex = self.getIndex(movie)							# movieIndex is to store index of movie in MovAct
		actors = []

		if movieIndex != -1:
			index = 0

			# iterate through edges[0] (indexes of movies)

			for edge_movieIndex in self.edges[0]:
				if edge_movieIndex == movieIndex:					# check for movieIndex and edge_movieIndex are equal
					edge_actorIndex = self.edges[1][index]			# with the help of index find out actorIndex from edges
					try:
						actor = self.ActMov[edge_actorIndex]		# actor stores name
					except Exception:
						actor = ""
					actors.append(actor)							# list of actors
				index = index + 1
		return actors

	# This method displays the list of actors those are common in both the movies.
	def getCommonActor(self, movA, movB):
		actorsA = self.getActors(str(movA.strip()))
		actorsB = self.getActors(str(movB.strip()))
		common = (x for x in actorsA if x in actorsB) 				# checking whether there is any common actor
		for actor in common:
			return actor
		return

	# This method tells whether there is any relation between movA and movB
	# movA is related to movB if there is atleast one common actor between them
	def findMovieRelation(self, movA, movB):
		file = open("outputPS2.txt", "a+")
		file.write("--------Function findMovieRelation --------\n")
		file.write("Movie A: " + movA + "\n")
		file.write("Movie B: " + movB + "\n")

		actor = self.getCommonActor(movA, movB)
		if actor and (actor != ""):
			file.write("Related: Yes, " + actor + "\n")
		else:
			file.write("Sorry! No Relation Found.\n")
		file.close()
		return

	# This method tells whether there is any trans relation between movA and movB
	# movA is trans related to movB if R(movA,movC) and R(movC,movB) exists
	def findMovieTransRelation(self, movA, movB):
		relation = False
		movA = movA.strip()
		movB = movB.strip()
		file = open("outputPS2.txt", "a+")
		file.write("--------Function findMovieTransRelation --------\n")
		file.write("Movie A: " + movA + "\n")
		file.write("Movie B: " + movB + "\n")
		movies = set(self.edges[0])									# movies contains all the unique indexes of movie(Vertices)
		if len(movies) != 0:

			#iterate through movies set

			for movieIndex in movies:
				new_movie = self.ActMov[movieIndex]

				if new_movie == movA :     							# new_movie should be different from movA and movB
					continue

				actorA = self.getCommonActor(movA, new_movie)  		#common actor between movA and new_movie
				if actorA and actorA != "":
					actorB = self.getCommonActor(new_movie, movB)	#common actor between movB and new_movie
					if actorB and actorB != "":
						file.write("Related: Yes, " + movA + " > " + actorA + " > " + new_movie + " > " + actorB + " > " + movB + "\n")
						relation = True
		if not relation:
			file.write("Sorry! No Movie Trans Relation Found.\n")
		file.close()
		return

	def tests(self):
		with open("promptsPS2.txt") as file:
			lines = file.read()
		file.close()

		for line in lines.split("\n"):
			if "searchActor" in line:
				actor = line.replace("searchActor:", "").strip()
				self.displayMoviesOfActor(actor)
			elif "searchMovie" in line:
				movie = line.replace("searchMovie:", "").strip()
				self.displayActorsOfMovie(movie)
			elif "TMovies" in line:
				movies = line.replace("TMovies:", "").strip().split(":")
				self.findMovieTransRelation(movies[0], movies[1])
			elif "RMovies" in line:
				movies = line.replace("RMovies:", "").strip().split(":")
				self.findMovieRelation(movies[0], movies[1])

if __name__ == "__main__":
	bsGraph = BSGraph()
	bsGraph.readActMovfile("inputPS2.txt")
	bsGraph.displayActMov()
	bsGraph.tests()
