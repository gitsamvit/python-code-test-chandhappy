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

  def test_check_and_alert(self):
    self.assertTrue(typewise_alert.check_and_alert('TO_CONTROLLER',{'coolingType':'PASSIVE_COOLING'}, 100)== print('65261, TOO_HIGH'))
    self.assertTrue(typewise_alert.check_and_alert('TO_EMAIL',{'coolingType':'HI_ACTIVE_COOLING'}, 50)== print('To: a.b@c.com\nHi, the temperature is too high'))

  def test_send_to_contoroller(self):
    self.assertTrue(typewise_alert.send_to_controller('NORMAL') == print('65261, NORMAL'))
    self.assertTrue(typewise_alert.send_to_controller('TOO_HIGH') == print('65261, TOO_HIGH'))
 
  def test_send_to_email(self):
    self.assertTrue(typewise_alert.send_to_email("TOO_LOW") == print("To: a.b@c.com\nHi, the temperature is too low") )
    self.assertTrue(typewise_alert.send_to_email("NORMAL") == None)
    self.assertTrue(typewise_alert.send_to_email("TOO_HIGH") == print("To: a.b@c.com\nHi, the temperature is too high") )


if __name__ == '__main__':
  unittest.main()
