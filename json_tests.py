import json
import unittest


class JsonTests(unittest.TestCase):

    def test_json(self):
        with open('test.json') as json_file:
            json_data = json.load(json_file)

            assert 'bitly' in json_data
            assert 'username' in json_data['bitly']
            assert 'password' in json_data['bitly']
            assert 'access_token' in json_data['bitly']
            assert json_data['bitly']['username'] == 'bitly_username'
            assert json_data['bitly']['password'] == 'bitly_password'
            assert json_data['bitly']['access_token'] == 'bitly_access_token'

            assert 'toggl' in json_data
            assert 'workspace_id' in json_data['toggl']
            assert 'api_token' in json_data['toggl']
            assert json_data['toggl']['workspace_id'] == 'toggle_workspace_id'
            assert json_data['toggl']['api_token'] == 'toggle_api_token'


if __name__ == '__main__':
    unittest.main()
