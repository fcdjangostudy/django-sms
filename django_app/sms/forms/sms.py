from django import forms


class SendsmsForm(forms.Form):
    phone_number = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder': '수신자 번호를 입력',
            },
        )
    )
    message = forms.CharField(
        max_length=90,
        widget=forms.TextInput(
            attrs={
                'placeholder': '보낼 메세지 입력',
            },
        ),
    )
