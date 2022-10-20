import requests
import time
import assembly_ai
from assembly_ai.endpoints import submit_transcript


def get_headers():
    return {"authorization": assembly_ai.api_key, "content-type": "application/json"}


def submit_url_for_transcription(
    audio_url: str,
    sentiment_analysis: bool = False,
    auto_chapters: bool = False,
    entity_detection: bool = False,
    auto_highlights: bool = False,
) -> dict:
    json = {
        "audio_url": audio_url,
        "sentiment_analysis": sentiment_analysis,
        "auto_chapters": auto_chapters,
        "entity_detection": entity_detection,
        "auto_highlights": auto_highlights,
    }
    response = requests.post(submit_transcript, json=json, headers=get_headers())
    return response.json()


def get_status_of_transcription(transcripiton_id: str) -> str:
    endpoint = f"{submit_transcript}/{transcripiton_id}"
    response = requests.get(endpoint, headers=get_headers())
    return response.json()


def get_transcription_results(transcripiton_id: str, all_details: bool = False) -> dict:
    """Get the transcription results for the given id

    Args:
        transcripiton_id (str): Transcription id, which was returned by submit_url_for_transcription
        all_details (bool, optional): True returns all the details. Defaults to False.

    Returns:
        dict: _description_
    """
    full_details = get_status_of_transcription(transcripiton_id)
    status = full_details.get("status")
    while status not in ["completed", "error"]:
        time.sleep(5)  # sleep for secs
        full_details = get_status_of_transcription(transcripiton_id)
        status = full_details.get("status")

    if all_details:
        return full_details

    return {
        "id": full_details.get("id"),
        "confidence": full_details.get("confidence"),
        "text": full_details.get("text"),
    }
