#
#
# class SocialLoginAdapter(DefaultSocialAccountAdapter):
#     def pre_social_login(self, request, sociallogin):
#         # This is tested and should work
#         try:
#             user = User.objects.get(email=sociallogin.account.user.email)
#             sociallogin.connect(request, user)
#             # Create a response object
#             response = HttpResponse()
#             raise ImmediateHttpResponse(response)
#         except Exception:
#             pass