import unittest
import requests


class PythonTests(unittest.TestCase):

    def setUp(self):
        # define instructions that will be executed before each test method
        # we can do stuff like 'self.customvariable = <custom value>'
        pass

    def tearDown(self):
        # define instructions that will be executed after each test method
        pass

    def test_get_request(self):
        """uses http://httpbin.org"""
        r = requests.get('http://httpbin.org/get')
        assert r.ok is True
        assert r.status_code == 200

        r = requests.get('https://api.github.com/events')
        assert r.ok is True
        json_data = r.json()

        assert json_data[0]['id'] != 0

    def test_post_request(self):
        payload = {'content': "I really like requests.", 'user_id': 152}
        r = requests.post('http://httpbin.org/post', params=payload)
        assert r.ok is True
        json_data = r.json()
        assert json_data['args']['content'] == 'I really like requests.'
        assert json_data['args']['user_id'] == '152'

        assert json_data['args'].get('content') == 'I really like requests.'

        #submit data where key is a list
        payload = {'posts[]': [123, 456], 'posts2[]': [789, 987]}
        r = requests.delete('http://httpbin.org/delete', params=payload)
        json_data = r.json()
        assert len(json_data['args']) == 2
        #assert json_data['args']['posts[]'] is list # for some reason it is not a list
        assert len(json_data['args']['posts[]']) == 2
        assert json_data['args']['posts[]'][0] == '123'
        assert json_data['args']['posts2[]'][0] == '789'

    def test_authentication(self):
        """more likely a website, since APIs do auth through public/private keys"""
        # httpbasic sends password in plain text
        from requests.auth import HTTPBasicAuth
        r = requests.get('http://httpbin.org/basic-auth/user/password', auth=HTTPBasicAuth('user','password'))
        assert r.ok is True
        assert r.status_code == 200
        r = requests.get('http://httpbin.org/basic-auth/user/password', auth=HTTPBasicAuth('user','password2'))
        assert r.ok is False
        assert r.status_code == 401

        # httpdigest hashes password
        from requests.auth import HTTPDigestAuth
        r = requests.get('http://httpbin.org/digest-auth/auth/user/password', auth=HTTPDigestAuth('user','password'))
        assert r.ok is True
        assert r.status_code == 200
        r = requests.get('http://httpbin.org/digest-auth/auth/user/password', auth=HTTPDigestAuth('user','password2'))
        assert r.ok is False
        assert r.status_code == 401

if __name__ == '__main__':
    unittest.main()
