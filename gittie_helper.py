class GittieHelper():

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.air_polution = None
        self.day_of_year = None


    def set_temperature(self, temperature_degree):
        self.temperature  = temperature_degree

    def set_humidity(self, humidity_value):
        self.humidity = humidity_value

    def set_air_pollution(self, air_pollution_level):
        """
        Method sets air pollution level to attribute and validate input
        :param air_pollution_level:
        """
        self.air_pollution = air_pollution_level

    def set_day_of_the_year(self, day_number):
        """
        Method sets day number from beginning of the year to attribute and validate input
        :param day_number:
        """
        self.day_of_year = day_number

    def get_value_person_B(self):
        """
        Method should calculate if exiting home is safe for gittie
        """
        if (int(self.temperature) < 20) and (int(self.humidity) < 60) and (int(self.air_pollution) > 40 ):
            return True
        else:
            return False
