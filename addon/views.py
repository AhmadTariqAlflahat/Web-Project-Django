from django.shortcuts import redirect
from django.utils import translation
from django.core.exceptions import ObjectDoesNotExist

from web_project import settings
from addon.models import GlobalSetting

from uuid import uuid3


def set_language(request):
    if request.method == 'POST':
        request.session['preferred_language'] = language = request.POST['language']
        request.session.save()
        translation.activate(language)
        print(request.session.session_key)
        if request.user.is_authenticated:
            user_token = request.user.global_token
            if not GlobalSetting.objects.get(token=user_token):
                GlobalSetting.objects.create(
                    token=user_token,
                    language=language
                )
            else:
                addon_setting = GlobalSetting.objects.get(token=user_token)
                addon_setting.language = language
                addon_setting.save()
        else:
            session_token = request.session.session_key
            try:
                addon_setting = GlobalSetting.objects.get(token=session_token)
                addon_setting.language = language
                addon_setting.save()
            except ObjectDoesNotExist:
                GlobalSetting.objects.create(
                    token=session_token,
                    language=language
                )

    return redirect(request.POST['next'])