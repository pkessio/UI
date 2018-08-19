import unittest
import os
import json
from app import questions

class ApiTestCase(unittest.TestCase):
 def test_get_all_questions(self):
         results = self.client().post('/tests/', data=self.api)
         self.assertEqual(results.status_code, 201)
         results = self.client().get('/tests/')
         self.assertEqual(results.status_code, 200)
         self.assertIn('All questions', str(results.data))
         
         def tes_question_id_exixts(self):
                   """ check a question by id"""
                   questions_id = self.client().post('/api/', data=self.bucketlist)
                   self.assertEqual(questions_id.status_code, 201)
                   result_in_json = json.loads(questions_id.data.decode('utf-8').replace("'", "\""))
                   result = self.client().get(
                   '/api/{}'.format(result_in_json['id']))
                   self.assertEqual(result.status_code, 200)
                   self.assertIn('Qestion retrieved', str(result.data))