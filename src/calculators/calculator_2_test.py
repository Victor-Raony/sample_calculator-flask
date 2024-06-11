from typing import Dict
from pytest import raises
from .calculator_2 import Calculator2

class MockRequest:
  def __init__(self,body:Dict) -> None:
    self.json = body

def test_calculate():
  mock_request = MockRequest(body={ "numbers" : [ 1, 2, 3, 4, 5 ] })
  
  calculator_2 = Calculator2()
  calculator_2.calculate(mock_request)
  formated_response = calculator_2.calculate(mock_request)
  
  assert isinstance(formated_response, dict)
  assert formated_response == { 'data': { 'Calculator': 2, 'result': 0.08 } }
