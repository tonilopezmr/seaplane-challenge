import sys
sys.path.append("..")

import unittest
import os

from wordladder import WordLadder

class TestCase:

  def __init__(
    self,     
    name,
    start, 
    target, 
    dictionary, 
    expected_distance, 
    expected_path
  ):    
    self.name = name
    self.start = start
    self.target = target
    self.dictionary = {}
    self.expected_distance = expected_distance
    self.expected_path = expected_path

    for key in dictionary:
      self.dictionary[key] = 1


class WordLadderTests(unittest.TestCase):
    pass

def generate_test(test_case):
    def test(self):
      word_ladder = WordLadder()       
      result = word_ladder.shortest_path(test_case.start, test_case.target, test_case.dictionary)
                  
      self.assertEqual(result.distance, test_case.expected_distance)
      self.assertEqual(result.path, test_case.expected_path)        
    return test

def read_test_cases(dir_path):
    tests_cases = []

    for file_name in os.listdir(dir_path):        
        if os.path.isfile(os.path.join(dir_path, file_name)):            
            with open(os.path.join(dir_path, file_name), 'r') as f:
              lines = list(map(lambda x: x.replace('\n', ''), f.readlines()))
              dictionary = lines[0].split(',')
              start = lines[1]
              target = lines[2]
              distance = int(lines[4])
              dic_path = lines[5].split(',')
              tests_cases.append(TestCase(file_name, start, target, dictionary, distance, dic_path))  
    
    return tests_cases



def generate_tests(dir_path):
    test_cases = read_test_cases(dir_path)

    for test_case in test_cases:
        test_name = 'test_%s' % test_case.name
        test = generate_test(test_case)
        setattr(WordLadderTests, test_name, test)

if __name__ == '__main__':      
    dir_path = './testcases'        

    generate_tests(dir_path)
        
    unittest.main()

