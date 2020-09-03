import os
import sys

sys.path.insert(0, os.getcwd())
from RESTful_test2 import create_app


application = create_app(config_name='production')
