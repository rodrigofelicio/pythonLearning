movies =[]
MENU_PROMPT = "\nEnter 'a' to ADD a movie, 'l' to SEE your movies, 'f' to FIND a movie by title, or 'q' to QUIT: "

def list_movies():
    for movie in movies:
        print_movie(movie)


def print_movie(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Release Year: {movie['year']}") 


def add_movie():
    title = input("Enter the movie title: ")
    director = input("Enter the movie director: ")
    year = input("Enter the movie release year: ")
    
    movies.append({
        'title': title,
        'director': director,
        'year': year
    })
    list_movies()


def find_movie_by_title():
    movie_title = input("Please, enter the movie title: ")

    for movie in movies:
        if movie["title"] == movie_title:
            print_movie(movie)

user_options = {
    "a": add_movie,
    "l": list_movies,
    "f": find_movie_by_title
}

def menu():
    action = input(MENU_PROMPT)
    while action !='q':
        if action in user_options:
            selected_function = user_options[action]
            selected_function()
        else:
            print(f"Unknown command. please, {MENU_PROMPT}")
        
        action = input(MENU_PROMPT)

menu()