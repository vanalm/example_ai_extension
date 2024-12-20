import functions_framework
import os
import requests
from flask import request, jsonify

# Set your OpenAI API key. For production, consider using environment 
variables:
# gcloud functions deploy summarizeText --set-env-vars 
OPENAI_API_KEY=YOUR_KEY
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY', 'YOUR_OPENAI_API_KEY')

@functions_framework.http
def summarizeText(request):
    if request.method != 'POST':
        return jsonify({"error": "Only POST requests allowed"}), 405

    req_data = request.get_json(silent=True)
    if not req_data or 'text' not in req_data:
        return jsonify({"error": "No text provided in request body"}), 400
    
    text_to_summarize = req_data['text']

    # Call the OpenAI API
    try:
        response = requests.post(
            'https://api.openai.com/v1/chat/completions',
            headers={
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {OPENAI_API_KEY}'
            },
            json={
                'model': 'gpt-3.5-turbo',
                'messages': [
                    {'role': 'system', 'content': 'You are a helpful 
assistant that summarizes text.'},
                    {'role': 'user', 'content': f'Summarize this text: 
{text_to_summarize}'}
                ],
                'max_tokens': 150,
                'temperature': 0.7
            }
        )

        result = response.json()
        if 'error' in result:
            return jsonify({"error": result['error']['message']}), 500

        summary = (result.get('choices', [{}])[0]
                        .get('message', {})
                        .get('content', 'No summary returned.')).strip()

        return jsonify({"summary": summary}), 200
    except Exception as e:
        print(e)
        return jsonify({"error": "Internal server error"}), 500

