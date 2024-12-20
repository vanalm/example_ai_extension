// popup.js

const summarizeBtn = document.getElementById('summarizeBtn');
const summaryResult = document.getElementById('summaryResult');
const loading = document.getElementById('loading');

// Replace with your actual Cloud Function URL from the deployment step
const CLOUD_FUNCTION_URL = "https://us-central1-practice-dev-project.cloudfunctions.net/summarizeText";

summarizeBtn.addEventListener('click', () => {
  summaryResult.textContent = "";
  loading.style.display = "block";

  chrome.storage.sync.get(['selectedText'], async (data) => {
    const textToSummarize = data.selectedText;

    if (!textToSummarize) {
      loading.style.display = "none";
      summaryResult.textContent = "No text selected. Please highlight text on a webpage first.";
      return;
    }

    try {
      const response = await fetch(CLOUD_FUNCTION_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: textToSummarize })
      });

      const result = await response.json();
      loading.style.display = "none";

      if (result.error) {
        summaryResult.textContent = "Error: " + result.error;
      } else {
        summaryResult.textContent = result.summary || "No summary returned.";
      }
    } catch (error) {
      loading.style.display = "none";
      summaryResult.textContent = "Error fetching summary: " +
        error.message;
    }
  });
});

