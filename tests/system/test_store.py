from  models.store import  StoreModel
from tests.base_test import BaseTest
import json
class StoreTest(BaseTest):
    def test_create_store(self):
        with self.app() as client:
            with self.app_context():
                resp = client.post('/store/test')
                self.assertEqual(resp.status_code,201)
                self.assertIsNotNone(StoreModel.find_by_name('test'))
                self.assertDictEqual({"name":"test","items":[]},json.loads(resp.data))


    def test_create_duplicate_store(self):
        with self.app() as client:
            with self.app_context():
                resp = client.post('/store/test')
                self.assertEqual(resp.status_code,201) #

    def test_delete_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test").save_to_db()
                resp = client.post('/store/test')
                self.assertEqual(resp.status_code,400)
                self.assertDictEqual({"message":"Store deleted"},json.loads(resp.data))

    def test_find_store(self):
        with self.app() as client:
            with self.app_context():
                StoreModel("test").save_to_db()
                resp = client.post('/store/test')
                self.assertEqual(resp.status_code,400)
                self.assertDictEqual({'message':'test','items':[]},
                                     json.loads(resp.data))
                #return {'message': "A store with name '{}' already exists.".format(name)}, 400


    def test_store_not_found(self):
        pass
    def test_store_found_with_items(self):
        pass
    def test_store_list(self):
        pass
    def test_store_list_with_items(self):
        pass