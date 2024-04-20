## Django Tips for Microsoft Oryx

Oryx attempts to build and run Django apps appropriately, but some configuration is not automated, so following are instructions for setting this yourself. 

Add App Service's default suffix to the list of allowed hosts in  settings.py: 
   Tip: use `['*']` for testing
```
// settings.py
ALLOWED_HOSTS = [
    '.azurewebsites.net'
]
```

Oryx runs manage.py ***collectstatic*** on your behalf unless you specify the DISABLE_COLLECTSTATIC env var 
Make sure you've set STATIC_ROOT in settings.py:
```
// settings.py
STATIC_ROOT = './static/'
```

### add CSRF TRUSTE DOMAIN
Also add trusted Origin Parameters to allow the Azure Web App to access Django's default Admin page:
Make sure the domain doesn't contain a trailing slash like `"....domain.net/"`
```
// settings.py
CSRF_TRUSTED_ORIGINS = ['https://www.domain.net'] //For Django 4.0 and above "scheme and host" are needed
CSRF_TRUSTED_ORIGINS = ['www.domain.net'] //For Django 3.2 and lower only "host" is needed
```

Some helpful links:
https://stackoverflow.com/questions/38841109/csrf-validation-does-not-work-on-django-using-https

https://learn.microsoft.com/en-us/training/modules/django-deployment/3-deployment-considerations