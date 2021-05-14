# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Order, Points
#
#
# @receiver(post_save, sender=Order)
# def collect_points(sender, instance, created, **kwargs):
#     total_price = instance.total_price
#     print(total_price)
#     if created==False:
#         if instance.total_price <= 10000:
#             abc = 0.01 * instance.total_price
#         else:
#             abc = 0.75 * instance.total_price
#         new_point = Points.objects.create(user=instance.user, points_gained=abc)
#
#         try:
#             # Check if user already has points and update if so
#             points = Points.objects.get(user=instance.user)
#             points.points_gained = abc
#             points.save(update_fields=['points_gained'])
#         except Points.DoesNotExist:
#             # User does not have points yet, create points
#             Points.objects.create(user=instance.user,
#                                   points_gained=abc)
#
#
# #post_save.connect(collect_points, sender=Order)