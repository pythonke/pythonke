from django.shortcuts import render

def main(request):

    context = {
        'github_url': 'https://github.com/pythonke',
        'facebook_url': 'https://www.facebook.com/pythonkosice',
        'youtube_url': 'https://www.youtube.com/channel/UCMUL-iVRHxZnGfSvcNUz3Aw',
        'project_url': 'https://github.com/pythonke/pythonke'
    }

    return render(request, 'main.html', context)

