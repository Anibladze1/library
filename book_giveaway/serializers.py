from rest_framework import serializers

from book_giveaway.models import BookBorrowRequest


class BookBorrowRequestSerializer(serializers.ModelSerializer):
	owner = serializers.SerializerMethodField()
	location = serializers.SerializerMethodField()
	requester = serializers.HiddenField(default=serializers.CurrentUserDefault())
	
	class Meta:
		model = BookBorrowRequest
		fields = ["book", "owner", "location", "requester"]
		
		validators = [
			serializers.UniqueTogetherValidator(
				queryset=BookBorrowRequest.objects.all(), fields=("book", "requester"), message="Request Already Exists."
			)
		]
		
	def get_location(self, obj):
		return obj.book.location
	
	def get_owner(self, obj):
		return obj.book.owner
	
	
class ListBookRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = BookBorrowRequest
		fields = "__all__"
