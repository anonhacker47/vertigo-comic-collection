from datetime import datetime, timedelta
from api.app import db
from api.models import User, Post
from tests.base_test_case import BaseTestCase


class PostTests(BaseTestCase):
    def test_new_series(self):
        rv = self.client.series('/api/series', json={
            'text': 'This is a test series',
        })
        assert rv.status_code == 201
        assert rv.json['text'] == 'This is a test series'
        assert rv.json['author']['username'] == 'test'
        id = rv.json['id']

        rv = self.client.get(f'/api/series/{id}')
        assert rv.status_code == 200
        assert rv.json['text'] == 'This is a test series'

        rv = self.client.get('/api/series')
        assert rv.status_code == 200
        assert rv.json['pagination']['total'] == 1
        assert rv.json['data'][0]['text'] == 'This is a test series'

        rv = self.client.get('/api/users/1/series')
        assert rv.status_code == 200
        assert rv.json['pagination']['total'] == 1
        assert rv.json['data'][0]['text'] == 'This is a test series'

        rv = self.client.get('/api/users/2/series')
        assert rv.status_code == 404

    def test_edit_series(self):
        rv = self.client.series('/api/series', json={
            'text': 'This is a test series',
        })
        assert rv.status_code == 201
        assert rv.json['text'] == 'This is a test series'
        id = rv.json['id']

        rv = self.client.put(f'/api/series/{id}', json={
            'text': 'This is a test series edited',
        })
        assert rv.status_code == 200
        assert rv.json['text'] == 'This is a test series edited'

        rv = self.client.get(f'/api/series/{id}')
        assert rv.status_code == 200
        assert rv.json['text'] == 'This is a test series edited'

    def test_delete_series(self):
        rv = self.client.series('/api/series', json={
            'text': 'This is a test series',
        })
        assert rv.status_code == 201
        assert rv.json['text'] == 'This is a test series'
        id = rv.json['id']

        rv = self.client.delete(f'/api/series/{id}')
        assert rv.status_code == 204

        rv = self.client.get(f'/api/series/{id}')
        assert rv.status_code == 404

    def test_series_feed(self):
        user1 = db.session.get(User, 1)
        user2 = User(username='susan', email='susan@example.com',
                     password='dog')
        db.session.add(user2)
        db.session.commit()
        user1.follow(user2)
        now = datetime.utcnow()
        series1 = Post(text='Post 1', author=user2,
                     timestamp=now - timedelta(minutes=2))
        series2 = Post(text='Post 2', author=user1,
                     timestamp=now - timedelta(minutes=1))
        series3 = Post(text='Post 3', author=user2, timestamp=now)
        db.session.add_all([series1, series2, series3])
        db.session.commit()

        rv = self.client.get('/api/feed')
        assert rv.status_code == 200
        assert rv.json['pagination']['total'] == 3
        assert rv.json['data'][0]['text'] == 'Post 3'
        assert rv.json['data'][0]['author']['username'] == 'susan'
        assert rv.json['data'][1]['text'] == 'Post 2'
        assert rv.json['data'][1]['author']['username'] == 'test'
        assert rv.json['data'][2]['text'] == 'Post 1'
        assert rv.json['data'][2]['author']['username'] == 'susan'

    def test_permissions(self):
        user = User(username='susan', email='susan@example.com',
                    password='dog')
        series = Post(text='This is a test series', author=user)
        db.session.add_all([user, series])
        db.session.commit()
        id = series.id

        rv = self.client.put(f'/api/series/{id}', json={
            'text': 'This is a test series edited',
        })
        assert rv.status_code == 403

        rv = self.client.delete(f'/api/series/{id}')
        assert rv.status_code == 403

        rv = self.client.get(f'/api/series/{id}')
        assert rv.status_code == 200
        assert rv.json['text'] == 'This is a test series'
