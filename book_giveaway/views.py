from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from book.models import Book
from book_giveaway.models import BookBorrowRequest
from book_giveaway.serializers import BookBorrowRequestSerializer, ListBookRequestSerializer


class RequestBookView(generics.CreateAPIView):
	serializer_class = BookBorrowRequestSerializer
	permission_classes = [IsAuthenticated]
	
	def post(self, request, *args, **kwargs):
		serializer = self.serializer_class(data=request.data, context={"request": request, "user": request.user})
		serializer.is_valid(raise_exception=True)
		serializer.save()

		return Response({"message": "Your Request Has Been Sent To Book Owner"}, status=status.HTTP_200_OK)
	
	
class GetBookRequestListView(generics.ListAPIView):
	permission_classes = [IsAuthenticated]
	serializer_class = ListBookRequestSerializer

	def get_queryset(self):
		owner = self.request.user
		queryset = BookBorrowRequest.objects.filter(book__owner=owner)
		return queryset
	
	def get(self, request):
		objects = self.get_queryset()
		serializer = self.serializer_class(objects, many=True, context={"request": request})
		
		return Response(serializer.data, status=status.HTTP_200_OK)
	

class ConfirmBookBorrowRequestView(generics.UpdateAPIView):
	queryset = BookBorrowRequest.objects.all()
	serializer_class = BookBorrowRequestSerializer
	permission_classes = [IsAuthenticated]

	def put(self, request, *args, **kwargs):
		instance = self.get_object()
		if instance.book.owner == request.user and instance.book.is_available:
			instance.is_confirmed = True
			instance.book.is_available = False
			instance.save()
			instance.book.save()
			return Response({'message': 'Request confirmed successfully'}, status=status.HTTP_200_OK)
		else:
			return Response({'error': 'You are not able to give away this book'}, status=status.HTTP_400_BAD_REQUEST)
	
	
# class ReturnBookView(generics.UpdateAPIView):
# 	queryset = Book.objects.all()
# 	serializer_class = BookBorrowRequestSerializer
# 	permission_classes = [IsAuthenticated]
#
# 	def update(self, request, *args, **kwargs):
# 		book = self.get_object()
#
# 		if book.recipient != request.user:
# 			return Response({"error": "Only the recipient can return the book"}, status=status.HTTP_403_FORBIDDEN)
#
# 		book.recipient = None
# 		book.save()
#
# 		return Response({"message": "Book returned successfully"}, status=status.HTTP_200_OK)