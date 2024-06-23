API_URL = "https://api-inference.huggingface.co/models/google/pegasus-xsum"
headers = {"Authorization": "Bearer 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"}
response = requests.post(API_URL, headers=headers, json=payload)
result = response.json()
    
if isinstance(result, list) and len(result) > 0 and isinstance(result[0], dict):
    summary_text = result[0].get('summary_text', '')
    return summary_text
    return None