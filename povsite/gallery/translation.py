from .models import *
from modeltranslation.translator import register, TranslationOptions


@register(Gallery)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('title', 'content_text', 'content',)


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ('name', 'surname', 'brand_name', 'biography',)


@register(Project)
class CategoryProjectTranslationOptions(TranslationOptions):
    fields = ("name", 'description', 'title_block_description', 'block_description_one', 'block_description_two',)


@register(Themes)
class GalleryTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(LandingPage)
class LandingPageTranslationOptions(TranslationOptions):
    fields = (
        'logo_text', 'logo_header', 'about_us', 'about_us_title', 'about_us_text', 'projects', 'team', 'logo_footer',)


@register(WhatBlock)
class WhatBlockTranslationOptions(TranslationOptions):
    fields = ('name', 'title', 'text',)
