

class TestExample:
    """ Test python api on AnyBlok models"""

    def test_create_example(self, rollback_registry):
        registry = rollback_registry
        ex = registry.Example.insert(name="plop")
        assert registry.Example.query().count() == 2
        assert ex.name == "plop"
