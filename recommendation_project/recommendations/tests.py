from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Student, Professor, Skill, RecommendationRequest, RecommendationLetter


class RecommendationAPITests(APITestCase):
    def setUp(self):
        # create some initial objects used across tests
        self.student_data = {'name': 'Alice', 'email': 'alice@example.com', 'university': 'Example U'}
        self.prof_data = {'name': 'Dr. Bob', 'email': 'bob@uni.edu', 'department': 'Physics'}

    def test_create_student_and_professor_and_request_and_letter(self):
        # create student
        resp = self.client.post(reverse('student-list-create'), self.student_data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        student_id = resp.data['id']

        # create professor
        resp = self.client.post(reverse('professor-list-create'), self.prof_data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        prof_id = resp.data['id']

        # create recommendation request
        req_data = {'student': student_id, 'professor': prof_id, 'message': 'Please write me a letter'}
        resp = self.client.post(reverse('request-list-create'), req_data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        request_id = resp.data['id']

        # update request status
        resp = self.client.patch(reverse('request-detail', args=[request_id]), {'status': 'accepted'})
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['status'], 'accepted')

        # add a skill
        resp = self.client.post('/skills/', {'name': 'Python'})
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        skill_id = resp.data['id']

        # create recommendation letter
        letter_data = {'request': request_id, 'content': 'Great student', 'skills': [skill_id]}
        resp = self.client.post('/letters/', letter_data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(resp.data['request'], request_id)

        # retrieve letter
        resp = self.client.get(f'/letters/{resp.data["id"]}/')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn(skill_id, resp.data['skills'])

