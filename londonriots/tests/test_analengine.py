from londonriots.tests import TestLR
import datetime as dt
import londonriots.analengine.epsilon as anal

class TestAnalEngine(TestLR):
    def setUp(self):
        TestLR.setUp(self)
        self.start_time = dt.datetime(2011, 9, 9, 5)
        self.epsilon = dt.timedelta(hours=5)
        self.named_entities = anal.named_entities_in_time_range(self.start_time, self.epsilon)

    def test_analengine_named_entities(self):
        self.assert_(self.named_entities.count() > 0)
