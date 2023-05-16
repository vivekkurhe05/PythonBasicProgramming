from configparser import ConfigParser

# Create object of configparser class
config=ConfigParser()

# To read data from config file
config.read("Config.cfg")
print(config.get("Section1","username"))