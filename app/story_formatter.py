def format_stories_to_string(stories):
    stories_string = ""
    for story in stories:
        title = story["title"]
        abstract = story["abstract"]
        section = story["section"]
        subsection = story["subsection"]
        stories_string += f"""Section: {section}\n Subsection: {subsection}\nTitle: {title}\nAbstract: {abstract}\n"""
    return stories_string
