from instapy import InstaPy
from instapy import smart_run

session = InstaPy(username='dixxtelleszin', password='24719860')

with smart_run(session):
	session.set_do_follow(enabled = True, percentage = 20)
	session.set_do_like(enabled = True, percentage= 100)

	session.like_by_tags(['skywalker'], amount=200)

	comentarios = ['Awesome !', 'May the force be with u']
	session.set_do_comment(enabled=True, percentage=95)
	#session.set_comments(comentarios, media= 'Photo')
	session.join_pods()