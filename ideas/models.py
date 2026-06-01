from django.db import models

class Idea(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)   # added so fixtures/templates work
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class IdeaCategory(models.Model):
    name = models.CharField(max_length=100)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="categories")

    def __str__(self):
        return self.name


class IdeaVote(models.Model):
    voter = models.CharField(max_length=100)
    vote = models.BooleanField(default=True)
    idea = models.ForeignKey(Idea, on_delete=models.CASCADE, related_name="votes")

    def __str__(self):
        return f"{self.voter} voted {'Yes' if self.vote else 'No'}"
