# AI Summarizer Browser Extension

This repository contains a working example of a Chrome browser extension 
that lets you highlight text on any webpage and summarize it using 
OpenAI’s GPT model. It uses a serverless backend running on Google Cloud 
Functions for secure API key management and request handling.

## Overview

- **Browser Extension:**  
  - Built with HTML, CSS, and JavaScript (Manifest V3).
  - Allows users to highlight text on a webpage and then, with a single 
click, sends the selected text to a Google Cloud Function for 
summarization.
  
- **Google Cloud Function (Python):**  
  - Receives a POST request with the highlighted text.
  - Uses the OpenAI API to generate a summary.
  - Returns the summary as a JSON response.
  - Keeps the OpenAI API key secure on the server side.

## Prerequisites

- **OpenAI API Key:**  
  You need an OpenAI API key with access to `gpt-3.5-turbo` or `gpt-4`.
  
- **Google Cloud Account:**  
  A Google Cloud project with billing enabled.  
  GCP CLI (`gcloud`) is required for deploying the Cloud Function.

- **Chrome Browser:**  
  To load the extension locally.

## File Structure

. ├─ extension/ │ ├─ manifest.json │ ├─ background.js │ ├─ 
contentScript.js │ ├─ popup.html │ ├─ popup.js │ └─ 
cloud-function/ ├─ main.py ├─ requirements.txt

markdown
Copy code

- **extension/**: Contains the Chrome extension files.
- **cloud-function/**: Contains the Google Cloud Function code (Python) 
and requirements.

## Deploying the Cloud Function

1. Navigate to the `cloud-function` directory:
   ```bash
   cd cloud-function
Install dependencies locally if needed:

bash
Copy code
pip install -r requirements.txt
(This is optional, as GCP will install dependencies upon deployment.)

Deploy the function to Google Cloud (2nd Gen):

bash
Copy code
gcloud functions deploy summarizeText \
  --gen2 \
  --runtime python310 \
  --region=us-central1 \
  --entry-point summarizeText \
  --trigger-http \
  --allow-unauthenticated \
  --set-env-vars OPENAI_API_KEY=YOUR_OPENAI_API_KEY
Replace YOUR_OPENAI_API_KEY with your actual OpenAI key.
After deployment, you’ll get a URL of the form:

bash
Copy code
https://us-central1-YOUR_PROJECT.cloudfunctions.net/summarizeText
Setting Up the Extension
Open extension/popup.js and replace the CLOUD_FUNCTION_URL with the URL 
from the deployed Cloud Function:

javascript
Copy code
const CLOUD_FUNCTION_URL = 
"https://us-central1-YOUR_PROJECT.cloudfunctions.net/summarizeText";
Load the extension in Chrome:

Go to chrome://extensions
Enable Developer Mode.
Click “Load unpacked.”
Select the extension folder.
The extension should now be visible in your toolbar (or in the puzzle 
piece menu).
Note: If you don’t see it, pin it from the Extensions menu (the puzzle 
piece icon).

How It Works
Highlight Text:
On any webpage, select some text.

Click Extension Icon:
Open the extension’s popup by clicking the icon in the browser’s toolbar.

Summarize:
Click “Summarize Highlighted Text.” The extension sends the selected text 
to your Cloud Function.

AI Summary:
The Cloud Function uses the OpenAI API to summarize the text and returns a 
concise summary, displayed in the popup.

Security Considerations
The OpenAI API key is stored securely on the server side (in the Cloud 
Function), not in the client-side extension code.
In production, consider using gcloud functions deploy with environment 
variables rather than hardcoding the API key.
For further security, use a secrets manager like Google Secret Manager.
Troubleshooting
Cloud Function Not Deploying:
Ensure functions-framework and requests are in requirements.txt. Use the 
--gen2 flag for 2nd gen functions.

CORS or Network Issues:
Since this is a serverless function and a Chrome extension, you should not 
need CORS adjustments. If requests fail, check Cloud Function logs in GCP 
Console.

No Summary Returned:
Check the OpenAI API usage and error messages. Ensure your API key is 
correct and you have quota.

Contributing
Feel free to submit issues or PRs for improvements. This is a simple 
starter template, not a production solution.

License
This project is licensed under the MIT License. See LICENSE for details.

