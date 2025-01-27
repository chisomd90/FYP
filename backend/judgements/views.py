from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Judgement, Case
from .serializers import JudgementSerializer
from .permissions import IsJudgeOrReadOnly

# List/Create Judgments
class JudgementListCreateView(generics.ListCreateAPIView):
    queryset = Judgement.objects.all()
    serializer_class = JudgementSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        case_id = self.request.data.get('case')
        if case_id:
            # Retrieve the case
            case = Case.objects.get(id=case_id)

            # Ensure the judge matches the case's judge
            serializer.save(judge=case.judge, case=case)
        else:
            # Fallback: Default to the current authenticated user
            serializer.save(judge=self.request.user)


# Retrieve/Update/Delete Judgments
class JudgementDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Judgement.objects.all()
    serializer_class = JudgementSerializer
    permission_classes = [permissions.IsAuthenticated, IsJudgeOrReadOnly]

# Filter Judgements by Case or Judge
@api_view(['GET'])
def filter_judgements(request):
    case_id = request.query_params.get('case_id')
    judge_id = request.query_params.get('judge_id')

    if case_id:
        judgements = Judgement.objects.filter(case_id=case_id)
    elif judge_id:
        judgements = Judgement.objects.filter(judge_id=judge_id)
    else:
        judgements = Judgement.objects.all()

    serializer = JudgementSerializer(judgements, many=True)
    return Response(serializer.data)
