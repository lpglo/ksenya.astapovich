import re


def add_ing_to_words(text):
    def add_ing(word):
        return word + 'ing' if word else ''

    words = re.findall(r'\b\w+\b|[^\w\s]', text)

    result = ' '.join([add_ing(word) if word.isalpha() else word for word in words])

    return re.sub(r'\s+([^\w\s])', r'\1', result)


text = (
    "Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, facilisis vitae semper at,"
    + " dignissim vitae libero"
)

result_text = add_ing_to_words(text)

print(result_text)
