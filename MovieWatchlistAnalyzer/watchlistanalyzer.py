"""
MOVIE WATCHLIST ANALYZER
Step01: Create a list of dictionaries having movie title, genre, rating, year
Step02: Create a user_watchlist dictionary having the list of movie titles under their name as key.
Step03: Create the display movies function. This will print mvoies in tabular format.
Step04: Create function to get the highest rated movies. Use sorted function, key as ratings, reverse = True.
     --> Get the top X movies that the user specifies and display it using display function
Step05: Function to filter movies after the year specified. Use list comprehension and give condition e.g. movies['year'] > 2020
Step06: Create function to get a set of all genres in the movies list.
Step07: Use the above function to create search_by_genre function. Check whether a searched genre exists or not
     --> if exists then return movies having that genre
Step08: Now move to watchlist operation. Create a function to add movie to some users watchlist
     --> Input username and movie name. If moviename exists in movies list then only proceed
     --> If username exists and movie name not present then append the movie name to that users list 
     --> If username not exists, create a new key of username and add the list as value
Step09: Create display watchlist function t display watchlist of any user. Take input of the username. Display the movie titles
Step10: Create a function to get the users genres in a set.
     --> Use for loop to loop through the usernames.
     --> use nested loops to loop through the movies list. 
     --> If movie title matches with the users movie in watchlist, append the genre of that movie to genre dictionary under user's key
Step11: Use the get_users_genre to compare the genre matching between 2 users. This function matches the genre using '&'.
Step12: Use the main function for the whole application to function seamlessly.
"""

movies = [
    {
        "title": "Interstellar",
        "genre": "Sci-Fi",
        "rating": 9.1,
        "year": 2014
    },
    {
        "title": "Oppenheimer",
        "genre": "Drama",
        "rating": 8.9,
        "year": 2023
    },
    {
        "title": "Dune: Part Two",
        "genre": "Sci-Fi",
        "rating": 8.7,
        "year": 2024
    },
    {
        "title": "The Batman",
        "genre": "Action",
        "rating": 7.8,
        "year": 2022
    },
    {
        "title": "Parasite",
        "genre": "Thriller",
        "rating": 8.5,
        "year": 2019
    }
]

user_watchlist = {
   "Sagnik": ["Interstellar", "Dune: Part Two", "Parasite"],
   "Soma": ["Parasite", "The Batman", "Oppenheimer"]
   }

def display_movies(dict):
   print(
      f"{'Movies':<18}"
      f"{'Genre':<12}"
      f"{'Rating':<8}"
      f"{'Year':<6}"   
   )
   print("-"*43)
   for movie in dict:
      print(
         f"{movie['title']:<18}"
         f"{movie['genre']:<12}"
         f"{movie['rating']:<8}"
         f"{movie['year']:<6}"
      )



def highest_rated():
   x = int(input("\nFilter top X: "))
   sorted_ratings = sorted(movies, key = lambda x: x['rating'], reverse = True)
   top_x = sorted_ratings[:x]
   return top_x, x


def movies_after_year():
   year = int(input("\nFilter movies after year: "))
   filtered = [movie for movie in movies if movie['year'] > year]
   return filtered


def get_genre():
   genre = {movie['genre'] for movie in movies}
   return genre


def search_by_genre(genre):
   while True:
      search = input("\nSearch by Genre: ").strip().lower()
      if search in [x.lower() for x in genre]:
         filtered_genre = [movie for movie in movies if movie['genre'].lower() == search]
         break
      else:
         print("Searched genre is not available")
   return filtered_genre


def add_watchlist(watchlist):
   user = input("Enter username: ")
   while True:
      name = input("Enter movie name: ")
      if name not in [movie['title'] for movie in movies]:
         print("This movie is not available in our library")
         continue
      if user not in watchlist.keys():
         watchlist[user] = [name]
         print("User and movie Added.")
         break
      elif name in watchlist[user]:
         print(f"Movie already exists in {user}'s watchlist")
      else:
         watchlist[user].append(name)
         print("User watchlist updated.")
         break
   return watchlist


def display_user_watchlist(watchlist):
   while True:
      name = input("\nEnter Username: ")
      if name in watchlist.keys():
         print(f"\nUser: {name} ->")
         for movie in watchlist[name]: print(f"{movie}")
         break
      print("Username not found.")


def get_user_genre(watchlist):
   user_genre = {}
   for name in watchlist.keys():
      all_genre = []
      for movie in movies:
         if movie['title'] in watchlist[name]:
            all_genre.append(movie['genre'])
      user_genre[name] = set(all_genre)

   return user_genre


def compare_user(user_genre):
   while True:
      user_1 = input("\nEnter first user: ")
      user_2 = input("Enter second user: ")
      if user_1 not in user_genre.keys() or user_2 not in user_genre.keys():
         print("User not found. Try again")
         continue
      common = user_genre[user_1] & user_genre[user_2]
      print(f"Common Genre between {user_1} and {user_2}: ")
      for i in common: print(i)
      break


def main():
   print("\n===== MOVIE WATCHLIST ANALYZER =====\n")
   while True:
      print("\n1. Display Movies")
      print("2. Top Rated Movies")
      print("3. Filter Movies by Year")
      print("4. Search By Genre")
      print("5. See User Watchlist")
      print("6. Add movies to user watchlist")
      print("7. Compare 2 Users based on their Genre")
      print("8. Exit")
      
      option = int(input("Enter any option between [1-7]: "))

      if option == 1:
         display_movies(movies)

      elif option == 2:
         top_rated, x = highest_rated()
         print(f"\nTop {x} Movies: ")
         display_movies(top_rated)

      elif option == 3:
         filtered_year = movies_after_year()
         display_movies(filtered_year)

      elif option == 4:
         all_genre = get_genre()
         search = search_by_genre(all_genre)
         display_movies(search)

      elif option == 5:
         display_user_watchlist(user_watchlist)

      elif option == 6:
         add_watchlist(user_watchlist)

      elif option == 7:
         user_genre = get_user_genre(user_watchlist)
         compare_user(user_genre)

      elif option == 8:
         break
         
      else:
         print("Invalid Input. Enter between [1-8]")
         break

main()