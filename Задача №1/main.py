import json


class CountriesIterate:

    list_names_and_links = list()

    def __init__(self, path_json):
        self.file = open(path_json)

    def __iter__(self):
        self.cursor = -1
        self.get_name_country()
        return self

    def get_name_country(self):
        countries_json = self.file.read()
        list_countries = json.loads(countries_json)
        for country in list_countries:
            name_country = country['name']['common'].replace(" ", "_")
            name_and_link_country = f"{country['name']['common']} – {'https://en.wikipedia.org/wiki/' + name_country}\n"
            self.list_names_and_links.append(name_and_link_country)

    def __next__(self):
        self.cursor += 1
        if self.cursor == len(self.list_names_and_links):
            raise StopIteration
        link = self.list_names_and_links[self.cursor]
        return link


with open('country_links.txt', 'a', encoding='UTF-8') as country_links_file:
    for country_link in CountriesIterate('countries.json'):
        country_links_file.write(f'{country_link}')

 
