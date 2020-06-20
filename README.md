# Graph-of-Movie-and-Actor

Problem Statement 
Assume that you are managing an entertainment website for which you have to store information about movies and the actors who played a role in them. You are given a list of N actors and M movies with the following two constraints. 
1. A movie can have at most 2 actors associated with it. 
2. A particular actor can act in more than 2 movies. 
Model the following problem as a graph based problem. Clearly state how the vertices and edges can be modelled such that this graph can be used to answer the following queries efficiently. 
The queries are: 
    1. List the movies and the actors represented in the graph 
    2. List the names of the movies in which performer A has acted 

3. List the names of the performers in the movie X 
4. Consider the following relation R on the movies 
"Movie A is related to Movie B if there is at least one actor common in the movies A and B. In this case, we write R(A, B)".
Given any two movies A and B, verify if R(A, B)? 

5. Consider the following relation T on the movies. T(A, B) is true if 
  a. T(A, B) = R(A , B) (or)
  b. There is a movie C such that R(A, C) and also R(C, B). Given any two movies A and B, verify if T(A, B) exists / is True? 
6. Perform an analysis for the questions above and give the running time. 


 
