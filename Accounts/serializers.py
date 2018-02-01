from django.contrib.auth import get_user_model
from rest_framework import serializers


User = get_user_model()

# class RegisterSerializer(serializers.Serializer):

class RegisterSerializer(serializers.ModelSerializer):
	# email = serializers.EmailField(
	# 	label='Email Address',
	# 	max_length=255,
	# )
	# first_name = serializers.CharField(
	# 	label='First name',
	# 	max_length=255,
	# 	allow_blank=False
	# )
	# last_name = serializers.CharField(
	# 	label='Last name',
	# 	max_length=255,
	# 	allow_blank=False
	# )
	password1 = serializers.CharField(
		label='Password',
		min_length = 6,
		write_only = True
	)
	password2 = serializers.CharField(
		label='Confirm password',
		min_length = 6,
		write_only = True
	)

	class Meta:
		model = User
		fields = ['email', 'first_name', 'last_name', 'password1', 'password2',]

	# # profile_pic = serializers.ImageField(
	# # 	max_length = 500,
	# # 	allow_empty_file=False
	# # )

	# def validate_email(self, email):
	# 	strip_email = email.strip()
	# 	if User.objects.filter(email=strip_email) != None:
	# 		raise serializers.ValidationError("Email already exists")
	# 	return strip_email

	def validate_password1(self, password):
		return password.strip()

	def validate(self, data):
		if data['password1'] != data['password2']:
			raise serializers.ValidationError('The passwords did not match.')
		return data

	def save(self):
		post_data = {
			'email': self.validated_data.get('email', ''),
			'first_name': self.validated_data.get('first_name', ''),
			'last_name': self.validated_data.get('last_name', ''),
			'password': self.validated_data.get('password1', '')
		}
		created_user = User.objects.create_user(
							email=post_data['email'],
					 		first_name=post_data['first_name'],
					 		last_name=post_data['last_name'],
					 		password=post_data['password']
	 					)
		return created_user