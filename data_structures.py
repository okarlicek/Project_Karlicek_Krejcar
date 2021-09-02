class VaccCenter():
    def __init__(self, name, region, link):
        self.name = name
        self.region = region
        self.link = link
        self.vacc_id = link[39:]
        self.center_type = {}
        self.info = {}
        self.open_hours = {}
        self.vaccines = {}

    def add_center_type(self, center_type):
        self.center_type = center_type

    def add_info(self, info):
        self.info = info

    def add_open_hours(self, open_hours):
        self.open_hours = open_hours

    def add_vaccines(self, vaccines):
        self.vaccines = vaccines

    def __repr__(self):
        return f"VaccCenter({self.name})"