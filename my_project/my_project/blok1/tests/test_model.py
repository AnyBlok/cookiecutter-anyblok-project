from anyblok.tests.testcase import BlokTestCase


class TestExample(BlokTestCase):
    """ Test python api on AnyBlok models"""

    def test_create_example(self):
        ex = self.registry.Example.insert(name="plop")
        self.assertEqual(self.registry.Example.query().count(), 1)
        self.assertEqual(ex.name, "plop")
