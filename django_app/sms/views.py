from django.shortcuts import render

from .forms import SendsmsForm

from sdk.api.message import Message
from sdk.exceptions import CoolsmsException


def sendsms(request):
    if request.method == 'POST':
        form = SendsmsForm(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            messages = form.cleaned_data['message']

            api_key = "NCSGLMHSQ2FTVZUA"
            api_secret = "2ZNM5ZPZR07QHSLHVIFAH3XZR1GAGM2F"
            cool = Message(api_key, api_secret)

            params = dict()
            params['type'] = 'sms'
            params['to'] = phone_number
            params['from'] = '01029953874'
            params['text'] = messages

            cool.send(params)
            aftersend = True
        else:
            aftersend = False

        context = {
            'aftersend': aftersend
        }
        return render(request, 'sms/sendsms.html', context)



    form = SendsmsForm()

    context = {
        'form': form,
    }

    return render(request, 'sms/sendsms.html', context)




if __name__ == "__main__":

    # set api key
    api_key = "NCS5805501D62D8B"
    api_secret = "A86DF83FB2F77AC52F0322A8B1B294A1"

    params = dict()
    params['type'] = 'sms'
    params['to'] = '01044345289'
    params['from'] = '01029953874'
    params['text'] = "yungkyang's test message"

    cool = Message(api_key, api_secret)

    try:
        response = cool.send(params)
        print('Success Count : {}'.format(response['success_count']))
        print('Error Count : {}'.format(response['error_count']))
        print('Group ID : {}'.format(response['group_id']))

        if "error_list" in response:
            print("Error List : {}".format(response['error_list']))

    except CoolsmsException as e:
        print("Error Code : {}".format(e.code))
        print("Error Message : {}".format(e.msg))

    sys.exit()