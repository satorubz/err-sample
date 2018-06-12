from errbot import BotPlugin, botcmd, re_botcmd
#import re
#import sys
#import pprint
#import time
#from user_state import UserState
#from itertools import chain
#import watson_developer_cloud
#from assistant import Assistant

CONFIG_TEMPLATE = {'WORKSPACE_NAME': 'Car Dashborad - Sample',
                   'ASSISTANT_USERNAME': 'changeme',
                   'ASSISTANT_PASSWORD': 'changeme',
                   'ASSISTANT_VERSION_DATA': '2018-02-16' }

class errsample(BotPlugin):
    """Example plugin for Errbot"""
    #def __init__(self):
    #    self.running = True
    #    #
    #    self.delay = 0.5  # second
    #    #self.user_state_map = {}
    #    #self.pp = pprint.PrettyPrinter(indent=4)

    #def get_configuration_template(self):
    #    return CONFIG_TEMPLATE

    #def check_configuration(self, configuration):
    #    pass

    #def configure(self, configuration):
    #    if configuration is not None and configuration != {}:
    #        config = dict(chain(CONFIG_TEMPLATE.items(),
    #                            configuration.items()))
    #    else:
    #        config = CONFIG_TEMPLATE

    #    super(PluginExample, self).configure(config)

    #@re_botcmd(pattern=r"^[Ww][Aa][Tt][Ss][Oo][Nn] ",prefixed=False )
    @botcmd
    def watson(self, msg, args):
        return "Hello World!" 



