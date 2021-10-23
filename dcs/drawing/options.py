from dataclasses import dataclass

class Options:
    hiddenOnF10Map: dict[str, dict[str, bool]]

    def __init__(self):
        self.hiddenOnF10Map = Options.get_default_hidden()
    
    def load_from_dict(self, data):
        self.hiddenOnF10Map = data["hiddenOnF10Map"]

    def dict(self):
        d = {}
        d["hiddenOnF10Map"] = {}
        for option_group_name in self.hiddenOnF10Map.keys():
            d["hiddenOnF10Map"][option_group_name] = self.hiddenOnF10Map[option_group_name]

        return d

    @staticmethod
    def get_default_hidden():
        d = {}
        d["Observer"] = {
            "Neutral": False,
            "Blue": False,
            "Red": False,
        }
        d["Instructor"] = {
            "Neutral": False,
            "Blue": False,
            "Red": False,
        }
        d["ForwardObserver"] = {
            "Neutral": False,
            "Blue": False,
            "Red": False,
        }
        d["Spectrator"] = { 
            "Neutral": False,
            "Blue": False,
            "Red": False,
        }
        d["ArtilleryCommander"] = {
            "Neutral": False,
            "Blue": False,
            "Red": False,
        }
        d["Pilot"] = {
            "Neutral": False,
            "Blue": False,
            "Red": False,
        }
        return d