from django.core.management.base import BaseCommand
from caribbean.models import MadmexCaribesample

class Command(BaseCommand):
    def handle(self, **options):
        for sample in MadmexCaribesample.objects.all():
            if sample.tag_editable != sample.tag or sample.validated:
                sample.tag_editable = sample.tag
                sample.validated = False
                sample.save()
        print('Done.')