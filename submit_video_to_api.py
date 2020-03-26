
# if you haven't already, install the SDK with 'pip install --user sightengine'

# it seems that the sightengine module needs to be loaded or something)
#  sightengine in /home/rstudio-user/.local/lib/python2.7/site-packages (1.4.0)
import sightengine
from sightengine.client import SightengineClient
client = SightengineClient('{1364743499}','{qXgiAZEBx4we4u8WVktV}')
client.check('nudity').video('https://www.crunchyroll.com/goblin-slayer/episode-1-the-fate-of-particular-adventurers-777760', 'https://www.crunchyroll.com/goblin-slayer/episode-1-the-fate-of-particular-adventurers-777760')
