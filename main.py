favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edwin': ['ruby', 'go'],
    'phil': ['python', 'haskel'],
}

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages "
              f"are: ")
    elif len(languages) <= 1:
        print(f"\n{name.title()}'s favorite language "
              f"is: ")
    for language in languages:
        print(f"\t{language.title()}")
