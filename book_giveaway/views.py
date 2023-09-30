from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated

from book_giveaway.models import AskForBookRequest
from book_giveaway.serializers import AskForBookRequestSerializer, ListBookRequestSerializer


class RequestBookView(generics.CreateAPIView):
    """
    API endpoint to request a book.

    **Permissions**:
    - Only authenticated users can make a request.
    """
    serializer_class = AskForBookRequestSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request, "user": request.user})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Your Request Has Been Sent To Book Owner"}, status=status.HTTP_200_OK)


class GetBookRequestListView(generics.ListAPIView):
    """
    API endpoint to list all book requests made to the authenticated user (book owner).

    **Permissions**:
    - Only authenticated users can view the requests made to them.
    """
    permission_classes = [IsAuthenticated]
    serializer_class = ListBookRequestSerializer

    def get_queryset(self):
        owner = self.request.user
        queryset = AskForBookRequest.objects.filter(book__owner=owner)
        return queryset

    def get(self, request, *args, **kwargs):
        objects = self.get_queryset()
        serializer = self.serializer_class(objects, many=True, context={"request": request})

        return Response(serializer.data, status=status.HTTP_200_OK)


class ConfirmBookRequestView(generics.UpdateAPIView):
    """
    API endpoint to confirm a book request.

    **Permissions**:
    - Only authenticated users can confirm a request.

    **Conditions**:
    - The user must be the owner of the book and the book must be available.
    """
    queryset = AskForBookRequest.objects.all()
    serializer_class = AskForBookRequestSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.book.owner == request.user and instance.book.is_available:
            instance.is_confirmed = True
            instance.book.is_available = False
            instance.book.owner = instance.requester
            instance.save()
            instance.book.save()
            return Response({'message': 'Request confirmed successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'You are not able to give away this book'}, status=status.HTTP_400_BAD_REQUEST)
