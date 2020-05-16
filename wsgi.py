from whitenoise.django import DjangoWhiteNoise
from dotenv import load_dotenv

load_dotenv()
application = DjangoWhiteNoise(application)
