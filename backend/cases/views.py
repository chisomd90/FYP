from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Case
from accounts.models import CustomUser
import json

class CaseView(View):
    def get(self, request, case_id=None):
        if case_id:
            try:
                case = Case.objects.get(pk=case_id)
                data = {
                    "id": case.id,
                    "case_number": case.case_number,
                    "title": case.title,
                    "plaintiff": case.plaintiff,
                    "defendant": case.defendant,
                    "judge": case.judge.username,
                    "lawyers": [lawyer.username for lawyer in case.lawyers.all()],
                    "status": case.status,
                    "created_at": case.created_at,
                    "updated_at": case.updated_at,
                }
                return JsonResponse(data, safe=False, status=200)
            except Case.DoesNotExist:
                return JsonResponse({"error": "Case not found"}, status=404)
        cases = Case.objects.all()
        data = [
            {
                "id": case.id,
                "case_number": case.case_number,
                "title": case.title,
                "plaintiff": case.plaintiff,
                "defendant": case.defendant,
                "status": case.status,
            }
            for case in cases
        ]
        return JsonResponse(data, safe=False, status=200)

    @method_decorator(csrf_exempt)
    def post(self, request):
        try:
            data = json.loads(request.body)
            judge = CustomUser.objects.get(id=data['judge'])
            lawyers = CustomUser.objects.filter(id__in=data['lawyers'])
            case = Case.objects.create(
                case_number=data['case_number'],
                title=data['title'],
                plaintiff=data['plaintiff'],
                defendant=data['defendant'],
                judge=judge,
                status=data.get('status', 'ongoing')
            )
            case.lawyers.set(lawyers)
            case.save()
            return JsonResponse({"message": "Case created successfully"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    @method_decorator(csrf_exempt)
    def put(self, request, case_id):
        try:
            data = json.loads(request.body)
            case = Case.objects.get(pk=case_id)
            case.case_number = data.get('case_number', case.case_number)
            case.title = data.get('title', case.title)
            case.plaintiff = data.get('plaintiff', case.plaintiff)
            case.defendant = data.get('defendant', case.defendant)
            case.status = data.get('status', case.status)
            if 'judge' in data:
                judge = CustomUser.objects.get(id=data['judge'])
                case.judge = judge
            if 'lawyers' in data:
                lawyers = CustomUser.objects.filter(id__in=data['lawyers'])
                case.lawyers.set(lawyers)
            case.save()
            return JsonResponse({"message": "Case updated successfully"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    @method_decorator(csrf_exempt)
    def delete(self, request, case_id):
        try:
            case = Case.objects.get(pk=case_id)
            case.delete()
            return JsonResponse({"message": "Case deleted successfully"}, status=204)
        except Case.DoesNotExist:
            return JsonResponse({"error": "Case not found"}, status=404)
