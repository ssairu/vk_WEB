from django.contrib.contenttypes.models import ContentType
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from random import sample
from app.models import Profile, Question, Answer, Tag, Like


class Command(BaseCommand):
    help = 'Fill the database with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Ratio for data creation')

    def handle(self, *args, **options):
        ratio = options['ratio']

        self.create_users(ratio)
        self.create_tags(ratio)
        self.create_questions(ratio)
        self.create_answers(ratio)
        self.create_likes(ratio)

        self.stdout.write(self.style.SUCCESS(f'Successfully filled the database with test data (Ratio: {ratio})'))

    def create_users(self, ratio):
        for i in range(ratio):
            user = User.objects.create_user(username=f'user_{i}', password=f'password_{i}')
            Profile.objects.create(user=user)
        # users = [User(username=f'user_{i}', password=f'password_{i}') for i in range(ratio)]
        # usersT = User.objects.bulk_create(users)
        #
        # profiles = [Profile(user=usersT[0])]
        # profilesT = Profile.objects.bulk_create(profiles)

    def create_tags(self, ratio):
        tags = [Tag(tag_name=f'tag_{i}') for i in range(ratio)]
        tagsT = Tag.objects.bulk_create(tags)

    def create_questions(self, ratio):
        for i in range(ratio * 10):
            user = Profile.objects.get(user__username=f'user_{i // 10}')
            title = f'Вопрос {i}'
            content = f'''{i} - Если я верю, что не могу что-то сделать, 
            это делает меня неспособным это сделать. Но когда я верю, 
            что могу, тогда я обретаю способность делать это, 
            даже если вначале у меня ее не было'''
            tags = sample(list(Tag.objects.all()), i % 5 + 1)
            question = Question.objects.create(author=user, title=title, content=content)
            question.tags.add(*tags)

    def create_answers(self, ratio):
        for i in range(ratio * 100):
            user = Profile.objects.get(user__username=f'user_{i // 100}')
            question = Question.objects.get(title=f'Вопрос {i % 10}')
            text = f'''Ответ {i} - Эдисон терпел неудачу 10 000 раз, 
            прежде чем изобрел электрический свет. 
            Не расстраивайтесь, если вы потерпите неудачу несколько раз'''
            accepted = bool(i % 2)
            Answer.objects.create(author=user, question=question, text=text, accepted=accepted)

    def create_likes(self, ratio):
        for i in range(ratio * 200):
            user = User.objects.get(username=f'user_{i // 200}')
            content_type = ContentType.objects.get_for_model(Question if bool(i % 2) else Answer)
            object_id = i % 500 + 200
            Like.objects.create(user=user, content_type=content_type, object_id=object_id)
