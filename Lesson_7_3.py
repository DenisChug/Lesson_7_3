class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                text_file = file.read().lower()
                for i in punctuation:
                    text_file = text_file.replace(i,'')
                all_words[name] = text_file.split()
        return all_words

    def find(self, word):
        rez = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                rez[name] = str((words.index(word.lower()) + 1))
        return rez

    def count(self, word):
        rez = {}
        counter = 0
        for name, words in self.get_all_words().items():
            for item in words:
                if word.lower() == item:
                    counter += 1
        rez[name] = counter
        return rez




finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('text')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))
