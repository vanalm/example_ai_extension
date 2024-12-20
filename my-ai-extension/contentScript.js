// contentScript.js
(function() {
  document.addEventListener("mouseup", () => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText) {
      chrome.storage.sync.set({ selectedText });
    }
  });
})();

