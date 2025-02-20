from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserActivity
from .serializers import UserActivitySerializer

@api_view(['POST'])
def track_activity(request):
    data = request.data.copy()  # نسخة من البيانات الأصلية
    try:
        # تحويل timestamp إلى تنسيق صحيح
        data['timestamp'] = datetime.strptime(data['timestamp'], "%m/%d/%Y, %I:%M:%S %p").isoformat()
    except ValueError:
        return Response({"error": "Invalid timestamp format"}, status=400)

    serializer = UserActivitySerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data saved successfully!"}, status=201)
    return Response(serializer.errors, status=400)
