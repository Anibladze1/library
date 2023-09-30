from rest_framework import serializers

from book_giveaway.models import AskForBookRequest


class AskForBookRequestSerializer(serializers.ModelSerializer):
	owner = serializers.SerializerMethodField()
	location = serializers.SerializerMethodField()
	requester = serializers.HiddenField(default=serializers.CurrentUserDefault())
	
	class Meta:
		model = AskForBookRequest
		fields = ["book", "owner", "location", "requester"]
		
		validators = [
			serializers.UniqueTogetherValidator(
				queryset=AskForBookRequest.objects.all(), fields=("book", "requester"), message="Request Already Exists."
			)
		]
		
	def get_location(self, obj):
		return obj.book.location
	
	def get_owner(self, obj):
		return obj.book.owner


	
	
class ListBookRequestSerializer(serializers.ModelSerializer):
	class Meta:
		model = AskForBookRequest
		fields = "__all__"
