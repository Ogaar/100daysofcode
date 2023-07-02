import configparser
# File for learning config files
# Config files are helpful to allow easy configuration for applications as well as not hard coding passwords. Also, so
# passwords aren't stored in the code/public git repo. For this example, the config file will be stored in Git.
config = configparser.ConfigParser()
config.read('C:\\Users\\oscar\\OneDrive\\Documents\\100daysofcode\\100daysofcode\\general_learning\\configs\\config.ini')

password = config.get('DEFAULT', 'password')
print(password)

xp_multiplier = config.get('DEFAULT', 'xp_multiplier')
print(xp_multiplier)