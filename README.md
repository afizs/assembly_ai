# AssemblyAI Python SDK

`assembly_ai_plus` is a Python SDK for Assembly AI. You can read more about Assembly AI here: https://www.assemblyai.com/docs/ 

# Installation 

`pip install assembly-ai-plus`

# Usage

Here is the example to extract text from audio file 👇

```
import assembly_ai
assembly_ai.api_key = YOUR_ASSEMBLY_AI_KEY
response = assembly_ai.submit_url_for_transcription(audio_url='https://bit.ly/3yxKEIY', 
                                                    sentiment_analysis=True)
```

# Output

```
print(f'Full Transcribe: {all_results.get("text")} \n\n')
print('Sentiment Analysis Details: ', all_results.get('sentiment_analysis_results'))

Full Transcribe: You know, demons on TV like that. And and for people to expose themselves to being rejected on TV or, you know, humili humiliated by Fear Factor or, you know. 


Sentiment Analysis Details:  [{'text': 'You know, demons on TV like that.', 'start': 387, 'end': 2347, 'sentiment': 'NEGATIVE', 'confidence': 0.5303722620010376, 'speaker': None}, {'text': 'And and for people to expose themselves to being rejected on TV or, you know, humili humiliated by Fear Factor or, you know.', 'start': 2380, 'end': 11625, 'sentiment': 'NEGATIVE', 'confidence': 0.8029202222824097, 'speaker': None}]
```
                                    