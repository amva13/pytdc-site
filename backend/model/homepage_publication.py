
class HomepagePublication(dict):

    def __init__(self, name, venue, year, month, links = {}):
        self["name"] = name
        self["venue"] = venue
        self["year"] = year
        self["month"] = month
        self["links"] = links