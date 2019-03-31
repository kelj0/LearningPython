import unittest
import os

from app import app

class BasicTestCase(unittest.TestCase):
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/',content_type='html/text')
        self.assertEqual(response.status_code,200)
    
    def test_files_folder_exists(self):
        tester = os.path.exists("FILES")
        self.assertTrue(tester)

class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['FILES_FOLDER'] = 'FILES'
        if not os.path.exists('FILES'):
            os.mkdir(os.path.join(basedir,app.config['FILES_FOLDER']))
        for i in range(5):
            with open(os.path.join(basedir,app.config['FILES_FOLDER'],str(i)+"file.txt"),'w+') as f:
                f.write("This is dummy text in {}file.txt".format(i))
        self.app = app.test_client()

    def test_dummy_files(self):
        rv = self.app.get('/')
        self.assertNotIn(b'Files folder is empty',rv.data)



if __name__ == "__main__":
    unittest.main()