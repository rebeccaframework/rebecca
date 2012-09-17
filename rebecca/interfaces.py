from zope.interface import Interface


class IList(Interface):
    """ interface for list like object. """

    def __len__(self):
        """ Called to implement the built-in function `len()`."""

    def __getitem__(self, key):
        """ Called to implement evaluation of self[key]."""

    def __setitem__(self, key, value):
        """Called to implement assignment of self[key] """

    def __delitem__(self, key):
        """ Called to implement deletion of self[key]."""

    def __iter__(self):
        """ """

    def __reversed__(self):
        """ """

