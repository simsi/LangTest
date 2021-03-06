
from logic import login
from logic import testSelection
from logic import editTest
from logic import test
from common import dated_score_handler
import logging
import sys

logging.getLogger().setLevel(logging.INFO)

class Manager:
    def __init__(self, UI_factory, data_manager):
        self.logprefix = "Manager"
        logging.info("{0}:{1}: start".format(self.logprefix, "__init__"))
        self.data_manager = data_manager
        self.UI_factory = UI_factory
        self.dated_score_handler = dated_score_handler.DatedScoreHandler()
    
    def do_login(self):
        logging.info("{0}:{1}:".format(self.logprefix, "do_login"))
        theLogin = login.Login(self, self.UI_factory, self.data_manager.get_data_factory().get_user_manager())
        theLogin.start()    

    def do_create_test(self, test_name, test_id):
        self.test_name = test_name
        self.test_id = test_id
        logging.info("{0}:{1}:".format(self.logprefix, "do_create_test"))
    
    def do_test_selection(self, user_name, user_id):
        self.user_name = user_name
        self.user_id = user_id
        logging.info("{0}:{1}:".format(self.logprefix, "do_test_selection"))
        theTestSelection = testSelection.TestSelection(self, 
                                                       self.UI_factory, 
                                                       self.data_manager.get_data_factory().get_test_manager(),
                                                       self.user_name,
                                                       self.user_id,
                                                       self.dated_score_handler)
        theTestSelection.start()

    def do_edit_test(self, test_name, test_id):
        self.test_name = test_name
        self.test_id = test_id
        theEditTest = editTest.EditTest(self,
                                        self.UI_factory,
                                        self.data_manager.get_data_factory().get_test_manager(),
                                        self.data_manager.get_data_factory().get_persistency_manager(),
                                        self.user_name,
                                        self.user_id,
                                        test_name,
                                        test_id)
        theEditTest.start()
        
    def do_test(self):
        theTest = test.Test(self,
                            self.UI_factory,
                            self.data_manager.get_data_factory().get_test_manager(),
                            self.data_manager.get_data_factory().get_persistency_manager(),
                            self.user_name,
                            self.user_id,
                            self.test_name,
                            self.test_id,
                            self.dated_score_handler)
        theTest.start()

    def quit(self):
        self.data_manager.quit()
        sys.exit(0)