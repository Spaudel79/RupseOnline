# class AddtoOrderItemView(APIView):
#     permission_classes = [IsAuthenticated]
    # queryset = OrderItem.objects.all()
    # serializer_class = OrderItemSerializer
    # @action(detail=True, methods=['post'])
# @login_required
#     def post(self, request, pk):
#         item = get_object_or_404(Product, pk=pk)
#         order_item, created = OrderItem.objects.get_or_create(
#             item=item,
#             user=self.request.user,
#             ordered=False
#         )
#         order_qs = Order.objects.filter(user=self.request.user, ordered=False)
#
#         if order_qs.exists():
#             order = order_qs[0]
#
#             if order.items.filter(item__pk=item.pk).exists():
#                 order_item.quantity += 1
#                 order_item.save()
#                 return Response({"message": "Quantity is added",
#                                  },
#                                 status=status.HTTP_200_OK
#                                 )
#             else:
#                 order.items.add(order_item)
#                 return Response({"message": " Item added to your cart", },
#                                 status=status.HTTP_200_OK,
#                                 )
#         else:
            # ordered_date = datetime.now()
            # order = Order.objects.create(user=self.request.user, ordered_date=ordered_date)
            # order.items.add(order_item)
            # return Response({"message": "Order is created & Item added to your cart", },
            #                 status=status.HTTP_200_OK,
            #                 )
            #serializer = BillingDetailsSerializer(data=request.data)
            # if serializer.is_valid():
            #     serializer.save()
            #     return Response ({"message": "Order is created & Item added to your cart",
            #                   "data" : serializer.data},
            #                  status=status.HTTP_200_OK,
            #                  )
            #
            # else:
            #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)