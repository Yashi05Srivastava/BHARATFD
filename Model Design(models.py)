from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()
    question_hi = models.TextField(blank=True, null=True)  # Hindi translation
    question_bn = models.TextField(blank=True, null=True)  # Bengali translation

    def translate_question(self, lang_code):
        """
        Dynamically retrieve translated text or fallback to English
        """
        translations = {
            'hi': self.question_hi,
            'bn': self.question_bn,
        }
        return translations.get(lang_code, self.question)
    
    def save(self, *args, **kwargs):
        """
        Automatically translate question to other languages
        """
        translator = Translator()
        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest='hi').text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest='bn').text
        super().save(*args, **kwargs)

    def __str__(self):
        return self.question
