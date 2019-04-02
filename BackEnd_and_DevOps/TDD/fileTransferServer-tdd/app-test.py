import unittest
import os
import io
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
            self.createDummyFile('%sfile.txt'%i,"This is dummy text in ")
        self.app = app.test_client()

    # helper functions
    def createDummyFile(self,filename,text):
        with open(os.path.join(app.config['FILES_FOLDER'],filename),'w+') as f:
                f.write("{0} {1}".format(text,filename))

    def removeFile(self,path):
        os.remove(path)

    # asserts
    def test_dummy_files(self):
        rv = self.app.get('/')
        self.assertNotIn(b'Files folder is empty',rv.data)

    def test_file_upload(self):
        data = {'filename': 'testFile.txt'}
        with open(os.path.join(app.config['FILES_FOLDER'],"testFile.txt"),'w+') as f:
                f.write("This file is used in testing")
        data['file'] = (io.BytesIO(b"abcdef"), 'testFile.txt')
        response = self.app.post(
            '/upload', data=data, follow_redirects=True,
            content_type='multipart/form-data'
        )
        try:
            self.assertIn(b'testFile.txt', response.data)
        finally:
            self.removeFile(os.path.join(app.config['FILES_FOLDER'],"testFile.txt"))

    def test_remove_file(self):
        self.createDummyFile("testfileforremove.txt",'test')
        response = self.app.post(
            '/remove',data=dict(filename='testfileforremove.txt'),follow_redirects=True
        )
        try:
            self.assertEqual(response.status_code,200)
        except:
            self.removeFile(os.path.join(app.config['FILES_FOLDER'],"testfileforremove.txt"))

        response = self.app.post(
            '/remove',data=dict(filename="ghost_file.ghost"),follow_redirects=True
        )
        self.assertEqual(response.status_code,405)


if __name__ == "__main__":
    unittest.main()