import unittest
import urllib.parse
import html


class UrlTests(unittest.TestCase):

    def test_url_get_path(self):
        url1 = 'http://intellitect.com/building-single-page-applications-spa-with-the-journey-framework/'
        url2 = 'http://intellitect.com/building-single-page-applications-spa-with-the-journey-framework/?utm_source=social&utm_medium=blog%20article&utm_campaign=Building%20Single%20Page%20Applications%20(SPA)%20with%20the%20Journey%20Framework%20%2F%20Grant%20Erickson'
        intended_path = '/building-single-page-applications-spa-with-the-journey-framework/'

        path = urllib.parse.urlsplit(url1)
        assert path[2] == intended_path
        path = urllib.parse.urlsplit(url2)
        assert path[2] == intended_path

        parsed = urllib.parse.urlparse(url2)
        temp = urllib.parse.parse_qs(parsed.query)
        assert temp['utm_source'][0] == 'social'
        assert temp['utm_medium'][0] == 'blog article'
        assert temp['utm_campaign'][0] == 'Building Single Page Applications (SPA) with the Journey Framework / Grant Erickson'

        temp_url = 'http://blogs.msdn.com/b/visualstudio/archive/2015/07/21/visual-studio-2015-rtm-what-s-new-in-the-ide.aspx?utm_source=newsletters&utm_medium=email&utm_campaign=IntelliTect.com'

        print(urllib.parse.urlparse(temp_url)[0])
        print(urllib.parse.urlparse(temp_url)[1])
        print(urllib.parse.urlparse(temp_url)[0]+"://"+urllib.parse.urlparse(temp_url)[1])

    def test_escape(self):
        temp = '#<>"aaa"'
        assert html.escape(temp,quote=True) == '#&lt;&gt;&quot;aaa&quot;'

if __name__ == '__main__':
    unittest.main()
