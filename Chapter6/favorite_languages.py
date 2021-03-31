favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for user in sorted(favorite_languages.keys()):
    print(user.title())

print("\n")

for language in set(favorite_languages.values()):
    print(language.title())