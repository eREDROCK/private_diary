from django import forms 

class InquiryForm(forms.Form):
  name=forms.CharField(label='お名前',max_length=30)
  email=forms.EmailField(label='メールアドレス')
  title=forms.CharField(label='タイトル',max_length=30)
  message=forms.CharField(label='メッセージ',widget=forms.Textarea)

  def __init__(self,*args,**kwargs):
    super().__init__(*args,**kwargs)

    self.field['name'].widget.attrs['class']='form-control'
    self.field['name'].widget.attrs['placeholder']='お名前をここに入力してください。'
    self.field['email'].widget.attrs['class']='form-control'
    self.field['email'].widget.attrs['placeholder']='メールアドレスをここに入力してください。'
    self.field['title'].widget.attrs['class']='form-control'
    self.field['title'].widget.attrs['placeholder']='タイトルをここに入力してください。'
    self.field['message'].widget.attrs['class']='form-control'
    self.field['message'].widget.attrs['placeholder']='メッセージをここに入力してください。'