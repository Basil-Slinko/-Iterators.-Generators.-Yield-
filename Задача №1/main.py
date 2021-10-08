import json


class CountriesIterate:

    def __init__(self, path):
        self.path = path

    def __iter__(self):
        with open(self.path, "r", encoding="utf-8") as file:
            countries_json = file.read()
            list_countries = json.loads(countries_json)
            for country in list_countries:
                self.name_country = country['name']['common'].replace(" ", "_")
                with open("countries_list.txt", "a", encoding="utf-8") as countries_list:
                    countries_list.write(
                        f"{country['name']['common']} – {'https://en.wikipedia.org/wiki/' + self.name_country}\n")
        return self

    def __next__(self):
        if not self.name_country:
            raise StopIteration
        return self


if __name__ == '__main__':

    for country in CountriesIterate('countries.json'):
        print(country)
        break
