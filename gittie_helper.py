class GittieHelper():

    """initial function"""

    def __init__(self):
        self.temperature = None
        self.humidity = None
        self.air_polution = None
        self.day_of_year = None

        """set. temperature"""

    def set_temperature(self, temperature_degree):
        self.temperature  = temperature_degree
        """set humitidyty"""

        
    def set_humidity(self, humidity_value):
        self.humidity = humidity_value

    def set_air_pollution(self, air_pollution_level):
        """
        Method sets air pollution level to attribute and validate input
        :param air_pollution_level:
        """
        self.air_pollution = air_pollution_level

    def set_day_of_the_year(self, day_number):
"""hbkjfhsbkdjhgbdkrjbgkdjrk"""
        self.day_of_year = day_number


    def get_value_method(self):
        """check a tem, air and hum"""

        if self.temperature > 20 and self.humidity < 60 and self.air_pollution < 40:
            return "You can go out"
        else:
            return "Stay home!!!!"

