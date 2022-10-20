__version__ = "0.0.1"

import requests

from assembly_ai.walkthroughs import (submit_url_for_transcription, 
                                      get_status_of_transcription, 
                                      get_transcription_results)

api_key = None
audio_url = None

endpoint = "https://api.assemblyai.com/v2/transcript"
