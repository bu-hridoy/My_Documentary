from django import forms  
from documentary.models import Document  
class DocumentForm(forms.ModelForm):  
    class Meta:  
        model = Document 
        fields = "__all__"  

