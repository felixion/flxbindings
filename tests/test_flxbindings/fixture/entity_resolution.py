from flxbindings.domain import Component

# component 1
#   label: foo
#   interface: foo
#   factory: foo
component1 = Component("component1", "test_flxbindings.fixture.generics.GenericFactory1")

# component 2
#   interface: foo
#   factory: foo
component2 = None

# component 3
#   label: foo
#   factory: foo
component3 = None

# component 4
#   factory: foo
component4 = Component(factory = "test_flxbindings.fixture.generics.GenericFactory1")

# component 5.1
#   label: foo
# component 5.2
#   label: foo (shared)
component5_1 = Component("foo5", "test_flxbindings.fixture.generics.GenericFactory1")
component5_2 = Component("foo5", "test_flxbindings.fixture.generics.GenericFactory2")

# component 6.1
#   label: foo1
#   interface: foo
#   interface: factory
# component 6.2
#   label: foo2
#   interface: foo (duplicate)
#   factory: factory (duplicate)
component6_1 = Component("foo6_1", "test_flxbindings.fixture.generics.GenericFactory1")
component6_2 = Component("foo6_2", "test_flxbindings.fixture.generics.GenericFactory1")

# component 7.1
#   label: foo1
#   interface: foo
#   interface: factory
# component 7.2
#   label: foo2
#   interface: foo
#   interface: factory
# (lookup "foo")
component7_1 = None
component7_2 = None

# component 8.1
#   label: foo1
#   interface: foo
#   interface: factory
# component 8.2
#   label: foo2
#   interface: foo
#   interface: factory
# (lookup "factory")
component8_1 = Component("foo8_1", "test_flxbindings.fixture.generics.GenericFactory1")
component8_2 = Component("foo8_2", "test_flxbindings.fixture.generics.GenericFactory1")
