class DummySession(list):

    def query(self, model):
        self.model = model
        return self

    def count(self):
        return len(self)
