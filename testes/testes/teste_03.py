import unittest
import requests

class TesteRegressaoAPI(unittest.TestCase):
    BASE_URL = "https://jsonplaceholder.typicode.com"  # API de teste gratuita

    # Testes para endpoints principais
    def test_get_posts(self):
        """Verifica se o endpoint de posts ainda retorna dados válidos"""
        response = requests.get(f"{self.BASE_URL}/posts")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
        self.assertIn('userId', response.json()[0])
        self.assertIn('title', response.json()[0])

    def test_create_post(self):
        """Testa a criação de um novo post"""
        new_post = {
            'title': 'Teste de regressão',
            'body': 'Conteúdo do teste',
            'userId': 1
        }
        response = requests.post(f"{self.BASE_URL}/posts", json=new_post)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['title'], new_post['title'])

    def test_comments_por_post(self):
        """Verifica se os comentários de um post podem ser recuperados"""
        response = requests.get(f"{self.BASE_URL}/posts/1/comments")
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)
        self.assertIn('email', response.json()[0])

    # Teste de dados críticos (não devem mudar)
    def test_dados_consistentes(self):
        """Verifica se dados críticos permanecem consistentes"""
        response = requests.get(f"{self.BASE_URL}/users/1")
        data = response.json()
        self.assertEqual(data['username'], "Bret")
        self.assertEqual(data['address']['city'], "Gwenborough")

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
