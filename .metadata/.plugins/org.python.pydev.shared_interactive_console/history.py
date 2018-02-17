import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'Djangoa_web_project.settings'; import django
if django.VERSION <= (1, 5):
    from django.core import management
    import Djangoa_web_project.settings as settings
    management.setup_environ(settings)
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
import sys; print('%s %s' % (sys.executable or sys.platform, sys.version))
import os; os.environ['DJANGO_SETTINGS_MODULE'] = 'django_site.settings'; import django
if django.VERSION <= (1, 5):
    from django.core import management
    import django_site.settings as settings
    management.setup_environ(settings)
else:
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
