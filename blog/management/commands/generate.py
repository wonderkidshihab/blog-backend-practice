import random

from django.contrib.auth.models import User
from django.utils import timezone
from faker import Faker

from blog.models import Category, Post
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(self, *args, **options):
        fake = Faker()

        # Create dummy categories
        categories = ["Technology", "Science", "Travel", "Food", "Fashion"]

        for category_name in categories:
            category = Category.objects.create(
                name=category_name,
                slug=category_name.lower().replace(" ", "-")
            )
            category.save()

        # Create dummy users
        users = User.objects.all()

        # Generate dummy posts
        num_posts = 20

        for _ in range(num_posts):
            category = random.choice(Category.objects.all())
            author = random.choice(users)
            title = fake.sentence(nb_words=6)
            excerpt = fake.paragraph(nb_sentences=3)
            content = fake.text(max_nb_chars=1000)
            slug = fake.slug()
            published = fake.date_time_between(start_date="-1y", 
                                            end_date="now", 
                                            tzinfo=timezone.get_current_timezone())
            status = random.choice(["draft", "published"])

            post = Post.objects.create(
                category=category,
                title=title,
                excerpt=excerpt,
                content=content,
                slug=slug,
                published=published,
                author=author,
                status=status,
                thumbnail=None 
            )
            post.save()
            self.stdout.write(self.style.SUCCESS(f"Created post: {post.title}"))

        self.stdout.write(self.style.SUCCESS("Dummy data generated successfully!"))
