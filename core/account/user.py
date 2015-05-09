from core.issue.issue_serializer import IssueSerializer
from core.models import IssueModel
from core.utility.error_exceptions import SerializerError


class User():
    def __init__(self, model):
        self._user = model

    def __str__(self):
        return str(self._user.__dict__)

    def raise_issue(self, args):
        args["user"] = self._user.pk

        serializer = IssueSerializer(data=args)
        if serializer.is_valid():
            serializer.save()
        else:
            raise SerializerError(serializer.errors)

    @staticmethod
    def get_recommend_list():
        data = {
            'subject': list(set(IssueModel.objects.values_list('subject', flat=True))),
            'description': list(set(IssueModel.objects.values_list('description', flat=True))),
            'place': list(set(IssueModel.objects.exclude(place__isnull=True).values_list('place', flat=True))),
        }
        return data