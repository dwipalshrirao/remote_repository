from django import forms

class insertingDataform(forms.Form):
	product_id=forms.IntegerField(
		label="enter your id",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'product_id',
				'class': 'form-control'
			}
		)
	)
	product_name = forms.CharField(
		label="enter your name",
		widget=forms.TextInput(
			attrs={
				'placeholder': 'product_name',
				'class': 'form-control'
			}
		)
	)
	product_cost = forms.IntegerField(
		label="enter product cost",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'product_cost',
				'class': 'form-control'
			}
		)
	)
	product_class = forms.CharField(
		label="enter product class",
		widget=forms.TextInput(
			attrs={
				'placeholder': 'product_class',
				'class': 'form-control'
			}
		)
	)
	no_of_products = forms.IntegerField(
		label="enter no. of products",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'no. of products',
				'class': 'form-control'
			}
		)
	)
	y=range(2000,2020)
	manufacture_date = forms.DateField(
		label="enter manufacture date",
		widget=forms.SelectDateWidget(years=y))

	expirydate = forms.DateField(
		label="enter date of expiry",
		widget=forms.SelectDateWidget())
	customer_name = forms.CharField(
		label="enter cust name",
		widget=forms.TextInput(
			attrs={
				'placeholder': 'cust_name',
				'class': 'form-control'
			}
		)
	)
	mobile = forms.IntegerField(
		label="enter custmer mobile no.",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'cust mobile no',
				'class': 'form-control'
			}
		)
	)
	Email = forms.EmailField(
		label="enter cust mail id",
		widget=forms.TextInput(
			attrs={
				'placeholder': 'Email id',
				'class': 'form-control'
			}
		)
	)


class updatingdataform(forms.Form):
	product_id = forms.IntegerField(
		label="enter your id",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'product_id',
				'class': 'form-control'
			}
		)
	)
	product_cost = forms.IntegerField(
		label="enter product cost",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'product_cost',
				'class': 'form-control'
			}
		)
	)
class retrive_dataform(forms.Form):
	product_id = forms.IntegerField(
		label="enter your id",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'product_id',
				'class': 'form-control'
			}
		)
	)
	product_cost = forms.IntegerField(
		label="enter product cost",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'product_cost',
				'class': 'form-control'
			}
		)
	)

class deletingdataform(forms.Form):
	product_id = forms.IntegerField(
		label="enter your id",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'product_id',
				'class': 'form-control'
			}
		)
	)
	product_cost = forms.IntegerField(
		label="enter product cost",
		widget=forms.NumberInput(
			attrs={
				'placeholder': 'product_cost',
				'class': 'form-control'
			}
		)
	)