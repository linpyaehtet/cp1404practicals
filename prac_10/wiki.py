import wikipedia

search_phrase = input("Enter page title: ")
while search_phrase != "":
    try:
        user_chosen_page = wikipedia.page(search_phrase)
        print(f"{user_chosen_page.title}")
        print(f"{user_chosen_page.summary}\n{user_chosen_page.url}")
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"We need a more specific title. Try one of the following, or a new search:\n{e.options}")
    except wikipedia.exceptions.PageError:
        print(f"Page id \"{search_phrase}\" does not match any pages. Try another id!")
    except Exception as e:
        print(f"(An unexpected error occurred: {e})")
    search_phrase = input("Enter page title: ")
    print()
print("Thank you.")

