import requests

from django.core.management.base import BaseCommand, CommandError
from realty import models


class Command(BaseCommand):
    help = 'Fills database with test data.'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Filling provinces'))

        for name, content in self._get_provinces().items():
            self.stdout.write('Adding province "{}"'.format(name))
            models.Province.objects.create(
                name=name,
                x_u=content['boundaries']['upperLeft']['x'],
                y_u=content['boundaries']['upperLeft']['y'],
                x_b=content['boundaries']['bottomRight']['x'],
                y_b=content['boundaries']['bottomRight']['y']
            )

        self.stdout.write(self.style.SUCCESS('Fetching properties from github.'))

        props_response = requests.get(
            'https://raw.githubusercontent.com/VivaReal/code-challenge/master/properties.json')

        props = dict(props_response.json())

        total = props['totalProperties']

        for i, prop in enumerate(props['properties'], start=1):
            if i % 100 == 0:
                self.stdout.write('Creating property {} of {}.'.format(i, total))

            models.Property.objects.create(
                id=prop['id'],
                title=prop['title'],
                price=prop['price'],
                description=prop['description'],
                x=prop['lat'],
                y=prop['long'],
                beds=prop['beds'],
                baths=prop['baths'],
                square_meters=prop['squareMeters'],
            )

    def _get_provinces(self):
        return {
            'Gode': {
                'boundaries': {
                    'upperLeft': {
                        'x': 0,
                        'y': 1000
                    },
                    'bottomRight': {
                        'x': 600,
                        'y': 500
                    }
                }
            },
            'Ruja': {
                'boundaries': {
                    'upperLeft': {
                        'x': 400,
                        'y': 1000
                    },
                    'bottomRight': {
                        'x': 1100,
                        'y': 500
                    }
                }
            },
            'Jaby': {
                'boundaries': {
                    'upperLeft': {
                        'x': 1100,
                        'y': 1000
                    },
                    'bottomRight': {
                        'x': 1400,
                        'y': 500
                    }
                }
            },
            'Scavy': {
                'boundaries': {
                    'upperLeft': {
                        'x': 0,
                        'y': 500
                    },
                    'bottomRight': {
                        'x': 600,
                        'y': 0
                    }
                }
            },
            'Groola': {
                'boundaries': {
                    'upperLeft': {
                        'x': 600,
                        'y': 500
                    },
                    'bottomRight': {
                        'x': 800,
                        'y': 0
                    }
                }
            },
            'Nova': {
                'boundaries': {
                    'upperLeft': {
                        'x': 800,
                        'y': 500
                    },
                    'bottomRight': {
                        'x': 1400,
                        'y': 0
                    }
                }
            }
        }
