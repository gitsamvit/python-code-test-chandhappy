import unittest
import typewise_alert


class TypewiseTest(unittest.TestCase):
  def test_infers_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.infer_breach(20, 50, 100) == 'TOO_LOW')
    self.assertTrue(typewise_alert.infer_breach(70, 50, 100) == 'NORMAL')
    self.assertTrue(typewise_alert.infer_breach(110, 50, 100) == 'TOO_HIGH')

  def test_classify_temp_breach_as_per_limits(self):
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 10)== 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', 80)== 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('PASSIVE_COOLING', -120)== 'TOO_LOW')

    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 20)== 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', 70)== 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('HI_ACTIVE_COOLING', -110)== 'TOO_LOW')

    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 30)== 'NORMAL')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 90)== 'TOO_HIGH')
    self.assertTrue(typewise_alert.classify_temperature_breach('MED_ACTIVE_COOLING', 0)== 'NORMAL')



if __name__ == '__main__':
  unittest.main()
