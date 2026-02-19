

# Prints documents in good way
def print_docs(docs):
    for d in docs:
        print(
            f'Title: "{d["title"]}"  ' #here and below have space to seperate ethe feild better, prints it by colums
            f'Genres: {(d["genres"]).title()}  '
            f'Director: {d["director"].title()}  '
            f'Length: {d["length"]} min'
        )