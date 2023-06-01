"""
Description:
 Uses a complex data structure to store information about me.

Usage:
 python about_me.py
"""
def main():
    # Step 2: Create a complex data structure that holds information about me
    about_me = {
        # TODO: Put full name into data structure
        'Name' : 'Manuprasad Variyath Jayakumar', 
        # TODO: Put student ID into data structure
        'student ID' : '10291276',
        # TODO: Put list of 3 pizza toppings into data structure
        'pizza toppings' : ['mushroom',
                            'pineapple' 
                            
        ],

        'movies': [
            # TODO: Change this to a movie you like
            {
                'title': 'Shoalin Soccer',
                'genre': 'comedy'
            },
            # TODO: Add one more movie
            {
                'tittle' : 'Kungfu Hustle',
                'genre' : 'action' 
            }
        ]
    }

    # Step 3: Print student name and ID
    print_student_name_and_id(about_me)

    # Step 4: Print a bullet list of pizza toppings
    print_pizza_toppings(about_me)

    # Step 5: Add pizza toppings to the data structure
    # TODO: Change to pizza toppings you like
    add_pizza_toppings(about_me, ['olives', 'onion'])
    print_pizza_toppings(about_me)

    # Step 6: Add another movie to the data structure
    # TODO: Change to a movie you like
    add_movie(about_me, 'Iron Man', 'action')

    # Step 7: Print a comma-separated list of movie genres
    print_movie_genres(about_me)

    # Step 8: Print a comma-separated list of movie titles
    print_movie_titles(about_me['movies'])

def print_student_name_and_id(my_info):
    """Prints sentences containing student name and ID

    Args:
        my_info (dict): Data structure containing information about me
    """
    # TODO: Complete function body per Step 3
    # Print sentence containing name
    # Print sentence containing student ID
    full_name = my_info['Name']
    first_name = full_name.split()[0]
    student_id = my_info['student ID']

    print(f"My name is {full_name}, but you can call me Sir {first_name}.")
    print(f"My student ID is {student_id}.")


def print_pizza_toppings(my_info):
    """Prints a bullet list of favourite pizza toppings

    Args:
        my_info (dict): Data structure containing information about me
    """
    print(f'My favourite pizza toppings are: ')
    for pizza_toppings in my_info['pizza toppings']:
        print(f'- {pizza_toppings}')

     
        
       


def add_pizza_toppings(my_info, toppings):
    """Adds some pizza toppings to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        toppings (list): List of pizza toppings
    """
    my_info['pizza toppings'].extend(list(toppings))
    for i, pizza_topping in enumerate(my_info['pizza toppings']):
        my_info['pizza toppings'][i] = pizza_topping.lower()
    my_info['pizza toppings'].sort()

    return 


    
def add_movie(my_info, title, genre):
    """Adds a movie to the list of favourites

    Args:
        my_info (dict): Data structure containing information about me
        title (str): Movie title
        genre (str): Movie genre
    """
    new_movie = {"title": title, "genre": genre}
    my_info["movies"].append(new_movie)

    return 




def print_movie_genres(my_info):
    """Prints a sentence listing all favourite movie genres

    Args:
        my_info (dict): Data structure containing information about me
    """
    genres = [New_movie['genre'] for New_movie in my_info['movies']]
    genres_list = ', '.join(genres) 
    print(f" I like to watch {genres_list} movies.")
    



def print_movie_titles(movie_list):
    """Prints a sentence listing all favourite movie titles

    Args:
        movie_list (list): List of favourite movies
    """
    movie_names = [New_movie['title'] for New_movie in movie_list]
    all_movies = ', '.join(movie_names)
    print(f'Some of my favourite movies are {all_movies}!')



if __name__ == '__main__':
    main()