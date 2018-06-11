# Recommender System

Original matrix (Rows=Users, Columns=Ratings from 0-5, 0=User has not rated the movie):  
```
[0.0000, 4.0000, 5.0000, 0.0000, 4.0000, 4.0000, 0.0000]  
[4.0000, 0.0000, 4.0000, 0.0000, 0.0000, 3.0000, 0.0000]  
[5.0000, 3.0000, 1.0000, 2.0000, 5.0000, 0.0000, 2.0000]  
[4.0000, 1.0000, 5.0000, 1.0000, 1.0000, 5.0000, 4.0000]  
[1.0000, 5.0000, 0.0000, 4.0000, 0.0000, 0.0000, 0.0000]  
[0.0000, 0.0000, 0.0000, 0.0000, 5.0000, 2.0000, 0.0000]  
[0.0000, 1.0000, 5.0000, 1.0000, 0.0000, 0.0000, 1.0000]  
[2.0000, 0.0000, 1.0000, 0.0000, 2.0000, 2.0000, 0.0000]  
[2.0000, 5.0000, 0.0000, 1.0000, 5.0000, 0.0000, 0.0000]  
[3.0000, 2.0000, 5.0000, 0.0000, 0.0000, 1.0000, 0.0000]  
```
Output:

List of recommendations based on user similarity:   
Person 1 will most likely enjoy movie 1.  
Person 1 will most likely enjoy movie 4.  
Person 1 will most likely enjoy movie 7.  
Person 2 will most likely enjoy movie 7.  
Person 5 will most likely enjoy movie 5.  
Person 6 will most likely enjoy movie 1.  
Person 6 will most likely enjoy movie 7.  

List of recommendations based on movie/item similarity:   
Person 1 will most likely enjoy movie 1.  
Person 2 will most likely enjoy movie 2.  
Person 2 will most likely enjoy movie 5.  
Person 5 will most likely enjoy movie 5.  
Person 6 will most likely enjoy movie 2.  
Person 7 will most likely enjoy movie 6.  
