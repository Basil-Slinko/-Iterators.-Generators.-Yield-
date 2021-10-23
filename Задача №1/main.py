import json


class CountriesIterate:

    def __init__(self, path_json, path_list_links):
        self.file = open(path_json)
        self.path_list_links = path_list_links

    def __iter__(self):
        self.get_name_country()
        return self

    def get_name_country(self):
        countries_json = self.file.read()
        list_countries = json.loads(countries_json)
        for country in list_countries:
            name_country = country['name']['common'].replace(" ", "_")
            name_and_link_country = f"{country['name']['common']} – {'https://en.wikipedia.org/wiki/' + name_country}\n"
            with open(self.path_list_links, 'a', encoding='UTF-8') as country_links_file:
                country_links_file.write(f'{name_and_link_country}')

    def __next__(self):
        if self.__iter__() is None:
            raise StopIteration
        return self


if __name__ == '__main__':
    pr = CountriesIterate('countries.json', 'countries_list.txt')
    pr.__iter__()
