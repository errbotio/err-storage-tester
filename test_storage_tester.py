from errbot.backends.test import testbot
class TestMyPlugin(object):
    extra_plugin_dir = '.'
    def test_command(self, testbot):
        testbot.assertCommand('!teststorage', 'OK')
