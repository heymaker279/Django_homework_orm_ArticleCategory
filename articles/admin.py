from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, ArticleSection, Section


class ArticleSectionInlineFormset(BaseInlineFormSet):
    def clean(self):
        count_is_main = 0
        count_tags = 0
        for form in self.forms:
            if len(form.cleaned_data) != 0:
                count_tags += 1
                if form.cleaned_data['is_main']:
                    count_is_main += 1
        if count_is_main > 1:
            raise ValidationError('Основным может быть только один раздел')
        if count_is_main == 0:
            raise ValidationError('Укажите основной раздел')
        if count_tags == 0:
            raise ValidationError('Укажите основной раздел')
            # В form.cleaned_data будет словарь с данными
            # каждой отдельной формы, которые вы можете проверить
            # form.cleaned_data
            # вызовом исключения ValidationError можно указать админке о наличие ошибки
            # таким образом объект не будет сохранен,
            # а пользователю выведется соответствующее сообщение об ошибке
            # raise ValidationError('Тут всегда ошибка')
        return super().clean()  # вызываем базовый код переопределяемого метода


class ArticleSectionInline(admin.TabularInline):
    model = ArticleSection
    formset = ArticleSectionInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [ArticleSectionInline]


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['name']
