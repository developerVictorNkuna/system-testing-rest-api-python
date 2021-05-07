from models.user import UserModel
from tests.base_test import BaseTest

import json  # convert our data into json{"key":"value",pair} format



class UserTest(BaseTest):
    def test_register_user(self):
        with self.app() as client:
            with self.app_context():
                response = client.post('/register', data={"username": "test", "password": '1234'})

                self.assertEqual(response.status_code, 201)
                self.assertIsNotNone(UserModel.find_by_username('test'))
                self.assertDictEqual({"Message":"User created successfully"},json.loads(response.data))

    def test_register_and_login(self):
        with self.app() as client:
            with self.app_context():
                request = client.post('/register', data={"username": "test", "password": '1234'})
                auth_response = client.post('/auth',data =json.dumps({'username':'test',
                                                          'password':'1234'}),
                                            headers={"Content-Type":"application/json"})
                self.assertIn("access_token",json.loads(auth_response.data).keys())
                #send the token to this endpoint,require access token securely convert response data into json ,assuming the key wiill be a list,acces token is in the list


    def test_register_duplicate(self):
        with self.app() as client:
            with self.app_context():
                client.post('/register',data={'username':"test","password":"1234"})
                response = client.post('/register', data={"username": "test", "password": '1234'})

                self.assertEqual(response.status_code,400)
                self.assertDictEqual({"Message":"A user with that username already"},json.loads(response.data))


